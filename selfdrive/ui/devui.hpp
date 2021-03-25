#pragma once
#include "ui.hpp"

int dev_ui_draw_measure(UIState *s,  const char* bb_value, const char* bb_uom, const char* bb_label,
    int bb_x, int bb_y, int bb_uom_dx,
    NVGcolor bb_valueColor, NVGcolor bb_labelColor, NVGcolor bb_uomColor,
    int bb_valueFontSize, int bb_labelFontSize, int bb_uomFontSize );

void dev_ui_draw_measures_left(UIState *s, int bb_x, int bb_y, int bb_w );
void dev_ui_draw_measures_right(UIState *s, int bb_x, int bb_y, int bb_w );
void dev_ui_draw_ui(UIState *s);
