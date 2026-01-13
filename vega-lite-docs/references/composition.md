# Composition

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Composing Layered & Multi-view Plots
Source: https://vega.github.io/vega-lite/docs/composition.html

With Vega-Lite, you can not only create single view visualizations, but also facet (facet.html), layer (layer.html), concatenate (concat.html), and repeat (repeat.html) these views into layered or multiview displays.
A layered or multi-view display can also be composed with other views. Through this hierarchical composition, you can create a whole dashboard as a single specification.
Vega-Lites compiler infers how input data should be reused across constituent views, and whether scale domains should be unioned or remain independent.
## Documentation Overview
- Faceting (#faceting)
- Layering (#layering)
- Concatenation (#concatenation)
- Repeating (#repeating)
- Resolution (#resolution)
## Faceting
With the `facet` operator, you can partition the data and create a view for each subset to create a trellis plot (https://en.wikipedia.org/wiki/Small_multiple). As a shortcut, Vega-Lite also has the `column` and `row` encoding channels (encoding.html#facet) to quickly create a faceted view.
Learn how to use it on the facet page (facet.html).
## Layering
With the `layer` operator, you can place multiple views on top of each other. This can be useful to add annotations to views. Vega-Lite automatically unions scale domains and combines axes and legends.
However, Vega-Lite can not enforce that a unioned domain is semantically meaningful. To prohibit layering of composite views with incompatible layouts, the layer operator restricts its operands to be single or layered views.
Learn how to use it on the layering page (layer.html).
## Concatenation
To place views side-by-side, Vega-Lite provides operators for horizontal (`hconcat`) and vertical (`vconcat`) concatenation.
Learn how to use it on the concatenation page (concat.html).
## Repeating
Often, you may concatenate similar views where the only difference is the field that is used in an encoding. The `repeat` operator is a shortcut that creates a view for each entry in an array of fields.
The `repeat` operator generates multiple plots like `facet`. However, unlike `facet` it allows full replication of a data set in each view.
Learn how to use it on the repeat page (repeat.html).
## Resolution
Vega-Lite determines whether scale domains should be unioned. If the scale domain is unioned, axes and legends can be merged. Otherwise they have to be independent.
To override scale, axis, and legend resolution, you can set the resolve (resolve.html) property.

## Layering views
Source: https://vega.github.io/vega-lite/docs/layer.html

Sometimes, its useful to superimpose one chart on top of another. You can accomplish this by using the `layer` operator. This operator is one of Vega-Lites view composition operators (composition.html). To define a layered chart, put multiple specifications into an array under the `layer` property.
```
{
  "layer": [
    ...  // Single or layered view specifications
  ]
}

```

In addition to common properties of a view specification (spec.html#common), a layer specification has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| layer | LayerSpec [] | UnitSpec [] | Required. Layer or single view specifications to be layered. Note : Specifications inside layer cannot use row and column channels as layering facet specifications is not allowed. Instead, use the facet operator and place a layer inside a facet. |
| width | Number | String | Object | The width of a visualization. For a plot with a continuous x-field, width should be a number. For a plot with either a discrete x-field or no x-field, width can be either a number indicating a fixed width or an object in the form of {step: number} defining the width per discrete step. (No x-field is equivalent to having one discrete step.) To enable responsive sizing on width, it should be set to "container" . Default value: Based on config.view.continuousWidth for a plot with a continuous x-field and config.view.discreteWidth otherwise. Note: For plots with row and column channels , this represents the width of a single view and the "container" option cannot be used. See also: width documentation. |
| height | Number | String | Object | The height of a visualization. For a plot with a continuous y-field, height should be a number. For a plot with either a discrete y-field or no y-field, height can be either a number indicating a fixed height or an object in the form of {step: number} defining the height per discrete step. (No y-field is equivalent to having one discrete step.) To enable responsive sizing on height, it should be set to "container" . Default value: Based on config.view.continuousHeight for a plot with a continuous y-field and config.view.discreteHeight otherwise. Note: For plots with row and column channels , this represents the height of a single view and the "container" option cannot be used. See also: height documentation. |
| view | ViewBackground | An object defining the view backgrounds fill and stroke. Default value: none (transparent) |
| encoding | SharedEncoding | A shared key-value mapping between encoding channels and definition of fields in the underlying layers. |
| projection | Projection | An object defining properties of the geographic projection shared by underlying layers. |
| resolve | Resolve | Scale, axis, and legend resolutions for view composition specifications. |

Please note that you can only layer single or layered views to guarantee that the combined views have a compatible layout. For instance, it is not clear how a composed view with two views side-by-side could be layered on top of a single view.
## Example
A layered chart consistent of multiple charts that are drawn on top of each other. We will start by creating specifications for the individual layers and eventually combine them in a single `layer` spec.
The first chart is a line chart that shows the stock price of different stocks over time.
The second chart shows the mean price of individual stocks with a rule mark. The `rule` mark is a special mark that can span the whole width/height of a single view specification.
To layer these two charts on top of each other, we have to put the two specifications in the same layer array. Note that we can leave `data` at the top level as both layers use the same data.
See the example gallery (/vega-lite/examples/#layering) for more layering examples.
### Combined Scales and Guides
When you have different scales in different layers, the scale domains are unioned so that all layers can use the same scale. In the example above, Vega-Lite automatically uses a common y-axis and color legend. We can disable this by setting the `resolve` property.
The default resolutions (resolve.html) for layer are shared scales, axes, and legends.
In the chart below, we set the y-scales of the different layers to be independent with `"resolve": {"scale": {"y": "independent"}}`.

## Faceting a Plot into a Trellis Plot
Source: https://vega.github.io/vega-lite/docs/facet.html

A Trellis plot (or small multiple) (https://en.wikipedia.org/wiki/Small_multiple) is a series of similar plots that displays different subsets of the same data, facilitating comparison across subsets.
There are two ways to facet views in Vega-Lite:
First, the `facet` operator (#facet-operator) is one of Vega-Lites view composition operators (composition.html). This is the most flexible way to create faceted plots and allows composition with other operators.
Second, as a shortcut you can use the `facet`, `column`, or `row` encoding channels (#facet-channels).
## Documentation Overview
- Facet Operator (#facet-operator)
- Facet Field Definition (#field-def)
- Row/Column Facet Mapping (#mapping)
- Facet Headers (#header)
- Example (#example)
- Row-Facet (#row-full)
- Wrapped Facet (#facet-full)
- Facet, Row, and Column Encoding Channels (#facet-row-and-column-encoding-channels)
- Facet Field Definition (#facet-field-definition)
- Examples (#examples)
- Row Facet (with Row Encoding) (#row-encoding)
- Grid Facet (with Row and column Encoding) (#grid-facet-with-row-and-column-encoding)
- Wrapped Facet (with Facet Encoding) (#facet-encoding)
- Resolve (#resolve)
- Facet Configuration (#config)
## Facet Operator
To create a faceted view, define how the data should be faceted in `facet` and how each facet should be displayed in the `spec`.
```
{
  "facet": {
    ... // Facet definition
  },
  "spec": ...  // Specification
}

```

In addition to common properties of a view specification (spec.html#common), a facet specification has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| facet | FacetFieldDef | FacetMapping | Required. Definition for how to facet the data. One of: 1) a field definition for faceting the plot by one field 2) An object that maps row and column channels to their field definitions |
| spec | LayerSpec | UnitSpec | Required. A specification of the view that gets faceted. |
| columns | Number | The number of columns to include in the view composition layout. Default value : undefined  An infinite number of columns (a single row) will be assumed. This is equivalent to hconcat (for concat ) and to using the column channel (for facet and repeat ). Note : 1) This property is only for: the general (wrappable) concat operator (not hconcat / vconcat ) the facet and repeat operator with one field/repetition definition (without row/column nesting) 2) Setting the columns to 1 is equivalent to vconcat (for concat ) and to using the row channel (for facet and repeat ). |

### Facet Field Definition
A facet field definition (encoding.html#field-def) has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| bin | Boolean | BinParams | Null | A flag for binning a quantitative field, an object defining binning parameters , or indicating that the data for x or y channel are binned before they are imported into Vega-Lite ( "binned" ). If true , default binning parameters will be applied. If "binned" , this indicates that the data for the x (or y ) channel are already binned. You can map the bin-start field to x (or y ) and the bin-end field to x2 (or y2 ). The scale and axis will be formatted similar to binning in Vega-Lite. To adjust the axis ticks based on the bin step, you can also set the axiss tickMinStep property. Default value: false See also: bin documentation. |
| field | Field | Required. A string defining the name of the field from which to pull a data value or an object defining iterated values from the repeat operator. See also: field documentation. Notes: 1) Dots ( . ) and brackets ( [ and ] ) can be used to access nested objects (e.g., "field": "foo.bar" and "field": "foo['bar']" ). If field names contain dots or brackets but are not nested, you can use \\ to escape dots and brackets (e.g., "a\\.b" and "a\\[0\\]" ). See more details about escaping in the field documentation . 2) field is not required if aggregate is count . |
| timeUnit | TimeUnit | String | TimeUnitParams | Time unit (e.g., year , yearmonth , month , hours ) for a temporal field. or a temporal field that gets casted as ordinal . Default value: undefined (None) See also: timeUnit documentation. |
| type | String | The type of measurement ( "quantitative" , "temporal" , "ordinal" , or "nominal" ) for the encoded field or constant value ( datum ). It can also be a "geojson" type for encoding geoshape . Vega-Lite automatically infers data types in many cases as discussed below. However, type is required for a field if: (1) the field is not nominal and the field encoding has no specified aggregate (except argmin and argmax ), bin , scale type, custom sort order, nor timeUnit or (2) if you wish to use an ordinal scale for a field with bin or timeUnit . Default value: 1) For a data field , "nominal" is the default data type unless the field encoding has aggregate , channel , bin , scale type, sort , or timeUnit that satisfies the following criteria: "quantitative" is the default type if (1) the encoded field contains bin or aggregate except "argmin" and "argmax" , (2) the encoding channel is latitude or longitude channel or (3) if the specified scale type is a quantitative scale . "temporal" is the default type if (1) the encoded field contains timeUnit or (2) the specified scale type is a time or utc scale "ordinal" is the default type if (1) the encoded field contains a custom sort order , (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding channel is order . 2) For a constant value in data domain ( datum ): "quantitative" if the datum is a number "nominal" if the datum is a string "temporal" if the datum is a date time object Note: Data type describes the semantics of the data rather than the primitive data types (number, string, etc.). The same primitive data type can have different types of measurement. For example, numeric data can represent quantitative, ordinal, or nominal data. Data values for a temporal field can be either a date-time string (e.g., "2015-03-07 12:32:17" , "17:01" , "2015-03-16" . "2015" ) or a timestamp number (e.g., 1552199579097 ). When using with bin , the type property can be either "quantitative" (for using a linear bin scale) or "ordinal" (for using an ordinal bin scale) . When using with timeUnit , the type property can be either "temporal" (default, for using a temporal scale) or "ordinal" (for using an ordinal scale) . When using with aggregate , the type property refers to the post-aggregation data type. For example, we can calculate count distinct of a categorical field "cat" using {"aggregate": "distinct", "field": "cat"} . The "type" of the aggregate output is "quantitative" . Secondary channels (e.g., x2 , y2 , xError , yError ) do not have type as they must have exactly the same type as their primary channels (e.g., x , y ). See also: type documentation. |
| header | Header | Null | An object defining properties of a facets header. |

Note
- Unlike a positional field definition (encoding.html#position-field-def), a facet field definition has the `header` property instead of `scale` and `axis`.
- Since `facet`, `row` and `column` represent actual data fields that are used to partition the data, they cannot encode a constant `value`. In addition, you should not facet by quantitative fields unless they are binned (bin.html), or temporal fields unless you use `timeUnit` (timeunit.html).
### Row/Column Facet Mapping
The `facet` property of a faceted view specification describes mappings between `row` and `column` and their field definitions:
| Property | Type | Description |
| --- | --- | --- |
| column | FacetFieldDef | A field definition for the horizontal facet of trellis plots. |
| row | FacetFieldDef | A field definition for the vertical facet of trellis plots. |

### Facet Headers
Similar to axes of position channels, a header (header.html) of a facet channel provides guides to convey the data value that each row and column represent.
You can find more about facet headers in the header documentation (header.html).
### Example
Here are examples of full row-facet and wrapped facet specifications. For more example, see the example gallery (/vega-lite/examples/#trellis).
#### Row-Facet
The following specification uses the `facet` operator to vertically facet the histograms for the horsepower of cars by origin (using `"row"`). Each chart shows the histogram for one origin (Europe, Japan, and USA).

This is the same example as below (#row-encoding) but the facet operator is more flexible as it allows composition and more customization such as overriding scale, axis, and legend resolution.
#### Wrapped Facet

## Facet, Row, and Column Encoding Channels
The facet channels (encoding.html#facet) (`facet`, `row`, and `column`) are encoding channels (encoding.html#channels) that serves as macros for a facet specification. Vega-Lite automatically translates this shortcut to use the facet operator.
### Facet Field Definition
In addition to `field` (field.html), `type` (type.html), `bin` (bin.html), and `timeUnit` (timeunit.html), field definitions (#field-def) for `row`, `column` and `facet` channels may also include these properties:
| Property | Type | Description |
| --- | --- | --- |
| align | String | The alignment to apply to row/column facets subplot. The supported string values are "all" , "each" , and "none" . For "none" , a flow layout will be used, in which adjacent subviews are simply placed one after the other. For "each" , subviews will be aligned into a clean grid structure, but each row or column may be of variable size. For "all" , subviews will be aligned and each row or column will be sized identically based on the maximum observed size. String values for this property will be applied to both grid rows and columns. Default value: "all" . |
| center | Boolean | Boolean flag indicating if facets subviews should be centered relative to their respective rows or columns. Default value: false |
| spacing | Number | The spacing in pixels between facets sub-views. Default value : Depends on "spacing" property of the view composition configuration ( 20 by default) |

In addition, the `facet` channel should include the `columns` property:
| Property | Type | Description |
| --- | --- | --- |
| columns | Number | The number of columns to include in the view composition layout. Default value : undefined  An infinite number of columns (a single row) will be assumed. This is equivalent to hconcat (for concat ) and to using the column channel (for facet and repeat ). Note : 1) This property is only for: the general (wrappable) concat operator (not hconcat / vconcat ) the facet and repeat operator with one field/repetition definition (without row/column nesting) 2) Setting the columns to 1 is equivalent to vconcat (for concat ) and to using the row channel (for facet and repeat ). |

Meanwhile, the `row` and `column` channel could include the following properties:
| Property | Type | Description |
| --- | --- | --- |
| align | String | The alignment to apply to row/column facets subplot. The supported string values are "all" , "each" , and "none" . For "none" , a flow layout will be used, in which adjacent subviews are simply placed one after the other. For "each" , subviews will be aligned into a clean grid structure, but each row or column may be of variable size. For "all" , subviews will be aligned and each row or column will be sized identically based on the maximum observed size. String values for this property will be applied to both grid rows and columns. Default value: "all" . |
| center | Boolean | Boolean flag indicating if facets subviews should be centered relative to their respective rows or columns. Default value: false |
| spacing | Number | The spacing in pixels between facets sub-views. Default value : Depends on "spacing" property of the view composition configuration ( 20 by default) |

### Examples
Here are examples of row-facet and wrapped facet plots that use encoding to specify the faceted fields. For more example, see the example gallery (/vega-lite/examples/#trellis).
#### Row Facet (with Row Encoding)

Under the hood, Vega-Lite translates this spec with `"row"` channel to the more flexible specs with the facet operator above (#row-full).
#### Grid Facet (with Row and column Encoding)
Using both `"row"` and `"column"` channels produce a grid of small multiples.

#### Wrapped Facet (with Facet Encoding)

Under the hood, Vega-Lite translates this spec with `"facet"` channel to the more flexible specs with the facet operator above (#facet-full).
## Resolve
The default resolutions (resolve.html) for row/column facet are shared scales, axes, and legends.
To override this behavior, you can set `resolve` to `"independent"`:

## Facet Configuration
```
// Top-level View Specification
{
  ...,
  "config": { // Configuration Object

    "facet": { // - Facet Configuration
      "spacing": ...,
      "columns": ...,
    },
    ...
  }
}

```

The facet configuration supports the following properties:
| Property | Type | Description |
| --- | --- | --- |
| columns | Number | The number of columns to include in the view composition layout. Default value : undefined  An infinite number of columns (a single row) will be assumed. This is equivalent to hconcat (for concat ) and to using the column channel (for facet and repeat ). Note : 1) This property is only for: the general (wrappable) concat operator (not hconcat / vconcat ) the facet and repeat operator with one field/repetition definition (without row/column nesting) 2) Setting the columns to 1 is equivalent to vconcat (for concat ) and to using the row channel (for facet and repeat ). |
| spacing | Number | The default spacing in pixels between composed sub-views. Default value : 20 |

## Concatenating views
Source: https://vega.github.io/vega-lite/docs/concat.html

To place views side-by-side, Vega-Lites view composition (composition.html) provides the following concatenation operators:
- `hconcat` (#hconcat) - horizontal concatenation
- `vconcat` (#vconcat) - vertical concatenation
- `concat` (#concat) - general concatenation (wrappable)
If you concatenate similar views where the only difference is the field that is used in an encoding, use the `repeat` operator (repeat.html).
## Documentation Overview
- Horizontal Concatenation (#hconcat)
- Example (#example)
- Vertical Concatenation (#vconcat)
- Example (#example-1)
- General (Wrappable) Concatenation (#concat)
- Example (#example-2)
- Resolve (#resolve)
- Concat Configuration (#config)
## Horizontal Concatenation
To put multiple views into a column, set the `"hconcat"` to an array of view specifications.
```
{
  "hconcat": [
    ...  // Specifications
  ],
  ...
}

```

In addition to common properties of a view specification (spec.html#common), a horizontal concat specification has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| hconcat | Any |  |

### Example

## Vertical Concatenation
To put multiple views into a row, set the `"vconcat"` to an array of view specifications.
```
{
  "vconcat": [
    ...  // Specifications
  ],
  ...
}

```

In addition to common properties of a view specification (spec.html#common), a vertical concat specification has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| vconcat | Any |  |

### Example

## General (Wrappable) Concatenation
To put multiple views into a flexible flow layout, set the `"concat"` to an array of view specifications and specify the `"columns"` property to set the number of maximum items per rows.
```
{
  "concat": [
    ...  // Specifications
  ],
  "columns": ...,
  ...
}

```

In addition to common properties of a view specification (spec.html#common), a general concat specification has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| concat | Any |  |
| columns | Any |  |

### Example

## Resolve
The default resolutions (resolve.html) for concatenation are independent scales and axes for position channels (encoding.html#position) and shared scales and legends for all other channels. Currently, Vega-Lite does not support shared axes for concatenated views.
## Concat Configuration
```
// Top-level View Specification
{
  ...,
  "config": { // Configuration Object

    "concat": { // - Concat Configuration
      "spacing": ...,
      "columns": ...,
    },
    ...
  }
}

```

The concat configuration supports the following properties:
| Property | Type | Description |
| --- | --- | --- |
| columns | Number | The number of columns to include in the view composition layout. Default value : undefined  An infinite number of columns (a single row) will be assumed. This is equivalent to hconcat (for concat ) and to using the column channel (for facet and repeat ). Note : 1) This property is only for: the general (wrappable) concat operator (not hconcat / vconcat ) the facet and repeat operator with one field/repetition definition (without row/column nesting) 2) Setting the columns to 1 is equivalent to vconcat (for concat ) and to using the row channel (for facet and repeat ). |
| spacing | Number | The default spacing in pixels between composed sub-views. Default value : 20 |

## Repeat a View
Source: https://vega.github.io/vega-lite/docs/repeat.html

The `repeat` operator is part of Vega-Lites view composition (composition.html). It provides a shortcut that creates a view for each entry in an array of fields. This operator generates multiple plots like `facet` (facet.html). However, unlike `facet` it allows full replication of a data set in each view.
## Documentation Overview
- Repeat Operator (#repeat-operator)
- Row/Column/Layer Repeat Mapping (#repeat-mapping)
- Examples (#examples)
- Repeated Line Charts (#repeated-line-charts)
- Multi-series Line Chart with Repeated Layers (#multi-series-line-chart-with-repeated-layers)
- Repeated Histogram (Wrapped) (#repeated-histogram-wrapped)
- Scatterplot Matrix (SPLOM) (#scatterplot-matrix-splom)
- Resolve (#resolve)
- Repeat Configuration (#config)
## Repeat Operator
To repeat a view, define what fields should be used for each entry. Then define the repeated view in `spec` with a reference to a repeated field (`{"repeat": ...}`).
```
{
  "repeat": {
    ... // Repeat definition
  },
  "spec": ... // Specification
}

```

In addition to common properties of a view specification (spec.html#common), a repeat specification has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| repeat | Any |  |
| spec | Any |  |
| columns | Any |  |

## Row/Column/Layer Repeat Mapping
The `repeat` property can be an object with at least one of `"row"`, `"column"` and `"layer"` properties, which define the list of fields that should be repeated into a row, a column, or a layer.
Note that when you repeat views into layers, the views are superimposed. Even if different layers use different colors, Vega-Lite will not generate a legend and not stack marks such as bars or areas. If you want a legend or stack different fields, use the fold transform (fold.html) to convert your data to long form and then use a color encoding.
| Property | Type | Description |
| --- | --- | --- |
| row | String[] | An array of fields to be repeated vertically. |
| column | String[] | An array of fields to be repeated horizontally. |

## Examples
### Repeated Line Charts
For instance, you can use this operator to quickly create an overview over the trends in multiple variables.

Note how the field for the y channel refers to a repeated field.
```
"y": {
  "field": {"repeat": "repeat"}
  ...
},

```

### Multi-series Line Chart with Repeated Layers
You can also use `repeat` with `layer` to create a multi-series line chart. Here we map a repeater field as data value (`datum` (datum.html)) for the color encoding.

### Repeated Histogram (Wrapped)

### Scatterplot Matrix (SPLOM)
Repeat can be used to create a scatterplot matrix (SPLOM), where each cell shows a different 2D projection of the same data table. Here, we define both `row` and `column`.

You can also check the interactive SPLOM example (/vega-lite/examples/interactive_splom.html).
## Resolve
The default resolutions (resolve.html) for repeat are independent scales and axes for position channels (encoding.html#position) and shared scales and legends for all other channels. Currently, Vega-Lite does not support shared axes for repeated views.
## Repeat Configuration
Since repeat is a shorthand for concatenation, the concat configuration (concat.html#config) is also used for repeated views.
```
// Top-level View Specification
{
  ...,
  "config": { // Configuration Object

    "concat": { // - Concat Configuration
      "spacing": ...,
      "columns": ...,
    },
    ...
  }
}

```

The repeat configuration supports the following properties:
| Property | Type | Description |
| --- | --- | --- |
| columns | Number | The number of columns to include in the view composition layout. Default value : undefined  An infinite number of columns (a single row) will be assumed. This is equivalent to hconcat (for concat ) and to using the column channel (for facet and repeat ). Note : 1) This property is only for: the general (wrappable) concat operator (not hconcat / vconcat ) the facet and repeat operator with one field/repetition definition (without row/column nesting) 2) Setting the columns to 1 is equivalent to vconcat (for concat ) and to using the row channel (for facet and repeat ). |
| spacing | Number | The default spacing in pixels between composed sub-views. Default value : 20 |

## Scale and Guide Resolution
Source: https://vega.github.io/vega-lite/docs/resolve.html

Vega-Lite determines whether scale domains should be unioned. If the scale domain is unioned, axes and legends can be merged. Otherwise they have to be independent.
```
{
  "resolve": {
    // Scale resolution
    "scale": {
      CHANNEL: ...
    },
    // Axis resolution for position channels
    "axis": {
      POSITION_CHANNEL: ...
    },
    // Legend resolution for non-position channels
    "legend": {
      NON_POSITION_CHANNEL: ...
    }
  }
}

```

`resolve` is an object where the keys are `scale`, `axis`, or `legend` and the values are again objects that define the resolution for different channels.
For scales, resolution can be specified for every channel. For axes, resolutions can be defined for `x` and `y` (positional channels). For legends, resolutions can be defined for `color`, `opacity`, `shape`, and `size` (non-positional channels).
There are two options to resolve a scale, axis, or legend: `"shared"` and `"independent"`. Independent scales imply independent axes and legends.
The defaults are documented on the faceting (facet.html#resolve), layering (layer.html#resolve), concatenation (concat.html#resolve), and repeating (repeat.html#resolve) pages.
## Example
In this example, we use two independent color scales for two repeated charts. Note how Vega-Lite automatically creates separate legends for each chart.

