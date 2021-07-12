#include "selfdrive/ui/ui.h"

#include <assert.h>
#include <map>
#include <cmath>
#include <iostream>
#include <algorithm>

#include "common/transformations/coordinates.hpp"
#include "selfdrive/common/util.h"
#include "selfdrive/common/timing.h"
#include "selfdrive/ui/devui.hpp"
#include "selfdrive/ui/paint.h"

const int lr_w = 180;
const int lr_h = 5;
const int value_fontSize=30;
const int label_fontSize=15;
const int uom_fontSize = 15;
const int bb_uom_dx =  (int)(lr_w/2 - uom_fontSize*2.5);

//DEV START: functions added for the display of various items
static void dev_ui_draw_measure(UIState *s,  const char* bb_value, const char* bb_uom, const char* bb_label,
    Rect *rel_rect, const Rect &rect, NVGcolor bb_valueColor)  {
  nvgTextAlign(s->vg, NVG_ALIGN_CENTER | NVG_ALIGN_BASELINE);
  int dx = 0;
  if (strlen(bb_uom) > 0) {
    dx = (int)(uom_fontSize*2.5/2);
  }

  //print value
  nvgFontFace(s->vg, "sans-semibold");
  nvgFontSize(s->vg, value_fontSize*2.5);
  nvgFillColor(s->vg, bb_valueColor);
  nvgText(s->vg, rel_rect->x-dx/2, rel_rect->y+ (int)(value_fontSize*2.5)+5, bb_value, NULL);

  //print label
  nvgFontFace(s->vg, "sans-regular");
  nvgFontSize(s->vg, label_fontSize*2.5);
  nvgFillColor(s->vg, COLOR_WHITE);
  nvgText(s->vg, rel_rect->x, rel_rect->y + (int)(value_fontSize*2.5)+5 + (int)(label_fontSize*2.5)+5, bb_label, NULL);

  //print uom
  if (strlen(bb_uom) > 0) {
      nvgSave(s->vg);
    int rx = rel_rect->x + bb_uom_dx + value_fontSize -3;
    int ry = rel_rect->y + (int)(value_fontSize*2.5/2)+25;
    nvgTranslate(s->vg,rx,ry);
    nvgRotate(s->vg, -1.5708); //-90deg in radians
    nvgFontFace(s->vg, "sans-regular");
    nvgFontSize(s->vg, (int)(uom_fontSize*2.5));
    nvgFillColor(s->vg, COLOR_WHITE);
    nvgText(s->vg, 0, 0, bb_uom, NULL);
    nvgRestore(s->vg);
  }

  rel_rect->h += (int)((value_fontSize + label_fontSize)*2.5) + 5;
  rel_rect->y = rect.y + rel_rect->h;
}

static void dev_ui_draw_frame(UIState *s, Rect *rel_rect, const Rect &rect) {
  const Rect r = {rect.x, rect.y, rect.w, (((int)((value_fontSize + label_fontSize)*2.5) + 5) * 5) +20};
  ui_fill_rect(s->vg, r, COLOR_BLACK_ALPHA(100), 30.);
  ui_draw_rect(s->vg, r, COLOR_WHITE_ALPHA(100), 6, 20.);
}

static void dev_ui_draw_cpu_temp(UIState *s, Rect *rel_rect, const Rect &rect) {
  //CPU TEMP
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = COLOR_WHITE;
    snprintf(val_str, sizeof(val_str), "%.0f°C", (round((s->scene.deviceState.getCpuTempC()[0]))));
    snprintf(uom_str, sizeof(uom_str), "%d%%", (s->scene.deviceState.getCpuUsagePercent()));
    dev_ui_draw_measure(s,  val_str, uom_str, "CPU TEMP", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_gps_accuracy(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add Ublox GPS accuracy
  const UIScene *scene = &s->scene;
  if (scene->gps_external.getAccuracy() != 0.00) {
    char val_str[16];
    char uom_str[3];
    NVGcolor val_color = COLOR_WHITE;
    //show red/orange if gps accuracy is low
      if(scene->gps_external.getAccuracy() > 0.85) {
         val_color = COLOR_YELLOW;
      }
      if(scene->gps_external.getAccuracy() > 1.3) {
         val_color = COLOR_RED;
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
    dev_ui_draw_measure(s,  val_str, uom_str, "GPS PREC", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_gps_altitude(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add altitude
  const UIScene *scene = &s->scene;
  if (scene->gps_external.getAccuracy() != 0.00) {
    char val_str[16];
    char uom_str[3];
    NVGcolor val_color = COLOR_WHITE;
    snprintf(val_str, sizeof(val_str), "%.1f", (s->scene.gps_external.getAltitude()));
    snprintf(uom_str, sizeof(uom_str), "m");
    dev_ui_draw_measure(s,  val_str, uom_str, "ALTITUDE", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_steering_torque(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add EPS Motor Torque
  if (true) {
    char val_str[16];
    char uom_str[3];
    NVGcolor val_color = COLOR_WHITE; //TODO: Add orange/red color depending on torque intensity. <1x limit = white, btwn 1x-2x limit = orange, >2x limit = red
    snprintf(val_str, sizeof(val_str), "%.0f", (s->scene.car_state.getSteeringTorqueEps()));
    snprintf(uom_str, sizeof(uom_str), "Nm");
    dev_ui_draw_measure(s,  val_str, uom_str, "EPS TRQ", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_aego(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add aEgo
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = COLOR_WHITE;
    snprintf(val_str, sizeof(val_str), "%.1f", (s->scene.car_state.getAEgo()));
    snprintf(uom_str, sizeof(uom_str), "m/s²");
    dev_ui_draw_measure(s,  val_str, uom_str, "ACCEL", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_radar_distance(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add visual radar relative distance
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = COLOR_WHITE;
    if (s->scene.lead_data[0].getStatus()) {
      //show RED if less than 5 meters
      //show orange if less than 15 meters
      if((int)(s->scene.lead_data[0].getDRel()) < 15) {
        val_color = COLOR_YELLOW;
      }
      if((int)(s->scene.lead_data[0].getDRel()) < 5) {
        val_color = COLOR_RED;
      }
      // lead car relative distance is always in meters
      snprintf(val_str, sizeof(val_str), "%d", (int)s->scene.lead_data[0].getDRel());
    } else {
       snprintf(val_str, sizeof(val_str), "-");
    }
    snprintf(uom_str, sizeof(uom_str), "m");
    dev_ui_draw_measure(s,  val_str, uom_str, "REL DIST", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_radar_speed(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add visual radar relative speed
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = COLOR_WHITE;
    if (s->scene.lead_data[0].getStatus()) {
      //show Orange if negative speed (approaching)
      //show Orange if negative speed faster than 5mph (approaching fast)
      if((int)(s->scene.lead_data[0].getVRel()) < 0) {
        val_color = COLOR_YELLOW;
      }
      if((int)(s->scene.lead_data[0].getVRel()) < -5) {
        val_color = COLOR_RED;
      }
      // lead car relative speed is always in meters
      if (s->scene.is_metric) {
         snprintf(val_str, sizeof(val_str), "%d", (int)(s->scene.lead_data[0].getVRel() * 3.6 + 0.5));
      } else {
         snprintf(val_str, sizeof(val_str), "%d", (int)(s->scene.lead_data[0].getVRel() * 2.2374144 + 0.5));
      }
    } else {
       snprintf(val_str, sizeof(val_str), "-");
    }
    if (s->scene.is_metric) {
      snprintf(uom_str, sizeof(uom_str), "km/h");;
    } else {
      snprintf(uom_str, sizeof(uom_str), "mph");
    }
    dev_ui_draw_measure(s,  val_str, uom_str, "REL SPEED", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_steering_angle(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add steering angle
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = COLOR_WHITE;
    //show Orange if more than 6 degrees
    //show red if  more than 12 degrees
    if(((int)(s->scene.car_state.getSteeringAngleDeg()) < -6) || ((int)(s->scene.car_state.getSteeringAngleDeg()) > 6)) {
      val_color = COLOR_YELLOW;
    }
    if(((int)(s->scene.car_state.getSteeringAngleDeg()) < -12) || ((int)(s->scene.car_state.getSteeringAngleDeg()) > 12)) {
      val_color = COLOR_RED;
    }
    // steering is in degrees
    snprintf(val_str, sizeof(val_str), "%.0f°",(s->scene.car_state.getSteeringAngleDeg()));

    snprintf(uom_str, sizeof(uom_str), "");
    dev_ui_draw_measure(s,  val_str, uom_str, "REAL STEER", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_desired_steering_angle(UIState *s, Rect *rel_rect, const Rect &rect) {
  //add desired steering angle
  if (true) {
    char val_str[16];
    char uom_str[6];
    NVGcolor val_color = COLOR_WHITE;
    if (s->scene.controls_state.getEnabled()) {
      float curvature = s->scene.controls_state.getDesiredCurvatureDeg();
      //show Orange if more than 6 degrees
      //show red if  more than 12 degrees
      if(((int)(curvature) < -6) || ((int)(curvature) > 6)) {
        val_color = COLOR_YELLOW;
      }
      if(((int)(curvature) < -12) || ((int)(curvature) > 12)) {
        val_color = COLOR_RED;
      }
      // steering is in degrees
      snprintf(val_str, sizeof(val_str), "%.0f°",(curvature));
    } else {
       snprintf(val_str, sizeof(val_str), "-");
    }
      snprintf(uom_str, sizeof(uom_str), "");
      dev_ui_draw_measure(s,  val_str, uom_str, "DESIR STEER", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_engine_rpm(UIState *s, Rect *rel_rect, const Rect &rect) {
  //engineRPM
  if (true) {
    char val_str[16];
    char uom_str[4];
    NVGcolor val_color = COLOR_WHITE;
    if(((int)(s->scene.car_state.getEngineRPM())) == 0) {
      snprintf(val_str, sizeof(val_str), "OFF");
    } else {
      snprintf(val_str, sizeof(val_str), "%d", (int)(s->scene.car_state.getEngineRPM()));
    }
    snprintf(uom_str, sizeof(uom_str), "");
    dev_ui_draw_measure(s,  val_str, uom_str, "ENG RPM", rel_rect, rect, val_color);
  }
}

static void dev_ui_draw_measures_right(UIState *s, const Rect &rect) {
  Rect rel_rect = {rect.x + (int)(rect.w/2), rect.y, rect.w, rect.h};

  dev_ui_draw_frame(s, &rel_rect, rect);
  dev_ui_draw_cpu_temp(s, &rel_rect, rect);
  dev_ui_draw_radar_distance(s, &rel_rect, rect);
  dev_ui_draw_radar_speed(s, &rel_rect, rect);
  dev_ui_draw_aego(s, &rel_rect, rect);
  dev_ui_draw_engine_rpm(s, &rel_rect, rect);
}

static void dev_ui_draw_measures_left(UIState *s, const Rect &rect) {
  Rect rel_rect = {rect.x + (int)(rect.w/2), rect.y, rect.w, rect.h};

  dev_ui_draw_frame(s, &rel_rect, rect);
  dev_ui_draw_gps_accuracy(s, &rel_rect, rect);
  dev_ui_draw_gps_altitude(s, &rel_rect, rect);
  dev_ui_draw_steering_angle(s, &rel_rect, rect);
  dev_ui_draw_desired_steering_angle(s, &rel_rect, rect);
  dev_ui_draw_steering_torque(s, &rel_rect, rect);
}

void dev_ui_draw_ui(UIState *s)
{
  const Rect l_rect = {(s->viz_rect.x + (bdr_is * 2)), (s->viz_rect.y  + (int)(bdr_is * 1.5)) + 220, lr_w, lr_h};
  const Rect r_rect = {s->viz_rect.x + s->viz_rect.w - lr_w - (bdr_is * 2), (s->viz_rect.y + (int)(bdr_is * 1.5)) + 220, lr_w, lr_h};

  dev_ui_draw_measures_left(s, l_rect);
  dev_ui_draw_measures_right(s, r_rect);
}

//DEV END: functions added for the display of various items
