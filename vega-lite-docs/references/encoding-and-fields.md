# Encoding And Fields

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Encoding
Source: https://vega.github.io/vega-lite/docs/encoding.html

An integral part of the data visualization process is encoding data with visual properties of graphical marks. The `encoding` property of a single view specification represents the mapping between encoding channels (#channels) (such as `x`, `y`, or `color`) and data fields (#field-def), constant visual values (#value-def), or constant data values (datum) (#datum-def).
```
// Specification of a Single View
{
  "data": ... ,
  "mark": ... ,
  "encoding": {     // Encoding
    // Position Channels
    "x": ...,
    "y": ...,
    "x2": ...,
    "y2": ...,
    "xError": ...,
    "yError": ...,
    "xError2": ...,
    "yError2": ...,

    // Polar Position Channels
    "theta": ...,
    "radius": ...,
    "theta2": ...,
    "radius2": ...,

    // Geographic Position Channels
    "longitude": ...,
    "latitude": ...,
    "longitude2": ...,
    "latitude2": ...,

    // Mark Properties Channels
    "color": ...,
    "opacity": ...,
    "fillOpacity": ...,
    "strokeOpacity": ...,
    "strokeWidth": ...,
    "strokeDash": ...,
    "size": ...,
    "angle": ...,
    "shape": ...,

    // Text and Tooltip Channels
    "text": ...,
    "tooltip": ...,

    // Hyperlink Channel
    "href": ...,

    // Description Channel
    "description": ...,

    // Level of Detail Channel
    "detail": ...,

    // Key Channel
    "key": ...,

    // Order Channel
    "order": ...,

    // Facet Channels
    "facet": ...,
    "row": ...,
    "column": ...
  },
  ...
}

```

## Encoding Channels
The keys in the `encoding` object are encoding channels. Vega-Lite supports the following groups of encoding channels
- Position Channels (#position): `x`, `y`, `x2`, `y2`, `xError`, `yError`, `xError2`, `yError2`
- Position Offset Channels (#position-offset): `xOffset`, `yOffset`
- Polar Position Channels (#polar): `theta`, `theta2`, `radius`, `radius2`
- Geographic Position Channels (#geo): `longitude`, `latitude`, `longitude2`, `latitude2`
- Mark Property Channels (#mark-prop): `angle`, `color` (and `fill` / `stroke`), `opacity`, `fillOpacity`, `strokeOpacity`, `shape`, `size`, `strokeDash`, `strokeWidth`
- Text and Tooltip Channels (#text): `text`, `tooltip`
- Hyperlink Channel (#href): `href`
- Description Channel (#description): `description`
- Level of Detail Channel (#detail): `detail`
- Key Channel (#key): `key`
- Order Channel (#order): `order`
- Facet Channels (#facet): `facet`, `row`, `column`
## Channel Definition
Each channel definition object must be one of the following:
- Field definition (#field-def), which describes the data field encoded by the channel.
- Value definition (#value-def), which describes an encoded constant visual value.
- Datum definition (#datum-def), which describes a constant data value encoded via a scale.
### Field Definition
```
// Specification of a Single View
{
  ...,
  "encoding": {     // Encoding
    ...: {
      "field": ...,
      "type": ...,
      ...
    },
    ...
  },
  ...
}

```

To encode a particular field in the data set with an encoding channel, the channels field definition must describe the `field` (field.html) name and its data `type` (type.html). To facilitate data exploration, Vega-Lite also provides inline field transforms (`aggregate` (aggregate.html), `bin` (bin.html), `sort` (sort.html), `stack` (stack.html), and `timeUnit` (timeunit.html)) as a part of a field definition in addition to the top-level `transform` (transform.html).
All field definitions support the following properties:
| Property | Type | Description |
| --- | --- | --- |
| field | Field | Required. A string defining the name of the field from which to pull a data value or an object defining iterated values from the repeat operator. See also: field documentation. Notes: 1) Dots ( . ) and brackets ( [ and ] ) can be used to access nested objects (e.g., "field": "foo.bar" and "field": "foo['bar']" ). If field names contain dots or brackets but are not nested, you can use \\ to escape dots and brackets (e.g., "a\\.b" and "a\\[0\\]" ). See more details about escaping in the field documentation . 2) field is not required if aggregate is count . |
| type | String | The type of measurement ( "quantitative" , "temporal" , "ordinal" , or "nominal" ) for the encoded field or constant value ( datum ). It can also be a "geojson" type for encoding geoshape . Vega-Lite automatically infers data types in many cases as discussed below. However, type is required for a field if: (1) the field is not nominal and the field encoding has no specified aggregate (except argmin and argmax ), bin , scale type, custom sort order, nor timeUnit or (2) if you wish to use an ordinal scale for a field with bin or timeUnit . Default value: 1) For a data field , "nominal" is the default data type unless the field encoding has aggregate , channel , bin , scale type, sort , or timeUnit that satisfies the following criteria: "quantitative" is the default type if (1) the encoded field contains bin or aggregate except "argmin" and "argmax" , (2) the encoding channel is latitude or longitude channel or (3) if the specified scale type is a quantitative scale . "temporal" is the default type if (1) the encoded field contains timeUnit or (2) the specified scale type is a time or utc scale "ordinal" is the default type if (1) the encoded field contains a custom sort order , (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding channel is order . 2) For a constant value in data domain ( datum ): "quantitative" if the datum is a number "nominal" if the datum is a string "temporal" if the datum is a date time object Note: Data type describes the semantics of the data rather than the primitive data types (number, string, etc.). The same primitive data type can have different types of measurement. For example, numeric data can represent quantitative, ordinal, or nominal data. Data values for a temporal field can be either a date-time string (e.g., "2015-03-07 12:32:17" , "17:01" , "2015-03-16" . "2015" ) or a timestamp number (e.g., 1552199579097 ). When using with bin , the type property can be either "quantitative" (for using a linear bin scale) or "ordinal" (for using an ordinal bin scale) . When using with timeUnit , the type property can be either "temporal" (default, for using a temporal scale) or "ordinal" (for using an ordinal scale) . When using with aggregate , the type property refers to the post-aggregation data type. For example, we can calculate count distinct of a categorical field "cat" using {"aggregate": "distinct", "field": "cat"} . The "type" of the aggregate output is "quantitative" . Secondary channels (e.g., x2 , y2 , xError , yError ) do not have type as they must have exactly the same type as their primary channels (e.g., x , y ). See also: type documentation. |
| bin | Boolean | BinParams | String | Null | A flag for binning a quantitative field, an object defining binning parameters , or indicating that the data for x or y channel are binned before they are imported into Vega-Lite ( "binned" ). If true , default binning parameters will be applied. If "binned" , this indicates that the data for the x (or y ) channel are already binned. You can map the bin-start field to x (or y ) and the bin-end field to x2 (or y2 ). The scale and axis will be formatted similar to binning in Vega-Lite. To adjust the axis ticks based on the bin step, you can also set the axiss tickMinStep property. Default value: false See also: bin documentation. |
| timeUnit | TimeUnit | String | TimeUnitParams | Time unit (e.g., year , yearmonth , month , hours ) for a temporal field. or a temporal field that gets casted as ordinal . Default value: undefined (None) See also: timeUnit documentation. |
| aggregate | Aggregate | Aggregation function for the field (e.g., "mean" , "sum" , "median" , "min" , "max" , "count" ). Default value: undefined (None) See also: aggregate documentation. |
| band | Any |  |
| title | Text | Null | A title for the field. If null , the title will be removed. Default value: derived from the fields name and transformation function ( aggregate , bin and timeUnit ). If the field has an aggregate function, the function is displayed as part of the title (e.g., "Sum of Profit" ). If the field is binned or has a time unit applied, the applied function is shown in parentheses (e.g., "Profit (binned)" , "Transaction Date (year-month)" ). Otherwise, the title is simply the field name. Notes : 1) You can customize the default field title format by providing the fieldTitle property in the config or fieldTitle function via the compile functions options . 2) If both field definitions title and axis, header, or legend title are defined, axis/header/legend title will be used. |

In addition, field definitions for different encoding channels may support the following properties:
-
`scale` (scale.html) - The function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) for position (#position) and mark property (#mark-prop) channels.
-
`axis` (axis.html) - The guiding visualization to aid interpretation of scales for position channels (#position).
-
`legend` (legend.html) - The guiding visualization to aid interpretation of mark property channels (#mark-prop).
-
`format` (format.html) - The formatting pattern for text value for text channels (#text).
-
`stack` (stack.html) - Type of stacking offset if a position field (#position) with continuous domain should be stacked.
-
`sort` (sort.html) - Sort order for a field for position (#position) and mark property (#mark-prop) channels.
-
`condition` (condition.html) - The conditional encoding rule for mark property (#mark-prop) and text (#text) channels.
To see a list of additional properties for each type of encoding channels, please see the specific sections for position (#position), mark property (#mark-prop), text and tooltip (#text), detail (#detail), order (#order), and facet (#facet) channels.
### Value Definition
```
// Specification of a Single View
{
  ...,
  "encoding": {     // Encoding
    ...: {
      "value": ...
    },
    ...
  },
  ...
}

```

To map a constant visual value to an encoding channel, the channels value definition must describe the `value` property. (See the `value` (value.html) page for more examples.)
### Datum Definition
```
// Specification of a Single View
{
  ...,
  "encoding": {     // Encoding
    ...: {
      "datum": ...
    },
    ...
  },
  ...
}

```

To map a constant data value (`datum`) via a scale to an encoding channel, the channels value definition must describe the `datum` property. (See the `datum` (datum.html) page for more examples.)
| Property | Type | Description |
| --- | --- | --- |
| datum | PrimitiveValue | DateTime | ExprRef | RepeatRef | A constant value in data domain. |

Similar to a field definition, datum definition of different encoding channels may support `band`, `scale`, `axis`, `legend`, `format`, or `condition` properties. However, data transforms (`aggregate`, `bin`, `timeUnit`, `sort` cannot be applied to a datum definition).
## Position Channels
`x` and `y` position channels determine the position of the marks, or width/height of horizontal/vertical `"area"` and `"bar"`. In addition, `x2` and `y2` can specify the span of ranged `area` (area.html#ranged), `bar` (bar.html#ranged), `rect` (rect.html#ranged), and `rule` (rule.html#ranged).
By default, Vega-Lite automatically generates a scale (scale.html) and an axis (axis.html) for each field mapped to a position channel. If unspecified, properties of scales and axes are determined based on a set of rules by the compiler. `scale` and `axis` properties of the field definition can be used to customize their properties.
| Property | Type | Description |
| --- | --- | --- |
| x | PositionDef | X coordinates of the marks, or width of horizontal "bar" and "area" without specified x2 or width . The value of this channel can be a number or a string "width" for the width of the plot. |
| y | PositionDef | Y coordinates of the marks, or height of vertical "bar" and "area" without specified y2 or height . The value of this channel can be a number or a string "height" for the height of the plot. |
| x2 | Position2Def | X2 coordinates for ranged "area" , "bar" , "rect" , and "rule" . The value of this channel can be a number or a string "width" for the width of the plot. |
| y2 | Position2Def | Y2 coordinates for ranged "area" , "bar" , "rect" , and "rule" . The value of this channel can be a number or a string "height" for the height of the plot. |

### Position Field Definition and Datum Definition
In addition to the general field definition properties (#field-def), field definitions for `x` and `y` channels may include the properties listed below. Similarly, datum definitions (#datum-def) for `x` and `y` channels also support these properties.
| Property | Type | Description |
| --- | --- | --- |
| scale | Scale | Null | An object defining properties of the channels scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels. If null , the scale will be disabled and the data value will be directly encoded . Default value: If undefined, default scale properties are applied. See also: scale documentation. |
| axis | Axis | Null | An object defining properties of axiss gridlines, ticks and labels. If null , the axis for the encoding channel will be removed. Default value: If undefined, default axis properties are applied. See also: axis documentation. |
| sort | Sort | Sort order for the encoded field. For continuous fields (quantitative or temporal), sort can be either "ascending" or "descending" . For discrete fields, sort can be one of the following: "ascending" or "descending"  for sorting by the values natural order in JavaScript. A string indicating an encoding channel name to sort by (e.g., "x" or "y" ) with an optional minus prefix for descending sort (e.g., "-x" to sort by x-field, descending). This channel string is short-form of a sort-by-encoding definition . For example, "sort": "-x" is equivalent to "sort": {"encoding": "x", "order": "descending"} . A sort field definition for sorting by another field. An array specifying the field values in preferred order . In this case, the sort order will obey the values in the array, followed by any unspecified values in their original order. For discrete time field, values in the sort array can be date-time definition objects . In addition, for time units "month" and "day" , the values can be the month or day names (case insensitive) or their 3-letter initials (e.g., "Mon" , "Tue" ). null indicating no sort. Default value: "ascending" Note: null and sorting by another channel is not supported for row and column . See also: sort documentation. |
| impute | ImputeParams | Null | An object defining the properties of the Impute Operation to be applied. The field value of the other positional channel is taken as key of the Impute Operation. The field of the color channel if specified is used as groupby of the Impute Operation. See also: impute documentation. |
| stack | String | Null | Boolean | Type of stacking offset if the field should be stacked. stack is only applicable for x , y , theta , and radius channels with continuous domains. For example, stack of y can be used to customize stacking for a vertical bar chart. stack can be one of the following values: "zero" or true : stacking with baseline offset at zero value of the scale (for creating typical stacked bar and area chart). "normalize" - stacking with normalized domain (for creating normalized stacked bar and area charts and pie charts with percentage tooltip ). - "center" - stacking with center baseline (for streamgraph ). null or false - No-stacking. This will produce layered bar and area chart. Default value: zero for plots with all of the following conditions are true: (1) the mark is bar , area , or arc ; (2) the stacked measure channel (x or y) has a linear scale; (3) At least one of non-position channels mapped to an unaggregated field that is different from x and y. Otherwise, null by default. See also: stack documentation. |

Note: `x2` and `y2` do not have their own definitions for `scale`, `axis`, `sort`, and `stack` since they share the same scales and axes with `x` and `y` respectively.
## Position Offset Channels
`xOffset` and `yOffset` position channels determine additional offset to the `x` or `y` position.
### Position Offset Field Definition and Datum Definition
In addition to the general field definition properties (#field-def), field definitions for `xOffset` and `yOffset` channels may include the properties listed below. Similarly, datum definitions (#datum-def) for `x` and `y` channels also support these properties.
| Property | Type | Description |
| --- | --- | --- |
| scale | Scale | Null | An object defining properties of the channels scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels. If null , the scale will be disabled and the data value will be directly encoded . Default value: If undefined, default scale properties are applied. See also: scale documentation. |
| sort | Sort | Sort order for the encoded field. For continuous fields (quantitative or temporal), sort can be either "ascending" or "descending" . For discrete fields, sort can be one of the following: "ascending" or "descending"  for sorting by the values natural order in JavaScript. A string indicating an encoding channel name to sort by (e.g., "x" or "y" ) with an optional minus prefix for descending sort (e.g., "-x" to sort by x-field, descending). This channel string is short-form of a sort-by-encoding definition . For example, "sort": "-x" is equivalent to "sort": {"encoding": "x", "order": "descending"} . A sort field definition for sorting by another field. An array specifying the field values in preferred order . In this case, the sort order will obey the values in the array, followed by any unspecified values in their original order. For discrete time field, values in the sort array can be date-time definition objects . In addition, for time units "month" and "day" , the values can be the month or day names (case insensitive) or their 3-letter initials (e.g., "Mon" , "Tue" ). null indicating no sort. Default value: "ascending" Note: null and sorting by another channel is not supported for row and column . See also: sort documentation. |

### Example: Grouped Bar Chart

Note: Read here (size.html#offset-step) for more details about how to set step size for offset scale.
### Example: Jittering

## Polar Position Channels
`theta` and `radius` position channels determine the position or interval on polar coordinates for `arc` and `text` marks.
| Property | Type | Description |
| --- | --- | --- |
| theta | PolarDef | For arc marks, the arc length in radians if theta2 is not specified, otherwise the start arc angle. (A value of 0 indicates up or north, increasing values proceed clockwise.) For text marks, polar coordinate angle in radians. |
| radius | PolarDef | The outer radius in pixels of arc marks. |
| theta2 | Position2Def | The end angle of arc marks in radians. A value of 0 indicates up or north, increasing values proceed clockwise. |
| radius2 | Position2Def | The inner radius in pixels of arc marks. |

### Polar Field Definition and Datum Definition
Polar field and datum definitions may include `scale`, `stack`, and `sort` properties, similar to position field and datum definitions (#position-field-def).
## Geographic Position Channels
`longitude` and `latitude` channels can be used to encode geographic coordinate data via a projection (projection.html). In addition, `longitude2` and `latitude2` can specify the span of geographically projected ranged `area` (area.html#ranged), `bar` (bar.html#ranged), `rect` (rect.html#ranged), and `rule` (rule.html#ranged).
| Property | Type | Description |
| --- | --- | --- |
| longitude | LatLongDef | Longitude position of geographically projected marks. |
| latitude | LatLongDef | Latitude position of geographically projected marks. |
| longitude2 | Position2Def | Longitude-2 position for geographically projected ranged "area" , "bar" , "rect" , and "rule" . |
| latitude2 | Position2Def | Latitude-2 position for geographically projected ranged "area" , "bar" , "rect" , and "rule" . |

See an example that uses `longitude` and `latitude` channels in a map (/vega-lite/examples/geo_circle.html) or another example that draws line segments (`rule`s) between points in a map (/vega-lite/examples/geo_rule.html).
## Mark Property Channels
Mark properties channels map data fields to visual properties of the marks. By default, Vega-Lite automatically generates a scale and a legend for each field mapped to a mark property channel. If unspecified, properties of scales and legends are determined based on a set of rules by the compiler. `scale` and `legend` properties of the field definition can be used to customize their properties. In addition, definitions of mark property channels can include the `condition` property to specify conditional logic.
Here are the list of mark property channels:
| Property | Type | Description |
| --- | --- | --- |
| angle | MarkPropDef | Rotation angle of point and text marks. |
| color | MarkPropDef | Color of the marks  either fill or stroke color based on the filled property of mark definition. By default, color represents fill color for "area" , "bar" , "tick" , "text" , "trail" , "circle" , and "square" / stroke color for "line" and "point" . Default value: If undefined, the default color depends on mark config s color property. Note: 1) For fine-grained control over both fill and stroke colors of the marks, please use the fill and stroke channels. The fill or stroke encodings have higher precedence than color , thus may override the color encoding if conflicting encodings are specified. 2) See the scale documentation for more information about customizing color scheme . |
| fill | MarkPropDef | Fill color of the marks. Default value: If undefined, the default color depends on mark config s color property. Note: The fill encoding has higher precedence than color , thus may override the color encoding if conflicting encodings are specified. |
| stroke | MarkPropDef | Stroke color of the marks. Default value: If undefined, the default color depends on mark config s color property. Note: The stroke encoding has higher precedence than color , thus may override the color encoding if conflicting encodings are specified. |
| opacity | MarkPropDef | Opacity of the marks. Default value: If undefined, the default opacity depends on mark config s opacity property. |
| fillOpacity | MarkPropDef | Fill opacity of the marks. Default value: If undefined, the default opacity depends on mark config s fillOpacity property. |
| strokeOpacity | MarkPropDef | Stroke opacity of the marks. Default value: If undefined, the default opacity depends on mark config s strokeOpacity property. |
| shape | MarkPropDef | Shape of the mark. For point marks the supported values include: - plotting shapes: "circle" , "square" , "cross" , "diamond" , "triangle-up" , "triangle-down" , "triangle-right" , or "triangle-left" . - the line symbol "stroke" - centered directional shapes "arrow" , "wedge" , or "triangle" - a custom SVG path string (For correct sizing, custom shape paths should be defined within a square bounding box with coordinates ranging from -1 to 1 along both the x and y dimensions.) For geoshape marks it should be a field definition of the geojson data Default value: If undefined, the default shape depends on mark config s shape property. ( "circle" if unset.) |
| size | MarkPropDef | Size of the mark. For "point" , "square" and "circle" ,  the symbol size, or pixel area of the mark. For "bar" and "tick"  the bar and ticks size. For "text"  the texts font size. Size is unsupported for "line" , "area" , and "rect" . (Use "trail" instead of line with varying size) |
| strokeDash | NumericArrayMarkPropDef | Stroke dash of the marks. Default value: [1,0] (No dash). |
| strokeWidth | MarkPropDef | Stroke width of the marks. Default value: If undefined, the default stroke width depends on mark config s strokeWidth property. |

### Mark Property Field Definition and Datum Definition
Field definitions (#field-def) for mark property channels may also include the properties list below (in addition to `field` (field.html), `type` (type.html), `bin` (bin.html), `timeUnit` (timeunit.html) and `aggregate` (aggregate.html)).
Similarly, datum definitions (#datum-def) for mark property channels also support these properties.
| Property | Type | Description |
| --- | --- | --- |
| scale | Scale | Null | An object defining properties of the channels scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels. If null , the scale will be disabled and the data value will be directly encoded . Default value: If undefined, default scale properties are applied. See also: scale documentation. |
| legend | Legend | Null | An object defining properties of the legend. If null , the legend for the encoding channel will be removed. Default value: If undefined, default legend properties are applied. See also: legend documentation. |
| condition | ConditionalValueDef | ConditionalValueDef [] | One or more value definition(s) with a parameter or a test predicate . Note: A field definitions condition property can only contain conditional value definitions since Vega-Lite only allows at most one encoded field per encoding channel. |

### Mark Property Value Definition
In addition to the constant `value`, value definitions (#value-def) of mark properties channels can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| condition | ConditionalFieldDef | ConditionalValueDef | ConditionalValueDef [] | A field definition or one or more value definition(s) with a parameter predicate. |

See the `condition` (condition.html) page for examples how to specify condition logic.
## Text and Tooltip Channels
Text and tooltip channels directly encode text values of the data fields. By default, Vega-Lite automatically determines appropriate format for quantitative and temporal values. Users can set `format` property to customize text and time format. Similar to mark property channels, definitions of text and tooltip channels can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| text | TextFieldDef | Text of the text mark. |
| tooltip | StringFieldDefWithCondition | StringValueDefWithCondition | StringFieldDef[] | Null | The tooltip text to show upon mouse hover. Specifying tooltip encoding overrides the tooltip property in the mark definition . See the tooltip documentation for a detailed discussion about tooltip in Vega-Lite. |

### Text and Tooltip Field Definition
In addition to the general field definition properties (#field-def), field definitions for `text` and `tooltip` channels may also include these properties:
| Property | Type | Description |
| --- | --- | --- |
| format | Format | The text format specifier for formatting number and date/time in labels of guides (axes, legends, headers) and text marks. If the format type is "number" (e.g., for quantitative fields), this is a D3s number format pattern string . If the format type is "time" (e.g., for temporal fields), this is either: a) D3s time format pattern if you desire to set a static time format. b) dynamic time format specifier object if you desire to set a dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the date lies on a year, month, date, hour, etc. boundary). When used with a custom formatType , this value will be passed as format alongside datum.value to the registered function. Default value: Derived from numberFormat config for number format and from timeFormat config for time format. |
| formatType | String | The format type for labels. One of "number" , "time" , or a registered custom format type . Default value: "time" for temporal fields and ordinal and nominal fields with timeUnit . "number" for quantitative fields as well as ordinal and nominal fields without timeUnit . |
| condition | ConditionalValueDef | ConditionalValueDef [] | One or more value definition(s) with a parameter or a test predicate . Note: A field definitions condition property can only contain conditional value definitions since Vega-Lite only allows at most one encoded field per encoding channel. |

### Text and Tooltip Value Definition
In addition to the constant `value`, value definitions (#value-def) of `text` and `tooltip` channels can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| condition | ConditionalStringFieldDef | ConditionalValueDef | ConditionalValueDef [] | A field definition or one or more value definition(s) with a parameter predicate. |

### Multiple Field Definitions for Tooltips
Similar to `detail` (#detail), you can use an array of field definitions. Vega-Lite will display a tooltip with multiple fields. Vega tooltip (https://github.com/vega/vega-tooltip/) will display a table that shows the name of the field and its value. See the tooltip (tooltip.html) page for details.
## Hyperlink Channel
By setting the `href` channel, a mark becomes a hyperlink. The specified URL is loaded upon a mouse click. When the `href` channel is specified, the `cursor` mark property (mark.html#hyperlink) is set to `"pointer"` by default to serve as affordance for hyperlinks.
| Property | Type | Description |
| --- | --- | --- |
| href | StringFieldDefWithCondition | StringValueDefWithCondition | A URL to load upon mouse click. |

### Hyperlink Field Definition
In addition to the general field definition properties (#field-def), field definitions for the `href` channel can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| condition | Any |  |

The example below shows how the href channel can be used to provide links to external resources with more details.

### Hyperlink Value Definition
In addition to the constant `value`, value definitions (#value-def) of the `href` channel can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| condition | ConditionalStringFieldDef | ConditionalValueDef | ConditionalValueDef [] | A field definition or one or more value definition(s) with a parameter predicate. |

## Description Channel
By setting the `description` channel, you can add a text description to the mark for ARIA accessibility (SVG output only). The `"aria-label"` attribute in the generated SVG will be set to this description.
By default, Vega-Lite generates a description based on the encoding similar to default tooltips (/vega-lite/docs/tooltip.html#encoding). To disable automatic descriptions, set `config.aria` (config.html#aria-config) to false. No description will be generated if `mark.aria` (/vega-lite/docs/mark.html#general) is set to false.
| Property | Type | Description |
| --- | --- | --- |
| description | StringFieldDefWithCondition | StringValueDefWithCondition | A text description of this mark for ARIA accessibility (SVG output only). For SVG output the "aria-label" attribute will be set to this description. |

### Description Field Definition
In addition to the general field definition properties (#field-def), field definitions for the `description` channel can include these properties:
| Property | Type | Description |
| --- | --- | --- |
| format | Format | The text format specifier for formatting number and date/time in labels of guides (axes, legends, headers) and text marks. If the format type is "number" (e.g., for quantitative fields), this is a D3s number format pattern string . If the format type is "time" (e.g., for temporal fields), this is either: a) D3s time format pattern if you desire to set a static time format. b) dynamic time format specifier object if you desire to set a dynamic time format that uses different formats depending on the granularity of the input date (e.g., if the date lies on a year, month, date, hour, etc. boundary). When used with a custom formatType , this value will be passed as format alongside datum.value to the registered function. Default value: Derived from numberFormat config for number format and from timeFormat config for time format. |
| formatType | String | The format type for labels. One of "number" , "time" , or a registered custom format type . Default value: "time" for temporal fields and ordinal and nominal fields with timeUnit . "number" for quantitative fields as well as ordinal and nominal fields without timeUnit . |
| condition | ConditionalValueDef | ConditionalValueDef [] | One or more value definition(s) with a parameter or a test predicate . Note: A field definitions condition property can only contain conditional value definitions since Vega-Lite only allows at most one encoded field per encoding channel. |

### Description Value Definition
In addition to the constant `value`, value definitions (#value-def) of the `description` channel can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| condition | ConditionalStringFieldDef | ConditionalValueDef | ConditionalValueDef [] | A field definition or one or more value definition(s) with a parameter predicate. |

## Level of Detail Channel
Grouping data is another important operation in data visualization. For line and area marks, mapping a unaggregated data field (field without `aggregate` function) to any non-position (#position) channel will group the lines and stacked areas by the field. For aggregated plots (aggregate.html), all unaggregated fields encoded are used as grouping fields in the aggregation (similar to fields in `GROUP BY` in SQL).
`detail` channel specify an additional grouping field (or fields) for grouping data without mapping the field(s) to any visual properties.
| Property | Type | Description |
| --- | --- | --- |
| detail | FieldDef | FieldDef [] | Additional levels of detail for grouping data in aggregate views and in line, trail, and area marks without mapping data to a specific visual channel. |

#### Examples
Here is a scatterplot showing average horsepower and displacement for cars from different origins. We map `Origin` to `detail` channel to use the field as a group-by field without mapping it to visual properties of the marks.
Here is a line chart showing stock prices of 5 tech companies over time. We map `symbol` variable (stock market ticker symbol) to `detail` to use them to group lines.
Here is a ranged dot plot showing life expectancy change in the five largest countries between 1955 and 2000. We use `detail` here to group the lines such that they range only from one year to another within a country (as opposed to jumping between countries as well).
## Key Channel
The key channel can enable object constancy for transitions over dynamic data. When a visualizations data is updated (via Vegas View API (https://vega.github.io/vega/docs/api/view/#data)), the key value will be used to match data elements to existing mark instances.
| Property | Type | Description |
| --- | --- | --- |
| key | FieldDef | A data field to use as a unique key for data binding. When a visualizations data is updated, the key value will be used to match data elements to existing mark instances. Use a key channel to enable object constancy for transitions over dynamic data. |

## Order Channel
`order` channel can define a data field (or a ordered list of data fields) that are used to sorts stacking order for stacked charts (see an example in the `stack` page (stack.html#order)), the order of data points in line marks for connected scatterplots (see an example in the `line` page (line.html#connected-scatter-plot)), and which data points are plotted on top in a chart (the zorder, see an example in the gallery (/vega-lite/examples/selection_type_point_zorder.html)).
| Property | Type | Description |
| --- | --- | --- |
| order | OrderFieldDef | OrderFieldDef [] | OrderValueDef | OrderOnlyDef | Order of the marks. For stacked marks, this order channel encodes stack order . For line and trail marks, this order channel encodes order of data points in the lines. This can be useful for creating a connected scatterplot . Setting order to {"value": null} makes the line marks use the original order in the data sources. Otherwise, this order channel encodes layer order of the marks. Note : In aggregate plots, order field should be aggregate d to avoid creating additional aggregation grouping. |

### Order Field Definition
In addition to the general field definition properties (#field-def), field definitions for the `order` channel can include `sort`.
| Property | Type | Description |
| --- | --- | --- |
| sort | String | The sort order. One of "ascending" (default) or "descending" . |

### Order Value Definition
In addition to the constant `value`, value definitions (#value-def) of the `order` channel can include the `condition` property to specify conditional logic.
| Property | Type | Description |
| --- | --- | --- |
| condition | ConditionalValueDef | ConditionalValueDef [] | One or more value definition(s) with a parameter or a test predicate . Note: A field definitions condition property can only contain conditional value definitions since Vega-Lite only allows at most one encoded field per encoding channel. |

## Facet Channels
`facet`, `row` and `column` are special encoding channels that facets single plots into trellis plots (or small multiples) (https://en.wikipedia.org/wiki/Small_multiple).
| Property | Type | Description |
| --- | --- | --- |
| facet | FacetFieldDef | A field definition for the (flexible) facet of trellis plots. If either row or column is specified, this channel will be ignored. |
| row | FacetFieldDef | A field definition for the vertical facet of trellis plots. |
| column | FacetFieldDef | A field definition for the horizontal facet of trellis plots. |

For more information, read the facet documentation (facet.html).

## Field
Source: https://vega.github.io/vega-lite/docs/field.html

```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {     // Encoding
    ...: {
      "field": ..., // Field
      "type": "quantitative",
      ...
    },
    ...
  },
  ...
}

```

A field definition (encoding.html#field-def) of an encoding channel (encoding.html#channels) must include a `field` in order to map an encoding channel to a data field. The sort field definition (sort.html#sort-field) can also have the `field` property to sort the encoded field by another field as well.
The `field` property can be one of:
1) A string representing the data field.
For example, we can set `field` to `"precipitation"` to map it to `x` position.

Valid JavaScript object access paths using either dot (e.g., `foo.bar`) or bracket with quotes (e.g., `foo['bar']`) notations can be used in `field` to perform nested object lookups. If field names contain dots or brackets but are not nested, use `\\` to escape dots and brackets. For example, if the field name is `a.b`, use `a\\.b`. Similarly, if the field name is `a[0]`, use `a\\[0\\]`.
Further note that in JSON, you have to escape backslashes. Hence, a single backslash (`\`) is escaped as `\\\\` in JSON. You also need to escape quotes (`\"`) and use special escape characters for newlines (`\n`), carriage returns (`\r`), and tabs (`\t`).
2) An object defining iterated values from the `repeat` operator
For example, we can set `field` of `x` channel to `{"repeat": "column"}` to create a histogram of different fields.

See the `repeat` (repeat.html) page for more information about the `repeat` operator and more examples.

## Type
Source: https://vega.github.io/vega-lite/docs/type.html

If a field is specified, the channel definition must describe the encoded datas type based on their level of measurement (https://en.wikipedia.org/wiki/Level_of_measurement). The supported data types are: `"quantitative"` (#quantitative), `"temporal"` (#temporal), `"ordinal"` (#ordinal), `"nominal"` (#nominal), and `"geojson"` (#geojson).
| Property | Type | Description |
| --- | --- | --- |
| type | String | The type of measurement ( "quantitative" , "temporal" , "ordinal" , or "nominal" ) for the encoded field or constant value ( datum ). It can also be a "geojson" type for encoding geoshape . Vega-Lite automatically infers data types in many cases as discussed below. However, type is required for a field if: (1) the field is not nominal and the field encoding has no specified aggregate (except argmin and argmax ), bin , scale type, custom sort order, nor timeUnit or (2) if you wish to use an ordinal scale for a field with bin or timeUnit . Default value: 1) For a data field , "nominal" is the default data type unless the field encoding has aggregate , channel , bin , scale type, sort , or timeUnit that satisfies the following criteria: "quantitative" is the default type if (1) the encoded field contains bin or aggregate except "argmin" and "argmax" , (2) the encoding channel is latitude or longitude channel or (3) if the specified scale type is a quantitative scale . "temporal" is the default type if (1) the encoded field contains timeUnit or (2) the specified scale type is a time or utc scale "ordinal" is the default type if (1) the encoded field contains a custom sort order , (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding channel is order . 2) For a constant value in data domain ( datum ): "quantitative" if the datum is a number "nominal" if the datum is a string "temporal" if the datum is a date time object Note: Data type describes the semantics of the data rather than the primitive data types (number, string, etc.). The same primitive data type can have different types of measurement. For example, numeric data can represent quantitative, ordinal, or nominal data. Data values for a temporal field can be either a date-time string (e.g., "2015-03-07 12:32:17" , "17:01" , "2015-03-16" . "2015" ) or a timestamp number (e.g., 1552199579097 ). When using with bin , the type property can be either "quantitative" (for using a linear bin scale) or "ordinal" (for using an ordinal bin scale) . When using with timeUnit , the type property can be either "temporal" (default, for using a temporal scale) or "ordinal" (for using an ordinal scale) . When using with aggregate , the type property refers to the post-aggregation data type. For example, we can calculate count distinct of a categorical field "cat" using {"aggregate": "distinct", "field": "cat"} . The "type" of the aggregate output is "quantitative" . Secondary channels (e.g., x2 , y2 , xError , yError ) do not have type as they must have exactly the same type as their primary channels (e.g., x , y ). See also: type documentation. |

## Quantitative
Quantitative data expresses some kind of quantity. Typically this is numerical data. For example `7.3`, `42.0`, `12.1`.
Quantitative data can represent either the ratio or interval level of measurement (https://en.wikipedia.org/wiki/Level_of_measurement). By default, Vega-Lite includes zero values in the x, y, and size scales for quantitative fields, which is more appropriate for ratio data. However, you can manually set the scales `zero` property (scale.html#continuous) to `false` if you have interval data.
## Temporal
Temporal data supports date-times and times such as `"2015-03-07 12:32:17"`, `"17:01"`, `"2015-03-16"`, `"2015"`, `1552199579097` (timestamp).
Note that when a `"temporal"` type is used for a field, Vega-Lite will treat it as a continuous field and thus will use a `time` scale (scale.html#time) to map its data to visual values. For example, the following bar chart shows the mean precipitation for different months.

## Ordinal
Ordinal data represents ranked order (1st, 2nd, ...) by which the data can be sorted. However, as opposed to quantitative data, there is no notion of relative degree of difference between them. For illustration, a size variable might have the following values `small`, `medium`, `large`, `extra-large`. We know that medium is larger than small and same for extra-large larger than large. However, we cannot compare the magnitude of relative difference, for example, between (1) `small` and `medium` and (2) `medium` and `large`. Similarly, we cannot say that `large` is two times as large as `small`.
To use an ordinal field with a sort order other than the natural order, you may want to use the `sort` (sort.html#sort-array) property to specify a customized order:
Note: If an encoding includes a custom sort order, Vega-Lite uses the ordinal type by default, so you actually can omit `"type": "ordinal"` from the specification above.
### Casting a Temporal Field as an Ordinal Field
To treat a date-time field with `timeUnit` as a discrete field, you can cast it to be an `"ordinal"` field. This type casting can be useful for time units with low cardinality such as `"month"`.

### Casting a Binned Field as an Ordinal Field
Setting a binned fields `type` to `"ordinal"` produces a histogram with an ordinal scale.
## Nominal
Nominal data, also known as categorical data, differentiates between values based only on their names or categories. For example, gender, nationality, music genre, and name are nominal data. Numbers may be used to represent the variables but the number do not determine magnitude or ordering. For example, if a nominal variable contains three values 1, 2, and 3. We cannot claim that 1 is less than 2 nor 3.
## GeoJSON
GeoJSON data represents geographic shapes specified as GeoJSON (http://geojson.org/).

## Property Types
Source: https://vega.github.io/vega-lite/docs/types.html

Reference documentation for common property types expected by Vega-Lite specification properties.
## Documentation Overview
- Primitive Types (#primitive-types)
- Any (#any)
- Array (#array)
- Boolean (#boolean)
- Color (#color)
- Expression Reference (ExprRef) (#exprref)
- Expression (#expression)
- Number (#number)
- Object (#object)
- String (#string)
- Text (#text)
- URL (#url)
- Special Object Types (#special-object-types)
## Primitive Types
### Any
Accepts any literal value, including a string, number, boolean, or `null`.
### Array
Accepts array values. For example: `[]`, `[1, 2, 3]`, `["foo", "bar"]`. If individual array items must adhere to a specific type, bracket notation  such as `Number[]` or `String[]`  is used to indicate the item type.
In most cases, arrays may also have signal references (#Signal) as items. For example: `[{"signal": "width"}, {"signal": "height"}]`.
### Boolean
Accepts boolean values. For example: `true`, `false`.
### Color
Accepts a valid CSS color string (https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). For example: `#f304d3`, `#ccc`, `rgb(253, 12, 134)`, `steelblue`.
### Expression Reference (ExprRef)
An object with an `expr` property defining a Vega Expression (#expression).
For example, we can set mark `color` to be `{expr: "lab(50,10,30)"}`.
### Expression
To enable custom calculations, Vega-Lite uses Vegas expression language for writing basic formulas. Each datum object can be referred using bound variable `datum`.
Please read the Vega documentation for expressions (https://vega.github.io/vega/docs/expressions/) for details.
### Number
Accepts number values. For example: `1`, `3.14`, `1e5`.
### Object
Accepts general object literals. For example: `{"left":5, "right":30, "top":5, "bottom":50}`. The valid object property names and types will vary across properties; read the individual property descriptions for more information.
### String
Accepts general string values. For example: `"bold"`, `"step-before"`, `""`. The valid object property names and types may vary across properties; read the individual property descriptions for more information.
### Text
Accepts string values or arrays of strings (for multi-line text).
### URL
Accepts a valid URL string linking to external site or resource. For example: `"data/stocks.csv"`, `"images/logo.png"`, `"https://vega.github.io/"`.
## Special Object Types
Please see the following pages for other special object types:
- Date Time (datetime.html)
- Gradient (gradient.html)
- Predicate (predicate.html)

## Value
Source: https://vega.github.io/vega-lite/docs/datum.html

```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {     // Encoding
    ...: {
      "datum": ..., // Value
    },
    ...
  },
  ...
}

```

You can use a datum definition (encoding.html#datum-def) to map a constant data value to an encoding channel (encoding.html#channels) via an underlying scale by setting the `datum` property.
## Examples
### Highlight a Specific Data Value
`datum` is particularly useful for annotating a certain data value.
For example, you can use it with a rule mark to highlight a certain threshold value (e.g., 200 dollars stock price).

You can also use datum with a date time (datetime.html) definition, for example, to highlight a certain year:

### Using Datum to Color Multi-series Chart
Another application of `datum` is to color a multi-series line chart created with `repeat`.

## Value
Source: https://vega.github.io/vega-lite/docs/value.html

```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {     // Encoding
    ...: {
      "value": ..., // Value
    },
    ...
  },
  ...
}

```

You can use a value definition (encoding.html#value-def) to map a constant value to an encoding channel (encoding.html#channels) by setting the `value` property.
For example, you can set `color` and `shape` of a scatter plot to constant values.

Similarly, `value` for `size` channel of bar marks will adjust the bars size. By default, there will be 1 pixel offset between bars. The following example sets the size to 10 to add more offset between bars.

Note: Mapping an encoding channel to a constant `value` is equivalent to setting a property of the `"mark"` (mark.html#mark-def) definition block. For example, you can also set color and shape of marks by setting `"mark"` to `{"color": "#ff9900", "shape": "square"}`. However, unlike mark definition properties, `value` definition of an encoding channel can also be combined with `condition` to specify conditional encoding. See the `condition` (condition.html) page for more details.

## Condition
Source: https://vega.github.io/vega-lite/docs/condition.html

```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    ...: {
      // Conditional encoding channel definition (if-clause)
      "condition": {
        // Parameter name or a test predicate
        "param/test": ...,
        // Field / value definition if the data is included in the `param` or if the `test` predicate is satisfied
        "field/value": ...,
        ...
      },

      // (Optional else-clause) Field / value definition if the data is NOT included in the `param` / if the `test` predicate is NOT satisfied
      "field/value": ...,
      ...
    },
    ...
  },
  ...
}

```

For mark property channels (encoding.html#mark-prop) as well as text and tooltip channels (encoding.html#text), the `condition` property of their channel definitions can be used to determine encoding rules based on whether data values satisfy a parameter (parameter.html) (e.g. fall withing a selection parameter (parameter.html#select)) or satisfy a `test` predicate.
There are two ways to specify the condition:
(1) Specifying `param` name:
| Property | Type | Description |
| --- | --- | --- |
| param | String | Required. Filter using a parameter name. |
| empty | Boolean | For selection parameters, the predicate of empty selections returns true by default. Override this behavior, by setting this property empty: false . |

(2) Specifying a `test` predicate:
| Property | Type | Description |
| --- | --- | --- |
| test | Predicate | Required. Predicate for triggering the condition |

In addition, there are two ways to encode the data that satisfy the specified condition:
-
Combining one conditional field definition (#field) with a single base value or datum definition.
-
Combining one or more conditional datum or value definitions (#value) with a field, datum, or value definition.
## Conditional Field Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    ...: {
      // A conditional field definition (if-clause)
      "condition": {
        // Parameter name or a test predicate
        "param/test": ...,

        // Field if the data is included in the `param` or if the `test` predicate is satisfied
        "field": ...,
        "type": ...,
        ...
      },

      // (Optional else-clause) value if the data is NOT included in the `param` / if the `test` predicate is NOT satisfied
      "value/datum": ...
    },
    ...
  },
  ...
}

```

A conditional field definition uses a data-driven encoding rule when marks satisfy a parameter (parameter.html) (e.g. fall within a selection parameter (parameter.html#select)) or satisfy a logical predicate. A value definition can be specified as the else case when the condition is not satisfied otherwise.
A condition field definition must contain either a `param` name or a `test` predicate (#condition) in addition to the encoded `field` name and its data `type` like a typical field definition (encoding.html#field-def). In addition, a condition field definition may contain other encoding properties including transformation functions (`aggregate` (aggregate.html), `bin` (bin.html), `timeUnit` (timeunit.html)) as well as `scale` (scale.html) and `legend` (legend.html) (for mark property channels ({encoding.html#mark-prop})) or `format` (format.html) (for text and tooltip channels (encoding.html#text)).
For example, in the following plot, the color of `rect` marks is driven by a conditional field definition. Drag an interval selection and observe that marks are colored based on their aggregated count if they lie within the interval, and are grey otherwise.
Note: When using a conditional field definition, only `value` or `datum` may be specified as the else (outer) branch.
## Conditional Value Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    ...: {
      // A conditional value definition (if-clause)
      "condition": { // Parameter name or a test predicate
        "param/test": ..., // Value if the data is included in the `param` or if the `test` predicate is satisfied
        "value/datum": ...
      },

      // (Optional else-clause) field if the data is NOT included in the `param` / if the `test` predicate is NOT satisfied
      "field": ... ,
      "type": ...,
      ...
    },
    ...
  },
  ...
}

```

Condition value definitions and conditional datum definitions use a constant value encoding when data satisfy a parameter (parameter.html) (e.g. fall withing a selection parameter (parameter.html#select)) or satisfy a logical predicate. Another field, datum, or value definition can be specified as the else case when the condition is not satisfied.
A condition value/datum definition must contain either a `param` name or a `test` predicate (#condition) in addition to the encoded constant `value` (encoding.html#value-def) or constant data value (`datum` (encoding.html#datum-def)).
For example, in the visualization below, a conditional value definition causes marks that fall within a dragged interval to be larger than those that lie outside it.
A field mapping can also be specified as the else (outer) branch. For example, below, we invert our original example: a conditional value definition sets the `rect` marks to grey when they do not lie within the selection, and a regular field mapping is used otherwise. Notice, no marks are initially colored grey. This is because empty selections are treated as containing all data values.
Besides specifying `param` name, we can also specify a `test` condition.
This plot uses a conditional value definition value to use a black label for a light background.
The next plot uses a conditional value definition to color data points with null values in grey. Note that if the else case value is not specified, default mark color will be applied.

## Sorting
Source: https://vega.github.io/vega-lite/docs/sort.html

```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "field": ...,
      "type": ...,
      "sort": ...,         // sort
      ...
    },
    "y": ...,
    ...
  },
  ...
}

```

The `sort` property of a mark properties channel (encoding.html#mark-props) determines the order of the scale domain. Supported `sort` values depend on the fields scale type.
## Documentation Overview
- Sorting Continuous Fields (#sorting-continuous-fields)
- Example: Reversed X-Scale (#example-reversed-x-scale)
- Sorting Discrete Fields (#sorting-discrete-fields)
- Sort by the Fields Natural Order (#sort-by-the-fields-natural-order)
- Sort by Another Encoding Channel (#sort-by-encoding)
- Sort by a Different Field (#sort-by-a-different-field)
- Specifying Custom Sort Order (#specifying-custom-sort-order)
- No Sorting (#no-sorting)
## Sorting Continuous Fields
If the channel has a continuous field (quantitative or time), `sort` can have the following values:
- `"ascending"` (Default)  the field is sorted by the fields value in ascending order.
- `"descending"`  the field is sorted by the fields value in descending order.
#### Example: Reversed X-Scale
Setting xs `sort` to `"descending"` reverses the x-axis. Thus, the following visualizations x-axis starts on the maximum value of the field Horsepower and ends on zero.
## Sorting Discrete Fields
If the channel has a discrete scale (ordinal or nominal), `sort` can be one of: `"ascending"`, `"descending"`, a sort-by-encoding definition (#sort-by-encoding) for sorting by another encoding a sort field definition (#sort-field) for sorting by another field, an array specifying preferred order (#sort), or `null`.
### Sort by the Fields Natural Order
To order the data by the values natural order in JavaScript (e.g.,`"a"` < `"b"`), the `sort` property can be:
- `"ascending"` (Default)  sort by the fields value in ascending order.
- `"descending"`  sort by the fields value in descending order.
### Sort by Another Encoding Channel
To sort data by another encoding channel, the `sort` property can be an encoding channel name to sort by (e.g., `"x"` or `"y"`) with an optional minus prefix for descending sort (e.g., `"-x"` to sort by x-field, descending).
For example, the following plot sorts the y-values by the x-values (in descending order).
This is equivalent to using an object with the `encoding` and optional `"order"` property:
| Property | Type | Description |
| --- | --- | --- |
| encoding | String | Required. The encoding channel to sort by (e.g., "x" , "y" ) |
| order | String | Null | The sort order. One of "ascending" (default), "descending" , or null (do not sort). |

For example, `"sort": "-x"` is equivalent to `"sort": {"encoding": "x", "order": "descending"}`.
### Sort by a Different Field
To order data by another field, `sort` can be an encoding sort field definition, which has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| field | Field | The data field to sort by. Default value: If unspecified, defaults to the field specified in the outer data reference. |
| op | String | An aggregate operation to perform on the field prior to sorting (e.g., "count" , "mean" and "median" ). An aggregation is required when there are multiple values of the sort field for each encoded data field. The input data objects will be aggregated, grouped by the encoded data field. For a full list of operations, please see the documentation for aggregate . Default value: "sum" for stacked plots. Otherwise, "min" . |
| order | String | Null | The sort order. One of "ascending" (default), "descending" , or null (do not sort). |

For example, the following plot sorts `"age"` values on the y-axis by `"sum"` of `"people"`. Note that this is equivalent to the example above.
### Specifying Custom Sort Order
If the `sort` property is an array, it specifies the preferred order of values.
In the case that sort array contains every field value, the sort order will follow the specified values in the array.
If some values are ignored, the sort order will precede by the specified values in the array while unspecified values will follow their original order. For example, this plots orders `B`, `A` and `C` first, followed by `Z`, `Y`, `X`.
For discrete time fields, values in the sort array can be date-time definition objects (types#datetime). In addition, for time units `"month"` and `"day"`, the values can be the month or day names (case insensitive) or their 3-letter initials (e.g., `"Mon"`, `"Tue"`).
For example, the following chart orders the day to start on Monday (instead of Sunday by default).
Note: It is also possible to sort by providing custom `scale`s `domain` (scale.html#domain). However, it is more error-prone compared to using a `sort` array since `domain` requires every possible value to be included in the array. Thus, any value omitted from `domain` will not render properly.
### No Sorting
If `sort` is `null`, the field is not sorted. This is equivalent to specifying `sort: false` in Vegas scales (https://vega.github.io/vega/docs/scales/#sort).
Note: `null` is not supported for `row` and `column`.

## Stack
Source: https://vega.github.io/vega-lite/docs/stack.html

To stack fields in Vega-Lite, users can either use the `stack` property of an encoding field definition (#encoding) or a `stack` transform inside the `transform` (#transform) array.
## Documentation Overview
- Stack in Encoding Field Definition (#encoding)
- Stack Bar Chart (#bar)
- Stack Area Chart (#area)
- Normalized Stacked Bar and Area Charts (#normalized)
- Streamgraph (#streamgraph)
- Layered Bar Chart (#layered-bar-chart)
- Diverging Stacked Bar Chart (Stacked with negative values) (#order)
- Sorting Stack Order (#sorting-stack-order)
- Layering Lines on top of Stacked Area Chart (#layering-lines-on-top-of-stacked-area-chart)
- Stack Transform (#transform)
- Diverging Bar Chart (#diverging-bar-chart)
- Mosaic Chart (#mosaic-chart)
## Stack in Encoding Field Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {     // Encoding
    "x" or "y": {
      "field": ...,
      "type": "quantitative",
      "stack": ..., // Stack
      ...
    },
    ...
  },
  ...
}

```

The `stack` property of a position field definition (encoding.html#position-field-def) determines type of stacking offset if the field should be stacked.
| Property | Type | Description |
| --- | --- | --- |
| stack | String | Null | Boolean | Type of stacking offset if the field should be stacked. stack is only applicable for x , y , theta , and radius channels with continuous domains. For example, stack of y can be used to customize stacking for a vertical bar chart. stack can be one of the following values: "zero" or true : stacking with baseline offset at zero value of the scale (for creating typical stacked bar and area chart). "normalize" - stacking with normalized domain (for creating normalized stacked bar and area charts and pie charts with percentage tooltip ). - "center" - stacking with center baseline (for streamgraph ). null or false - No-stacking. This will produce layered bar and area chart. Default value: zero for plots with all of the following conditions are true: (1) the mark is bar , area , or arc ; (2) the stacked measure channel (x or y) has a linear scale; (3) At least one of non-position channels mapped to an unaggregated field that is different from x and y. Otherwise, null by default. See also: stack documentation. |

### Stack Bar Chart
Adding a color field to a bar chart also creates stacked bar chart by default.

### Stack Area Chart
Similarly, adding a color field to area chart also creates stacked area chart by default.

### Normalized Stacked Bar and Area Charts
You can set `stack` to `"normalize"` to create normalized (or percentage) stacked bar and area charts.
### Streamgraph
Setting `stack` to `"center"` for a stacked area chart creates a streamgraph:
### Layered Bar Chart
If `stack` is `null`, the marks will be layered on top of each other. In this example, setting the marks `opacity` to be semi-transparent (`0.6`) creates a layered bar chart.
### Diverging Stacked Bar Chart (Stacked with negative values)
The stack transform can also handle negative values by creating a diverging stacked bar chart.
Note: that the stack transform cannot handle if there should be items stacked in the middle like in the Diverging Stacked Bar Chart with Neutral Parts (https://vega.github.io/vega-lite/examples/bar_diverging_stack_transform.html) example.
### Sorting Stack Order
You can use the order channel to sort the order of stacked marks.
For example, given a stacked bar chart for the barley dataset:
By default, the stacked bar are sorted by the stack grouping fields (`color` in this example).
Mapping the sum of yield to `order` channel will sort the layer of stacked bar by the sum of yield instead.
Here we can see that site with higher yields for each type of barley are put on the top of the stack (rightmost).
If you want to define custom sort order, you can derive a new field using the `calculate` transform (calculate.html) and sort by that field instead. For example, the following plot makes University Farm and Grand Rapids be the first (`0`) and second values in the stack order:
Note: we plan to have a better syntax for customized sort order (https://github.com/vega/vega-lite/issues/2915) in the future.
### Layering Lines on top of Stacked Area Chart
Since `line` marks are not stacked by default, to layer lines on top of stacked area charts, you have to manually set the `stack` offset for the lines.
## Stack Transform
```
// Any View Specification
{
  ...
  "transform": [
    // Stack Transform
    {
      "stack": ...,
      "groupby": ...,
      "offset": ...,
      "sort": ...,
      "as": ...
    }
    ...
  ],
  ...
}

```

For example, here is the same normalized stacked bar chart (stack.html#normalized) of the `"population"`, grouped by `"age"` and colored by `"gender"`, but this time using the `stack` property of `transform`.
The `stack` transform in the `transform` array has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| stack | String | Required. The field which is stacked. |
| groupby | String[] | Required. The data fields to group by. |
| offset | String | Mode for stacking marks. One of "zero" (default), "center" , or "normalize" . The "zero" offset will stack starting at 0 . The "center" offset will center the stacks. The "normalize" offset will compute percentage values for each stack point, with output values in the range [0,1] . Default value: "zero" |
| sort | SortField [] | Field that determines the order of leaves in the stacked charts. |
| as | String | String[] | Required. Output field names. This can be either a string or an array of strings with two elements denoting the name for the fields for stack start and stack end respectively. If a single string(e.g., "val" ) is provided, the end field will be "val_end" . |

We can use `stack` transform in conjunction with other transforms to create more complicated charts.
### Diverging Bar Chart
Here we initially `stack` by `"question"` and then use `window` transform to offset each stack.
### Mosaic Chart
To create a mosaic chart we `stack` twice, once in each direction along with `window` transform.
To add labels to this chart, consult this example (/vega-lite/examples/rect_mosaic_labelled_with_offset).

## Band Position
Source: https://vega.github.io/vega-lite/docs/bandposition.html

Band properties can be used to adjust mark bandwidth or position for band scales, bin intervals, or time unit intervals.
| Property | Type | Description |
| --- | --- | --- |
| bandPosition | Number | Relative position on a band of a stacked, binned, time unit, or band scale. For example, the marks will be positioned at the beginning of the band if set to 0 , and at the middle of the band if set to 0.5 . |

## Examples
### Line Position
By default, points in line marks are placed at the beginning of a time interval (e.g., month):
Setting `bandPosition` to `0.5` moves the points to the middle of the time interval.
### Bar Position
By default, bar marks are placed from the beginning of a time interval (e.g., month) to the end of the interval:
Setting `bandPosition` to `0` moves the bar to center-align with ticks.

## Customizing Size
Source: https://vega.github.io/vega-lite/docs/size.html

This page describe how to adjust width and height of visualizations in Vega-Lite.
## Documentation Overview
- Width and Height of Single and Layered Plots (#width-and-height-of-single-and-layered-plots)
- Default Width and Height (#default-width-and-height)
- Specifying Fixed Width and Height (#specifying-fixed-width-and-height)
- Specifying Responsive Width and Height (#specifying-responsive-width-and-height)
- Specifying Width and Height per Discrete Step (#specifying-width-and-height-per-discrete-step)
- Step for Offset Channel (#offset-step)
- Autosize (#autosize)
- Limitations (#limitations)
- Example (#example)
- Width and Height of Multi-View Displays (#width-and-height-of-multi-view-displays)
## Width and Height of Single and Layered Plots
Single view (spec.html#single) and layer (layer.html) specifications can contain the `width` and `height` properties for customizing the view size. By default, `width` and `height` set the size of the data rectangle (plotting) dimensions. To set the overall size of the visualization, the `autosize` (#autosize) property can be specified.
### Default Width and Height
If the top-level `width` / `height` property is not specified, the width / height of a single view is determined based on the view config.
The width will be based on `config.view.continuousWidth` for a plot with a continuous x-field (`200` by default). For a plot with either a discrete x-field or no x-field, the width is based on `config.view.discreteWidth`, which is set to have step width based on the default step size (`config.view.step`  `20` by default).
Similarly, the height will be based on `config.view.continuousHeight` for a plot with a continuous y-field and `config.view.discreteHeight` for a plot with either a discrete y-field or no y-field.
For example, the following bar chart has a fixed 200px height and a 20px width per x-fields discrete step.

### Specifying Fixed Width and Height
The view `width` and `height` property can be set to numbers indicating fixed width and height of the plot.
For a discrete axis, specifying a fixed size (e.g., width in the following plot) would automatically scale the discrete step to fit the size.

Warning: If the cardinality of a discrete x- or y-field is too high, the plot might become too packed.

### Specifying Responsive Width and Height
You can set the top-level `width` or `height` properties to `"container"` to indicate that the width or height of the plot should be the same as its surrounding container. The `width` and `height` can be set independently, for example, you can have a responsive `width` and a fixed `height` by setting `width` to `"container"` and `height` to a number.
After setting `width` or `height` to `"container"`, you need to ensure that the containers width or height is determined outside the plot. For example, the container can be a `<div>` element that has style `width: 100%; height: 300px`. When the container is not available or its size is not defined (e.g., in server-side rendering), the default width and height are `config.view.continuousWidth` and `config.view.continuousHeight`, respectively.

Limitations:
- This responsive mode is available only for single view or layer specifications.
- Vega listens to the `window.resize` event to update plot size from container size. This should cover many use cases. However, if you change the container size programmatically (e.g., you build a custom divider view), youll need to trigger `window.resize` manually. In a modern browser, you can do: `window.dispatchEvent(new Event('resize'));`.
### Specifying Width and Height per Discrete Step
For a discrete x-field or discrete y-field, we can also set `width` (or `height`) to be an object indicating the width (or height) per discrete `step`.

Note: By default, Vega-Lite sets padding for band and point scales (scale.html#band) such that width/height = number of unique values * step. See the scale documentation (scale.html#band) to read more about the relationship among width/height, step, and other scale properties.
#### Step for Offset Channel
For a discrete x-field or discrete y-field with nested offset, the step will be applied to the offset step by default.

To specify step for the x/y scale instead, you can include `"for": "position"` in the `width` or `height`.

### Autosize
The specified dimensions of a chart as explained above set the size of the data rectangle (plotting) dimensions. You can override this behavior by setting the autosize property in the top level specification (spec.html#top-level). Please note the limitations below (#limitations).
Note that for performance reasons Vega-Lite doesnt re-calculate layouts on every view change by default. If your view is cut off after the view updates, you can either set `resize` to `true` or manually call `view.resize()` through the Vega view API (https://vega.github.io/vega/docs/api/view/#view_resize).
The autosize property can be a string or an object with the following properties:
| Property | Type | Description |
| --- | --- | --- |
| type | String | The sizing format type. One of "pad" , "fit" , "fit-x" , "fit-y" , or "none" . See the autosize type documentation for descriptions of each. Default value : "pad" |
| resize | Boolean | A boolean flag indicating if autosize layout should be re-calculated on every view update. Default value : false |
| contains | String | Determines how size calculation should be performed, one of "content" or "padding" . The default setting ( "content" ) interprets the width and height settings as the data rectangle (plotting) dimensions, to which padding is then added. In contrast, the "padding" setting includes the padding within the view size calculations, such that the width and height settings indicate the total intended size of the view. Default value : "content" |

The total size of a Vega-Lite visualization may be determined by multiple factors: specified width, height, and padding values, as well as content such as axes, legends, and titles. To support different use cases, there are three different autosize types for determining the final size of a visualization view:
- `none`: No automatic sizing is performed. The total visualization size is determined solely by the provided width, height and padding values. For example, by default the total width is calculated as `width + padding.left + padding.right`. Any content lying outside this region will be clipped. If autosize.contains is set to `"padding"`, the total width is instead simply width.
- `pad`: Automatically increase the size of the view such that all visualization content is visible. This is the default autosize setting, and ensures that axes, legends and other items outside the normal width and height are included. The total size will often exceed the specified width, height, and padding.
- `fit`: Automatically adjust the layout in an attempt to force the total visualization size to fit within the given width, height and padding values. This setting causes the plotting region to be made smaller in order to accommodate axes, legends and titles. As a result, the value of the width and height signals may be changed to modify the layout. Though effective for many plots, the `fit` method can not always ensure that all content remains visible. For example, if the axes and legends alone require more space than the specified width and height, some of the content will be clipped. Similar to `none`, by default the total width will be `width + padding.left + padding.right`, relative to the original, unmodified width value. If autosize.contains is set to `"padding"`, the total width will instead be the original width.
- `fit-x`: Automatically adjust the layout in an attempt to force the total visualization size to fit within the given width and left and right padding values.
- `fit-y`: Automatically adjust the layout in an attempt to force the total visualization size to fit within the given height and top and bottom padding values.
#### Limitations
In order to `fit` a chart into specified dimensions, it has to satisfy two requirements:
- The view must be either a single (spec.html#single) view or a layered (layer.html) view. Fit does not work with other kinds of composed views (`facet`/`hconcat`/`vconcat`/`repeat`).
- The width and height of the chart cannot depend on an explicitly specified `step` of a discrete scale. Discrete scale `step` has higher precendence than `fit`, and the respective channel of fit will be dropped. E.g., an explicit `step` on a `width` will drop `x` from `fit` and make it `fit-y`.
#### Example
Below is an example of a bar chart that fits exactly into 300px width and the default 200px height.

## Width and Height of Multi-View Displays
The width and height of multi-view displays including concatenated (concat.html), faceted (facet.html), and repeated (repeat.html) are determined based on the size of the composed unit and layered views. To adjust the size of multi-view displays, you can set the `width` and `height` properties of the inner unit and layered views.
For example, you can adjust `width` and `height` of the inner single view specification to adjust the size of a faceted plot.

Note: If you use the `row` or `column` channel to create a faceted plot, `width` and `height` will be applied to the inner single-view plot. For example, this specification is equivalent to the specification above.

## Date Time
Source: https://vega.github.io/vega-lite/docs/datetime.html

A date time definition object (as used in filter transform (filter.html), scale domain (scale.html#domain), and axis (axis.html#ticks)/legend (legend.html#properties) values) provides a convenient way to specify a date time value (without having to specify a timestamp integer).
A date time definition object must have at least one of the following properties:
| Property | Type | Description |
| --- | --- | --- |
| year | Number | Integer value representing the year. |
| quarter | Number | Integer value representing the quarter of the year (from 1-4). |
| month | Number | String | One of: (1) integer value representing the month from 1 - 12 . 1 represents January; (2) case-insensitive month name (e.g., "January" ); (3) case-insensitive, 3-character short month name (e.g., "Jan" ). |
| date | Number | Integer value representing the date (day of the month) from 1-31. |
| day | Number | String | Value representing the day of a week. This can be one of: (1) integer value  1 represents Monday; (2) case-insensitive day name (e.g., "Monday" ); (3) case-insensitive, 3-character short day name (e.g., "Mon" ). Warning: A DateTime definition object with day ** should not be combined with year , quarter , month , or date . |
| hours | Number | Integer value representing the hour of a day from 0-23. |
| minutes | Number | Integer value representing the minute segment of time from 0-59. |
| seconds | Number | Integer value representing the second segment (0-59) of a time value |
| milliseconds | Number | Integer value representing the millisecond segment of time. |

For example `{"year": 2006, "month": "jan", "date": 1}` represents Jan 1, 2006.

