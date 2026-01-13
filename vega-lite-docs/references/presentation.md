# Presentation

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Axis
Source: https://vega.github.io/vega-lite/docs/axis.html

Axes provide axis lines, ticks, and labels to convey how a positional range represents a data range. Simply put, axes visualize scales.
By default, Vega-Lite automatically creates axes with default properties for `x` and `y` channels when they encode data fields. User can set the `axis` property of x- or y-field definition (encoding.html#field) to an object to customize axis properties (#axis-properties) or set `axis` to `null` to remove the axis.
Besides `axis` property of a field definition, the configuration object (`config` (config.html)) also provides axis config (#config) (`config: {axis: {...}}`) for setting default axis properties for all axes.
## Documentation Overview
- Axis Properties (#axis-properties)
- General (#general)
- Example: Using Axis `minExtent` to Align Multi-View Plots (#example-using-axis-minextent-to-align-multi-view-plots)
- Domain (#domain)
- Labels (#labels)
- Example: Using Axis `labelExpr` to Display Initial Letters of Month Name (#example-using-axis-labelexpr-to-display-initial-letters-of-month-name)
- Ticks (#ticks)
- Example: Using Axis `tickBand` to Show Grid Between Marks (#example-using-axis-tickband-to-show-grid-between-marks)
- Title (#title)
- Example: Customize Title (#example-customize-title)
- Grid (#grid)
- Conditional Axis Properties (#conditional)
- Example: Conditional Axis Properties and Multi-Line Axis Label (#example-conditional-axis-properties-and-multi-line-axis-label)
- Axis Config (#config)
## Axis Properties
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "field": ...,
      "type": ...,
      "axis": {                // Axis
        ...
      },
      ...
    },
    "y": ...,
    ...
  }
}

```

To customize axis, you can specify an `axis` object in an encoding channels definition (encoding.html). This section lists all properties of axes.
See also: This interactive article (https://beta.observablehq.com/@jheer/a-guide-to-guides-axes-legends-in-vega) demonstrates axes and legends in the underlying Vega language.
### General
| Property | Type | Description |
| --- | --- | --- |
| aria | Boolean | ExprRef | A boolean flag indicating if ARIA attributes should be included (SVG output only). If false , the aria-hidden attribute will be set on the output SVG group, removing the axis from the ARIA accessibility tree. Default value: true |
| bandPosition | Number | ExprRef | An interpolation fraction indicating where, for band scales, axis ticks should be positioned. A value of 0 places ticks at the left edge of their bands. A value of 0.5 places ticks in the middle of their bands. Default value: 0.5 |
| description | String | ExprRef | A text description of this axis for ARIA accessibility (SVG output only). If the aria property is true, for SVG output the aria-label attribute will be set to this description. If the description is unspecified it will be automatically generated. |
| maxExtent | Number | ExprRef | The maximum extent in pixels that axis ticks and labels should use. This determines a maximum offset value for axis titles. Default value: undefined . |
| minExtent | Number | ExprRef | The minimum extent in pixels that axis ticks and labels should use. This determines a minimum offset value for axis titles. Default value: 30 for y-axis; undefined for x-axis. |
| orient | String | ExprRef | The orientation of the axis. One of "top" , "bottom" , "left" or "right" . The orientation can be used to further specialize the axis type (e.g., a y-axis oriented towards the right edge of the chart). Default value: "bottom" for x-axes and "left" for y-axes. |
| offset | Number | ExprRef | The offset, in pixels, by which to displace the axis from the edge of the enclosing group or data rectangle. Default value: derived from the axis config s offset ( 0 by default) |
| position | Number | ExprRef | The anchor position of the axis in pixels. For x-axes with top or bottom orientation, this sets the axis group x coordinate. For y-axes with left or right orientation, this sets the axis group y coordinate. Default value : 0 |
| style | String | String[] | A string or array of strings indicating the name of custom styles to apply to the axis. A style is a named collection of axis property defined within the style configuration . If style is an array, later styles will override earlier styles. Default value: (none) Note: Any specified style will augment the default style. For example, an x-axis mark with "style": "foo" will use config.axisX and config.style.foo (the specified style "foo" has higher precedence). |
| translate | Number | ExprRef | Coordinate space translation offset for axis layout. By default, axes are translated by a 0.5 pixel offset for both the x and y coordinates in order to align stroked lines with the pixel grid. However, for vector graphics output these pixel-specific adjustments may be undesirable, in which case translate can be changed (for example, to zero). Default value: 0.5 |
| zindex | Number | A non-negative integer indicating the z-index of the axis. If zindex is 0, axes should be drawn behind all chart elements. To put them in front, set zindex to 1 or more. Default value: 0 (behind the marks). |

#### Example: Using Axis `minExtent` to Align Multi-View Plots
By default, Vega-Lite automatically sets the axis extent (the space axis ticks and labels use). However, to align axes between multiple plots in multi-view displays, you can manually set `minExtent` (and optionally `maxExtent`) to make the extent consistent across plots.
### Domain
| Property | Type | Description |
| --- | --- | --- |
| domain | Boolean | A boolean flag indicating if the domain (the axis baseline) should be included as part of the axis. Default value: true |
| domainCap | String | ExprRef | The stroke cap for the domain lines ending style. One of "butt" , "round" or "square" . Default value: "butt" |
| domainColor | Null | Color | ExprRef | Color of axis domain line. Default value: "gray" . |
| domainOpacity | Number | ExprRef | Opacity of the axis domain line. |
| domainWidth | Number | ExprRef | Stroke width of axis domain line Default value: 1 |
| domainDash | Number[] | ExprRef | An array of alternating [stroke, space] lengths for dashed domain lines. |
| domainDashOffset | Number | ExprRef | The pixel offset at which to start drawing with the domain dash array. |

### Labels
| Property | Type | Description |
| --- | --- | --- |
| format | Format | The text format specifier for formatting number and date/time in labels of guides (axes, legends, headers) and text marks. If the format type is "number" (e.g., for quantitative fields), this is a D3s number format pattern string . If the format type is "time" (e.g., for temporal fields), this is either: a) D3s time format pattern if you desire to set a static time format. b) dynamic time format specifier object if you desire to set a dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the date lies on a year, month, date, hour, etc. boundary). When used with a custom formatType , this value will be passed as format alongside datum.value to the registered function. Default value: Derived from numberFormat config for number format and from timeFormat config for time format. |
| formatType | String | The format type for labels. One of "number" , "time" , or a registered custom format type . Default value: "time" for temporal fields and ordinal and nominal fields with timeUnit . "number" for quantitative fields as well as ordinal and nominal fields without timeUnit . |
| labels | Boolean | A boolean flag indicating if labels should be included as part of the axis. Default value: true . |
| labelAlign | String | ExprRef | ConditionalAxisString | Horizontal text alignment of axis tick labels, overriding the default setting for the current axis orientation. |
| labelAngle | Number | ExprRef | The rotation angle of the axis labels. Default value: -90 for nominal and ordinal fields; 0 otherwise. |
| labelBaseline | String | ExprRef | ConditionalAxisString | Vertical text baseline of axis tick labels, overriding the default setting for the current axis orientation. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , or "line-bottom" . The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. |
| labelBound | Number | Boolean | ExprRef | Indicates if labels should be hidden if they exceed the axis range. If false (the default) no bounds overlap analysis is performed. If true , labels will be hidden if they exceed the axis range by more than 1 pixel. If this property is a number, it specifies the pixel tolerance: the maximum amount by which a label bounding box may exceed the axis range. Default value: false . |
| labelColor | Null | Color | ExprRef | ConditionalAxisColor | The color of the tick label, can be in hex color code or regular color name. |
| labelExpr | String | Vega expression for customizing labels. Note: The label text and value can be assessed via the label and value properties of the axiss backing datum object. |
| labelFlush | Boolean | Number | Indicates if the first and last axis labels should be aligned flush with the scale range. Flush alignment for a horizontal axis will left-align the first label and right-align the last label. For vertical axes, bottom and top text baselines are applied instead. If this property is a number, it also indicates the number of pixels by which to offset the first and last labels; for example, a value of 2 will flush-align the first and last labels and also push them 2 pixels outward from the center of the axis. The additional adjustment can sometimes help the labels better visually group with corresponding axis ticks. Default value: true for axis of a continuous x-scale. Otherwise, false . |
| labelFlushOffset | Number | ExprRef | Indicates the number of pixels by which to offset flush-adjusted labels. For example, a value of 2 will push flush-adjusted labels 2 pixels outward from the center of the axis. Offsets can help the labels better visually group with corresponding axis ticks. Default value: 0 . |
| labelFont | String | ExprRef | ConditionalAxisString | The font of the tick label. |
| labelFontSize | Number | ExprRef | ConditionalAxisNumber | The font size of the label, in pixels. |
| labelFontStyle | String | ExprRef | ConditionalAxisString | Font style of the title. |
| labelFontWeight | String | Number | ExprRef | ConditionalAxisString | Font weight of axis tick labels. |
| labelLimit | Number | ExprRef | Maximum allowed pixel width of axis tick labels. Default value: 180 |
| labelLineHeight | Number | ExprRef | Line height in pixels for multi-line label text or label text with "line-top" or "line-bottom" baseline. |
| labelOffset | Number | ExprRef | ConditionalAxisNumber | Position offset in pixels to apply to labels, in addition to tickOffset. Default value: 0 |
| labelOpacity | Number | ExprRef | ConditionalAxisNumber | The opacity of the labels. |
| labelOverlap | String | ExprRef | The strategy to use for resolving overlap of axis labels. If false (the default), no overlap reduction is attempted. If set to true or "parity" , a strategy of removing every other label is used (this works well for standard linear axes). If set to "greedy" , a linear scan of the labels is performed, removing any labels that overlaps with the last visible label (this often works better for log-scaled axes). Default value: true for non-nominal fields with non-log scales; "greedy" for log scales; otherwise false . |
| labelPadding | Number | ExprRef | ConditionalAxisNumber | The padding in pixels between labels and ticks. Default value: 2 |
| labelSeparation | Number | ExprRef | The minimum separation that must be between label bounding boxes for them to be considered non-overlapping (default 0 ). This property is ignored if labelOverlap resolution is not enabled. |

See also: `guide-label` style config (mark.html#style-config) (common styles for axis, legend (legend.html), and header (facet.html#header) labels).
#### Example: Using Axis `labelExpr` to Display Initial Letters of Month Name
### Ticks
| Property | Type | Description |
| --- | --- | --- |
| ticks | Boolean | Boolean value that determines whether the axis should include ticks. Default value: true |
| tickBand | String | ExprRef | For band scales, indicates if ticks and grid lines should be placed at the "center" of a band (default) or at the band "extent" s to indicate intervals |
| tickCap | String | ExprRef | The stroke cap for the tick lines ending style. One of "butt" , "round" or "square" . Default value: "butt" |
| tickColor | Null | Color | ExprRef | ConditionalAxisColor | The color of the axiss tick. Default value: "gray" |
| tickCount | Number | String | Object | ExprRef | A desired number of ticks, for axes visualizing quantitative scales. The resulting number may be different so that values are nice (multiples of 2, 5, 10) and lie within the underlying scales range. For scales of type "time" or "utc" , the tick count can instead be a time interval specifier. Legal string values are "millisecond" , "second" , "minute" , "hour" , "day" , "week" , "month" , and "year" . Alternatively, an object-valued interval specifier of the form {"interval": "month", "step": 3} includes a desired number of interval steps. Here, ticks are generated for each quarter (Jan, Apr, Jul, Oct) boundary. Default value : Determine using a formula ceil(width/40) for x and ceil(height/40) for y. |
| tickDash | Number[] | ExprRef | ConditionalAxisNumberArray | An array of alternating [stroke, space] lengths for dashed tick mark lines. |
| tickExtra | Boolean | Boolean flag indicating if an extra axis tick should be added for the initial position of the axis. This flag is useful for styling axes for band scales such that ticks are placed on band boundaries rather in the middle of a band. Use in conjunction with "bandPosition": 1 and an axis "padding" value of 0 . |
| tickMinStep | Number | ExprRef | The minimum desired step between axis ticks, in terms of scale domain values. For example, a value of 1 indicates that ticks should not be less than 1 unit apart. If tickMinStep is specified, the tickCount value will be adjusted, if necessary, to enforce the minimum step value. |
| tickOffset | Number | ExprRef | Position offset in pixels to apply to ticks, labels, and gridlines. |
| tickOpacity | Number | ExprRef | ConditionalAxisNumber | Opacity of the ticks. |
| tickRound | Boolean | Boolean flag indicating if pixel position values should be rounded to the nearest integer. Default value: true |
| tickSize | Number | ExprRef | ConditionalAxisNumber | The size in pixels of axis ticks. Default value: 5 |
| tickWidth | Number | ExprRef | ConditionalAxisNumber | The width, in pixels, of ticks. Default value: 1 |
| values | Number[] | String[] | Boolean[] | DateTime [] | ExprRef | Explicitly set the visible axis tick values. |

#### Example: Using Axis `tickBand` to Show Grid Between Marks
Using `tickBand`, we can change the axis ticks and gridlines to be drawn between marks.
### Title
| Property | Type | Description |
| --- | --- | --- |
| title | Text | Null | A title for the field. If null , the title will be removed. Default value: derived from the fields name and transformation function ( aggregate , bin and timeUnit ). If the field has an aggregate function, the function is displayed as part of the title (e.g., "Sum of Profit" ). If the field is binned or has a time unit applied, the applied function is shown in parentheses (e.g., "Profit (binned)" , "Transaction Date (year-month)" ). Otherwise, the title is simply the field name. Notes : 1) You can customize the default field title format by providing the fieldTitle property in the config or fieldTitle function via the compile functions options . 2) If both field definitions title and axis, header, or legend title are defined, axis/header/legend title will be used. |
| titleAlign | String | ExprRef | Horizontal text alignment of axis titles. |
| titleAnchor | Null | String | ExprRef | Text anchor position for placing axis titles. |
| titleAngle | Number | ExprRef | Angle in degrees of axis titles. |
| titleBaseline | String | ExprRef | Vertical text baseline for axis titles. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , or "line-bottom" . The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. |
| titleColor | Null | Color | ExprRef | Color of the title, can be in hex color code or regular color name. |
| titleFont | String | ExprRef | Font of the title. (e.g., "Helvetica Neue" ). |
| titleFontSize | Number | ExprRef | Font size of the title. |
| titleFontStyle | String | ExprRef | Font style of the title. |
| titleFontWeight | String | Number | ExprRef | Font weight of the title. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| titleLimit | Number | ExprRef | Maximum allowed pixel width of axis titles. |
| titleLineHeight | Number | ExprRef | Line height in pixels for multi-line title text or title text with "line-top" or "line-bottom" baseline. |
| titleOpacity | Number | ExprRef | Opacity of the axis title. |
| titlePadding | Number | ExprRef | The padding, in pixels, between title and axis. |
| titleX | Number | ExprRef | X-coordinate of the axis title relative to the axis group. |
| titleY | Number | ExprRef | Y-coordinate of the axis title relative to the axis group. |

#### Example: Customize Title
For example, the following plot has a customized x-axis title.
See also: Axis Title Config (#title-config) and `guide-title` style config (mark.html#style-config) (common styles for axis, legend (legend.html), and header (facet.html#header) titles).
### Grid
| Property | Type | Description |
| --- | --- | --- |
| grid | Boolean | A boolean flag indicating if grid lines should be included as part of the axis Default value: true for continuous scales that are not binned; otherwise, false . |
| gridCap | String | ExprRef | The stroke cap for grid lines ending style. One of "butt" , "round" or "square" . Default value: "butt" |
| gridColor | Null | Color | ExprRef | ConditionalAxisColor | Color of gridlines. Default value: "lightGray" . |
| gridDash | Number[] | ExprRef | ConditionalAxisNumberArray | An array of alternating [stroke, space] lengths for dashed grid lines. |
| gridOpacity | Number | ExprRef | ConditionalAxisNumber | The stroke opacity of grid (value between [0,1]) Default value: 1 |
| gridWidth | Number | ExprRef | ConditionalAxisNumber | The grid width, in pixels. Default value: 1 |

### Conditional Axis Properties
We can set axis properties (which can be of type ConditionalAxisProperty) to a conditional value definition (condition.html#value).
Note that each axis tick, grid line, and label instance is backed by a data object with the following fields, which may be accessed as part of the test condition in a condition axis property.
- `label` - the string label
- `value` - the data value
- `index` - fractional tick index (`0` for the first tick and `1` for the last tick)
### Example: Conditional Axis Properties and Multi-Line Axis Label
In the following example, we adjust the `gridDash` and `tickDash` properties in a line chart based on whether a particular grid line falls on a year boundary. We also use the `labelExpr` property to show multi-line labels for year and month, showing the year number only for January of each year.
We can also conditionally hide some labels and ticks in the following Lasagna plot using conditional `labelColor` and `tickColor`:
## Axis Config
```
// Top-level View Specification
{
  ...
  "config": {
    "axis": : ...,
    "axisX": : ...,
    "axisY": : ...,
    "axisLeft": : ...,
    "axisRight": : ...,
    "axisTop": : ...,
    "axisBottom": : ...,
    "axisBand": : ...,
    "axisQuantitative": : ...,
    "axisTemporal": : ...,
    ...
  }
}

```

Axis configuration defines default settings for axes. Properties defined under the `"axis"` property in the top-level `config` (config.html) object are applied to all axes.
Additional property blocks can target more specific axis types based on the orientation (`"axisX"`, `"axisY"`, `"axisLeft"`, `"axisTop"`, etc.), band scale type (`"axisBand"`), scales data type (`"axisDiscrete"`, `"axisQuantitative"`, and `"axisTemporal"`), or both orientation and scale/data type (e.g., `"axisXTemporal"`). For example, properties defined under the `"axisBand"` property will only apply to axes visualizing `"band"` scales.
An axis configuration supports all axis properties (#properties) except `position`, `orient`, `format`, `values`, and `zindex`. In addition, it also supports the `disable` property:
| Property | Type | Description |
| --- | --- | --- |
| disable | Boolean | Disable axis by default. |

Note:
-
If multiple axis config blocks apply to a single axis, type-based options take precedence over orientation-based options, which in turn take precedence over general options.
-
If an axis config has a style property, the style will have lower precedence than any of the axis config properties.
-
In summary, here is the precedence level order for each axis property (from the highest to the lowest):
- Axis properties (`axis.*`)
- Axis style (`config.axis[axis.style].*`)
- Orientation and type based axis config (e.g., `config.axisXBand.*`)
- Type-based axis config (e.g., `config.axisBand.*`)
- Orientation-based axis config (`config.axisX/Y.*`)
- General axis config (`config.axis.*`)
- Style of orientation and type based axis config (e.g., `config.style[config.axisXBand.style].*`)
- Style of type-based axis config (e.g., `config.style[config.axisBand.style].*`)
- Style of orientation-based axis config (e.g., `config.style[config.axisX.style].*`)
- Style general axis config (`config.style[config.axis.style].*`)
See also: Axis Labels Properties (#labels) and `guide-label` style config (mark.html#style-config) (common styles for by axis, legend (legend.html), and header (facet.html#header) labels).

## Legend
Source: https://vega.github.io/vega-lite/docs/legend.html

Similar to axes (axis.html), legends visualize scales. However, whereas axes aid interpretation of scales with positional ranges, legends aid interpretation of scales with ranges such as colors, shapes and sizes.
By default, Vega-Lite automatically creates legends with default properties for `color`, `opacity`, `size`, and `shape` channels when they encode data fields. User can set the `legend` property of a mark property channels field definition (encoding.html#mark-prop) to an object to customize legend properties (#legend-properties) or set `legend` to `null` to remove the legend.
Besides `legend` property of a field definition, the configuration object (`config` (config.html)) also provides legend config (#config) (`config: {legend: {...}}`) for setting default legend properties for all legends.
- Legend Types (#legend-types)
- Combined Legend (#combined-legend)
- Legend Properties (#legend-properties)
- General (#properties)
- Gradient (#gradient)
- Labels (#labels)
- Symbols (#symbols)
- Symbol Layout (#symbol-layout)
- Title (#title)
- Legend Config (#config)
## Legend Types
By default, Vega-Lite automatically generates gradient legends for color channels with non-binned quantitative fields and temporal fields.
Otherwise, symbol legends are generated.
## Combined Legend
If multiple channels encode the same fields, Vega-Lite automatically combines their legends. For example, the following plot uses both `color` and `shape` to encode `Origin`; as a result, its legend shows the encoded colors and shapes.
## Legend Properties
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": ...,
    "y": ...,
    "color": {
      "field": ...,
      "type": ...,
      "legend": {                // legend
        ...
      },
      ...
    },
    ...
  }
}

```

To customize legends, you can specify a `legend` object in an encoding channels definition (encoding.html). This section lists all properties of legends.
See also: This interactive article (https://beta.observablehq.com/@jheer/a-guide-to-guides-axes-legends-in-vega) demonstrates axes and legends in the underlying Vega language.
### General
| Property | Type | Description |
| --- | --- | --- |
| aria | Boolean | ExprRef | A boolean flag indicating if ARIA attributes should be included (SVG output only). If false , the aria-hidden attribute will be set on the output SVG group, removing the legend from the ARIA accessibility tree. Default value: true |
| cornerRadius | Number | ExprRef | Corner radius for the full legend. |
| description | String | ExprRef | A text description of this legend for ARIA accessibility (SVG output only). If the aria property is true, for SVG output the aria-label attribute will be set to this description. If the description is unspecified it will be automatically generated. |
| direction | String | The direction of the legend, one of "vertical" or "horizontal" . Default value: For top-/bottom- orient ed legends, "horizontal" For left-/right- orient ed legends, "vertical" For top/bottom-left/right- orient ed legends, "horizontal" for gradient legends and "vertical" for symbol legends. |
| fillColor | Null | Color | ExprRef | Background fill color for the full legend. |
| legendX | Number | ExprRef | Custom x-position for legend with orient none. |
| legendY | Number | ExprRef | Custom y-position for legend with orient none. |
| offset | Number | ExprRef | The offset in pixels by which to displace the legend from the data rectangle and axes. Default value: 18 . |
| orient | String | The orientation of the legend, which determines how the legend is positioned within the scene. One of "left" , "right" , "top" , "bottom" , "top-left" , "top-right" , "bottom-left" , "bottom-right" , "none" . Default value: "right" |
| padding | Number | ExprRef | The padding between the border and content of the legend group. Default value: 0 . |
| strokeColor | Null | Color | ExprRef | Border stroke color for the full legend. |
| type | String | The type of the legend. Use "symbol" to create a discrete legend and "gradient" for a continuous color gradient. Default value: "gradient" for non-binned quantitative fields and temporal fields; "symbol" otherwise. |
| tickCount | TickCount | ExprRef | The desired number of tick values for quantitative legends. |
| values | Number[] | String[] | Boolean[] | DateTime [] | ExprRef | Explicitly set the visible legend values. |
| zindex | Number | A non-negative integer indicating the z-index of the legend. If zindex is 0, legend should be drawn behind all chart elements. To put them in front, use zindex = 1. |

### Gradient
| Property | Type | Description |
| --- | --- | --- |
| gradientLength | Number | ExprRef | The length in pixels of the primary axis of a color gradient. This value corresponds to the height of a vertical gradient or the width of a horizontal gradient. Default value: 200 . |
| gradientOpacity | Number | ExprRef | Opacity of the color gradient. |
| gradientStrokeColor | Null | Color | ExprRef | The color of the gradient stroke, can be in hex color code or regular color name. Default value: "lightGray" . |
| gradientStrokeWidth | Number | ExprRef | The width of the gradient stroke, in pixels. Default value: 0 . |
| gradientThickness | Number | ExprRef | The thickness in pixels of the color gradient. This value corresponds to the width of a vertical gradient or the height of a horizontal gradient. Default value: 16 . |

### Labels
| Property | Type | Description |
| --- | --- | --- |
| format | Format | The text format specifier for formatting number and date/time in labels of guides (axes, legends, headers) and text marks. If the format type is "number" (e.g., for quantitative fields), this is a D3s number format pattern string . If the format type is "time" (e.g., for temporal fields), this is either: a) D3s time format pattern if you desire to set a static time format. b) dynamic time format specifier object if you desire to set a dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the date lies on a year, month, date, hour, etc. boundary). When used with a custom formatType , this value will be passed as format alongside datum.value to the registered function. Default value: Derived from numberFormat config for number format and from timeFormat config for time format. |
| formatType | String | The format type for labels. One of "number" , "time" , or a registered custom format type . Default value: "time" for temporal fields and ordinal and nominal fields with timeUnit . "number" for quantitative fields as well as ordinal and nominal fields without timeUnit . |
| labelAlign | String | ExprRef | The alignment of the legend label, can be left, center, or right. |
| labelBaseline | String | ExprRef | The position of the baseline of legend label, can be "top" , "middle" , "bottom" , or "alphabetic" . Default value: "middle" . |
| labelColor | Null | Color | ExprRef | The color of the legend label, can be in hex color code or regular color name. |
| labelExpr | String | Vega expression for customizing labels. Note: The label text and value can be assessed via the label and value properties of the legends backing datum object. |
| labelFont | String | ExprRef | The font of the legend label. |
| labelFontSize | Number | ExprRef | The font size of legend label. Default value: 10 . |
| labelFontStyle | String | ExprRef | The font style of legend label. |
| labelLimit | Number | ExprRef | Maximum allowed pixel width of legend tick labels. Default value: 160 . |
| labelOffset | Number | ExprRef | The offset of the legend label. Default value: 4 . |
| labelOverlap | String | ExprRef | The strategy to use for resolving overlap of labels in gradient legends. If false , no overlap reduction is attempted. If set to true (default) or "parity" , a strategy of removing every other label is used. If set to "greedy" , a linear scan of the labels is performed, removing any label that overlaps with the last visible label (this often works better for log-scaled axes). Default value: true . |

### Symbols
| Property | Type | Description |
| --- | --- | --- |
| symbolDash | Number[] | ExprRef | An array of alternating [stroke, space] lengths for dashed symbol strokes. |
| symbolDashOffset | Number | ExprRef | The pixel offset at which to start drawing with the symbol stroke dash array. |
| symbolFillColor | Null | Color | ExprRef | The color of the legend symbol, |
| symbolOffset | Number | ExprRef | Horizontal pixel offset for legend symbols. Default value: 0 . |
| symbolOpacity | Number | ExprRef | Opacity of the legend symbols. |
| symbolSize | Number | ExprRef | The size of the legend symbol, in pixels. Default value: 100 . |
| symbolStrokeColor | Null | Color | ExprRef | Stroke color for legend symbols. |
| symbolStrokeWidth | Number | ExprRef | The width of the symbols stroke. Default value: 1.5 . |
| symbolType | String | ExprRef | The symbol shape. One of the plotting shapes circle (default), square , cross , diamond , triangle-up , triangle-down , triangle-right , or triangle-left , the line symbol stroke , or one of the centered directional shapes arrow , wedge , or triangle . Alternatively, a custom SVG path string can be provided. For correct sizing, custom shape paths should be defined within a square bounding box with coordinates ranging from -1 to 1 along both the x and y dimensions. Default value: "circle" . |

### Symbol Layout
| Property | Type | Description |
| --- | --- | --- |
| clipHeight | Number | ExprRef | The height in pixels to clip symbol legend entries and limit their size. |
| columnPadding | Number | ExprRef | The horizontal padding in pixels between symbol legend entries. Default value: 10 . |
| columns | Number | ExprRef | The number of columns in which to arrange symbol legend entries. A value of 0 or lower indicates a single row with one column per entry. |
| gridAlign | String | ExprRef | The alignment to apply to symbol legends rows and columns. The supported string values are "all" , "each" (the default), and none . For more information, see the grid layout documentation . Default value: "each" . |
| rowPadding | Number | ExprRef | The vertical padding in pixels between symbol legend entries. Default value: 2 . |
| symbolLimit | Number | ExprRef | The maximum number of allowed entries for a symbol legend. Additional entries will be dropped. |

### Title
| Property | Type | Description |
| --- | --- | --- |
| title | Text | Null | A title for the field. If null , the title will be removed. Default value: derived from the fields name and transformation function ( aggregate , bin and timeUnit ). If the field has an aggregate function, the function is displayed as part of the title (e.g., "Sum of Profit" ). If the field is binned or has a time unit applied, the applied function is shown in parentheses (e.g., "Profit (binned)" , "Transaction Date (year-month)" ). Otherwise, the title is simply the field name. Notes : 1) You can customize the default field title format by providing the fieldTitle property in the config or fieldTitle function via the compile functions options . 2) If both field definitions title and axis, header, or legend title are defined, axis/header/legend title will be used. |
| titleAlign | String | ExprRef | Horizontal text alignment for legend titles. Default value: "left" . |
| titleAnchor | Null | String | ExprRef | Text anchor position for placing legend titles. |
| titleBaseline | String | ExprRef | Vertical text baseline for legend titles. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , or "line-bottom" . The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. Default value: "top" . |
| titleColor | Null | Color | ExprRef | The color of the legend title, can be in hex color code or regular color name. |
| titleFont | String | ExprRef | The font of the legend title. |
| titleFontSize | Number | ExprRef | The font size of the legend title. |
| titleFontStyle | String | ExprRef | The font style of the legend title. |
| titleFontWeight | String | Number | ExprRef | The font weight of the legend title. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| titleLimit | Number | ExprRef | Maximum allowed pixel width of legend titles. Default value: 180 . |
| titleLineHeight | Number | ExprRef | Line height in pixels for multi-line title text or title text with "line-top" or "line-bottom" baseline. |
| titleOpacity | Number | ExprRef | Opacity of the legend title. |
| titlePadding | Number | ExprRef | The padding, in pixels, between title and legend. Default value: 5 . |

## Legend Config
```
// Top-level View Specification
{
  ...
  "config": {
    "legend": {
      ...
    }
  }
}

```

To provide themes for all legends, the legend config (`config: {legend: {...}}`) supports all legend properties (#properties) except `direction` (there are legend-specific `gradientDirection` and `symbolDirection` instead), `format`, `tickCount`, `values`, and `zindex`.
The legend configuration also supports the following properties:
| Property | Type | Description |
| --- | --- | --- |
| disable | Boolean | Disable legend by default |
| gradientDirection | String | ExprRef | The default direction ( "horizontal" or "vertical" ) for gradient legends. Default value: "vertical" . |
| gradientHorizontalMaxLength | Number | Max legend length for a horizontal gradient when config.legend.gradientLength is undefined. Default value: 200 |
| gradientHorizontalMinLength | Number | Min legend length for a horizontal gradient when config.legend.gradientLength is undefined. Default value: 100 |
| gradientLabelLimit | Number | ExprRef | The maximum allowed length in pixels of color ramp gradient labels. |
| gradientLabelOffset | Number | ExprRef | Vertical offset in pixels for color ramp gradient labels. Default value: 2 . |
| gradientVerticalMaxLength | Number | Max legend length for a vertical gradient when config.legend.gradientLength is undefined. Default value: 200 |
| gradientVerticalMinLength | Number | Min legend length for a vertical gradient when config.legend.gradientLength is undefined. Default value: 100 |
| symbolBaseFillColor | Null | Color | ExprRef | Default fill color for legend symbols. Only applied if there is no "fill" scale color encoding for the legend. Default value: "transparent" . |
| symbolBaseStrokeColor | Null | Color | ExprRef | Default stroke color for legend symbols. Only applied if there is no "fill" scale color encoding for the legend. Default value: "gray" . |
| symbolDirection | String | ExprRef | The default direction ( "horizontal" or "vertical" ) for symbol legends. Default value: "vertical" . |
| unselectedOpacity | Number | The opacity of unselected legend entries. Default value: 0.35. |

## Scale
Source: https://vega.github.io/vega-lite/docs/scale.html

Scales are functions that transform a domain of data values (numbers, dates, strings, etc.) to a range of visual values (pixels, colors, sizes). Internally, Vega-Lite uses Vega scales (https://vega.github.io/vega/docs/scales/), which are derived from the d3-scale (https://github.com/d3/d3-scale) library. For more background about scales, please see Introducing d3-scale (https://medium.com/@mbostock/introducing-d3-scale-61980c51545f) by Mike Bostock.
Vega-Lite automatically creates scales for fields that are mapped to position (encoding.html#position) and mark property (encoding.html#mark-prop) channels. To customize the scale of a field, users can provide a `scale` object as a part of the field definition (encoding.html#field) to customize scale properties (e.g., type (#type), domain (#domain), and range (#range)).
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "field": ...,
      "type": ...,
      "scale": {                // scale
        "type": ...,
        ...
      },
      ...
    },
    "y": ...,
    ...
  },
  ...
}

```

Besides the `scale` property of each encoding channel, the top-level configuration object (`config` (config.html)) also provides scale config (#config) (`config: {scale: {...}}`) for setting default scale properties for all scales.
For more information about guides that visualize the scales, please see the axes (axis.html) and legends (legend.html) pages.
## Documentation Overview
- Scale Types (#type)
- Scale Domains (#domain)
- Example: Customizing Domain for a Time Scale (#example-customizing-domain-for-a-time-scale)
- Example: Clipping or Removing Unwanted Data Points (#example-clipping-or-removing-unwanted-data-points)
- Example: Using `domainRaw` to bind domain interactively (#example-using-domainraw-to-bind-domain-interactively)
- Scale Ranges (#range)
- Example: Setting Color Range based on a Field (#example-setting-color-range-based-on-a-field)
- Example: Setting Range Min/Max (#example-setting-range-minmax)
- Color Schemes (#scheme)
- 1. Set a custom `scheme`. (#1-set-a-custom-scheme)
- 2. Setting the `range` property to an array of valid CSS color strings. (#2-setting-the-range-property-to-an-array-of-valid-css-color-strings)
- 3. Change the default color schemes using the range config. (#3-change-the-default-color-schemes-using-the-range-config)
- Common Scale Properties (#continuous)
- Continuous Scales (#continuous-scales)
- Linear Scales (#linear)
- Power Scales (#pow)
- Square Root Scales (#sqrt)
- Logarithmic Scales (#log)
- Symlog Scales (#symlog)
- Time and UTC Scales (#time)
- Piecewise and Diverging Scales (#piecewise)
- Discrete Scales (#discrete)
- Ordinal Scales (#ordinal)
- Band and Point Scales (#band)
- Discretizing Scales (#discretizing)
- Bin-Linear Scales (#bin-linear)
- Bin-Ordinal Scales (#bin-ordinal)
- Bins Parameter (#bins)
- Quantile Scales (#quantile)
- Quantize Scales (#quantize)
- Threshold Scales (#threshold)
- Disabling Scale (#disable)
- Configuration (#config)
- Scale Config (#scale-config)
- Padding (#padding)
- Range (#range)
- Scale Output for Invalid Values (#scale-output-for-invalid-values)
- Other (#other)
- Range Config (#range-config)
## Scale Types
The `type` property can be specified to customize the scale type.
| Property | Type | Description |
| --- | --- | --- |
| type | String | The type of scale. Vega-Lite supports the following categories of scale types: 1) Continuous Scales  mapping continuous domains to continuous output ranges ( "linear" , "pow" , "sqrt" , "symlog" , "log" , "time" , "utc" . 2) Discrete Scales  mapping discrete domains to discrete ( "ordinal" ) or continuous ( "band" and "point" ) output ranges. 3) Discretizing Scales  mapping continuous domains to discrete output ranges "bin-ordinal" , "quantile" , "quantize" and "threshold" . Default value: please see the scale type table . |

By default, Vega-Lite use the following scale types for the following data types (type.html) and encoding channels (encoding.html#channel):
|  | Nominal / Ordinal | Quantitative | Bin-Quantitative 1 | Temporal |
| --- | --- | --- | --- | --- |
| X, Y | Band / Point 2 | Linear | Linear | Time |
| Size, Opacity | Point | Linear | Linear | Time |
| Color | Ordinal | Linear | Bin-Ordinal | Linear |
| Shape | Ordinal | N/A | N/A | N/A |

 1 Quantitative fields with the `bin` (bin.html) transform.   2 For positional (x and y) nominal and ordinal fields, `"band"` scale is the default scale type for bar, image, rect, and rule marks while `"point"` is the default scales for all other marks.
## Scale Domains
By default, a scale in Vega-Lite draws domain values directly from a channels encoded field. Users can specify the `domain` property of a scale to customize its domain values. To sort the order of the domain of the encoded, the `sort` (sort.html) property of a field definition (encoding.html#field-def) can be specified.
| Property | Type | Description |
| --- | --- | --- |
| domain | Null[] | String[] | Number[] | Boolean[] | DateTime [] | ExprRef [] | String | ParameterExtent | DomainUnionWith | ExprRef | Customized domain values in the form of constant values or dynamic values driven by a parameter. 1) Constant domain for quantitative fields can take one of the following forms: A two-element array with minimum and maximum values. To create a diverging scale, this two-element array can be combined with the domainMid property. An array with more than two entries, for Piecewise quantitative scales . A string value "unaggregated" , if the input field is aggregated, to indicate that the domain should include the raw data values prior to the aggregation. 2) Constant domain for temporal fields can be a two-element array with minimum and maximum values, in the form of either timestamps or the DateTime definition objects . 3) Constant domain for ordinal and nominal fields can be an array that lists valid input values. 4) To combine (union) specified constant domain with the fields values, domain can be an object with a unionWith property that specify constant domain to be combined. For example, domain: {unionWith: [0, 100]} for a quantitative scale means that the scale domain always includes [0, 100] , but will include other values in the fields beyond [0, 100] . 5) Domain can also takes an object defining a field or encoding of a parameter that interactively determines the scale domain. |
| domainMax | Number | DateTime | ExprRef | Sets the maximum value in the scale domain, overriding the domain property. This property is only intended for use with scales having continuous domains. |
| domainMin | Number | DateTime | ExprRef | Sets the minimum value in the scale domain, overriding the domain property. This property is only intended for use with scales having continuous domains. |
| domainMid | Number | ExprRef | Inserts a single mid-point value into a two-element domain. The mid-point value must lie between the domain minimum and maximum values. This property can be useful for setting a midpoint for diverging color scales . The domainMid property is only intended for use with scales supporting continuous, piecewise domains. |
| domainRaw | ExprRef | An expression for an array of raw values that, if non-null, directly overrides the domain property. This is useful for supporting interactions such as panning or zooming a scale. The scale may be initially determined using a data-driven domain, then modified in response to user input by setting the rawDomain value. |

A common use case for the `domain` property is to limit, for example, the `x` range of values to include in a plot. However, setting the domain property alone is insufficient to achieve the desired effect.
### Example: Customizing Domain for a Time Scale
For a time scale, we can set scale domain to an array datetime objects (types.html#datetime), as shown below.
### Example: Clipping or Removing Unwanted Data Points
For example, consider the line plot specification below in which the `x` domain is restricted to the range `[300, 450]`.
There are two approaches to keep the mark from being plotted outside the desired `x` range of values.
-
The first one is to set `clip: true` in mark definition.
-
The second approach is to use `transform`. Note that these two approaches have slightly different behaviors. Using `transform` removes unwanted data points, yet setting `clip` to `true` clips the mark to be the enclosing groups width and height.
### Example: Using `domainRaw` to bind domain interactively
## Scale Ranges
The range of the scale represents the set of output visual values. Vega-Lite automatically determines the default range for each encoding channel (encoding.html#channel) using the following rules:
| Channels | Default Range |
| --- | --- |
| x | The range is by default [0, width] . |
| y | The range is by default [0, height] . |
| opacity | Derived from the scale config s min/maxOpacity . |
| color | Derived from the following named ranges based on the fields type :  "category" for nominal fields.  "ordinal" for ordinal fields.  "heatmap" for quantitative and temporal fields with "rect" marks and "ramp' for other marks. See the color scheme section for examples. |
| size | Derived from the following named ranges based on the mark type:  min/maxBandSize for bar and tick.  min/maxStrokeWidth for line and rule.  min/maxSize for point, square, and circle  min/maxFontSize for text |
| shape | Derived from the pre-defined named range "symbol" . |

To customize range values, users can directly specify `range` or specify the special `scheme` (#scheme) property for ordinal (#ordinal) and continuous (#continuous) color scales.
| Property | Type | Description |
| --- | --- | --- |
| range | String | Number[] | String[] | Number[] | ExprRef [] | FieldRange | The range of the scale. One of: A string indicating a pre-defined named scale range (e.g., example, "symbol" , or "diverging" ). For continuous scales , two-element array indicating minimum and maximum values, or an array with more than two entries for specifying a piecewise scale . For discrete and discretizing scales, an array of desired output values or an object with a field property representing the range values. For example, if a field color contains CSS color names, we can set range to {field: "color"} . Notes: 1) For color scales you can also specify a color scheme instead of range . 2) Any directly specified range for x and y channels will be ignored. Range can be customized via the views corresponding size ( width and height ). |
| rangeMin | Number | String | ExprRef | Sets the minimum value in the scale range, overriding the range property or the default range. This property is only intended for use with scales having continuous ranges. |
| rangeMax | Number | String | ExprRef | Sets the maximum value in the scale range, overriding the range property or the default range. This property is only intended for use with scales having continuous ranges. |

### Example: Setting Color Range based on a Field
In this example, we create a scale that maps the field `"l"` to colors specified in the field `"c"`:
Note: This only works if there is a 1:1 mapping between the color domain field (`l`) and the range field (`c`).
### Example: Setting Range Min/Max
We may use `rangeMin` if we want to override just the minimum value of the range, while keeping the default maximum value of the range.
Similarly, we may use `rangeMax` if we want to override just the maximum value of the range, while keeping the default minimum value of the range.
### Color Schemes
Color schemes provide a set of named color palettes as a scale range for the `color` channel. Vega-Lite (via Vega) provides a collection of perceptually-motivated color schemes, many of which are drawn from the d3-scale (https://github.com/d3/d3-scale), d3-scale-chromatic (https://github.com/d3/d3-scale-chromatic), and ColorBrewer (http://colorbrewer2.org/) projects.
By default, Vega-Lite assigns different default color schemes (#range-config) based on the types of the encoded fields:
- Nominal fields use the `"categorical"` pre-defined named range (#range-config) (the `"tableau10"` (https://vega.github.io/vega/docs/schemes/#tableau10) scheme by default).
- Ordinal fields use the `"ordinal"` pre-defined named color range (#range-config) (the `"blues"` (https://vega.github.io/vega/docs/schemes/#blues) color scheme by default).
- Quantitative and temporal fields use the pre-defined named color range (#range-config) `"heatmap"` (the `"viridis"` (https://vega.github.io/vega/docs/schemes/#viridis) scheme by default) for rect marks and `"ramp"` (the `"blues"` (https://vega.github.io/vega/docs/schemes/#blues) scheme by default) for other marks.
There are multiple ways to customize the scale range for the color encoding channel:
#### 1. Set a custom `scheme`.
| Property | Type | Description |
| --- | --- | --- |
| scheme | ColorScheme | SchemeParams | ExprRef | A string indicating a color scheme name (e.g., "category10" or "blues" ) or a scheme parameter object . Discrete color schemes may be used with discrete or discretizing scales. Continuous color schemes are intended for use with color scales. To set a custom scheme, instead set the list of values as the scale range . For the full list of supported schemes, please refer to the Vega Scheme reference. |

You can customize the scheme by referencing an existing color scheme (https://vega.github.io/vega/docs/schemes/). For example, the following plot uses the `"category20b"` scheme.
The `scheme` property can also be a scheme parameter object, which contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| name | ColorScheme | Required. A color scheme name for ordinal scales (e.g., "category10" or "blues" ). For the full list of supported schemes, please refer to the Vega Scheme reference. |
| extent | Number[] | The extent of the color range to use. For example [0.2, 1] will rescale the color scheme such that color values in the range [0, 0.2) are excluded from the scheme. |
| count | Number | The number of colors to use in the scheme. This can be useful for scale types such as "quantize" , which use the length of the scale range to determine the number of discrete bins for the scale domain. |

#### 2. Setting the `range` property to an array of valid CSS color strings.
#### 3. Change the default color schemes using the range config.
See the range config (#range-config) documentation for details.
## Common Scale Properties
In addition to `type`, `domain`, and `range`, all scales share the following properties:
| Property | Type | Description |
| --- | --- | --- |
| reverse | Boolean | ExprRef | If true, reverses the order of the scale range. Default value: false . |
| round | Boolean | ExprRef | If true , rounds numeric output values to integers. This can be helpful for snapping to the pixel grid. Default value: false . |

## Continuous Scales
Continuous scales map a continuous domain (numbers or dates) to a continuous output range (pixel locations, sizes, colors). Supported continuous scale types for quantitative fields are `"linear"` (#linear), `"log"` (#log), `"pow"` (#pow), `"sqrt"` (#sqrt), and `"symlog"` (#symlog). Meanwhile, supported continuous scale types for temporal fields are `"time"` (#time), `"utc"` (#utc), and `"symlog"` (#symlog).
By default, Vega-Lite uses `"linear"` scales for quantitative fields and uses `"time"` scales for temporal fields for all encoding channels (encoding.html#channel).
In addition to `type` (#type), `domain` (#domain), and `range` (#range), continuous scales support the following properties:
| Property | Type | Description |
| --- | --- | --- |
| clamp | Boolean | ExprRef | If true , values that exceed the data domain are clamped to either the minimum or maximum range value Default value: derived from the scale config s clamp ( true by default). |
| interpolate | String | ExprRef | ScaleInterpolateParams | The interpolation method for range values. By default, a general interpolator for numbers, dates, strings and colors (in HCL space) is used. For color ranges, this property allows interpolation in alternative color spaces. Legal values include rgb , hsl , hsl-long , lab , hcl , hcl-long , cubehelix and cubehelix-long (-long variants use longer paths in polar coordinate spaces). If object-valued, this property accepts an object with a string-valued type property and an optional numeric gamma property applicable to rgb and cubehelix interpolators. For more, see the d3-interpolate documentation . Default value: hcl |
| nice | Boolean | Number | String | Object | ExprRef | Extending the domain so that it starts and ends on nice round values. This method typically modifies the scales domain, and may only extend the bounds to the nearest round value. Nicing is useful if the domain is computed from data and may be irregular. For example, for a domain of [0.201479..., 0.996679...] , a nice domain might be [0.2, 1.0] . For quantitative scales such as linear, nice can be either a boolean flag or a number. If nice is a number, it will represent a desired tick count. This allows greater control over the step size used to extend the bounds, guaranteeing that the returned ticks will exactly cover the domain. For temporal fields with time and utc scales, the nice value can be a string indicating the desired time interval. Legal values are "millisecond" , "second" , "minute" , "hour" , "day" , "week" , "month" , and "year" . Alternatively, time and utc scales can accept an object-valued interval specifier of the form {"interval": "month", "step": 3} , which includes a desired number of interval steps. Here, the domain would snap to quarter (Jan, Apr, Jul, Oct) boundaries. Default value: true for unbinned quantitative fields without explicit domain bounds; false otherwise. |
| padding | Number | ExprRef | For continuous scales, expands the scale domain to accommodate the specified number of pixels on each of the scale range. The scale range must represent pixels for this parameter to function as intended. Padding adjustment is performed prior to all other adjustments, including the effects of the zero , nice , domainMin , and domainMax properties. For band scales, shortcut for setting paddingInner and paddingOuter to the same value. For point scales, alias for paddingOuter . Default value: For continuous scales, derived from the scale config s continuousPadding . For band and point scales, see paddingInner and paddingOuter . By default, Vega-Lite sets padding such that width/height = number of unique values * step . |
| zero | Boolean | ExprRef | If true , ensures that a zero baseline value is included in the scale domain. Default value: true for x and y channels if the quantitative field is not binned and no custom domain is provided; false otherwise. Note: Log, time, and utc scales do not support zero . |

### Linear Scales
Linear scales (`"linear"`) are quantitative scales scales that preserve proportional differences. Each range value y can be expressed as a linear function of the domain value x: y = mx + b.
### Power Scales
Power scales (`"pow"`) are quantitative scales scales that apply an exponential transform to the input domain value before the output range value is computed. Each range value y can be expressed as a polynomial function of the domain value x: y = mx^k + b, where k is the `exponent` value. Power scales also support negative domain values, in which case the input value and the resulting output value are multiplied by -1.
| Property | Type | Description |
| --- | --- | --- |
| exponent | Number | ExprRef | The exponent of the pow scale. |

### Square Root Scales
Square root (`"sqrt"`) scales are a convenient shorthand for power scales with an `exponent` of `0.5`, indicating a square root transform.
### Logarithmic Scales
Log scales (`"log"`) are quantitative scales in which a logarithmic transform is applied to the input domain value before the output range value is computed. Log scales are particularly useful for plotting data that varies over multiple orders of magnitude. The mapping to the range value y can be expressed as a logarithmic function of the domain value x: y = m loga(x) + b, where a is the logarithmic `base`.
As log(0) = -, a log scale domain must be strictly-positive or strictly-negative; the domain must not include or cross zero. A log scale with a positive domain has a well-defined behavior for positive values, and a log scale with a negative domain has a well-defined behavior for negative values. (For a negative domain, input and output values are implicitly multiplied by -1.) The behavior of the scale is undefined if you run a negative value through a log scale with a positive domain or vice versa.
| Property | Type | Description |
| --- | --- | --- |
| base | Number | ExprRef | The logarithm base of the log scale (default 10 ). |

Example: The following plot has a logarithmic y-scale.
### Symlog Scales
Symmetric log scales (symlog) are quantitative scales scales that provide scaling similar to log scales, but supports non-positive numbers. Symlog scales are particularly useful for plotting data that varies over multiple orders of magnitude but includes negative- or zero-valued data. For more, see A bi-symmetric log transformation for wide-range data (https://www.researchgate.net/profile/John_Webber4/publication/233967063_A_bi-symmetric_log_transformation_for_wide-range_data/links/0fcfd50d791c85082e000000.pdf) by Webber for more.
| Property | Type | Description |
| --- | --- | --- |
| constant | Number | ExprRef | A constant determining the slope of the symlog function around zero. Only used for symlog scales. Default value: 1 |

### Time and UTC Scales
Time and UTC scales (`"time"` and `"utc"`) are continuous scales (#quantitative) with a temporal domain: values in the input domain are assumed to be Date (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) objects or timestamps. Time scales use the current local timezone setting. UTC scales instead use Coordinated Universal Time (https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
### Piecewise and Diverging Scales
We can use any types of continuous scales (`"linear"` (scale.html#linear), `"pow"` (scale.html#pow), `"sqrt"` (scale.html#sqrt), `"log"` (scale.html#log), `"symlog"` (scale.html#symlog), `"time"` (scale.html#time), `"utc"` (scale.html#utc) to create a diverging color graph by specifying a custom `domain` with multiple elements.
If `range` is specified, the number of elements in `range` should match with the number of elements in `domain`. Diverging color `scheme`s (https://vega.github.io/vega/docs/schemes/#diverging) are also useful as a range for a piecewise scale.
Example
## Discrete Scales
Discrete scales map values from a discrete domain to a discrete or continuous range.
### Ordinal Scales
Ordinal scales (`"ordinal"`) have a discrete domain and range. These scales function as a lookup table from a domain value to a range value.
By default, Vega-Lite automatically creates ordinal scales for `color` and `shape` channels. For example, the following plot implicitly has two ordinal scales, which map the values of the field `"Origin"` to a set of `color`s and a set of `shape`s.
The `range` (#range) of an ordinal scale can be an array of desired output values, which are directly mapped to elements in the `domain` (#domain). Both `domain` and `range` array can be re-ordered to specify the order and mapping between the domain and the output range. For ordinal color scales, a custom `scheme` (#scheme) can be set as well.

### Band and Point Scales
Band and point scales accept a discrete domain similar to ordinal scales (#ordinal), but map this domain to a continuous, numeric output range such as pixels.
Band scales (`"band"`) compute the discrete output values by dividing the continuous range into uniform bands. Band scales are typically used for bar charts with an ordinal or categorical dimension.
In addition to a standard numerical range value (such as `[0, 500]`), band scales can be given a fixed step size for each band. The actual range is then determined by both the step size and the cardinality (element count) of the input domain.
This image from the d3-scale documentation (https://github.com/d3/d3-scale#band-scales) illustrates how a band scale works:

Point scales (`"point"`) are a variant of band scales (#band) where the internal band width is fixed to zero. Point scales are typically used for scatterplots with an ordinal or categorical dimension. Similar to band scales, point scale range values may be specified using either a numerical extent (`[0, 500]`) or a step size (`{"step": 20}`).
This image from the d3-scale documentation (https://github.com/d3/d3-scale#band-scales) illustrates how a point scale works:

By default, Vega-Lite uses band scales for nominal and ordinal fields on position channels (encoding.html#position) (`x` and `y`) of bar (bar.html) or rect (rect.html) marks. For `x` and `y` of other marks and `size` and `opacity`, Vega-Lite uses point scales by default.
For example, the following bar chart has uses a band scale for its x-position.
To customize the step size of band scales for x/y-fields, we can set the step property of the views `width`/`height`.
For example, we can either make a bar chart have a fixed width:

or set the width per discrete step:

To customize the range of band and point scales, users can provide the following properties:
| Property | Type | Description |
| --- | --- | --- |
| align | Number | ExprRef | The alignment of the steps within the scale range. This value must lie in the range [0,1] . A value of 0.5 indicates that the steps should be centered within the range. A value of 0 or 1 may be used to shift the bands to one side, say to position them adjacent to an axis. Default value: 0.5 |
| padding | Number | ExprRef | For continuous scales, expands the scale domain to accommodate the specified number of pixels on each of the scale range. The scale range must represent pixels for this parameter to function as intended. Padding adjustment is performed prior to all other adjustments, including the effects of the zero , nice , domainMin , and domainMax properties. For band scales, shortcut for setting paddingInner and paddingOuter to the same value. For point scales, alias for paddingOuter . Default value: For continuous scales, derived from the scale config s continuousPadding . For band and point scales, see paddingInner and paddingOuter . By default, Vega-Lite sets padding such that width/height = number of unique values * step . |
| paddingInner | Number | ExprRef | The inner padding (spacing) within each band step of band scales, as a fraction of the step size. This value must lie in the range [0,1]. For point scale, this property is invalid as point scales do not have internal band widths (only step sizes between bands). Default value: derived from the scale config s bandPaddingInner . |
| paddingOuter | Number | ExprRef | The outer padding (spacing) at the ends of the range of band and point scales, as a fraction of the step size. This value must lie in the range [0,1]. Default value: derived from the scale config s bandPaddingOuter for band scales and pointPadding for point scales. By default, Vega-Lite sets outer padding such that width/height = number of unique values * step . |

## Discretizing Scales
Discretizing scales break up a continuous domain into discrete segments, and then map values in each segment to a range value.
### Bin-Linear Scales
Binned linear scales (`"bin-linear"`) are a special type of linear scale for use with binned (bin.html) fields to correctly create legend labels. Vega-Lite always uses binned linear scales with binned quantitative fields on size and opacity channels.
For example, the following plot has a binned field on the `size` channel.

### Bin-Ordinal Scales
Binned ordinal scales (`"bin-ordinal"`) are a special type of ordinal scale for use with binned (bin.html) fields to correctly create legend labels. Vega-Lite always uses binned ordinal scales with binned quantitative fields on the color channel.
For example, the following plot has a binned field on the `color` channel.

Similar to ordinal (#ordinal) color scales, a custom `range` (#range) or `scheme` (#scheme) can be specified for binned ordinal scales.
In addition, `bins` property can be used to specify bin boundaries over the scale domain.
| Property | Type | Description |
| --- | --- | --- |
| bins | ScaleBins | Bin boundaries can be provided to scales as either an explicit array of bin boundaries or as a bin specification object. The legal values are: An array literal of bin boundary values. For example, [0, 5, 10, 15, 20] . The array must include both starting and ending boundaries. The previous example uses five values to indicate a total of four bin intervals: [0-5), [5-10), [10-15), [15-20]. Array literals may include signal references as elements. A bin specification object that indicates the bin step size, and optionally the start and stop boundaries. An array of bin boundaries over the scale domain. If provided, axes and legends will use the bin boundaries to inform the choice of tick marks and text labels. |

#### Bins Parameter
The bin specification object for the scale `bins` properties support the following properties:
| Property | Type | Description |
| --- | --- | --- |
| bins | Any |  |

### Quantile Scales
Quantile scales (`"quantile"`) map a sample of input domain values to a discrete range based on computed quantile (https://en.wikipedia.org/wiki/Quantile) boundaries. The domain is considered continuous and thus the scale will accept any reasonable input value; however, the domain is specified as a discrete set of sample values. The number of values in (i.e., the cardinality of) the output range determines the number of quantiles that will be computed from the domain. To compute the quantiles, the domain is sorted, and treated as a population of discrete values. The resulting quantile boundaries segment the domain into groups with roughly equals numbers of sample points per group. If the `range` is not specified, the domain will be segmented into 4 quantiles (quartiles) by default.
Quantile scales are particularly useful for creating color or size encodings with a fixed number of output values. Using a discrete set of encoding levels (typically between 5-9 colors or sizes) sometimes supports more accurate perceptual comparison than a continuous range. For related functionality see quantize scales (scale.html#quantize), which partition the domain into uniform domain extents, rather than groups with equal element counts. Quantile scales have the benefit of evenly distributing data points to encoded values. In contrast, quantize scales uniformly segment the input domain and provide no guarantee on how data points will be distributed among the output visual values.

### Quantize Scales
Quantize scales (`"quantize"`) are similar to linear scales (scale.html#linear), except they use a discrete rather than continuous range. The `quantize` scale maps continuous value to a discrete range by dividing the domain into uniform segments based on the number of values in (i.e., the cardinality of) the output range. Each range value y can be expressed as a quantized linear function of the domain value x: y = m round(x) + b. If the `range` property is not specified, the domain will be divided into 4 uniform segments by default.
Quantize scales are particularly useful for creating color or size encodings with a fixed number of output values. Using a discrete set of encoding levels (typically between 5-9 colors or sizes) sometimes supports more accurate perceptual comparison than a continuous range. For related functionality see quantile scales (scale.html#quantile), which partition the domain into groups with equal element counts, rather than uniform domain extents.
| Property | Type | Description |
| --- | --- | --- |
| nice | Boolean | Number | String | Object | ExprRef | Extending the domain so that it starts and ends on nice round values. This method typically modifies the scales domain, and may only extend the bounds to the nearest round value. Nicing is useful if the domain is computed from data and may be irregular. For example, for a domain of [0.201479..., 0.996679...] , a nice domain might be [0.2, 1.0] . For quantitative scales such as linear, nice can be either a boolean flag or a number. If nice is a number, it will represent a desired tick count. This allows greater control over the step size used to extend the bounds, guaranteeing that the returned ticks will exactly cover the domain. For temporal fields with time and utc scales, the nice value can be a string indicating the desired time interval. Legal values are "millisecond" , "second" , "minute" , "hour" , "day" , "week" , "month" , and "year" . Alternatively, time and utc scales can accept an object-valued interval specifier of the form {"interval": "month", "step": 3} , which includes a desired number of interval steps. Here, the domain would snap to quarter (Jan, Apr, Jul, Oct) boundaries. Default value: true for unbinned quantitative fields without explicit domain bounds; false otherwise. |
| zero | Boolean | ExprRef | If true , ensures that a zero baseline value is included in the scale domain. Default value: true for x and y channels if the quantitative field is not binned and no custom domain is provided; false otherwise. Note: Log, time, and utc scales do not support zero . |

### Threshold Scales
Threshold scales (`"threshold"`) are similar to quantize scales (scale.html#quantize), except they allow mapping of arbitrary subsets of the domain (not uniform segments) to discrete values in the range. The input domain is still continuous, and divided into slices based on a set of threshold values provided to the required `domain` property. The `range` property must have N+1 elements, where N is the number of threshold boundaries provided in the domain.

## Disabling Scale
To directly encode the data value, the `scale` property can be set to `null`.
For example, the follow bar chart directly encodes color names in the data.

## Configuration
```
// Top-level View Specification
{
  ...
  "config": {
    "scale": {
      ...                       // Scale Config
    },
    "range": {
      ...                       // Scale Range Config
    },
    ...
  }
  ...
}

```

### Scale Config
To provide themes for all scales, the scale config (`config: {scale: {...}}`) can contain the following properties:
#### Padding
| Property | Type | Description |
| --- | --- | --- |
| bandPaddingInner | Number | ExprRef | Default inner padding for x and y band scales. Default value: nestedOffsetPaddingInner for x/y scales with nested x/y offset scales. barBandPaddingInner for bar marks ( 0.1 by default) rectBandPaddingInner for rect and other marks ( 0 by default) |
| barBandPaddingInner | Number | ExprRef | Default inner padding for x and y band-ordinal scales of "bar" marks. Default value: 0.1 |
| rectBandPaddingInner | Number | ExprRef | Default inner padding for x and y band-ordinal scales of "rect" marks. Default value: 0 |
| bandWithNestedOffsetPaddingInner | Number | ExprRef | Default inner padding for x and y band scales with nested xOffset and yOffset encoding. Default value: 0.2 |
| offsetBandPaddingInner | Number | ExprRef | Default padding inner for xOffset/yOffsets band scales. Default Value: 0 |
| bandPaddingOuter | Number | ExprRef | Default outer padding for x and y band scales. Default value: paddingInner/2 (which makes width/height = number of unique values * step ) |
| bandWithNestedOffsetPaddingOuter | Number | ExprRef | Default outer padding for x and y band scales with nested xOffset and yOffset encoding. Default value: 0.2 |
| offsetBandPaddingOuter | Number | ExprRef | Default padding outer for xOffset/yOffsets band scales. Default Value: 0 |
| continuousPadding | Number | ExprRef | Default padding for continuous x/y scales. Default: The bar width for continuous x-scale of a vertical bar and continuous y-scale of a horizontal bar.; 0 otherwise. |
| pointPadding | Number | ExprRef | Default outer padding for x and y point-ordinal scales. Default value: 0.5 (which makes width/height = number of unique values * step ) |

#### Range
| Property | Type | Description |
| --- | --- | --- |
| maxBandSize | Number | The default max value for mapping quantitative fields to bars size/bandSize. If undefined (default), we will use the axiss size (width or height) - 1. |
| minBandSize | Number | The default min value for mapping quantitative fields to bar and ticks size/bandSize scale. Default value: 2 |
| maxFontSize | Number | The default max value for mapping quantitative fields to texts size/fontSize scale. Default value: 40 |
| minFontSize | Number | The default min value for mapping quantitative fields to texts size/fontSize scale. Default value: 8 |
| maxOpacity | Number | Default max opacity for mapping a field to opacity. Default value: 0.8 |
| minOpacity | Number | Default minimum opacity for mapping a field to opacity. Default value: 0.3 |
| maxSize | Number | Default max value for point size scale. |
| minSize | Number | Default minimum value for point size scale. Default value: 9 |
| maxStrokeWidth | Number | Default max strokeWidth for the scale of strokeWidth for rule and line marks and of size for trail marks. Default value: 4 |
| minStrokeWidth | Number | Default minimum strokeWidth for the scale of strokeWidth for rule and line marks and of size for trail marks. Default value: 1 |

#### Scale Output for Invalid Values
| Property | Type | Description |
| --- | --- | --- |
| invalid | ScaleInvalidDataConfig | An object that defines scale outputs per channel for invalid values (nulls and NaNs on a continuous scale). The keys in this object are the scale channels. The values is either "zero-or-min" (use zero if the scale includes zero or min value otherwise) or a value definition {value: ...} . Example: Setting this config.scale.invalid property to {color: {value: '#aaa'}} will make the visualization color all invalid values with #aaa. See https://vega.github.io/vega-lite/docs/invalid-data.html for more details. |

#### Other
| Property | Type | Description |
| --- | --- | --- |
| clamp | Boolean | ExprRef | If true, values that exceed the data domain are clamped to either the minimum or maximum range value |
| round | Boolean | ExprRef | If true, rounds numeric output values to integers. This can be helpful for snapping to the pixel grid. (Only available for x , y , and size scales.) |
| xReverse | Boolean | ExprRef | Reverse x-scale by default (useful for right-to-left charts). |
| useUnaggregatedDomain | Boolean | Use the source data range before aggregation as scale domain instead of aggregated data for aggregate axis. This is equivalent to setting domain to "unaggregate" for aggregated quantitative fields by default. This property only works with aggregate functions that produce values within the raw data domain ( "mean" , "average" , "median" , "q1" , "q3" , "min" , "max" ). For other aggregations that produce values outside of the raw data domain (e.g. "count" , "sum" ), this property is ignored. Default value: false |
| zero | Boolean | Default scale.zero for continuous scales except for (1) x/y-scales of non-ranged bar or area charts and (2) size scales. Default value: true |

### Range Config
The scale range configuration (`config: {range: {...}}`) defines key-value mapping for named scale ranges: the keys represent the range names, while the values define valid `range` (#range) or, for named color ranges, Vega scheme definitions (https://vega.github.io/vega/docs/schemes/#scheme-properties).
By default, Vega-Lite (via Vega) includes the following pre-defined named ranges:
| Property | Type | Description |
| --- | --- | --- |
| category | RangeScheme | Color [] | Default color scheme for categorical data. |
| diverging | RangeScheme | Color [] | Default color scheme for diverging quantitative ramps. |
| heatmap | RangeScheme | Color [] | Default color scheme for quantitative heatmaps. |
| ordinal | RangeScheme | Color [] | Default color scheme for rank-ordered data. |
| ramp | RangeScheme | Color [] | Default color scheme for sequential quantitative ramps. |
| symbol | String[] | Array of symbol names or paths for the default shape palette. |

See this file (https://github.com/vega/vega-parser/blob/master/src/config.js#L188) for the default values of named ranges.

## Format
Source: https://vega.github.io/vega-lite/docs/format.html

In Vega-Lite specifications you can customize the format of text marks (text.html), tooltips (tooltip.html#using-tooltip-channel), axis (axis.html), legend (legend.html), header (header.html) labels.
The text field definition (encoding.html#text) as well as definitions of axis (axis.html), legend (legend.html), header (header.html) labels include the following properties:
| Property | Type | Description |
| --- | --- | --- |
| format | Format | The text format specifier for formatting number and date/time in labels of guides (axes, legends, headers) and text marks. If the format type is "number" (e.g., for quantitative fields), this is a D3s number format pattern string . If the format type is "time" (e.g., for temporal fields), this is either: a) D3s time format pattern if you desire to set a static time format. b) dynamic time format specifier object if you desire to set a dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the date lies on a year, month, date, hour, etc. boundary). When used with a custom formatType , this value will be passed as format alongside datum.value to the registered function. Default value: Derived from numberFormat config for number format and from timeFormat config for time format. |
| formatType | String | The format type for labels. One of "number" , "time" , or a registered custom format type . Default value: "time" for temporal fields and ordinal and nominal fields with timeUnit . "number" for quantitative fields as well as ordinal and nominal fields without timeUnit . |

In addition, you can override the default formats in the config (config.html#format).
## Formatting Text Marks and Tooltips
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...
  "encoding": {
    ...,
    "text": {
      "field": ...,
      "type": ...,
      "format": ...,   // Format
      "formatType": ...,
      ...
    },
    ...
  }
}

```

Text marks and tooltips are formatted by setting the `format` property of text or tooltip channel definitions (encoding.html#text).
For example, we can use Vega-Lite to show the average horsepower for cars from different origins. To format the number to have 2 digits of precisions, we can use the format `.2f`.

Formatting tooltips or dates is done similarly.
## Formatting Axis, Legend, and Header Labels
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    ...: {
      "field": ...,
      "type": ...,
      "axis/legend/header": {                // Axis / Legend / Header
        "format": ...,
        "formatType": ...,
        ...
      },
      ...
    },
    ...
  }
}

```

### Quantitative Fields
Below, we override the default number formatting to use exponent notation set to two significant digits.

### Temporal Data
#### Default
By default, time fields may have dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the ticks date lies on a year, month, date, hour, etc. boundary).

#### Specifying Dynamic Time Format
We can override dynamic time format by setting `format` to an object where the keys are valid Vega time units (https://vega.github.io/vega/docs/api/time/#time-units) (e.g., `year`, `month`, etc) and the values are d3-time-format (https://d3js.org/d3-time-format#locale_format) specifier strings.

#### Specifying Static Time Format
If you prefer using a static time format, you can set `format` to a desired time format specifier string:

Note that time format can also contain text.

## Gradient
Source: https://vega.github.io/vega-lite/docs/gradient.html

A gradient definition specifies a gradient color pattern. Vega-Lite supports either a linear gradient or a radial gradient.
For example:
```
{
  "gradient": "linear",
  "stops": [
    {"offset": 0.0, "color": "red"},
    {"offset": 0.5, "color": "white"},
    {"offset": 1.0, "color": "blue"}
  ]
}

```

## Linear Gradient
A linear gradient interpolates colors along a line, from a starting point to an ending point. By default a linear gradient runs horizontally, from left to right. Use the x1, y1, x2, and y2 properties to configure the gradient direction. All coordinates are defined in a normalized [0, 1] coordinate space, relative to the bounding box of the item being colored.
| Property | Type | Description |
| --- | --- | --- |
| gradient | String | Required. The type of gradient. Use "linear" for a linear gradient. |
| x1 | Number | The starting x-coordinate, in normalized [0, 1] coordinates, of the linear gradient. Default value: 0 |
| x2 | Number | The ending x-coordinate, in normalized [0, 1] coordinates, of the linear gradient. Default value: 1 |
| y1 | Number | The starting y-coordinate, in normalized [0, 1] coordinates, of the linear gradient. Default value: 0 |
| y2 | Number | The ending y-coordinate, in normalized [0, 1] coordinates, of the linear gradient. Default value: 0 |
| stops | GradientStop [] | Required. An array of gradient stops defining the gradient color sequence. |

### Example: Gradient Area Plot
Setting the area plots `color` encoding to `"linear"` gradient value produces a gradient area plot
## Radial Gradient
A radial gradient interpolates colors between two circles, from an inner circle boundary to an outer circle boundary. By default a radial gradient runs from the center point of the coordinate system (zero radius inner circle), out to the maximum extent (0.5 radius outer circle). Use the x1, y1, x2, and y2 properties to configure the inner and outer circle center points, and use the r1 and r2 properties to configure the circle radii. All coordinates are defined in a normalized [0, 1] coordinate space, relative to the bounding box of the item being colored. A value of 1 corresponds to the maximum extent of the bounding box (width or height, whichever is larger).
| Property | Type | Description |
| --- | --- | --- |
| gradient | String | Required. The type of gradient. Use "radial" for a radial gradient. |
| x1 | Number | The x-coordinate, in normalized [0, 1] coordinates, for the center of the inner circle for the gradient. Default value: 0.5 |
| x2 | Number | The x-coordinate, in normalized [0, 1] coordinates, for the center of the outer circle for the gradient. Default value: 0.5 |
| y1 | Number | The y-coordinate, in normalized [0, 1] coordinates, for the center of the inner circle for the gradient. Default value: 0.5 |
| y2 | Number | The y-coordinate, in normalized [0, 1] coordinates, for the center of the outer circle for the gradient. Default value: 0.5 |
| r1 | Number | The radius length, in normalized [0, 1] coordinates, of the inner circle for the gradient. Default value: 0 |
| r2 | Number | The radius length, in normalized [0, 1] coordinates, of the outer circle for the gradient. Default value: 0.5 |
| stops | GradientStop [] | Required. An array of gradient stops defining the gradient color sequence. |

## Gradient Stop
A gradient stop consists of a Color (#Color) value and an offset progress fraction.
| Property | Type | Description |
| --- | --- | --- |
| color | Color | Required. The color value at this point in the gradient. |
| offset | Number | Required. The offset fraction for the color stop, indicating its position within the gradient. |

## Header
Source: https://vega.github.io/vega-lite/docs/header.html

Headers provide a title and labels for faceted plots (facet.html). A headers title describes the field that is used to facet the plot, while a headers labels describe that fields value for each subplot.
By default, Vega-Lite automatically creates headers with default properties for `row` and `column` channels of a faceted view. User can set the `header` property of row- or column-field definition (facet.html#field-def) to an object to customize header properties (#header-properties).
In addition to the `header` property of a row- or column-field definition, users can also set default header properties for all headers with the configuration objects (`config` (config.html)) header configuration (#config) (`config: {header: {...}}`).
## Documentation Overview
- Header Properties (#header-properties)
- General (#general)
- Labels (#labels)
- Title (#title)
- Example (#example)
- Header Config (#config)
## Header Properties
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "row": {
      "field": ...,
      "type": ...,
      "header": {...}, // Header
      ...
    },
    "x": ...,
    "y": ...,
    ...
  }
}

```

```
// A Facet Specification
{
  ...,
  "facet": {
    "row/column": {
      "field": ...,
      "type": ...,
      "header": {...}, // Header
      ...
    },
    ...
  },
  "spec": ...
}

```

To customize header, a `header` definiton in row- or column-field definitions (facet.html#mapping) can contain the following groups of properties:
### General
| Property | Type | Description |
| --- | --- | --- |
| title | Text | Null | A title for the field. If null , the title will be removed. Default value: derived from the fields name and transformation function ( aggregate , bin and timeUnit ). If the field has an aggregate function, the function is displayed as part of the title (e.g., "Sum of Profit" ). If the field is binned or has a time unit applied, the applied function is shown in parentheses (e.g., "Profit (binned)" , "Transaction Date (year-month)" ). Otherwise, the title is simply the field name. Notes : 1) You can customize the default field title format by providing the fieldTitle property in the config or fieldTitle function via the compile functions options . 2) If both field definitions title and axis, header, or legend title are defined, axis/header/legend title will be used. |

See also: You may also use `guide-title` and `guide-label` style configs (mark.html#style-config) to customize common styles for axis (axis.html), legend (legend.html), and header (header.html) labels and titles.
### Labels
| Property | Type | Description |
| --- | --- | --- |
| format | Format | The text format specifier for formatting number and date/time in labels of guides (axes, legends, headers) and text marks. If the format type is "number" (e.g., for quantitative fields), this is a D3s number format pattern string . If the format type is "time" (e.g., for temporal fields), this is either: a) D3s time format pattern if you desire to set a static time format. b) dynamic time format specifier object if you desire to set a dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the date lies on a year, month, date, hour, etc. boundary). When used with a custom formatType , this value will be passed as format alongside datum.value to the registered function. Default value: Derived from numberFormat config for number format and from timeFormat config for time format. |
| formatType | String | The format type for labels. One of "number" , "time" , or a registered custom format type . Default value: "time" for temporal fields and ordinal and nominal fields with timeUnit . "number" for quantitative fields as well as ordinal and nominal fields without timeUnit . |
| labelAlign | String | ExprRef | Horizontal text alignment of header labels. One of "left" , "center" , or "right" . |
| labelAnchor | Null | String | The anchor position for placing the labels. One of "start" , "middle" , or "end" . For example, with a label orientation of top these anchor positions map to a left-, center-, or right-aligned label. |
| labelAngle | Number | The rotation angle of the header labels. Default value: 0 for column header, -90 for row header. |
| labelBaseline | String | ExprRef | The vertical text baseline for the header labels. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , or "line-bottom" . The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the titleLineHeight rather than titleFontSize alone. |
| labelColor | Color | ExprRef | The color of the header label, can be in hex color code or regular color name. |
| labelExpr | String | Vega expression for customizing labels. Note: The label text and value can be assessed via the label and value properties of the headers backing datum object. |
| labelFont | String | ExprRef | The font of the header label. |
| labelFontSize | Number | ExprRef | The font size of the header label, in pixels. |
| labelFontStyle | String | ExprRef | The font style of the header label. |
| labelFontWeight | String | Number | ExprRef | The font weight of the header label. |
| labelLimit | Number | ExprRef | The maximum length of the header label in pixels. The text value will be automatically truncated if the rendered size exceeds the limit. Default value: 0 , indicating no limit |
| labelLineHeight | Number | ExprRef | Line height in pixels for multi-line header labels or title text with "line-top" or "line-bottom" baseline. |
| labelOrient | String | The orientation of the header label. One of "top" , "bottom" , "left" or "right" . |
| labelPadding | Number | ExprRef | The padding, in pixel, between facet headers label and the plot. Default value: 10 |

### Title
| Property | Type | Description |
| --- | --- | --- |
| titleAlign | String | ExprRef | Horizontal text alignment (to the anchor) of header titles. |
| titleAnchor | Null | String | The anchor position for placing the title. One of "start" , "middle" , or "end" . For example, with an orientation of top these anchor positions map to a left-, center-, or right-aligned title. |
| titleAngle | Number | The rotation angle of the header title. Default value: 0 . |
| titleBaseline | String | ExprRef | The vertical text baseline for the header title. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , or "line-bottom" . The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the titleLineHeight rather than titleFontSize alone. Default value: "middle" |
| titleColor | Color | ExprRef | Color of the header title, can be in hex color code or regular color name. |
| titleFont | String | ExprRef | Font of the header title. (e.g., "Helvetica Neue" ). |
| titleFontWeight | String | Number | ExprRef | Font weight of the header title. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| titleFontSize | Number | ExprRef | Font size of the header title. |
| titleFontStyle | String | ExprRef | The font style of the header title. |
| titleFontWeight | String | Number | ExprRef | Font weight of the header title. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| titleLimit | Number | ExprRef | The maximum length of the header title in pixels. The text value will be automatically truncated if the rendered size exceeds the limit. Default value: 0 , indicating no limit |
| titleLineHeight | Number | ExprRef | Line height in pixels for multi-line header title text or title text with "line-top" or "line-bottom" baseline. |
| titleOrient | String | The orientation of the header title. One of "top" , "bottom" , "left" or "right" . |
| titlePadding | Number | ExprRef | The padding, in pixel, between facet headers title and the label. Default value: 10 |

### Example

This example uses header properties to change the font size of this faceted plots title and labels.
## Header Config
```
// Top-level View Specification
{
  ...
  "config": {
    "header": {...},               // Header
    "headerRow": {...},
    "headerColumn": {...},
    "headerFacet": {...},
    ...
  }
}

```

The `header` property of the top-level `config` object sets the default properties for all headers. If header properties are set in row-, column-, or facet-field definitions (facet.html#mapping), these configuration values will be overridden. Additional property blocks can target more specific header types based on types of facet channels (`"headerRow"`, `"headerColumn"`, `"headerFacet"`).
The header configuration can contain any header properties (#general).

## View Title
Source: https://vega.github.io/vega-lite/docs/title.html

The `title` property of a view specification in Vega-Lite (spec.html) adds a descriptive title to a chart. The title property can be either a string or an object defining the title properties (#props).
For example, the following bar chart is titled A Simple Bar Chart.

## Title Properties Object
A `title` properties object can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| text | Text | ExprRef | Required. The title text. |
| align | String | Horizontal text alignment for title text. One of "left" , "center" , or "right" . |
| anchor | Null | String | The anchor position for placing the title. One of "start" , "middle" , or "end" . For example, with an orientation of top these anchor positions map to a left-, center-, or right-aligned title. Default value: "middle" for single and layered views. "start" for other composite views. Note: For now , anchor is only customizable only for single and layered views. For other composite views, anchor is always "start" . |
| angle | Number | ExprRef | Angle in degrees of title and subtitle text. |
| baseline | String | Vertical text baseline for title and subtitle text. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , or "line-bottom" . The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. |
| color | Null | Color | ExprRef | Text color for title text. |
| dx | Number | ExprRef | Delta offset for title and subtitle text x-coordinate. |
| dy | Number | ExprRef | Delta offset for title and subtitle text y-coordinate. |
| font | String | ExprRef | Font name for title text. |
| fontSize | Number | ExprRef | Font size in pixels for title text. |
| fontStyle | String | ExprRef | Font style for title text. |
| fontWeight | String | Number | ExprRef | Font weight for title text. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| frame | String | String | ExprRef | The reference frame for the anchor position, one of "bounds" (to anchor relative to the full bounding box) or "group" (to anchor relative to the group width or height). |
| limit | Number | ExprRef | The maximum allowed length in pixels of title and subtitle text. |
| lineHeight | Number | ExprRef | Line height in pixels for multi-line title text or title text with "line-top" or "line-bottom" baseline. |
| offset | Number | ExprRef | The orthogonal offset in pixels by which to displace the title group from its position along the edge of the chart. |
| orient | String | ExprRef | Default title orientation ( "top" , "bottom" , "left" , or "right" ) |
| style | String | String[] | A mark style property to apply to the title text mark. Default value: "group-title" . |
| subtitle | Text | The subtitle Text. |
| subtitleColor | Null | Color | ExprRef | Text color for subtitle text. |
| subtitleFont | String | ExprRef | Font name for subtitle text. |
| subtitleFontSize | Number | ExprRef | Font size in pixels for subtitle text. |
| subtitleFontStyle | String | ExprRef | Font style for subtitle text. |
| subtitleFontWeight | String | Number | ExprRef | Font weight for subtitle text. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| subtitleLineHeight | Number | ExprRef | Line height in pixels for multi-line subtitle text. |
| subtitlePadding | Number | ExprRef | The padding in pixels between title and subtitle text. |
| zindex | Number | The integer z-index indicating the layering of the title group relative to other axis, mark and legend groups. Default value: 0 . |

For example, we can customize the `anchor` of the title of a bar chart.

```
// Top-level View Specification
{
  ...
  "config": {
    "title": : {
      ...
    }
  }
}

```

## Title Config
To provide themes for all titles, the title configuration (`config: {title: {...}}`) supports all title properties (#props).

## Tooltip
Source: https://vega.github.io/vega-lite/docs/tooltip.html

Tooltips can provide details of a particular data point on demand. Tooltips for each single-view in Vega-Lite can be (1) generated based on the `encoding` (#encoding), (2) generated based on the underlying data point (#data), or (3) directly specified via the `tooltip` channel (#channel).
By default, the renderer will generate tooltips via native HTML title attribute (https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/title). The Vega Tooltip plugin (#plugin) can generate nice HTML tooltips.
## Documentation Overview
- Tooltip Based on Encoding (#encoding)
- Tooltip Based on Underlying Data Point (#data)
- Tooltip channel (#channel)
- Tooltip image (#tooltip-image)
- Disable tooltips (#disable-tooltips)
- Vega Tooltip plugin (#plugin)
## Tooltip Based on Encoding
Setting the `tooltip` property of the mark definition (/vega-lite/docs/mark.html#mark-def) (or config) to `true` enables the default tooltip, which is based on all fields specified in the `encoding`.
Note: This is equivalent to setting the `tooltip` property of the mark definition to `{"content": "encoding"}`.
## Tooltip Based on Underlying Data Point
Setting marks `tooltip` to `{"content": "data"}` will produce tooltips based on all fields in the underlying data.
## Tooltip channel
To create a tooltip, Vega-Lites `tooltip` (encoding.html#mark-properties-channels) channel can be mapped to a data field. For example, this bar chart supports tooltips for field `b`. Hover over the bar and notice the simple tooltip that displays the value of field `b` for each bar.
To show more than one field, you can provide an array of field definitions. Vega tooltip (https://github.com/vega/vega-tooltip/) will display a table that shows the name of the field and its value. Here is an example.
Alternatively, you can calculate (calculate.html) a new field that concatenates multiple fields (and use a single field definition).
To give the fields in the tooltip a label that is different from the field name, set the `title` parameter.
Note that encoding a field without an aggregate (aggregate.html) as a tooltip means that the field will be used to group aggregates by.
In the example below, adding the tooltip for b means that b becomes part of the fields to group by. Therefore, there is one tick per unique date value.
To avoid that the tooltips groups the data, add an aggregate to the tooltip encoding.
## Tooltip image
To display an image in a tooltip you can use the Vega Tooltip plugin (#plugin). Vega Tooltip requires the special field name `image` to indicate that the field values should be rendered as images instead of displayed as text. The image tooltip can be specified either by setting the `tooltip` property of the mark definition (as detailed above) or by passing the field as an array to the tooltip encoding channel, as in the example below:
In addition to providing the path to an image, the Vega Tooltip plugin can also render base64 encoded images prefixed with `data:image/png;base64,` similarly to how these are rendered inside HTML image tags (https://www.w3docs.com/snippets/html/how-to-display-base64-images-in-html.html). To change the maximum size of the rendered tooltip images, you can adjust the `max-width` and `max-height` properties of the CSS selector `#vg-tooltip-element img`.
## Disable tooltips
To disable tooltips for a particular single view specification, you can set the `"tooltip"` property of a mark definition block to `null`.
```
{
  "mark": {"type": ..., "tooltip": null, ...},
  "encoding": ...,
  ...
}

```

Alternatively, you can also set the `"tooltip"` encoding to `null`:
```
{
  "mark": ...,
  "encoding": {
    "tooltip": null
  },
  ...
}

```

To disable all tooltips, disable it in the config (config.html) with
```
"config": {
  "mark": {"tooltip": null}
}

```

## Vega Tooltip plugin
You can further customize the tooltip by specifying a custom event handler via `tooltipHandler` (https://vega.github.io/vega/docs/api/view/#view_tooltipHandler) of the `Vega View API` (https://vega.github.io/vega/docs/api/view/). Vega invokes the handler every time a tooltip is shown.
We provide Vega Tooltip (https://github.com/vega/vega-tooltip/), a tooltip handler that creates a customizable HTML tooltip. Below is an example of Vega-Lite visualization with Vega Tooltip (https://github.com/vega/vega-tooltip/) plugin. Vega Tooltip comes with Vega Embed (https://github.com/vega/vega-embed) so you might already be using it.
Without the tooltip plugin, Vega-Lite will generate tooltips via native HTML title attribute (https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/title). Move your cursor over one of the bars to see it (you might have to wait for a little bit for the tooltip to appear).

