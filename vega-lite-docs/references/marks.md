# Marks

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Mark
Source: https://vega.github.io/vega-lite/docs/mark.html

Marks are the basic visual building block of a visualization. They provide basic shapes whose properties (such as position, size, and color) can be used to visually encode data, either from a data field, or a constant value.
The `mark` property of a single view specification (spec.html#single) can either be (1) a string describing a mark type (#types) or (2) a mark definition object (#mark-def).
```
// Single View Specification
{
  "data": ... ,
  "mark": ... ,       // mark
  "encoding": ... ,
  ...
}

```

## Documentation Overview
- Mark Types (#types)
- Mark Definition Object (#mark-def)
- General Mark Properties (#general)
- Position and Offset Properties (#offset)
- Color Properties (#color)
- Stroke Style Properties (#stroke)
- Hyperlink Properties (#hyperlink)
- Mark Config (#config)
- Mark Style Config (#style-config)
- Example: Styling Labels (#example-styling-labels)
## Mark Types
Vega-Lite supports the following primitive `mark` types: `"area"` (area.html), `"bar"` (bar.html), `"circle"` (circle.html), `"line"` (line.html), `"point"` (point.html), `"rect"` (rect.html), `"rule"` (rule.html), `"square"` (square.html), `"text"` (text.html), `"tick"` (tick.html), and `"geoshape"` (geoshape.html). In general, one mark instance is generated per input data element. However, line and area marks represent multiple data elements as a contiguous line or shape.
In addition to primitive marks, Vega-Lite also support composite marks, which are macros for complex layered graphics that contain multiple primitive marks. Supported composite mark types include `"boxplot"` (boxplot.html), `"errorband"` (errorband.html), `"errorbar"` (errorbar.html).
For example, a bar chart has `mark` as a simple string `"bar"`.

## Mark Definition Object
```
// Single View Specification
{
  ...
  "mark": {
    "type": ...,       // mark
    ...
  },
  ...
}

```

To customize properties of a mark, users can set `mark` to be a mark definition object instead of a string describing mark type. The rest of this section lists standard mark properties for primitive mark types. Additionally, some marks may have special mark properties (listed in their documentation page). For example, point (point.html#properties) marks support `shape` and `size` properties in addition to these standard properties.
Note: If mark property encoding channels (encoding.html#mark-prop) are specified, these mark properties will be overridden.
### General Mark Properties
| Property | Type | Description |
| --- | --- | --- |
| type | String | Required. The mark type. This could a primitive mark type (one of "bar" , "circle" , "square" , "tick" , "line" , "area" , "point" , "geoshape" , "rule" , and "text" ) or a composite mark type ( "boxplot" , "errorband" , "errorbar" ). |
| aria | Boolean | ExprRef | A boolean flag indicating if ARIA attributes should be included (SVG output only). If false , the aria-hidden attribute will be set on the output SVG element, removing the mark item from the ARIA accessibility tree. |
| cursor | String | ExprRef | The mouse cursor used over the mark. Any valid CSS cursor type can be used. |
| description | String | ExprRef | A text description of the mark item for ARIA accessibility (SVG output only). If specified, this property determines the aria-label attribute . |
| style | String | String[] | A string or array of strings indicating the name of custom styles to apply to the mark. A style is a named collection of mark property defaults defined within the style configuration . If style is an array, later styles will override earlier styles. Any mark properties explicitly defined within the encoding will override a style default. Default value: The marks name. For example, a bar mark will have style "bar" by default. Note: Any specified style will augment the default style. For example, a bar mark with "style": "foo" will receive from config.style.bar and config.style.foo (the specified style "foo" has higher precedence). |
| tooltip | Number | String | Boolean | TooltipContent | ExprRef | Null | The tooltip text string to show upon mouse hover or an object defining which fields should the tooltip be derived from. If tooltip is true or {"content": "encoding"} , then all fields from encoding will be used. If tooltip is {"content": "data"} , then all fields that appear in the highlighted data point will be used. If set to null or false , then no tooltip will be used. See the tooltip documentation for a detailed discussion about tooltip in Vega-Lite. Default value: null |
| clip | Boolean | ExprRef | Whether a mark be clipped to the enclosing groups width and height. |
| invalid | String | Null | Invalid data mode, which defines how the marks and corresponding scales should represent invalid values ( null and NaN in continuous scales without defined output for invalid values). "filter"  Exclude all invalid values from the visualizations marks and scales . For path marks (for line, area, trail), this option will create paths that connect valid points, as if the data rows with invalid values do not exist. "break-paths-filter-domains"  Break path marks (for line, area, trail) at invalid values. For non-path marks, this is equivalent to "filter" . All scale domains will exclude these filtered data points. "break-paths-show-domains"  Break paths (for line, area, trail) at invalid values. Hide invalid values for non-path marks. All scale domains will include these filtered data points (for both path and non-path marks). "show" or null  Show all data points in the marks and scale domains. Each scale will use the output for invalid values defined in config.scale.invalid or, if unspecified, by default invalid values will produce the same visual values as zero (if the scale includes zero) or the minimum value (if the scale does not include zero). "break-paths-show-path-domains" (default)  This is equivalent to "break-paths-show-domains" for path-based marks (line/area/trail) and "filter" for non-path marks. Note : If any channels scale has an output for invalid values defined in config.scale.invalid , all values for the scales will be considered valid since they can produce a reasonable output for the scales. Thus, fields for such channels will not be filtered and will not cause path breaks. |
| order | Null | Boolean | For line and trail marks, this order property can be set to null or false to make the lines use the original order in the data sources. |

### Position and Offset Properties
| Property | Type | Description |
| --- | --- | --- |
| x | Number | String | ExprRef | X coordinates of the marks, or width of horizontal "bar" and "area" without specified x2 or width . The value of this channel can be a number or a string "width" for the width of the plot. |
| x2 | Number | String | ExprRef | X2 coordinates for ranged "area" , "bar" , "rect" , and "rule" . The value of this channel can be a number or a string "width" for the width of the plot. |
| width | Number | ExprRef | RelativeBandSize | Width of the marks. One of: A number representing a fixed pixel width. A relative band size definition. For example, {band: 0.5} represents half of the band. |
| height | Number | ExprRef | RelativeBandSize | Height of the marks. One of: A number representing a fixed pixel height. A relative band size definition. For example, {band: 0.5} represents half of the band |
| y | Number | String | ExprRef | Y coordinates of the marks, or height of vertical "bar" and "area" without specified y2 or height . The value of this channel can be a number or a string "height" for the height of the plot. |
| y2 | Number | String | ExprRef | Y2 coordinates for ranged "area" , "bar" , "rect" , and "rule" . The value of this channel can be a number or a string "height" for the height of the plot. |
| xOffset | Number | ExprRef | Offset for x-position. |
| x2Offset | Number | ExprRef | Offset for x2-position. |
| yOffset | Number | ExprRef | Offset for y-position. |
| y2Offset | Number | ExprRef | Offset for y2-position. |

### Color Properties
| Property | Type | Description |
| --- | --- | --- |
| filled | Boolean | Whether the marks color should be used as fill color instead of stroke color. Default value: false for all point , line , and rule marks as well as geoshape marks for graticule data sources; otherwise, true . Note: This property cannot be used in a style config . |
| color | Color | Gradient | ExprRef | Default color. Default value:  "#4682b4" Note: This property cannot be used in a style config . The fill and stroke properties have higher precedence than color and will override color . |
| fill | Color | Gradient | Null | ExprRef | Default fill color. This property has higher precedence than config.color . Set to null to remove fill. Default value: (None) |
| stroke | Color | Gradient | Null | ExprRef | Default stroke color. This property has higher precedence than config.color . Set to null to remove stroke. Default value: (None) |
| blend | Blend | ExprRef | The color blend mode for drawing an item on its current background. Any valid CSS mix-blend-mode value can be used. __Default value: "source-over" |
| opacity | Number | ExprRef | The overall opacity (value between [0,1]). Default value: 0.7 for non-aggregate plots with point , tick , circle , or square marks or layered bar charts and 1 otherwise. |
| fillOpacity | Number | ExprRef | The fill opacity (value between [0,1]). Default value: 1 |
| strokeOpacity | Number | ExprRef | The stroke opacity (value between [0,1]). Default value: 1 |

### Stroke Style Properties
| Property | Type | Description |
| --- | --- | --- |
| strokeCap | String | ExprRef | The stroke cap for line ending style. One of "butt" , "round" , or "square" . Default value: "butt" |
| strokeDash | Number[] | ExprRef | An array of alternating stroke, space lengths for creating dashed or dotted lines. |
| strokeDashOffset | Number | ExprRef | The offset (in pixels) into which to begin drawing with the stroke dash array. |
| strokeJoin | String | ExprRef | The stroke line join method. One of "miter" , "round" or "bevel" . Default value: "miter" |
| strokeMiterLimit | Number | ExprRef | The miter limit at which to bevel a line join. |
| strokeWidth | Number | ExprRef | The stroke width, in pixels. |

Here is an example to the usage of the stroke dash where 6 is the size of dashes, and 4 is the size of spaces:
### Hyperlink Properties
Marks can act as hyperlinks when the `href` property or channel (encoding.html#href) is defined. When the `href` property is specified, the `cursor` mark property (mark.html#hyperlink) is set to `"pointer"` by default to serve as affordance for hyperlinks.
| Property | Type | Description |
| --- | --- | --- |
| href | URI | ExprRef | A URL to load upon mouse click. If defined, the mark acts as a hyperlink. |

## Mark Config
```
// Top-level View Specification
{
  ...
  "config": {
    "mark": ...,
    "area": ...,
    "bar": ...,
    "circle": ...,
    "line": ...,
    "point": ...,
    "rect": ...,
    "rule": ...,
    "geoshape": ...,
    "square": ...,
    "text": ...,
    "tick": ...
  }
}

```

The `mark` property of the `config` (config.html) object sets the default properties for all marks. In addition, the `config` object also provides mark-specific config using its mark type as the property name (e.g., `config.area`) for defining default properties for each mark.
The global mark config (`config.mark`) supports all standard mark properties (except `type`, `style`, `clip`, and `orient`). For mark-specific config, please see the documentation for each mark type.
Note:
- If mark properties in mark definition (#mark-def) or mark property encoding channels (encoding.html#mark-prop) are specified, these config values will be overridden.
- Mark config do not support offset mark properties (#offset).
## Mark Style Config
```
{
  // Top Level Specification
  "config": {
    "style": {
      ...
    }
    ...
  }
}

```

In addition to the default mark properties above, default values can be further customized using named styles defined under the `style` property in the config object.
| Property | Type | Description |
| --- | --- | --- |
| style | Object | An object hash that defines key-value mappings to determine default properties for marks with a given style . The keys represent styles names; the values have to be valid mark configuration objects . |

For example, to set a default shape and stroke width for `point` marks with a style named `"triangle"`:
```
{
  "style": {
    "triangle": {
      "shape": "triangle-up",
      "strokeWidth": 2
    }
  }
}

```

Styles can then be invoked by including a `style` property within a mark definition object (#mark-def).
Note: To customize the style for guides (axes, headers, and legends), Vega-Lite also includes the following built-in style names:
- `"guide-label"`: style for axis, legend, and header labels
- `"guide-title"`: style for axis, legend, and header titles
- `"group-title"`: styles for chart titles
### Example: Styling Labels
You can use `text` marks (text.html) as labels for other marks by setting `style` for the marks and using style config (mark.html#style-config) to configure offset (`dx` or `dy`), `align`, and `baseline`.

See also: a similar example that uses mark definition to configure offset, align, and baseline (text.html#labels).

## Area
Source: https://vega.github.io/vega-lite/docs/area.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "area",
  "encoding": ... ,
  ...
}

```

`area` represent multiple data element as a single area shape. Area marks are often used to show change over time, using either a single area or stacked areas.
## Documentation Overview
- Area Mark Properties (#properties)
- Examples (#examples)
- Area Chart (#area-chart)
- Area Chart with Overlaying Lines and Point Markers (#area-chart-with-overlaying-lines-and-point-markers)
- Stacked Area Chart (#stacked-area-chart)
- Normalized Stacked Area Chart (#normalized-stacked-area-chart)
- Streamgraph (#streamgraph)
- Ranged Area (#ranged)
- Area Config (#config)
## Area Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "area",
    ...
  },
  "encoding": ... ,
  ...
}

```

An area mark definition can contain any standard mark properties (mark.html#mark-def) and the following line interpolation as well as line and point overlay properties:
| Property | Type | Description |
| --- | --- | --- |
| align | String | ExprRef | The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule). One of "left" , "right" , "center" . Note: Expression reference is not supported for range marks. |
| baseline | String | ExprRef | For text marks, the vertical text baseline. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , "line-bottom" , or an expression reference that provides one of the valid values. The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. For range marks, the vertical alignment of the marks. One of "top" , "middle" , "bottom" . Note: Expression reference is not supported for range marks. |
| orient | String | The orientation of a non-stacked bar, tick, area, and line charts. The value is either horizontal (default) or vertical. For bar, rule and tick, this determines whether the size of the bar and tick should be applied to x or y dimension. For area, this property determines the orient property of the Vega output. For line and trail marks, this property determines the sort order of the points in the line if config.sortLineBy is not specified. For stacked charts, this is always determined by the orientation of the stack; therefore explicitly specified value will be ignored. |
| interpolate | String | ExprRef | The line interpolation method to use for line and area marks. One of the following: "linear" : piecewise linear segments, as in a polyline. "linear-closed" : close the linear segments to form a polygon. "step" : alternate between horizontal and vertical segments, as in a step function. "step-before" : alternate between vertical and horizontal segments, as in a step function. "step-after" : alternate between horizontal and vertical segments, as in a step function. "basis" : a B-spline, with control point duplication on the ends. "basis-open" : an open B-spline; may not intersect the start or end. "basis-closed" : a closed B-spline, as in a loop. "cardinal" : a Cardinal spline, with control point duplication on the ends. "cardinal-open" : an open Cardinal spline; may not intersect the start or end, but will intersect other control points. "cardinal-closed" : a closed Cardinal spline, as in a loop. "bundle" : equivalent to basis, except the tension parameter is used to straighten the spline. "monotone" : cubic interpolation that preserves monotonicity in y. |
| tension | Number | ExprRef | Depending on the interpolation type, sets the tension parameter (for line and area marks). |
| line | Boolean | Object | A flag for overlaying line on top of area marks, or an object defining the properties of the overlayed lines. If this value is an empty object ( {} ) or true , lines with default properties will be used. If this value is false , no lines would be automatically added to area marks. Default value: false . |
| point | Boolean | Object | String | A flag for overlaying points on top of line or area marks, or an object defining the properties of the overlayed points. If this property is "transparent" , transparent points will be used (for enhancing tooltips and selections). If this property is an empty object ( {} ) or true , filled points with default properties will be used. If this property is false , no points would be automatically added to line or area marks. Default value: false . |

## Examples
### Area Chart
Using `area` mark with one temporal or ordinal field (typically on `x`) and one quantitative field (typically on `y`) produces an area chart. For example, the following area chart shows a number of unemployment people in the US over time.

### Area Chart with Overlaying Lines and Point Markers
By setting the `line` and `point` properties of the mark definition to `true` or an object defining a property of the overlaying point marks, we can overlay line and point markers on top of area.

Instead of using a single color as the fill color of the area, we can set it to a gradient (/vega-lite/docs/types.html#gradient). In this example, we are also customizing the overlay.

### Stacked Area Chart
Adding a color field to area chart creates stacked area chart by default. For example, here we split the area chart by industry.

### Normalized Stacked Area Chart
You can also create a normalized stacked area chart by setting `"stack"` to `"normalize"` in the encoding channel. Here we can easily see the percentage of unemployment across industries.

### Streamgraph
We can also shift the stacked area charts baseline to center and produces a streamgraph (https://datavizcatalogue.com/methods/stream_graph.html) by setting `"stack"` to `"center"` in the encoding channel.

### Ranged Area
Specifying `x2` or `y2` for the quantitative axis of area marks produce ranged areas. For example, we can use ranged area with the `ci0` and `ci0` aggregation operators (aggregate.html#ops) to highlight 95% confidence interval of a line chart that shows mean values over time.

## Area Config
```
// Top-level View Specification
{
  ...
  "config": {
    "area": ...,
    ...
  }
}

```

The `area` property of the top-level `config` (config.html) object sets the default properties for all area marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The area config can contain any area mark properties (#properties) (except `type`, `style`, `clip`, and `orient`).

## Bar
Source: https://vega.github.io/vega-lite/docs/bar.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "bar",
  "encoding": ... ,
  ...
}

```

Bar marks are useful in many visualizations, including bar charts, stacked bar charts (#stack), and timelines (#ranged).
## Documentation Overview
- Bar Mark Properties (#properties)
- Examples (#examples)
- Single Bar Chart (#single-bar-chart)
- Bar Chart (#bar-chart)
- Bar Chart with a Temporal Axis (#bar-chart-with-a-temporal-axis)
- Relative Bar Width (#relative-bar-width)
- Bar Chart with a Discrete Temporal Axis (#bar-chart-with-a-discrete-temporal-axis)
- Bar Chart with Rounded Corners (#bar-chart-with-rounded-corners)
- Bar Chart with Negative Values and Zero Baseline (#bar-chart-with-negative-values-and-zero-baseline)
- Histogram (#histogram)
- Stacked Bar Chart (#stack)
- Layered Bar Chart (#layered-bar-chart)
- Normalized Stacked Bar Chart (#normalized-stacked-bar-chart)
- Grouped Bar Chart (with Offset) (#grouped-bar-chart-with-offset)
- Grouped Bar Chart (with Facet) (#grouped-bar-chart-with-facet)
- Grouped Bar Chart (Multiple Measure with Repeat) (#grouped-bar-chart-multiple-measure-with-repeat)
- Ranged Bars (#ranged)
- Bar Config (#config)
## Bar Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "bar",
    ...
  },
  "encoding": ... ,
  ...
}

```

A bar mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| width | Number | ExprRef | RelativeBandSize | Width of the marks. One of: A number representing a fixed pixel width. A relative band size definition. For example, {band: 0.5} represents half of the band. |
| height | Number | ExprRef | RelativeBandSize | Height of the marks. One of: A number representing a fixed pixel height. A relative band size definition. For example, {band: 0.5} represents half of the band |
| orient | String | The orientation of a non-stacked bar, tick, area, and line charts. The value is either horizontal (default) or vertical. For bar, rule and tick, this determines whether the size of the bar and tick should be applied to x or y dimension. For area, this property determines the orient property of the Vega output. For line and trail marks, this property determines the sort order of the points in the line if config.sortLineBy is not specified. For stacked charts, this is always determined by the orientation of the stack; therefore explicitly specified value will be ignored. |
| align | String | ExprRef | The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule). One of "left" , "right" , "center" . Note: Expression reference is not supported for range marks. |
| baseline | String | ExprRef | For text marks, the vertical text baseline. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , "line-bottom" , or an expression reference that provides one of the valid values. The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. For range marks, the vertical alignment of the marks. One of "top" , "middle" , "bottom" . Note: Expression reference is not supported for range marks. |
| binSpacing | Number | Offset between bars for binned field. The ideal value for this is either 0 (preferred by statisticians) or 1 (Vega-Lite default, D3 example style). Default value: 1 |
| cornerRadius | Number | ExprRef | The radius in pixels of rounded rectangles or arcs corners. Default value: 0 |
| cornerRadiusEnd | Number | ExprRef | For vertical bars, top-left and top-right corner radius. For horizontal bars, top-right and bottom-right corner radius. |
| cornerRadiusTopLeft | Number | ExprRef | The radius in pixels of rounded rectangles top right corner. Default value: 0 |
| cornerRadiusTopRight | Number | ExprRef | The radius in pixels of rounded rectangles top left corner. Default value: 0 |
| cornerRadiusBottomRight | Number | ExprRef | The radius in pixels of rounded rectangles bottom right corner. Default value: 0 |
| cornerRadiusBottomLeft | Number | ExprRef | The radius in pixels of rounded rectangles bottom left corner. Default value: 0 |

## Examples
### Single Bar Chart
Mapping a quantitative field to either `x` or `y` of the `bar` mark produces a single bar chart.

### Bar Chart
If we map a different discrete field to the `y` channel, we can produce a horizontal bar chart. Specifying `"height": {"step": 17}` will adjust the bars height per discrete step.

### Bar Chart with a Temporal Axis
While the `bar` mark typically uses the x and y channels to encode a pair of discrete and continuous fields, it can also be used with continuous fields on both channels. For example, given a bar chart with a temporal field on x, we can see that the x-scale is a continuous scale. By default, the size of bars on continuous scales will be set based on the `continuousBandSize` config (#config).

{.#bar-width}
### Relative Bar Width
To adjust the bar to be smaller than the time unit step, you can adjust the bars width to be a proportion of band. For example, the following chart sets the width to be 70% of the x band width.

### Bar Chart with a Discrete Temporal Axis
If you want to use a discrete scale instead, you can cast the field to have an `"ordinal"` type. This casting strategy can be useful for time units with low cardinality such as `"month"`.

### Bar Chart with Rounded Corners
We can also adjust corner radius of the bar with various corner radius properties. For example, we can use `cornerRadiusEnd` to create a bar chart with rounded corners at the end of the bars.

### Bar Chart with Negative Values and Zero Baseline
When there are negative values, you may want to hide domain the axis domain line, and instead use a conditional grid color to draw a zero baseline.

### Histogram
If the data is not pre-aggregated (i.e. each record in the data field represents one item), mapping a binned (bin.html) quantitative field to `x` and aggregate `count` to `y` produces a histogram.

If you prefer to have histogram without gaps between bars, you can set the `binSpacing` mark property (#properties) to `0`.

### Stacked Bar Chart
Adding color to the bar chart (by using the `color` attribute) creates a stacked bar chart by default. Here we also customize the colors scale range to make the color a little nicer. (See `stack` (stack.html) for more details about customizing stack.)

### Layered Bar Chart
To disable stacking, you can alternatively set `stack` (stack.html) to `null`. This produces a layered bar chart. To make it clear that bars are layered, we can make marks semi-transparent by setting the `opacity` to a value between 0 and 1 (e.g., `0.7`).

### Normalized Stacked Bar Chart
You can also create a normalized stacked bar chart by setting `stack` (stack.html) to `"normalize"`. Here we can easily see the percentage of male and female population at different ages.

### Grouped Bar Chart (with Offset)

### Grouped Bar Chart (with Facet)
Alternatively, you can also use faceting (facet.html) to produce a grouped bar chart.

This allows you to use independent x-scale for each facet:

### Grouped Bar Chart (Multiple Measure with Repeat)

### Ranged Bars
Specifying `x2` or `y2` for the quantitative axis of bar marks creates ranged bars. For example, we can use ranged bars to create a gantt chart.

## Bar Config
```
// Top-level View Specification
{
  ...
  "config": {
    "bar": ...,
    ...
  }
}

```

The `bar` property of the top-level `config` (config.html) object sets the default properties for all bar marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
Besides standard bar mark properties (#properties), bar config can contain the following additional properties:
| Property | Type | Description |
| --- | --- | --- |
| continuousBandSize | Number | The default size of the bars on continuous scales. Default value: 5 |
| discreteBandSize | Number | RelativeBandSize | The default size of the bars with discrete dimensions. If unspecified, the default size is step-2 , which provides 2 pixel offset between bars. |
| minBandSize | Number | ExprRef | The minimum band size for bar and rectangle marks. Default value: 0.25 |

## Line
Source: https://vega.github.io/vega-lite/docs/line.html

```
{
  "data": ... ,
  "mark": "line",
  "encoding": ... ,
  ...
}

```

The `line` mark represents the data points stored in a field with a line connecting all of these points. Line marks are commonly used to depict trajectories or change over time. Unlike most other marks that represent one data element per mark, one line mark represents multiple data element as a single line, akin to `area` (area.html) and `trail` (trail.html).
Note: For line segments that connect (x,y) positions to (x2,y2) positions, please use `rule` (rule.html) marks. For continuous lines with varying size, please use `trail` (trail.html) marks.
## Documentation Overview
- Line Mark Properties (#properties)
- Examples (#examples)
- Line Chart (#line-chart)
- Multi-series Colored Line Chart (#multi-series-colored-line-chart)
- Multi-series Line Chart with Varying Dashes (#multi-series-line-chart-with-varying-dashes)
- Multi-series Line Chart with the Detail Channel (#line-detail)
- Line Chart with Point Markers (#line-chart-with-point-markers)
- Line Chart with Invalid Values (#line-invalid)
- Connected Scatter Plot (Line Chart with Custom Path) (#connected-scatter-plot)
- Line interpolation (#line-interpolation)
- Geo Line (#geo-line)
- Line Config (#config)
## Line Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "line",
    ...
  },
  "encoding": ... ,
  ...
}

```

An line mark definition can contain any standard mark properties (mark.html#mark-def) and the following line interpolation and point overlay properties:
| Property | Type | Description |
| --- | --- | --- |
| orient | String | The orientation of a non-stacked bar, tick, area, and line charts. The value is either horizontal (default) or vertical. For bar, rule and tick, this determines whether the size of the bar and tick should be applied to x or y dimension. For area, this property determines the orient property of the Vega output. For line and trail marks, this property determines the sort order of the points in the line if config.sortLineBy is not specified. For stacked charts, this is always determined by the orientation of the stack; therefore explicitly specified value will be ignored. |
| interpolate | String | ExprRef | The line interpolation method to use for line and area marks. One of the following: "linear" : piecewise linear segments, as in a polyline. "linear-closed" : close the linear segments to form a polygon. "step" : alternate between horizontal and vertical segments, as in a step function. "step-before" : alternate between vertical and horizontal segments, as in a step function. "step-after" : alternate between horizontal and vertical segments, as in a step function. "basis" : a B-spline, with control point duplication on the ends. "basis-open" : an open B-spline; may not intersect the start or end. "basis-closed" : a closed B-spline, as in a loop. "cardinal" : a Cardinal spline, with control point duplication on the ends. "cardinal-open" : an open Cardinal spline; may not intersect the start or end, but will intersect other control points. "cardinal-closed" : a closed Cardinal spline, as in a loop. "bundle" : equivalent to basis, except the tension parameter is used to straighten the spline. "monotone" : cubic interpolation that preserves monotonicity in y. |
| tension | Number | ExprRef | Depending on the interpolation type, sets the tension parameter (for line and area marks). |
| point | Boolean | Object | String | A flag for overlaying points on top of line or area marks, or an object defining the properties of the overlayed points. If this property is "transparent" , transparent points will be used (for enhancing tooltips and selections). If this property is an empty object ( {} ) or true , filled points with default properties will be used. If this property is false , no points would be automatically added to line or area marks. Default value: false . |

## Examples
### Line Chart
Using `line` with one temporal or ordinal field (typically on `x`) and another quantitative field (typically on `y`) produces a simple line chart with a single line.

We can add create multiple lines by grouping along different attributes, such as `color` or `detail`.
### Multi-series Colored Line Chart
Adding a field to a mark property channel (encoding.html#mark-prop) such as `color` groups data points into different series, producing a multi-series colored line chart.

We can use text marks and `argmax` (aggregate.html#argmax) to add labels to each line instead of using legends. Note that here we hide one of the line to avoid collision.

We can further apply `selection` (selection.html) to highlight a certain line on hover.

### Multi-series Line Chart with Varying Dashes
Adding a field to `strokeDash` also produces a multi-series line chart.

We can also use line grouping to create a line chart that has multiple parts with varying styles.

### Multi-series Line Chart with the Detail Channel
To group lines by a field without mapping the field to any visual properties, we can map the field to the `detail` (encoding.html#detail) channel to create a multi-series line chart with the same color.

The same method can be used to group lines for a ranged dot plot.

### Line Chart with Point Markers
By setting the `point` property of the mark definition to `true` or an object defining a property of the overlaying point marks, we can overlay point markers on top of line.

This is equivalent to adding another layer of filled point marks.

Note that the overlay point marks have `opacity` = 1 by default (instead of semi-transparent like normal point marks).
Here we create stroked points by setting their `\"filled\"` to `false` and their `fill` to `\"white\"`.

### Line Chart with Invalid Values
By default, data points with invalid x- or y-values (`null` or `NaN`) will cause break in the lines.

Note that individual points without connecting points will still be invisible by default.

To show individual points without connecting points, you may set `strokeCap` to `"square"`:

or overlay it with marker points:

### Connected Scatter Plot (Line Chart with Custom Path)
As shown in previous example, the lines path (order of points in the line) is determined by data values on the temporal/ordinal field by default. However, a field can be mapped to the `order` (encoding.html#order) channel for determining a custom path.
For example, to show a pattern of data change over time between gasoline price and average miles driven per capita we use `order` channel to sort the points in the line by time field (`year`). In this example, we also use the `point` property to overlay point marks over the line marks to highlight each data point.

### Line interpolation
The `interpolate` property of a mark definition (mark.html#mark-def) can be used to change line interpolation method. For example, we can set `interpolate` to `"monotone"`.

We can also set `interpolate` to `"step-after"` to create a step-chart.

For the list of all supported `interpolate` properties, please see the line mark properties (#properties) section.
### Geo Line
By mapping geographic coordinate data to `longitude` and `latitude` channels of a corresponding projection (projection.html), we can draw lines through geographic points.

## Line Config
```
// Top-level View Specification
{
  ...
  "config": {
    "line": ...,
    ...
  }
}

```

The `line` property of the top-level `config` (config.html) object sets the default properties for all line marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The line config can contain any line mark properties (#properties) (except `type`, `style`, and `clip`).

## Point
Source: https://vega.github.io/vega-lite/docs/point.html

```
{
  "data": ... ,
  "mark": "point",
  "encoding": ... ,
  ...
}

```

`point` mark represents each data point with a symbol. Point marks are commonly used in visualizations like scatterplots.
## Documentation Overview
- Point Mark Properties (#properties)
- Examples (#examples)
- Dot Plot (#dot-plot)
- Scatter Plot (#scatter-plot)
- Bubble Plot (#bubble-plot)
- Scatter Plot with Color and/or Shape (#color)
- Dot Plot with Jittering (#dot-plot-with-jittering)
- Wind Vector Map (#wind-vector-map)
- Geo Point (#geo-point)
- Point Config (#config)
## Point Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "point",
    ...
  },
  "encoding": ... ,
  ...
}

```

A point mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| shape | String | String | ExprRef | Shape of the point marks. Supported values include: plotting shapes: "circle" , "square" , "cross" , "diamond" , "triangle-up" , "triangle-down" , "triangle-right" , or "triangle-left" . the line symbol "stroke" centered directional shapes "arrow" , "wedge" , or "triangle" a custom SVG path string (For correct sizing, custom shape paths should be defined within a square bounding box with coordinates ranging from -1 to 1 along both the x and y dimensions.) Default value: "circle" |
| size | Number | ExprRef | Default size for marks. For point / circle / square , this represents the pixel area of the marks. Note that this value sets the area of the symbol; the side lengths will increase with the square root of this value. For bar , this represents the band size of the bar, in pixels. For text , this represents the font size, in pixels. Default value: 30 for point, circle, square marks; width/heights step 2 for bar marks with discrete dimensions; 5 for bar marks with continuous dimensions; 11 for text marks. |

## Examples
### Dot Plot
Mapping a field to either only `x` or only `y` of `point` marks creates a dot plot.

### Scatter Plot
Mapping fields to both the `x` and `y` channels creates a scatter plot.

By default, `point` marks only have borders and are transparent inside. You can create a filled point by setting `filled` to `true`.

### Bubble Plot
By mapping a third field to the `size` channel in the scatter plot (#scatter), we can create a bubble plot instead.

### Scatter Plot with Color and/or Shape
Fields can also be encoded in the scatter plot (#scatter) using the `color` or `shape` channels. For example, this specification encodes the field `Origin` with both `color` and `shape`.

### Dot Plot with Jittering
To jitter points on a discrete scale, you can add random offset:

### Wind Vector Map
We can also use point mark with angle encoding to create a wind vector map.

### Geo Point
By mapping geographic coordinate data to `longitude` and `latitude` channels of a corresponding projection (projection.html), we can visualize geographic points. The example below shows major airports in the US.

## Point Config
```
// Top-level View Specification
{
  ...
  "config": {
    "point": ...,
    ...
  }
}

```

The `point` property of the top-level `config` (config.html) object sets the default properties for all point marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The point config can contain any point mark properties (#properties) (except `type`, `style`, and `clip`).

## Circle
Source: https://vega.github.io/vega-lite/docs/circle.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "circle",
  "encoding": ... ,
  ...
}

```

`circle` mark is similar to `point` (point.html) mark, except that (1) the `shape` value is always set to `circle` (2) they are filled by default.
## Circle Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "circle",
    ...
  },
  "encoding": ... ,
  ...
}

```

A circle mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| size | Number | ExprRef | Default size for marks. For point / circle / square , this represents the pixel area of the marks. Note that this value sets the area of the symbol; the side lengths will increase with the square root of this value. For bar , this represents the band size of the bar, in pixels. For text , this represents the font size, in pixels. Default value: 30 for point, circle, square marks; width/heights step 2 for bar marks with discrete dimensions; 5 for bar marks with continuous dimensions; 11 for text marks. |

## Examples
### Scatterplot with Circle
Here is an example scatter plot with `circle` marks:

## Circle Config
```
// Top-level View Specification
{
  ...
  "config": {
    "circle": ...,
    ...
  }
}

```

The `circle` property of the top-level `config` (config.html) object sets the default properties for all circle marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The circle config can contain any circle mark properties (#properties) (except `type`, `style`, and `clip`).

## Square
Source: https://vega.github.io/vega-lite/docs/square.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "square",
  "encoding": ... ,
  ...
}

```

`square` marks is similar to `point` (point.html) mark, except that (1) the `shape` value is always set to `square` (2) they are filled by default.
## Square Mark Properties
A square mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| size | Number | ExprRef | Default size for marks. For point / circle / square , this represents the pixel area of the marks. Note that this value sets the area of the symbol; the side lengths will increase with the square root of this value. For bar , this represents the band size of the bar, in pixels. For text , this represents the font size, in pixels. Default value: 30 for point, circle, square marks; width/heights step 2 for bar marks with discrete dimensions; 5 for bar marks with continuous dimensions; 11 for text marks. |

## Example: Scatterplot with Square
Here are an example scatter plot with `square` marks:

## Square Config
```
// Top-level View Specification
{
  ...
  "config": {
    "square": ...,
    ...
  }
}

```

The `square` property of the top-level `config` (config.html) object sets the default properties for all square marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The square config can contain any point mark properties (#properties) (except `type`, `style`, and `clip`).

## Rect
Source: https://vega.github.io/vega-lite/docs/rect.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "rect",
  "encoding": ... ,
  ...
}

```

The `rect` mark represents an arbitrary rectangle.
## Documentation Overview
- Rect Mark Properties (#properties)
- Examples (#examples)
- Heatmap (#heatmap)
- Ranged Rectangles (#ranged)
- Rect Config (#config)
## Rect Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "rect",
    ...
  },
  "encoding": ... ,
  ...
}

```

A rect mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| width | Number | ExprRef | Width of the marks. |
| height | Number | ExprRef | Height of the marks. |
| align | String | ExprRef | The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule). One of "left" , "right" , "center" . Note: Expression reference is not supported for range marks. |
| baseline | String | ExprRef | For text marks, the vertical text baseline. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , "line-bottom" , or an expression reference that provides one of the valid values. The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. For range marks, the vertical alignment of the marks. One of "top" , "middle" , "bottom" . Note: Expression reference is not supported for range marks. |
| cornerRadius | Number | ExprRef | The radius in pixels of rounded rectangles or arcs corners. Default value: 0 |
| binSpacing | Any |  |

## Examples
### Heatmap
Using the `rect` marks with discrete fields on `x` and `y` channels creates a heatmap.

We can similarly use rect with binned fields and discretized temporal fields.

### Ranged Rectangles
Specifying both `x` and `x2` and/or `y` and `y2` creates a rectangle that spans over certain x and/or y values.
For example, we can use `rect` to create an annotation `layer` (layer.html) that provides a shading between global `min` and `max` values.

## Rect Config
```
// Top-level View Specification
{
  ...
  "config": {
    "rect": ...,
    ...
  }
}

```

The `rect` property of the top-level `config` (config.html) object sets the default properties for all rect marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
Besides standard rect mark properties (#properties) (except `type`, `style`, and `clip`), rect config can contain the following additional properties:
| Property | Type | Description |
| --- | --- | --- |
| continuousBandSize | Number | The default size of the bars on continuous scales. Default value: 5 |
| discreteBandSize | Number | RelativeBandSize | The default size of the bars with discrete dimensions. If unspecified, the default size is step-2 , which provides 2 pixel offset between bars. |
| minBandSize | Number | ExprRef | The minimum band size for bar and rectangle marks. Default value: 0.25 |

## Tick
Source: https://vega.github.io/vega-lite/docs/tick.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "tick",
  "encoding": ... ,
  ...
}

```

The `tick` mark represents each data point as a short line. This is a useful mark for displaying the distribution of values in a field.
## Documentation Overview
- Tick Mark Properties (#properties)
- Examples (#examples)
- Dot Plot (#dot-plot)
- Strip Plot (#strip-plot)
- Tick Config (#config)
- Example Customizing Ticks Size and Thickness (#example-customizing-ticks-size-and-thickness)
## Tick Mark Properties
A tick mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| cornerRadius | Number | ExprRef | The radius in pixels of rounded rectangles or arcs corners. Default value: 0 |
| orient | String | The orientation of a non-stacked bar, tick, area, and line charts. The value is either horizontal (default) or vertical. For bar, rule and tick, this determines whether the size of the bar and tick should be applied to x or y dimension. For area, this property determines the orient property of the Vega output. For line and trail marks, this property determines the sort order of the points in the line if config.sortLineBy is not specified. For stacked charts, this is always determined by the orientation of the stack; therefore explicitly specified value will be ignored. |

## Examples
### Dot Plot
For example, the following dot plot uses tick marks to show the distribution of rainfall over time.

### Strip Plot
The following strip-plot use `tick` mark to show the distribution of horsepower.

## Tick Config
```
// Top-level View Specification
{
  ...
  "config": {
    "tick": ...,
    ...
  }
}

```

The `tick` property of the top-level `config` (config.html) object sets the default properties for all tick marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
Besides standard mark config properties (mark.html#config), tick config can contain the following additional properties:
| Property | Type | Description |
| --- | --- | --- |
| bandSize | Number | The width of the ticks. Default value: 3/4 of step (width step for horizontal ticks and height step for vertical ticks). |
| thickness | Number | Thickness of the tick mark. Default value: 1 |

#### Example Customizing Ticks Size and Thickness

## Rule
Source: https://vega.github.io/vega-lite/docs/rule.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "rule",
  "encoding": ... ,
  ...
}

```

The `rule` mark represents each data point as a line segment. It can be used in two ways. First, as a line segment that spans the complete width or height of a view. Second, a rule can be used to draw a line segment between two positions.
## Documentation Overview
- Rule Mark Properties (#properties)
- Examples (#examples)
- Width/Height-Spanning Rules (#widthheight-spanning-rules)
- Ranged Rules (#ranged)
- Rule Config (#config)
## Rule Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "rule",
    ...
  },
  "encoding": ... ,
  ...
}

```

A rule mark definition can contain any standard mark properties (mark.html#mark-def).
## Examples
### Width/Height-Spanning Rules
If the `rule` mark only has `y` encoding, the output view produces horizontal rules that spans the complete width. Similarly, if the `rule` mark only has `x` encoding, the output view produces vertical rules that spans the height.
We can use rules to show the average price of different stocks akin to `tick` (tick.html) marks.

The fact that rule marks span the width or the height of a single view make them useful as an annotation layer (layer.html). For example, we can use rules to show average values of different stocks alongside the price curve.

We can also use a rule mark to show global mean value over a histogram.

### Ranged Rules
To control the spans of horizontal/vertical rules, `x` and `x2`/`y` and `y2` channels can be specified.
For example, we can use `y` and `y2` show the `"min"` and `"max"` values of horsepowers for cars from different locations.

We can also use rule to create error bars. In the example below, we use the `ci0` and `ci1` aggregation operators (aggregate.html#ops) to visualize the 95% confidence interval (https://en.wikipedia.org/wiki/Confidence_interval) as a measure of the spread of the average yields for a variety of barley strains.

Alternatively, we can create error bars showing one standard deviation (`stdev`) over and below the mean value.

## Rule Config
```
// Top-level View Specification
{
  ...
  "config": {
    "rule": ...,
    ...
  }
}

```

The `rule` property of the top-level `config` (config.html) object sets the default properties for all rule marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The rule config can contain any rule mark properties (#properties) (except `type`, `style`, and `clip`).

## Text
Source: https://vega.github.io/vega-lite/docs/text.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "text",
  "encoding": ... ,
  ...
}

```

`text` mark represents each data point with a text instead of a point.
## Documentation Overview
- Text Mark Properties (#properties)
- Examples (#examples)
- Text Table Heatmap (#text-table-heatmap)
- Labels (#labels)
- Scatterplot with Text (#scatterplot-with-text)
- Geo Text (#geo-text)
- Text Config (#config)
## Text Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "text",
    ...
  },
  "encoding": ... ,
  ...
}

```

A text mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| angle | Number | ExprRef | The rotation angle of the text, in degrees. |
| align | String | ExprRef | The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule). One of "left" , "right" , "center" . Note: Expression reference is not supported for range marks. |
| baseline | String | ExprRef | For text marks, the vertical text baseline. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , "line-bottom" , or an expression reference that provides one of the valid values. The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. For range marks, the vertical alignment of the marks. One of "top" , "middle" , "bottom" . Note: Expression reference is not supported for range marks. |
| dir | String | ExprRef | The direction of the text. One of "ltr" (left-to-right) or "rtl" (right-to-left). This property determines on which side is truncated in response to the limit parameter. Default value: "ltr" |
| dx | Number | ExprRef | The horizontal offset, in pixels, between the text label and its anchor point. The offset is applied after rotation by the angle property. |
| dy | Number | ExprRef | The vertical offset, in pixels, between the text label and its anchor point. The offset is applied after rotation by the angle property. |
| ellipsis | String | ExprRef | The ellipsis string for text truncated in response to the limit parameter. Default value: "..." |
| font | String | ExprRef | The typeface to set the text in (e.g., "Helvetica Neue" ). |
| fontSize | Number | ExprRef | The font size, in pixels. Default value: 11 |
| fontStyle | String | ExprRef | The font style (e.g., "italic" ). |
| fontWeight | String | Number | ExprRef | The font weight. This can be either a string (e.g "bold" , "normal" ) or a number ( 100 , 200 , 300 , ..., 900 where "normal" = 400 and "bold" = 700 ). |
| limit | Number | ExprRef | The maximum length of the text mark in pixels. The text value will be automatically truncated if the rendered size exceeds the limit. Default value: 0  indicating no limit |
| lineHeight | Number | ExprRef | The line height in pixels (the spacing between subsequent lines of text) for multi-line text marks. |
| radius | Number | ExprRef | For arc mark, the primary (outer) radius in pixels. For text marks, polar coordinate radial offset, in pixels, of the text from the origin determined by the x and y properties. Default value: min(plot_width, plot_height)/2 |
| text | Text | ExprRef | Placeholder text if the text channel is not specified |
| theta | Number | ExprRef | For arc marks, the arc length in radians if theta2 is not specified, otherwise the start arc angle. (A value of 0 indicates up or north, increasing values proceed clockwise.) For text marks, polar coordinate angle in radians. |

## Examples
### Text Table Heatmap

### Labels
You can also use `text` marks as labels for other marks and set offset (`dx` or `dy`), `align`, and `baseline` properties of the mark definition.

### Scatterplot with Text
Mapping a field to `text` channel of text mark sets the marks text value. For example, we can make a colored scatterplot with text marks showing the initial character of its origin, instead of `point` (point.html#color) marks.

### Geo Text
By mapping geographic coordinate data to `longitude` and `latitude` channels of a corresponding projection (projection.html), we can show text at accurate locations. The example below shows the name of every US state capital at the location of the capital.

## Text Config
```
// Top-level View Specification
{
  ...
  "config": {
    "text": ...,
    ...
  }
}

```

The `text` property of the top-level `config` (config.html) object sets the default properties for all text marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.

## Trail
Source: https://vega.github.io/vega-lite/docs/trail.html

```
{
  "data": ... ,
  "mark": "trail",
  "encoding": ... ,
  ...
}

```

The `trail` mark represents the data points stored in a field with a line connecting all of these points. Trail is similar to the `line` mark but a trail can have variable widths determined by backing data. Unlike lines, trails do not support different interpolation methods and use `fill` (not `stroke`) for their color. Trail marks are useful if you want to draw lines with changing size to reflect the underlying data.
## Documentation Overview
- Trail Mark Properties (#properties)
- Examples (#examples)
- A Line Chart with varying size using `trail` mark (#a-line-chart-with-varying-size-using-trail-mark)
- A Comet Chart showing changes between two states (#a-comet-chart-showing-changes-between-two-states)
- Trail Config (#config)
## Trail Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "trail",
    ...
  },
  "encoding": ... ,
  ...
}

```

A trail mark definition can contain any standard mark properties (mark.html#mark-def) and the following properties:
| Property | Type | Description |
| --- | --- | --- |
| orient | String | The orientation of a non-stacked bar, tick, area, and line charts. The value is either horizontal (default) or vertical. For bar, rule and tick, this determines whether the size of the bar and tick should be applied to x or y dimension. For area, this property determines the orient property of the Vega output. For line and trail marks, this property determines the sort order of the points in the line if config.sortLineBy is not specified. For stacked charts, this is always determined by the orientation of the stack; therefore explicitly specified value will be ignored. |

## Examples
### A Line Chart with varying size using `trail` mark

### A Comet Chart showing changes between two states

## Trail Config
```
// Top-level View Specification
{
  ...
  "config": {
    "trail": ...,
    ...
  }
}

```

The `trail` property of the top-level `config` (config.html) object sets the default properties for all trail marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The trail config can contain any trail mark properties (#properties) (except `type`, `style`, and `clip`).

## Image
Source: https://vega.github.io/vega-lite/docs/image.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "image",
  "encoding": ... ,
  ...
}

```

Image marks allow external images, such as icons or photographs, to be included in Vega-Lite visualizations. Image files such as PNG or JPG images are loaded from provided URLs.
## Documentation Overview
- Image Mark Properties (#properties)
- Examples (#examples)
- Scatterplot with Image Marks (#scatterplot-with-image-marks)
- Image Config (#image-config)
## Image Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "image",
    ...
  },
  "encoding": ... ,
  ...
}

```

An `image` mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| url | URI | ExprRef | The URL of the image file for image marks. |
| aspect | Boolean | ExprRef | Whether to keep aspect ratio of image marks. |
| align | String | ExprRef | The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule). One of "left" , "right" , "center" . Note: Expression reference is not supported for range marks. |
| baseline | String | ExprRef | For text marks, the vertical text baseline. One of "alphabetic" (default), "top" , "middle" , "bottom" , "line-top" , "line-bottom" , or an expression reference that provides one of the valid values. The "line-top" and "line-bottom" values operate similarly to "top" and "bottom" , but are calculated relative to the lineHeight rather than fontSize alone. For range marks, the vertical alignment of the marks. One of "top" , "middle" , "bottom" . Note: Expression reference is not supported for range marks. |

## Examples
### Scatterplot with Image Marks

## Image Config
```
// Top-level View Specification
{
  ...
  "config": {
    "image": ...,
    ...
  }
}

```

The `image` property of the top-level `config` (config.html) object sets the default properties for all image marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The image config can contain any image mark properties (#properties) (except `type`, `style`, and `clip`).

## Arc
Source: https://vega.github.io/vega-lite/docs/arc.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "arc",
  "encoding": ... ,
  ...
}

```

Arc marks are circular arcs defined by a center point plus angular and radial extents. Arc marks are typically used for radial plots such as pie and donut charts.
## Documentation Overview
- Arc Mark Properties (#properties)
- Examples (#examples)
- Pie and Donut Charts (#pie-and-donut-charts)
- Pie Charts with Tooltips (#tooltip)
- Arc Config (#arc-config)
- Faceted Pie Charts (#faceted-pie-charts)
## Arc Mark Properties
```
// Single View Specification
{
  ...
  "mark": {
    "type": "arc",
    ...
  },
  "encoding": ... ,
  ...
}

```

An `arc` mark definition can contain any standard mark properties (mark.html#mark-def) and the following special properties:
| Property | Type | Description |
| --- | --- | --- |
| radius | Number | ExprRef | For arc mark, the primary (outer) radius in pixels. For text marks, polar coordinate radial offset, in pixels, of the text from the origin determined by the x and y properties. Default value: min(plot_width, plot_height)/2 |
| radius2 | Number | ExprRef | The secondary (inner) radius in pixels of arc marks. Default value: 0 |
| innerRadius | Number | ExprRef | The inner radius in pixels of arc marks. innerRadius is an alias for radius2 . Default value: 0 |
| outerRadius | Number | ExprRef | The outer radius in pixels of arc marks. outerRadius is an alias for radius . Default value: 0 |
| theta | Number | ExprRef | For arc marks, the arc length in radians if theta2 is not specified, otherwise the start arc angle. (A value of 0 indicates up or north, increasing values proceed clockwise.) For text marks, polar coordinate angle in radians. |
| theta2 | Number | ExprRef | The end angle of arc marks in radians. A value of 0 indicates up or north, increasing values proceed clockwise. |
| cornerRadius | Number | ExprRef | The radius in pixels of rounded rectangles or arcs corners. Default value: 0 |
| padAngle | Number | ExprRef | The angular padding applied to sides of the arc, in radians. |
| radiusOffset | Number | ExprRef | Offset for radius. |
| radius2Offset | Number | ExprRef | Offset for radius2. |
| thetaOffset | Number | ExprRef | Offset for theta. |
| theta2Offset | Number | ExprRef | Offset for theta2. |

## Examples
### Pie and Donut Charts
We can create a pie chart by encoding `theta` and `color` or arc marks.

Setting `innerRadius` to non-zero values will create a donut chart.

You can also add a text layer to add labels to a pie chart.

Note: For now, you need to add `stack: true` (https://github.com/vega/vega-lite/issues/5078) to theta to force the text to apply the same polar stacking layout.
### Pie Charts with Tooltips
To add tooltip, you can set `tooltip: true` in `mark`

By default, the tooltip will show actual value of the theta field.
Alternatively, setting `stack: "normalize"` allows for tooltips that display the percentage of the pie taken up by a each slice.
## Arc Config
```
// Top-level View Specification
{
  ...
  "config": {
    "arc": ...,
    ...
  }
}

```

The `arc` property of the top-level `config` (config.html) object sets the default properties for all arc marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
The arc config can contain any arc mark properties (#properties) (except `type`, `style`, and `clip`).
## Faceted Pie Charts
By default, the theta channel in faceted charts resolves (resolve.html) to independent scales so that the ratios are comparable.

## Box Plot
Source: https://vega.github.io/vega-lite/docs/boxplot.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "boxplot",
  "encoding": ... ,
  ...
}

```

A box plot summarizes a distribution of quantitative values using a set of summary statistics. The median tick in the box represents the median. The lower and upper parts of the box represent the first and third quartile respectively. Depending on the type of box plot (#boxplot-types), the ends of the whiskers can represent multiple things.
To create a box plot, set `mark` to `"boxplot"`.
## Documentation Overview
- Box Plot Mark Properties (#properties)
- Types of Box Plot (#boxplot-types)
- Dimension & Orientation (#dims-orient)
- The Parts of Box Plots (#parts)
- Color, Size, and Opacity Encoding Channels (#color-size-and-opacity-encoding-channels)
- Tooltip Encoding Channels (#tooltip-encoding-channels)
- Mark Config (#config)
- Box Plot with Pre-Calculated Summaries (#box-plot-with-pre-calculated-summaries)
## Box Plot Mark Properties
A boxplots mark definition contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| type | BoxPlot | Required. The mark type. This could a primitive mark type (one of "bar" , "circle" , "square" , "tick" , "line" , "area" , "point" , "geoshape" , "rule" , and "text" ) or a composite mark type ( "boxplot" , "errorband" , "errorbar" ). |
| extent | String | Number | The extent of the whiskers. Available options include: "min-max" : min and max are the lower and upper whiskers respectively. A number representing multiple of the interquartile range. This number will be multiplied by the IQR to determine whisker boundary, which spans from the smallest data to the largest data within the range [Q1 - k * IQR, Q3 + k * IQR] where Q1 and Q3 are the first and third quartiles while IQR is the interquartile range ( Q3-Q1 ). Default value: 1.5 . |
| orient | String | Orientation of the box plot. This is normally automatically determined based on types of fields on x and y channels. However, an explicit orient be specified when the orientation is ambiguous. Default value: "vertical" . |
| size | Number | Size of the box and median tick of a box plot |
| color | Color | Gradient | ExprRef | Default color. Default value:  "#4682b4" Note: This property cannot be used in a style config . The fill and stroke properties have higher precedence than color and will override color . |
| opacity | Number | The opacity (value between [0,1]) of the mark. |
| invalid | String | Null | Invalid data mode, which defines how the marks and corresponding scales should represent invalid values ( null and NaN in continuous scales without defined output for invalid values). "filter"  Exclude all invalid values from the visualizations marks and scales . For path marks (for line, area, trail), this option will create paths that connect valid points, as if the data rows with invalid values do not exist. "break-paths-filter-domains"  Break path marks (for line, area, trail) at invalid values. For non-path marks, this is equivalent to "filter" . All scale domains will exclude these filtered data points. "break-paths-show-domains"  Break paths (for line, area, trail) at invalid values. Hide invalid values for non-path marks. All scale domains will include these filtered data points (for both path and non-path marks). "show" or null  Show all data points in the marks and scale domains. Each scale will use the output for invalid values defined in config.scale.invalid or, if unspecified, by default invalid values will produce the same visual values as zero (if the scale includes zero) or the minimum value (if the scale does not include zero). "break-paths-show-path-domains" (default)  This is equivalent to "break-paths-show-domains" for path-based marks (line/area/trail) and "filter" for non-path marks. Note : If any channels scale has an output for invalid values defined in config.scale.invalid , all values for the scales will be considered valid since they can produce a reasonable output for the scales. Thus, fields for such channels will not be filtered and will not cause path breaks. |

Besides the properties listed above, `"box"`, `"median"`, `"rule"`, `"outliers"`, and `"ticks"` can be used to specify the underlying mark properties (mark.html#mark-def) for different parts of the box plots (#parts) as well.
## Types of Box Plot
Vega-Lite supports two types of box plots, defined by the `extent` property in the mark definition object.
- Tukey Box Plot is the default box plot in Vega-Lite. For a Tukey box plot, the whisker spans from the smallest data to the largest data within the range [Q1 - k * IQR, Q3 + k * IQR] where Q1 and Q3 are the first and third quartiles while IQR is the interquartile range (Q3-Q1). In this type of box plot, you can specify the constant k by setting the `extent`. If there are outlier points beyond the whisker (#dims-orient), they will be displayed using point marks.
By default, the extent is `1.5`.
Explicitly setting `extent` to `1.5` produces the following identical plot.
- `min-max` Box Plot is a box plot where the lower and upper whiskers are defined as the min and max respectively. No points will be considered as outliers for this type of box plots.
## Dimension & Orientation
Vega-Lite supports both 1D and 2D box plots:
1D box plot shows the distribution of a continuous field.
A boxplots orientation is automatically determined by the continuous field axis. For example, you can create a vertical 1D box plot by encoding a continuous field on the y axis.
2D box plot shows the distribution of a continuous field, broken down by categories.
For 2D box plots with one continuous field and one discrete field, the box plot will be horizontal if the continuous field is on the x axis.
Alternatively, if the continuous field is on the y axis, the box plot will be vertical.
## The Parts of Box Plots
Under the hood, the `"boxplot"` mark is a composite mark (mark.html#composite-marks) that expands into a layered plot. For example, a basic 1D boxplot shown above (#dims-orient) is expanded to:
To customize different parts of the box, we can customize different parts of the box plot mark definition (#properties) or config (#config).
For example, we can customize the box plots `"median"` tick by setting `"color"` to `"red"` and set `"ticks"` to true to make the box plot includes end ticks:
## Color, Size, and Opacity Encoding Channels
You can customize the color, size, and opacity of the box in the `boxplot` by using the `color`, `size`, and `opacity` encoding channels (encoding.html#channels). The `size` is applied to only the box and median tick. The `color` is applied to only the box and the outlier points. Meanwhile, the `opacity` is applied to the whole `boxplot`.
An example of a `boxplot` where the `size` encoding channel is specified.
## Tooltip Encoding Channels
You can add custom tooltips to box plots. The custom tooltip will override the default boxplots tooltips.
If the field in the tooltip encoding is unaggregated, it replaces the tooltips of the outlier marks.
On the other hand, if the field in the tooltip encoding is aggregated, it replaces the tooltips of the box and whisker marks.
## Mark Config
```
{
  "boxplot": {
    "size": ...,
    "extent": ...,
    "box": ...,
    "median": ...,
    "whisker": ...,
    "outliers": ...
  }
}

```

The `boxplot` config object sets the default properties for `boxplot` marks.
The boxplot config can contain all boxplot mark properties (#properties) but currently not supporting `color`, `opacity`, and `orient`. Please see issue #3934 (https://github.com/vega/vega-lite/issues/3934).
## Box Plot with Pre-Calculated Summaries
If you have data summaries pre-calculated for a box plot, you can use `layer` to build a box plot like this:

## Error Band
Source: https://vega.github.io/vega-lite/docs/errorband.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "errorband",
  "encoding": ... ,
  ...
}

```

An error band summarizes an error range of quantitative values using a set of summary statistics, representing by area. Error band in Vega-Lite can either be used to aggregate raw data or directly visualize aggregated data.
To create an error band, set `mark` to `"errorband"`.
## Documentation Overview
- Error Band Mark Properties (#properties)
- Comparing the usage of Error Band to the usage of Error Bar (#compare-to-errorbar)
- Error Band (#errorband-ex)
- Error Bar (#error-bar)
- Using Error Band to Aggregate Raw Data (#raw-usage)
- Using Error Band to Visualize Aggregated Data (#pre-aggregated-usage)
- Dimension (#dimension)
- The Parts of Error Band (#parts)
- Color, and Opacity Encoding Channels (#color-and-opacity-encoding-channels)
- Tooltip Encoding Channels (#config)
- Mark Config (#mark-config)
## Error Band Mark Properties
An error bands mark definition can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| type | ErrorBand | Required. The mark type. This could a primitive mark type (one of "bar" , "circle" , "square" , "tick" , "line" , "area" , "point" , "geoshape" , "rule" , and "text" ) or a composite mark type ( "boxplot" , "errorband" , "errorbar" ). |
| extent | String | The extent of the band. Available options include: "ci" : Extend the band to the 95% bootstrapped confidence interval of the mean. "stderr" : The size of band are set to the value of standard error, extending from the mean. "stdev" : The size of band are set to the value of standard deviation, extending from the mean. "iqr" : Extend the band to the q1 and q3. Default value: "stderr" . |
| orient | String | Orientation of the error band. This is normally automatically determined, but can be specified when the orientation is ambiguous and cannot be automatically determined. |
| color | Color | Gradient | ExprRef | Default color. Default value:  "#4682b4" Note: This property cannot be used in a style config . The fill and stroke properties have higher precedence than color and will override color . |
| opacity | Number | The opacity (value between [0,1]) of the mark. |
| interpolate | String | The line interpolation method for the error band. One of the following: "linear" : piecewise linear segments, as in a polyline. "linear-closed" : close the linear segments to form a polygon. "step" : a piecewise constant function (a step function) consisting of alternating horizontal and vertical lines. The y-value changes at the midpoint of each pair of adjacent x-values. "step-before" : a piecewise constant function (a step function) consisting of alternating horizontal and vertical lines. The y-value changes before the x-value. "step-after" : a piecewise constant function (a step function) consisting of alternating horizontal and vertical lines. The y-value changes after the x-value. "basis" : a B-spline, with control point duplication on the ends. "basis-open" : an open B-spline; may not intersect the start or end. "basis-closed" : a closed B-spline, as in a loop. "cardinal" : a Cardinal spline, with control point duplication on the ends. "cardinal-open" : an open Cardinal spline; may not intersect the start or end, but will intersect other control points. "cardinal-closed" : a closed Cardinal spline, as in a loop. "bundle" : equivalent to basis, except the tension parameter is used to straighten the spline. "monotone" : cubic interpolation that preserves monotonicity in y. |
| tension | Number | The tension parameter for the interpolation type of the error band. |

Besides the properties listed above, `band` and `borders` can be used to specify the underlying mark properties (mark.html#mark-def) for different parts of the error band (#parts) as well.
## Comparing the usage of Error Band to the usage of Error Bar
All the properties and usage of error band are identical to error bars, except the `band` and `borders` that replace the error bars `rule` and `ticks`.
#### Error Band
#### Error Bar
## Using Error Band to Aggregate Raw Data
If the data is not aggregated yet, Vega-Lite will aggregate the data based on the `extent` properties in the mark definition as done in the error band showing confidence interval (#errorband-ex) above. All other `extent` values are defined in Error Bar (errorbar.html#raw-usage).
## Using Error Band to Visualize Aggregated Data
- Data is aggregated with low and high values of the error band
If the data is already pre-aggregated with low and high values of the error band, you can directly specify `x` and `x2` (or `y` and `y2`) to use error band as a ranged mark.
- Data is aggregated with center and error value(s)
If the data is already pre-aggregated with center and error values of the error band, you can use `x/y`, `x/yError`, and `x/yError2` as defined in Error Bar (errorbar.html#pre-aggregated-usage)
## Dimension
Vega-Lite supports both 1D and 2D error bands:
{:#1d} A 1D error band shows the error range of a continuous field; it can be used to show the global error range of the whole plot.
{:#2d} A 2D error band shows the error range of a continuous field for each dimension value such as year.
## The Parts of Error Band
Under the hood, the `errorband` mark is a composite mark (mark.html#composite-marks) that expands into a layered plot. For example, the basic 2D error band shown above (#2d) is equivalent to:
We can customize different parts of the error band mark definition (#properties) or config (#config).
For example, we can add the error bands borders and customize it by setting `borders` to `true` or adding a mark property to `borders`, such as `strokeDash` and `opacity`:
## Color, and Opacity Encoding Channels
You can customize the color, size, and opacity of the band in the `errorband` by using the `color`, and `opacity` encoding channels (encoding.html#channels), which applied to the whole `errorband`.
Here is an example of a `errorband` with the `color` encoding channel set to `{"value": "black"}`.
## Tooltip Encoding Channels
You can add custom tooltips to error bands. The custom tooltip will override the default error bands tooltips.
## Mark Config
```
{
  "errorband": {
    "extent": ...,
    "band": ...,
    "borders": ...
  }
}

```

The `errorband` config object sets the default properties for `errorband` marks.
The error band config can contain all error band mark properties (#properties) but currently not supporting `color`, `opacity`, and `orient`. Please see issue #3934 (https://github.com/vega/vega-lite/issues/3934).

## Error Bar
Source: https://vega.github.io/vega-lite/docs/errorbar.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "errorbar",
  "encoding": ... ,
  ...
}

```

An error bar summarizes an error range of quantitative values using a set of summary statistics, representing by rules (and optional end ticks). Error bars in Vega-Lite can either be used to aggregate raw data or directly visualize aggregated data.
To create an error bar, set `mark` to `"errorbar"`.
## Documentation Overview
- Error Bar Mark Properties (#properties)
- Using Error Bars to Aggregate Raw Data (#raw-usage)
- Using Error Bars to Visualize Aggregated Data (#pre-aggregated-usage)
- Dimension & Orientation (#dimension--orientation)
- The Parts of Error Bars (#parts)
- Color, and Opacity Encoding Channels (#color-and-opacity-encoding-channels)
- Tooltip Encoding Channels (#tooltip-encoding-channels)
- Mark Config (#config)
## Error Bar Mark Properties
An error bars mark definition contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| type | ErrorBar | Required. The mark type. This could a primitive mark type (one of "bar" , "circle" , "square" , "tick" , "line" , "area" , "point" , "geoshape" , "rule" , and "text" ) or a composite mark type ( "boxplot" , "errorband" , "errorbar" ). |
| extent | String | The extent of the rule. Available options include: "ci" : Extend the rule to the 95% bootstrapped confidence interval of the mean. "stderr" : The size of rule are set to the value of standard error, extending from the mean. "stdev" : The size of rule are set to the value of standard deviation, extending from the mean. "iqr" : Extend the rule to the q1 and q3. Default value: "stderr" . |
| orient | String | Orientation of the error bar. This is normally automatically determined, but can be specified when the orientation is ambiguous and cannot be automatically determined. |
| color | Color | Gradient | ExprRef | Default color. Default value:  "#4682b4" Note: This property cannot be used in a style config . The fill and stroke properties have higher precedence than color and will override color . |
| opacity | Number | The opacity (value between [0,1]) of the mark. |

Besides the properties listed above, `rule` and `ticks` can be used to specify the underlying mark properties (mark.html#mark-def) for different parts of the error bar (#parts) as well.
## Using Error Bars to Aggregate Raw Data
If the data is not aggregated yet, Vega-Lite will aggregate the data based on the `extent` properties in the mark definition.
- Error bars showing standard error is the default error bar in Vega-Lite. It can also be explicitly specified by setting `extent` to `"stderr"`. The length of lower and upper rules represent standard error. By default, the rule marks expand from the mean.
- Error bar showing standard deviation can be specified by setting `extent` to `"stdev"`. For this type of error bar, the length of lower and upper rules represent standard deviation. Like an error bar that shows Standard Error, the rule marks expand from the mean by default.
- Error bars showing confidence interval can be specified by setting `extent` to `"ci"`. For this type of error bar, the rule marks expand from the `"ci0"` value to `"ci1"` value, as defined in aggregate (aggregate.html#ops).
- Error bars showing interquartile range can be specified by setting `extent` to `"iqr"`. For this type of error bar, the rule marks expand from the first quartile to the third quartile.
## Using Error Bars to Visualize Aggregated Data
- Data is aggregated with low and high values of the error bars
If the data is already pre-aggregated with low and high values of the error bars, you can directly specify `x` and `x2` (or `y` and `y2`) to use error bar as a ranged mark.
- Data is aggregated with center and error value(s)
If the data is already pre-aggregated with center and error values of the error bars, you can directly specity `x` as center, `xError` and `xError2` as error values extended from center (or `y`, `yError`, and `yError2`). If `x/yError2` is omitted, error bars have symmetric error values.
Error bar with symmetric error values:
Error bar with asymmetric error values:
Note if error is pre-aggregated with asymmetric error values one of `x/yError` and `x/yError2` has to be positive value and other has to be negative value
## Dimension & Orientation
Vega-Lite supports both 1D and 2D error bars:
{:#1d} A 1D error bar shows the error range of a continuous field.
The orientation of an error bar is automatically determined by the continuous field axis. For example, you can create a vertical 1D error bar by encoding a continuous field on the y axis.
{:#2d} A 2D error bar shows the error range of a continuous field, broken down by categories.
For 2D error bars with one continuous field and one discrete field, the error bars will be horizontal if the continuous field is on the x axis.
Alternatively, if the continuous field is on the y axis, the error bar will be vertical.
## The Parts of Error Bars
Under the hood, the `errorbar` mark is a composite mark (mark.html#composite-marks) that expands into a layered plot. For example, a basic 1D error bar shown above (#1d) is expanded to:
We can customize different parts of the error bar mark definition (#properties) or config (#config).
For example, we can add the error bars end ticks and customize it by setting `ticks` to `true` or adding a mark property to `ticks`, such as setting `color` to `"teal"`:
## Color, and Opacity Encoding Channels
You can customize the color, size, and opacity of the bar in the `errorbar` by using the `color`, and `opacity` encoding channels (encoding.html#channels), which applied to the whole `errorbar`.
Here is an example of a `errorbar` with the `color` encoding channel set to `{"value": "#4682b4"}`.
## Tooltip Encoding Channels
You can add custom tooltips to error bars. The custom tooltip will override the default error bars tooltips.
## Mark Config
```
{
  "errorbar": {
    "extent": ...,
    "rule": ...,
    "ticks": ...
  }
}

```

The `errorbar` config object sets the default properties for `errorbar` marks.
The error bar config can contain all error bar mark properties (#properties) but currently does not support `color`, `opacity`, and `orient`. Please see issue #3934 (https://github.com/vega/vega-lite/issues/3934) for details.

## Geoshape
Source: https://vega.github.io/vega-lite/docs/geoshape.html

```
// Single View Specification
{
  "data": ... ,
  "mark": "geoshape",
  "encoding": ... ,
  ...
}

```

The `geoshape` mark represents an arbitrary shapes whose geometry is determined by specified GeoJSON shape data that is projected (projection.html) from geographical coordinates to pixels.
Here are an example choropleth making use of `geoshape` marks:

## Geoshape Config
```
// Top-level View Specification
{
  ...
  "config": {
    "geoshape": ...,
    ...
  }
}

```

The `geoshape` property of the top-level `config` (config.html) object sets the default properties for all geoshape marks. If mark property encoding channels (encoding.html#mark-prop) are specified for marks, these config values will be overridden.
For the list of all supported properties, please see the mark config documentation (mark.html#config).

