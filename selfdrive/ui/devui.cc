#include "ui.hpp"

#include <assert.h>
#include <map>
#include <cmath>
#include <iostream>
#include "common/util.h"
#include "common/timing.h"
#include <algorithm>

#define NANOVG_GLES3_IMPLEMENTATION
#include "nanovg_gl.h"
#include "nanovg_gl_utils.h"
#include "devui.hpp"
#include "sidebar.hpp"

//DEV START: functions added for the display of various items
static int dev_ui_draw_measure(UIState *s,  const char* bb_value, const char* bb_uom, const char* bb_label,
    int bb_x, int bb_y, int bb_uom_dx,
    NVGcolor bb_valueColor, NVGcolor bb_labelColor, NVGcolor bb_uomColor,
    int bb_valueFontSize, int bb_labelFontSize, int bb_uomFontSize )  {
  nvgTextAlign(s->vg, NVG_ALIGN_CENTER | NVG_ALIGN_BASELINE);
  int dx = 0;
  if (strlen(bb_uom) > 0) {
    dx = (int)(bb_uomFontSize*2.5/2);
   }
  //print value
  nvgFontFace(s->vg, "sans-semibold");
  nvgFontSize(s->vg, bb_valueFontSize*2.5);
  nvgFillColor(s->vg, bb_valueColor);
  nvgText(s->vg, bb_x-dx/2, bb_y+ (int)(bb_valueFontSize*2.5)+5, bb_value, NULL);
  //print label
  nvgFontFace(s->vg, "sans-regular");
  nvgFontSize(s->vg, bb_labelFontSize*2.5);
  nvgFillColor(s->vg, bb_labelColor);
  nvgText(s->vg, bb_x, bb_y + (int)(bb_valueFontSize*2.5)+5 + (int)(bb_labelFontSize*2.5)+5, bb_label, NULL);
  //print uom
  if (strlen(bb_uom) > 0) {
      nvgSave(s->vg);
    int rx =bb_x + bb_uom_dx + bb_valueFontSize -3;
    int ry = bb_y + (int)(bb_valueFontSize*2.5/2)+25;
    nvgTranslate(s->vg,rx,ry);
    nvgRotate(s->vg, -1.5708); //-90deg in radians
    nvgFontFace(s->vg, "sans-regular");
    nvgFontSize(s->vg, (int)(bb_uomFontSize*2.5));
    nvgFillColor(s->vg, bb_uomColor);
    nvgText(s->vg, 0, 0, bb_uom, NULL);
    nvgRestore(s->vg);
  }
  return (int)((bb_valueFontSize + bb_labelFontSize)*2.5) + 5;
}

static void dev_ui_draw_measures_left(UIState *s, int bb_x, int bb_y, int bb_w ) {
  const UIScene *scene = &s->scene;
  int bb_rx = bb_x + (int)(bb_w/2);
  int bb_ry = bb_y;
  int bb_h = 5;
  NVGcolor lab_color = nvgRGBA(255, 255, 255, 200);
  NVGcolor uom_color = nvgRGBA(255, 255, 255, 200);
  int value_fontSize=30;
  int label_fontSize=15;
  int uom_fontSize = 15;
  int bb_uom_dx =  (int)(bb_w /2 - uom_fontSize*2.5) ;
  //CPU TEMP
    if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    snprintf(val_str, sizeof(val_str), "%.0f°C", (round((s->scene.deviceState.getCpuTempC()[0]))));
    snprintf(uom_str, sizeof(uom_str), "%d%%", (s->scene.deviceState.getCpuUsagePercent()));
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "CPU TEMP",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }
  //add Ublox GPS accuracy
  if (scene->gps_external.getAccuracy() != 0.00) {
    char val_str[16];
    char uom_str[3];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    //show red/orange if gps accuracy is low
      if(scene->gps_external.getAccuracy() > 0.85) {
         val_color = nvgRGBA(255, 188, 3, 200);
      }
      if(scene->gps_external.getAccuracy() > 1.3) {
         val_color = nvgRGBA(255, 0, 0, 200);
      }
    // gps accuracy is always in meters
    if(scene->gps_external.getAccuracy() > 99 || scene->gps_external.getAccuracy() == 0) {
       snprintf(val_str, sizeof(val_str), "None");
    }else if(scene->gps_external.getAccuracy() > 9.99) {
      snprintf(val_str, sizeof(val_str), "%.1f", (s->scene.gps_external.getAccuracy()));
    }
    else {
      snprintf(val_str, sizeof(val_str), "%.2f", (s->scene.gps_external.getAccuracy()));
    }
    snprintf(uom_str, sizeof(uom_str), "%d", (s->scene.satelliteCount));
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "GPS PREC",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }
  //add altitude
  if (scene->gps_external.getAccuracy() != 0.00) {
    char val_str[16];
    char uom_str[3];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    snprintf(val_str, sizeof(val_str), "%.1f", (s->scene.gps_external.getAltitude()));
    snprintf(uom_str, sizeof(uom_str), "m");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "ALTITUDE",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }
    //add EPS Motor Torque
  if (true) {
    char val_str[16];
    char uom_str[3];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200); //TODO: Add orange/red color depending on torque intensity. <1x limit = white, btwn 1x-2x limit = orange, >2x limit = red
    snprintf(val_str, sizeof(val_str), "%.0f", (s->scene.car_state.getSteeringTorqueEps()));
    snprintf(uom_str, sizeof(uom_str), "Nm");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "EPS TRQ",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }
  //add aEgo
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    snprintf(val_str, sizeof(val_str), "%.1f", (s->scene.car_state.getSteeringTorqueEps()));
    snprintf(uom_str, sizeof(uom_str), "m/s²");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "ACCEL",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }
  //finally draw the frame
  bb_h += 20;
  nvgBeginPath(s->vg);
    nvgRoundedRect(s->vg, bb_x, bb_y, bb_w, bb_h, 20);
    nvgStrokeColor(s->vg, nvgRGBA(255,255,255,80));
    nvgStrokeWidth(s->vg, 6);
    nvgStroke(s->vg);
}

static void dev_ui_draw_measures_right(UIState *s, int bb_x, int bb_y, int bb_w ) {
  const UIScene *scene = &s->scene;
  int bb_rx = bb_x + (int)(bb_w/2);
  int bb_ry = bb_y;
  int bb_h = 5;
  NVGcolor lab_color = nvgRGBA(255, 255, 255, 200);
  NVGcolor uom_color = nvgRGBA(255, 255, 255, 200);
  int value_fontSize=30;
  int label_fontSize=15;
  int uom_fontSize = 15;
  int bb_uom_dx =  (int)(bb_w /2 - uom_fontSize*2.5) ;

  //add visual radar relative distance
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    if (s->scene.lead_data[0].getStatus()) {
      //show RED if less than 5 meters
      //show orange if less than 15 meters
      if((int)(s->scene.lead_data[0].getDRel()) < 15) {
        val_color = nvgRGBA(255, 188, 3, 200);
      }
      if((int)(s->scene.lead_data[0].getDRel()) < 5) {
        val_color = nvgRGBA(255, 0, 0, 200);
      }
      // lead car relative distance is always in meters
      snprintf(val_str, sizeof(val_str), "%d", (int)s->scene.lead_data[0].getDRel());
    } else {
       snprintf(val_str, sizeof(val_str), "-");
    }
    snprintf(uom_str, sizeof(uom_str), "m");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "REL DIST",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }

  //add visual radar relative speed
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    if (s->scene.lead_data[0].getStatus()) {
      //show Orange if negative speed (approaching)
      //show Orange if negative speed faster than 5mph (approaching fast)
      if((int)(s->scene.lead_data[0].getVRel()) < 0) {
        val_color = nvgRGBA(255, 188, 3, 200);
      }
      if((int)(s->scene.lead_data[0].getVRel()) < -5) {
        val_color = nvgRGBA(255, 0, 0, 200);
      }
      // lead car relative speed is always in meters
      if (s->is_metric) {
         snprintf(val_str, sizeof(val_str), "%d", (int)(s->scene.lead_data[0].getVRel() * 3.6 + 0.5));
      } else {
         snprintf(val_str, sizeof(val_str), "%d", (int)(s->scene.lead_data[0].getVRel() * 2.2374144 + 0.5));
      }
    } else {
       snprintf(val_str, sizeof(val_str), "-");
    }
    if (s->is_metric) {
      snprintf(uom_str, sizeof(uom_str), "km/h");;
    } else {
      snprintf(uom_str, sizeof(uom_str), "mph");
    }
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "REL SPEED",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }

  //add steering angle
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
      //show Orange if more than 6 degrees
      //show red if  more than 12 degrees
      if(((int)(s->scene.angleSteers) < -6) || ((int)(s->scene.angleSteers) > 6)) {
        val_color = nvgRGBA(255, 188, 3, 200);
      }
      if(((int)(s->scene.angleSteers) < -12) || ((int)(s->scene.angleSteers) > 12)) {
        val_color = nvgRGBA(255, 0, 0, 200);
      }
      // steering is in degrees
      snprintf(val_str, sizeof(val_str), "%.0f°",(s->scene.angleSteers));

      snprintf(uom_str, sizeof(uom_str), "");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "REAL STEER",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }

  //add desired steering angle
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    if (scene->controls_state.getEnabled()) {
      //show Orange if more than 6 degrees
      //show red if  more than 12 degrees
      if(((int)(s->scene.angleSteersDes) < -6) || ((int)(s->scene.angleSteersDes) > 6)) {
        val_color = nvgRGBA(255, 188, 3, 200);
      }
      if(((int)(s->scene.angleSteersDes) < -12) || ((int)(s->scene.angleSteersDes) > 12)) {
        val_color = nvgRGBA(255, 0, 0, 200);
      }
      // steering is in degrees
      snprintf(val_str, sizeof(val_str), "%.0f°",(s->scene.angleSteersDes));
    } else {
       snprintf(val_str, sizeof(val_str), "-");
    }
      snprintf(uom_str, sizeof(uom_str), "");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "DESIR STEER",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }
    //engineRPM
  if (true) {
    char val_str[16];
    char uom_str[4];
    NVGcolor val_color = nvgRGBA(255, 255, 255, 200);
    if(s->scene.engineRPM == 0) {
      snprintf(val_str, sizeof(val_str), "OFF");
    }
    else {snprintf(val_str, sizeof(val_str), "%d", (s->scene.engineRPM));}
    snprintf(uom_str, sizeof(uom_str), "");
    bb_h +=dev_ui_draw_measure(s,  val_str, uom_str, "ENG RPM",
        bb_rx, bb_ry, bb_uom_dx,
        val_color, lab_color, uom_color,
        value_fontSize, label_fontSize, uom_fontSize );
    bb_ry = bb_y + bb_h;
  }

  //finally draw the frame
  bb_h += 20;
  nvgBeginPath(s->vg);
    nvgRoundedRect(s->vg, bb_x, bb_y, bb_w, bb_h, 20);
    nvgStrokeColor(s->vg, nvgRGBA(255,255,255,80));
    nvgStrokeWidth(s->vg, 6);
    nvgStroke(s->vg);
}

static void dev_ui_draw_ui(UIState *s)
{
  //const UIScene *scene = &s->scene;
  const int bb_dml_w = 180;
  const int bb_dml_x = (s->scene.viz_rect.x + (bdr_is * 2));
  const int bb_dml_y = (s->scene.viz_rect.y  + (bdr_is * 1.5)) + 220;

  const int bb_dmr_w = 180;
  const int bb_dmr_x = s->scene.viz_rect.x + s->scene.viz_rect.w - bb_dmr_w - (bdr_is * 2);
  const int bb_dmr_y = (s->scene.viz_rect.y + (bdr_is * 1.5)) + 220;

  dev_ui_draw_measures_right(s, bb_dml_x, bb_dml_y, bb_dml_w);
  dev_ui_draw_measures_left(s, bb_dmr_x, bb_dmr_y-20, bb_dmr_w);
}

//DEV END: functions added for the display of various items
