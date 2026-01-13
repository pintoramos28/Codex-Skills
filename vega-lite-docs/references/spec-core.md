# Spec Core

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Vega-Lite View Specification
Source: https://vega.github.io/vega-lite/docs/spec.html

Vega-Lite specifications are JSON objects that describe a diverse range of interactive visualizations. The simplest form of specification is a specification of a single view (#single), which describes a view that uses a single mark type (mark.html) to visualize the data. Besides using a single view specification as a standalone visualization, Vega-Lite also provides operators for composing multiple view specifications into a layered or multi-view specification. These operators include `layer` (layer.html), `facet` (facet.html), `concat` (concat.html), and `repeat` (repeat.html).
## Documentation Overview
- Common Properties of Specifications (#common)
- Top-Level Specifications (#top-level)
- Single View Specifications (#single)
- View Background (#view-background)
- Example: Background (#example-background)
- Layered and Multi-view Specifications (#layered-and-multi-view-specifications)
- View Configuration (#config)
## Common Properties of Specifications
All view specifications in Vega-Lite can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| name | String | Name of the visualization for later reference. |
| description | String | Description of this mark for commenting purpose. |
| title | Text | TitleParams | Title for the plot. |
| data | Data | Null | Required. An object describing the data source. Set to null to ignore the parents data source. If no data is set, it is derived from the parent. |
| transform | Transform [] | An array of data transformations such as filter and new field calculation. |
| params | TopLevelParameter[] | An array of parameters that may either be simple variables, or more complex selections that map user input to data queries. |

In addition, all view composition specifications (`layer` (layer.html), `facet` (facet.html), `concat` (concat.html), and `repeat` (repeat.html)) can have the `resolve` property for scale, axes, and legend resolution (resolve.html):
| Property | Type | Description |
| --- | --- | --- |
| resolve | Resolve | Scale, axis, and legend resolutions for view composition specifications. |

Finally, all view layout composition (`facet` (facet.html), `concat` (concat.html), and `repeat` (repeat.html)) can have the following layout properties:
| Property | Type | Description |
| --- | --- | --- |
| align | String | Object | The alignment to apply to grid rows and columns. The supported string values are "all" , "each" , and "none" . For "none" , a flow layout will be used, in which adjacent subviews are simply placed one after the other. For "each" , subviews will be aligned into a clean grid structure, but each row or column may be of variable size. For "all" , subviews will be aligned and each row or column will be sized identically based on the maximum observed size. String values for this property will be applied to both grid rows and columns. Alternatively, an object value of the form {"row": string, "column": string} can be used to supply different alignments for rows and columns. Default value: "all" . |
| bounds | String | The bounds calculation method to use for determining the extent of a sub-plot. One of full (the default) or flush . If set to full , the entire calculated bounds (including axes, title, and legend) will be used. If set to flush , only the specified width and height values for the sub-view will be used. The flush setting can be useful when attempting to place sub-plots without axes or legends into a uniform grid structure. Default value: "full" |
| center | Boolean | Object | Boolean flag indicating if subviews should be centered relative to their respective rows or columns. An object value of the form {"row": boolean, "column": boolean} can be used to supply different centering values for rows and columns. Default value: false |
| spacing | Number | Object | The spacing in pixels between sub-views of the composition operator. An object of the form {"row": number, "column": number} can be used to set different spacing values for rows and columns. Default value : Depends on "spacing" property of the view composition configuration ( 20 by default) |

## Top-Level Specifications
In addition to the common properties (#common), any kind of top-level specifications (including a standalone single view specification as well as layered and multi-view specifications) can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| $schema | String | URL to JSON schema for a Vega-Lite specification. Unless you have a reason to change this, use https://vega.github.io/schema/vega-lite/v6.json . Setting the $schema property allows automatic validation and autocomplete in editors that support JSON schema. |
| background | Color | ExprRef | CSS color property to use as the background of the entire view. Default value: "white" |
| padding | Number | Object | ExprRef | The default visualization padding, in pixels, from the edge of the visualization canvas to the data rectangle. If a number, specifies padding for all sides. If an object, the value should have the format {"left": 5, "top": 5, "right": 5, "bottom": 5} to specify padding for each side of the visualization. Default value : 5 |
| autosize | String | AutoSizeParams | How the visualization size should be determined. If a string, should be one of "pad" , "fit" or "none" . Object values can additionally specify parameters for content sizing and automatic resizing. Default value : pad |
| config | Config | Vega-Lite configuration object. This property can only be defined at the top-level of a specification. |
| usermeta | Object | Optional metadata that will be passed to Vega. This object is completely ignored by Vega and Vega-Lite and can be used for custom metadata. |

## Single View Specifications
```
{
  // Properties for top-level specification (e.g., standalone single view specifications)
  "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
  "background": ...,
  "padding": ...,
  "autosize": ...,
  "config": ...,
  "usermeta": ...,

  // Properties for any specifications
  "title": ...,
  "name": ...,
  "description": ...,
  "data": ...,
  "transform": ...,

  // Properties for any single view specifications
  "width": ...,
  "height": ...,
  "mark": ...,
  "encoding": {
    "x": {
      "field": ...,
      "type": ...,
      ...
    },
    "y": ...,
    "color": ...,
    ...
  }
}

```

A single view specification describes a graphical `mark` (mark.html) type (e.g., `point`s or `bar`s) and its `encoding` (encoding.html), or the mapping between data values and properties of the mark. By simply providing the mark type and the encoding mapping, Vega-Lite automatically produces other visualization components including axes (axis.html), legends (legend.html), and scales (scale.html). Unless explicitly specified, Vega-Lite determines properties of these components based on a set of carefully designed rules. This approach allows Vega-Lite specifications to be succinct and expressive, but also enables customization.
As it is designed for analysis, Vega-Lite also supports data transformation such as aggregation (aggregate.html), binning (bin.html), time unit conversion (timeunit.html), filtering (transform.html), and sorting (sort.html).
To summarize, a single-view specification in Vega-Lite can have the following properties (in addition to common properties of a specification (#common)):
| Property | Type | Description |
| --- | --- | --- |
| mark | Mark | Required. A string describing the mark type (one of "bar" , "circle" , "square" , "tick" , "line" , "area" , "point" , "rule" , "geoshape" , and "text" ) or a mark definition object . |
| encoding | Encoding | A key-value mapping between encoding channels and definition of fields. |
| width | Number | String | Object | The width of a visualization. For a plot with a continuous x-field, width should be a number. For a plot with either a discrete x-field or no x-field, width can be either a number indicating a fixed width or an object in the form of {step: number} defining the width per discrete step. (No x-field is equivalent to having one discrete step.) To enable responsive sizing on width, it should be set to "container" . Default value: Based on config.view.continuousWidth for a plot with a continuous x-field and config.view.discreteWidth otherwise. Note: For plots with row and column channels , this represents the width of a single view and the "container" option cannot be used. See also: width documentation. |
| height | Number | String | Object | The height of a visualization. For a plot with a continuous y-field, height should be a number. For a plot with either a discrete y-field or no y-field, height can be either a number indicating a fixed height or an object in the form of {step: number} defining the height per discrete step. (No y-field is equivalent to having one discrete step.) To enable responsive sizing on height, it should be set to "container" . Default value: Based on config.view.continuousHeight for a plot with a continuous y-field and config.view.discreteHeight otherwise. Note: For plots with row and column channels , this represents the height of a single view and the "container" option cannot be used. See also: height documentation. |
| view | ViewBackground | An object defining the view backgrounds fill and stroke. Default value: none (transparent) |
| projection | Projection | An object defining properties of geographic projection, which will be applied to shape path for "geoshape" marks and to latitude and "longitude" channels for other marks. |

### View Background
The `background` property of a top-level view specification defines the background of the whole visualization canvas. Meanwhile, the `view` property of a single-view or layer (layer.html) specification can define the background of the view with the following properties:
| Property | Type | Description |
| --- | --- | --- |
| style | String | String[] | A string or array of strings indicating the name of custom styles to apply to the view background. A style is a named collection of mark property defaults defined within the style configuration . If style is an array, later styles will override earlier styles. Default value: "cell" Note: Any specified view background properties will augment the default style. |
| cornerRadius | Number | ExprRef | The radius in pixels of rounded rectangles or arcs corners. Default value: 0 |
| cursor | String | The mouse cursor used over the view. Any valid CSS cursor type can be used. |
| fill | Color | Null | ExprRef | The fill color. Default value: undefined |
| fillOpacity | Number | ExprRef | The fill opacity (value between [0,1]). Default value: 1 |
| opacity | Number | ExprRef | The overall opacity (value between [0,1]). Default value: 0.7 for non-aggregate plots with point , tick , circle , or square marks or layered bar charts and 1 otherwise. |
| stroke | Color | Null | ExprRef | The stroke color. Default value: "#ddd" |
| strokeCap | String | ExprRef | The stroke cap for line ending style. One of "butt" , "round" , or "square" . Default value: "butt" |
| strokeDash | Number[] | ExprRef | An array of alternating stroke, space lengths for creating dashed or dotted lines. |
| strokeDashOffset | Number | ExprRef | The offset (in pixels) into which to begin drawing with the stroke dash array. |
| strokeJoin | String | ExprRef | The stroke line join method. One of "miter" , "round" or "bevel" . Default value: "miter" |
| strokeMiterLimit | Number | ExprRef | The miter limit at which to bevel a line join. |
| strokeOpacity | Number | ExprRef | The stroke opacity (value between [0,1]). Default value: 1 |
| strokeWidth | Number | ExprRef | The stroke width, in pixels. |

#### Example: Background
For example, the following plot has orange as the whole visualization background color while setting the view background to yellow.

## Layered and Multi-view Specifications
To create layered and multi-view graphics, please refer to the following pages:
- `layer` (layer.html)
- `facet` (facet.html)
- `concat` (concat.html)
- `repeat` (repeat.html)
## View Configuration
```
// Top-level View Specification
{
  ...,
  "config": { // Configuration Object

    "view": { // - View Configuration

      // View Size
      "continuousWidth": ...,
      "continuousHeight": ...,
      "discreteWidth": ...,
      "discreteHeight": ...,
      // View Background Properties
      "fill": ...,
      "stroke": ...,
      ...
    },
    ...
  }
}

```

The style of a single view visualization can be customized by specifying the `view` property of the `config` object. The view config support all view background properties (#view-background) except `"style"`.
In addition, the following properties of the `view` configuration determine the default width and height of single and layered views.
| Property | Type | Description |
| --- | --- | --- |
| continuousWidth | Number | The default width when the plot has a continuous field for x or longitude, or has arc marks. Default value: 300 |
| continuousHeight | Number | The default height when the plot has a continuous y-field for x or latitude, or has arc marks. Default value: 300 |
| discreteWidth | Number | Object | The default width when the plot has non-arc marks and either a discrete x-field or no x-field. The width can be either a number indicating a fixed width or an object in the form of {step: number} defining the width per discrete step. Default value: a step size based on config.view.step . |
| discreteHeight | Number | Object | The default height when the plot has non arc marks and either a discrete y-field or no y-field. The height can be either a number indicating a fixed height or an object in the form of {step: number} defining the height per discrete step. Default value: a step size based on config.view.step . |
| step | Number | Default step size for x-/y- discrete fields. |

For example, setting the `step` property in the view config can adjust default discrete step in the plot.

For more information about view size, please see the size (size.html) documentation.

## Data
Source: https://vega.github.io/vega-lite/docs/data.html

Akin to Vega (https://www.github.com/vega/vega)s data model (https://vega.github.io/vega/docs/data/), the basic data model used by Vega-Lite is tabular data, similar to a spreadsheet or a database table. Individual data sets are assumed to contain a collection of records, which may contain any number of named data fields.
Vega-Lites `data` property describes the visualizations data source as part of the specification, which can be either inline data (#inline) (`values`) or a URL from which to load the data (#url) (`url`). Or, we can create an empty, named data source (#named) (`name`), which can be bound at runtime (https://vega.github.io/vega/docs/api/view/#data) or populated from top-level `datasets` (#datasets).
In addition, Vega-Lite includes data generators which can generate data sets such as numerical sequences or geographic reference elements such as GeoJSON graticule or sphere objects.
## Documentation Overview
- Types of Data Sources (#types-of-data-sources)
- Inline Data (#inline)
- Data from URL (#url)
- Named Data Sources (#named)
- Format (#format)
- json (#json)
- csv (#csv)
- tsv (#tsv)
- dsv (#dsv)
- topojson (#topojson)
- Data Generators (#data-generators)
- Sequence Generator (#sequence)
- Graticule Generator (#graticule)
- Sphere Generator (#sphere)
- Datasets (#datasets)
## Types of Data Sources
### Inline Data
Inline Data can be specified using `values` property. Here is a list of all properties of an inline `data` source:
| Property | Type | Description |
| --- | --- | --- |
| values | Array | Required. The full data set, included inline. This can be an array of objects or primitive values, an object, or a string. Arrays of primitive values are ingested as objects with a data property. Strings are parsed according to the specified format type. |
| name | String | Provide a placeholder name and bind data at runtime. |
| format | DataFormat | An object that specifies the format for parsing the data. |

For example, the following specification embeds an inline data table with nine rows and two columns (`a` and `b`).

If the input data is simply an array of primitive values, each value is mapped to the `data` property of a new object. For example `[5, 3, 8, 1]` is loaded as:
```
[{"data": 5}, {"data": 3}, {"data": 8}, {"data": 1}]

```

You can also inline a string that will be parsed according to the specified format type.

### Data from URL
Data can be loaded from a URL using the `url` property. In addition, the format of the input data can be specified using the `formatType` property. By default Vega-Lite will infer the type from the file extension.
Here is a list of all properties describing a `data` source from URL:
| Property | Type | Description |
| --- | --- | --- |
| url | String | Required. An URL from which to load the data set. Use the format.type property to ensure the loaded data is correctly parsed. |
| name | String | Provide a placeholder name and bind data at runtime. |
| format | DataFormat | An object that specifies the format for parsing the data. |

For example, the following specification loads data from a relative `url`: `data/cars.json`. Note that the format type is implicitly `"json"` by default.

### Named Data Sources
Data can also be added at runtime through the Vega View API (https://vega.github.io/vega/docs/api/view/#data). Data sources are referenced by name, which is specified in Vega-Lite with `name`.
Here is a list of all properties describing a named `data` source:
| Property | Type | Description |
| --- | --- | --- |
| name | String | Required. Provide a placeholder name and bind data at runtime. New data may change the layout but Vega does not always resize the chart. To update the layout when the data updates, set autosize or explicitly use view.resize . |
| format | DataFormat | An object that specifies the format for parsing the data. |

For example, to create a data source named `myData`, use the following data
```
{
  "name": "myData"
}

```

You can use the Vega view API (https://vega.github.io/vega/docs/api/view/#data) to load data at runtime and update the chart. Here is an example using Vega-Embed (https://github.com/vega/vega-embed):
```
vegaEmbed('#vis', spec).then((res) =>
  res.view
    .insert('myData', [
      /* some data array */
    ])
    .run(),
);

```

You can also use a changeset (https://github.com/vega/vega-view#view_change) to modify the data on the chart as done on this data streaming demo (/vega-lite/tutorials/streaming.html)
## Format
The format object describes the data format and additional parsing instructions.
| Property | Type | Description |
| --- | --- | --- |
| type | String | Type of input data: "json" , "csv" , "tsv" , "dsv" . Default value: The default format type is determined by the extension of the file URL. If no extension is detected, "json" will be used by default. |
| parse | Object | Null | If set to null , disable type inference based on the spec and only use type inference based on the data. Alternatively, a parsing directive object can be provided for explicit data types. Each property of the object corresponds to a field name, and the value to the desired data type (one of "number" , "boolean" , "date" , or null (do not parse the field)). For example, "parse": {"modified_on": "date"} parses the modified_on field in each input record a Date value. For "date" , we parse data based using JavaScripts Date.parse() . For Specific date formats can be provided (e.g., {foo: "date:'%m%d%Y'"} ), using the d3-time-format syntax . UTC date format parsing is supported similarly (e.g., {foo: "utc:'%m%d%Y'"} ). See more about UTC time |

### json
Loads a JavaScript Object Notation (JSON) file. Assumes row-oriented data, where each row is an object with named attributes. This is the default file format, and so will be used if no format property is provided. If specified, the `format` property should have a type property of `"json"`, and can also accept the following:
| Property | Type | Description |
| --- | --- | --- |
| property | String | The JSON property containing the desired data. This parameter can be used when the loaded JSON file may have surrounding structure or meta-data. For example "property": "values.features" is equivalent to retrieving json.values.features from the loaded JSON object. |

### csv
Load a comma-separated values (CSV) file. This format type does not support any additional properties.
### tsv
Load a tab-separated values (TSV) file. This format type does not support any additional properties.
### dsv
Load a delimited text file with a custom delimiter. This is a general version of CSV and TSV.
| Property | Type | Description |
| --- | --- | --- |
| delimiter | String | Required. The delimiter between records. The delimiter must be a single character (i.e., a single 16-bit code unit); so, ASCII delimiters are fine, but emoji delimiters are not. |

### topojson
Load a JavaScript Object Notation (JSON) file using the TopoJSON format. The input file must contain valid TopoJSON data. The TopoJSON input is then converted into a GeoJSON format. There are two mutually exclusive properties that can be used to specify the conversion process:
| Property | Type | Description |
| --- | --- | --- |
| feature | String | The name of the TopoJSON object set to convert to a GeoJSON feature collection. For example, in a map of the world, there may be an object set named "countries" . Using the feature property, we can extract this set and generate a GeoJSON feature object for each country. |
| mesh | String | The name of the TopoJSON object set to convert to mesh. Similar to the feature option, mesh extracts a named TopoJSON object set. Unlike the feature option, the corresponding geo data is returned as a single, unified mesh instance, not as individual GeoJSON features. Extracting a mesh is useful for more efficiently drawing borders or other geographic elements that you do not need to associate with specific regions such as individual countries, states or counties. |

## Data Generators
### Sequence Generator
The sequence generator creates a set of numeric values based on given start, stop, and (optional) step properties. By default, new objects with a single field named `data` are generated; use the `as` property to change the field name.
| Property | Type | Description |
| --- | --- | --- |
| start | Number | Required. The starting value of the sequence (inclusive). |
| stop | Number | Required. The ending value of the sequence (exclusive). |
| step | Number | The step value between sequence entries. Default value: 1 |
| as | String | The name of the generated sequence field. Default value: "data" |

For example, the following specification generates a domain of number values and then uses calculate transforms to draw a sine curve:

### Graticule Generator
A graticule is a grid formed by lines of latitude and longitude. The graticule generator creates a geographic grid (as GeoJSON (https://en.wikipedia.org/wiki/GeoJSON) data) to serve as a guiding element to include in maps. The graticule generator can be specified with either a boolean `true` value (indicating the default graticule) or a graticule property object:
| Property | Type | Description |
| --- | --- | --- |
| extent | Array | Sets both the major and minor extents to the same values. |
| extentMajor | Array | The major extent of the graticule as a two-element array of coordinates. |
| extentMinor | Array | The minor extent of the graticule as a two-element array of coordinates. |
| precision | Number | The precision of the graticule in degrees. Default value: 2.5 |
| step | Array | Sets both the major and minor step angles to the same values. |
| stepMajor | Array | The major step angles of the graticule. Default value: [90, 360] |
| stepMinor | Array | The minor step angles of the graticule. Default value: [10, 10] |

The following example generates a custom graticule and visualizes it using an orthographic projection:

### Sphere Generator
A GeoJSON (https://en.wikipedia.org/wiki/GeoJSON) sphere represents the full globe. The sphere generator injects a dataset whose contents are simply `[{"type": "Sphere"}]`. The resulting sphere can be used as a background layer within a map to represent the extent of the Earth. The sphere generator requires either a boolean `true` value or an empty object `{}` as its sole property.
The following example generates a layered base map containing a sphere (light blue fill) and a default graticule (black strokes):

## Datasets
Vega-Lite supports a top-level `datasets` property. This can be useful when the same data should be inlined in different places in the spec. Instead of setting values inline, specify datasets at the top level and then refer to the named (#named) datasource in the rest of the spec. `datasets` is a mapping from name to an inline (#inline) dataset.
```
    "datasets": {
      "somedata": [1,2,3]
    },
    "data": {
      "name": "somedata"
    }

```

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

## Configuration
Source: https://vega.github.io/vega-lite/docs/config.html

```
{
  ...,
  "config": {                // Configuration Object
    ...                      // - Top-level Configuration
    "axis"      : { ... },   // - Axis Configuration
    "header"    : { ... },   // - Header Configuration
    "legend"    : { ... },   // - Legend Configuration
    "mark"      : { ... },   // - Mark Configuration
    "style"     : { ... },   // - Style Configuration
    "range"     : { ... },   // - Scale Range Configuration
    "scale"     : { ... },   // - Scale Configuration
    "projection": { ... },   // - Projection Configuration
    "selection" : { ... },   // - Selection Configuration
    "title"     : { ... },   // - title Configuration
    "view"      : { ... }    // - View Configuration
    "concat"    : { ... }    // - Concat Configuration
    "facet"     : { ... }    // - Facet Configuration
    "repeat"    : { ... }    // - Repeat Configuration
    "locale"    : { ... }    // - Locale Configuration
    "aria"      : ...        // - Aria Configuration
  }
}

```

Vega-Lites `config` object lists configuration properties of a visualization for creating a consistent theme. (This `config` object in Vega-Lite is a superset of Vega config (https://vega.github.io/vega/docs/config/).)
The rest of this page outlines different types of config properties:
- Top-level Configuration (#top-level-config)
- Format Configuration (#format)
- Providing Custom Formatters (#custom-format-type)
- Customize Formatter for Tooltips only (#customize-formatter-for-tooltips-only)
- Guide Configurations (#axis-config)
- Axis Configurations (#axis-configurations)
- Header Configuration (#header-config)
- Legend Configuration (#legend-config)
- Built-in Guide Styles (#guide-config)
- Mark Configurations (#mark-config)
- Style Configuration (#style-configuration)
- Scale and Scale Range Configuration (#scale-config)
- Projection Configuration (#projection-config)
- Selection Configuration (#selection-config)
- Title Configuration (#title-config)
- View & View Composition Configuration (#view-config)
- Locale Configuration (#aria-config)
- ARIA Configuration (#aria-configuration)
## Top-level Configuration
A Vega-Lite `config` object can have the following top-level properties:
| Property | Type | Description |
| --- | --- | --- |
| autosize | String | AutoSizeParams | How the visualization size should be determined. If a string, should be one of "pad" , "fit" or "none" . Object values can additionally specify parameters for content sizing and automatic resizing. Default value : pad |
| background | Color | ExprRef | CSS color property to use as the background of the entire view. Default value: "white" |
| countTitle | String | Default axis and legend title for count fields. Default value: 'Count of Records . |
| fieldTitle | String | Defines how Vega-Lite generates title for fields. There are three possible styles: "verbal" (Default) - displays function in a verbal style (e.g., Sum of field, Year-month of date, field (binned)). "function" - displays function using parentheses and capitalized texts (e.g., SUM(field), YEARMONTH(date), BIN(field)). "plain" - displays only the field name without functions (e.g., field, date, field). |
| font | String | Default font for all text marks, titles, and labels. |
| lineBreak | String | ExprRef | A delimiter, such as a newline character, upon which to break text strings into multiple lines. This property provides a global default for text marks, which is overridden by mark or style config settings, and by the lineBreak mark encoding channel. If signal-valued, either string or regular expression (regexp) values are valid. |
| padding | Number | Object | ExprRef | The default visualization padding, in pixels, from the edge of the visualization canvas to the data rectangle. If a number, specifies padding for all sides. If an object, the value should have the format {"left": 5, "top": 5, "right": 5, "bottom": 5} to specify padding for each side of the visualization. Default value : 5 |
| tooltipFormat | FormatConfig | Define custom format configuration for tooltips. If unspecified, default format config will be applied. |

## Format Configuration
These config properties define the default number and time formats for text marks as well as axes, headers, tooltip, and legends:
| Property | Type | Description |
| --- | --- | --- |
| numberFormat | String | If numberFormatType is not specified, D3 number format for guide labels, text marks, and tooltips of non-normalized fields (fields without stack: "normalize" ). For example "s" for SI units. Use D3s number format pattern . If config.numberFormatType is specified and config.customFormatTypes is true , this value will be passed as format alongside datum.value to the config.numberFormatType function. |
| numberFormatType | String | Custom format type for config.numberFormat . Default value: undefined  This is equilvalent to call D3-format, which is exposed as format in Vega-Expression . Note: You must also set customFormatTypes to true to use this feature. |
| normalizedNumberFormat | String | If normalizedNumberFormatType is not specified, D3 number format for axis labels, text marks, and tooltips of normalized stacked fields (fields with stack: "normalize" ). For example "s" for SI units. Use D3s number format pattern . If config.normalizedNumberFormatType is specified and config.customFormatTypes is true , this value will be passed as format alongside datum.value to the config.numberFormatType function. Default value: % |
| normalizedNumberFormatType | String | Custom format type for config.normalizedNumberFormat . Default value: undefined  This is equilvalent to call D3-format, which is exposed as format in Vega-Expression . Note: You must also set customFormatTypes to true to use this feature. |
| timeFormat | String | Default time format for raw time values (without time units) in text marks, legend labels and header labels. Default value: "%b %d, %Y" Note: Axes automatically determine the format for each label automatically so this config does not affect axes. |
| timeFormatType | String | Custom format type for config.timeFormat . Default value: undefined  This is equilvalent to call D3-time-format, which is exposed as timeFormat in Vega-Expression . Note: You must also set customFormatTypes to true and there must not be a timeUnit defined to use this feature. |
| customFormatTypes | Boolean | Allow the formatType property for text marks and guides to accept a custom formatter function registered as a Vega expression . |

### Providing Custom Formatters
To customize how Vega-Lite formats numbers or text, you can register a custom formatter by
(1) Registering an expression function (https://vega.github.io/vega/docs/api/extensibility/#expressions) that takes a data point and an optional format property. For example, to register `customFormatA`, you need to register the function:
```
vega.expressionFunction('customFormatA', function(datum, params) {
  ...
  return "<formatted string>";
});

```

(2) Setting the `customFormatTypes` config to `true`.
```
{
  ...,
  "config": {"customFormatTypes": true}
}

```

(3) You can then use this custom format function with `format` and `formatType` properties in text encodings and guides (axis/legend/header).
```
{
  "format": <params>,
  "formatType": "customFormatA"
}

```

### Customize Formatter for Tooltips only
Since tooltips have more screen estate and less chance of collisions, sometimes it is desirable to have a truncated format in a visualization, with a longer format in the tooltip. For example, in the visualization below, we want the y-axis to have the format `d` so it does not have a decimal point, so as not to have incredibly long labels, but on the tooltip it has the longer `.8f`. To achieve this specificity, one can add a `tooltipFormat` prop to their config that conforms to the FormatConfig (#format) type.

## Guide Configurations
### Axis Configurations
Axis configurations define default settings for axes. Properties defined under the main `"axis"` object are applied to all axes. Additional property blocks can target more specific axis types based on the orientation (`"axisX"`, `"axisY"`, `"axisLeft"`, `"axisTop"`, etc.), band scale type (`"axisBand"`), scales data type (`"axisDiscrete"`, `"axisQuantitative"`, and `"axisTemporal"`), or both orientation and scale/data type (e.g., `"axisXTemporal"`). For example, properties defined under the `"axisBand"` property will only apply to axes visualizing `"band"` scales. If multiple axis config blocks apply to a single axis, type-based options take precedence over orientation-based options, which in turn take precedence over general options.
See more details in the axis documentation (axis.html#config).
| Property | Type | Description |
| --- | --- | --- |
| axis | AxisConfig | Axis configuration, which determines default properties for all x and y axes . For a full list of axis configuration options, please see the corresponding section of the axis documentation . |
| axisX | AxisConfig | X-axis specific config. |
| axisY | AxisConfig | Y-axis specific config. |
| axisLeft | AxisConfig | Config for y-axis along the left edge of the chart. |
| axisRight | AxisConfig | Config for y-axis along the right edge of the chart. |
| axisTop | AxisConfig | Config for x-axis along the top edge of the chart. |
| axisBottom | AxisConfig | Config for x-axis along the bottom edge of the chart. |
| axisBand | AxisConfig | Config for axes with band scales. |
| axisPoint | AxisConfig | Config for axes with point scales. |
| axisDiscrete | AxisConfig | Config for axes with point or band scales. |
| axisQuantitative | AxisConfig | Config for quantitative axes. |
| axisTemporal | AxisConfig | Config for temporal axes. |
| axisXBand | AxisConfig | Config for x-axes with band scales. |
| axisXPoint | AxisConfig | Config for x-axes with point scales. |
| axisXDiscrete | AxisConfig | Config for x-axes with point or band scales. |
| axisXQuantitative | AxisConfig | Config for x-quantitative axes. |
| axisXTemporal | AxisConfig | Config for x-temporal axes. |
| axisYBand | AxisConfig | Config for y-axes with band scales. |
| axisYPoint | AxisConfig | Config for y-axes with point scales. |
| axisYDiscrete | AxisConfig | Config for y-axes with point or band scales. |
| axisYQuantitative | AxisConfig | Config for y-quantitative axes. |
| axisYTemporal | AxisConfig | Config for y-temporal axes. |

### Header Configuration
| Property | Type | Description |
| --- | --- | --- |
| header | HeaderConfig | Header configuration, which determines default properties for all headers . For a full list of header configuration options, please see the corresponding section of in the header documentation . |

### Legend Configuration
| Property | Type | Description |
| --- | --- | --- |
| legend | LegendConfig | Legend configuration, which determines default properties for all legends . For a full list of legend configuration options, please see the corresponding section of in the legend documentation . |

### Built-in Guide Styles
In addition to axis, header, and legend styles, Vega-Lite also includes the following built-in styles that are shared across different kinds of guides:
- `"guide-label"`: style for axis, legend, and header labels
- `"guide-title"`: style for axis, legend, and header titles
- `"group-title"`: styles for chart titles
See the documentation about the style configuration (mark.html#style-config) for more information.
## Mark Configurations
The `mark` property of the `config` (config.html) object sets the default properties for all marks. In addition, the `config` object also provides mark-specific config using its mark type as the property name (e.g., `config.area`) for defining default properties for each mark.
| Property | Type | Description |
| --- | --- | --- |
| mark | MarkConfig | Mark Config |
| area | AreaConfig | Area-Specific Config |
| bar | BarConfig | Bar-Specific Config |
| circle | MarkConfig | Circle-Specific Config |
| line | LineConfig | Line-Specific Config |
| point | MarkConfig | Point-Specific Config |
| rect | RectConfig | Rect-Specific Config |
| geoshape | MarkConfig | Geoshape-Specific Config |
| rule | MarkConfig | Rule-Specific Config |
| square | MarkConfig | Square-Specific Config |
| text | MarkConfig | Text-Specific Config |
| tick | TickConfig | Tick-Specific Config |

## Style Configuration
In addition to the axis and mark config above, default values can be further customized using named styles defined under the `style` block. Styles can then be invoked by including a `style` property within a mark definition object (mark.html#mark-def) or an axis definition object (axis.html).
See the documentation about the mark style configuration (mark.html#style-config) for more information about how to use style configuration to customize mark style.
| Property | Type | Description |
| --- | --- | --- |
| style | Object | An object hash that defines key-value mappings to determine default properties for marks with a given style . The keys represent styles names; the values have to be valid mark configuration objects . |

## Scale and Scale Range Configuration
| Property | Type | Description |
| --- | --- | --- |
| scale | ScaleConfig | Scale configuration determines default properties for all scales . For a full list of scale configuration options, please see the corresponding section of the scale documentation . |
| range | RangeConfig | An object hash that defines default range arrays or schemes for using with scales. For a full list of scale range configuration options, please see the corresponding section of the scale documentation . |

## Projection Configuration
| Property | Type | Description |
| --- | --- | --- |
| projection | ProjectionConfig | Projection configuration, which determines default properties for all projections . For a full list of projection configuration options, please see the corresponding section of the projection documentation . |

## Selection Configuration
| Property | Type | Description |
| --- | --- | --- |
| selection | SelectionConfig | An object hash for defining default properties for each type of selections. |

## Title Configuration
| Property | Type | Description |
| --- | --- | --- |
| title | TitleConfig | Title configuration, which determines default properties for all titles . For a full list of title configuration options, please see the corresponding section of the title documentation . |

## View & View Composition Configuration
| Property | Type | Description |
| --- | --- | --- |
| view | ViewConfig | Default properties for single view plots . |
| concat | CompositionConfig | Default configuration for all concatenation and repeat view composition operators ( concat , hconcat , vconcat , and repeat ) |
| facet | CompositionConfig | Default configuration for the facet view composition operator |

Each of the view composition configurations (`concat` and `facet`) supports the following properties:
| Property | Type | Description |
| --- | --- | --- |
| columns | Number | The number of columns to include in the view composition layout. Default value : undefined  An infinite number of columns (a single row) will be assumed. This is equivalent to hconcat (for concat ) and to using the column channel (for facet and repeat ). Note : 1) This property is only for: the general (wrappable) concat operator (not hconcat / vconcat ) the facet and repeat operator with one field/repetition definition (without row/column nesting) 2) Setting the columns to 1 is equivalent to vconcat (for concat ) and to using the row channel (for facet and repeat ). |
| spacing | Number | The default spacing in pixels between composed sub-views. Default value : 20 |

Repeat uses the same configuration as concatenation.
## Locale Configuration
| Property | Type | Description |
| --- | --- | --- |
| locale | Locale | Locale definitions for string parsing and formatting of number and date values. The locale object should contain number and/or time properties with locale definitions . Locale definitions provided in the config block may be overridden by the View constructor locale option. |

## ARIA Configuration
| Property | Type | Description |
| --- | --- | --- |
| aria | Boolean | A boolean flag indicating if ARIA default attributes should be included for marks and guides (SVG output only). If false, the "aria-hidden" attribute will be set for all guides, removing them from the ARIA accessibility tree and Vega-Lite will not generate default descriptions for marks. Default value: true . |

## Modes for Handling Invalid Data
Source: https://vega.github.io/vega-lite/docs/invalid-data.html

This page discusses modes in Vega-Lite for handling invalid data (`null` and `NaN` in continuous scales).
The main configurations are `mark.invalid` (#mark) and `config.scale.invalid` (#scale). In addition, you can use other Vega-Lite features including conditional encodings, layering, or window transform to handle invalid and missing data (#other).
Note: Vega-Lite does not consider `null` and `NaN` in categorical scales and text encodings as invalid data:
- Categorical scales can treat nulls and NaNs as separate categories
- Similarly, text encodings can directly display nulls and NaNs.
## Documentation Overview
- Mark Invalid Mode (#mark-invalid-mode)
- Examples (#examples)
- `"filter"` (#filter)
- `"break-paths"` (#break-paths)
- `"break-paths-show-domains"` (#break-paths-show-domains)
- `"show"` (#show)
- `"break-paths-show-path-domains"` (Default) (#break-paths-show-path-domains-default)
- Scale Output for Invalid Values (#scale-output-for-invalid-values)
- Example: Output Color and Size with Filter Mode (#example-output-color-and-size-with-filter-mode)
- Example: Output Color with Show Mode (#example-output-color-with-show-mode)
- Other solutions (#other-solutions)
- Example: Conditional Encoding (#example-conditional-encoding)
- Example: Layering (#example-layering)
- Example: Using window transform to impute missing values (#example-using-window-transform-to-impute-missing-values)
## Mark Invalid Mode
You can use `mark.invalid` (or `config.mark.invalid`) to configure how marks and their corresponding scales handle invalid data (`null` and `NaN` in continuous scales).
| Property | Type | Description |
| --- | --- | --- |
| invalid | String | Null | Invalid data mode, which defines how the marks and corresponding scales should represent invalid values ( null and NaN in continuous scales without defined output for invalid values). "filter"  Exclude all invalid values from the visualizations marks and scales . For path marks (for line, area, trail), this option will create paths that connect valid points, as if the data rows with invalid values do not exist. "break-paths-filter-domains"  Break path marks (for line, area, trail) at invalid values. For non-path marks, this is equivalent to "filter" . All scale domains will exclude these filtered data points. "break-paths-show-domains"  Break paths (for line, area, trail) at invalid values. Hide invalid values for non-path marks. All scale domains will include these filtered data points (for both path and non-path marks). "show" or null  Show all data points in the marks and scale domains. Each scale will use the output for invalid values defined in config.scale.invalid or, if unspecified, by default invalid values will produce the same visual values as zero (if the scale includes zero) or the minimum value (if the scale does not include zero). "break-paths-show-path-domains" (default)  This is equivalent to "break-paths-show-domains" for path-based marks (line/area/trail) and "filter" for non-path marks. Note : If any channels scale has an output for invalid values defined in config.scale.invalid , all values for the scales will be considered valid since they can produce a reasonable output for the scales. Thus, fields for such channels will not be filtered and will not cause path breaks. |

### Examples
To understand how these modes affect common marks, see these examples below, which visualize this dataset:
```
[
  {"a": null, "b": 100},
  {"a": -10, "b": null},
  {"a": -5, "b": -25},
  {"a": -1, "b": -20},
  {"a": 0, "b": null},
  {"a": 1, "b": 30},
  {"a": 5, "b": 40},
  {"a": 10, "b": null}
]

```

by assigning `"a"` to x-axis (as quantitative and ordinal fields) and `"b"` to y-axis.
#### `"filter"`
The `"filter"` invalid mode excludes all invalid values from the visualizations marks and scales.
For path marks (for line, area, trail), this option will create paths that connect valid points, as if the points with invalid values do not exist.
#### `"break-paths"`
Break path marks (for line, area, trail) at invalid values. For non-path marks, this is equivalent to `"filter"`. All scale domains will exclude these filtered data points.
#### `"break-paths-show-domains"`
This option is like `"break-paths"`, except that all scale domains will instead include these filtered data points.
#### `"show"`
Include all data points in the marks and scale domains. Each scale will use the output for invalid values defined in `config.scale.invalid` or, if unspecified, by default invalid values will produce the same visual values as zero (if the scale includes zero) or the minimum value (if the scale does not include zero).
#### `"break-paths-show-path-domains"` (Default)
For historical reasons, Vega-Lite 5 currently uses `"break-paths-show-path-domains"` as the default invalid data mode (to avoid breaking changes). This is equivalent to `"break-path-keep-domains"` for path-based marks (line/area/trail) and `"filter"` for other marks.
## Scale Output for Invalid Values
You can use `config.scale.invalid` to defines scale outputs per channel for invalid values.
| Property | Type | Description |
| --- | --- | --- |
| invalid | ScaleInvalidDataConfig | An object that defines scale outputs per channel for invalid values (nulls and NaNs on a continuous scale). The keys in this object are the scale channels. The values is either "zero-or-min" (use zero if the scale includes zero or min value otherwise) or a value definition {value: ...} . Example: Setting this config.scale.invalid property to {color: {value: '#aaa'}} will make the visualization color all invalid values with #aaa. See https://vega.github.io/vega-lite/docs/invalid-data.html for more details. |

### Example: Output Color and Size with Filter Mode
A visualization with `"filter"` invalid data mode will not filter (not exclude) color and size encoding if `config.scale.invalid.color` and `config.scale.invalid.size` are specified.
Compare this with a similar spec, but without `config.scale.invalid`:
### Example: Output Color with Show Mode
As discussed earlier, by default invalid values will produce the same visual values as zero (if the scale includes zero) or the minimum value (if the scale does not include zero).
However, you may use `config.scale.invalid` to override the output for invalid data values:
## Other solutions
Note that `mark.invalid` and `config.scale.invalid` are options for handling invalid data without changing data or marks.
However, you may use other Vega-Lite features such as conditional encoding, layering, and window transforms to encode invalid data.
### Example: Conditional Encoding
If you do not use color encoding, you may use conditional color encoding to use a specific color (e.g., gray) to encode invalid values.
### Example: Layering
You may also use different marks (such as bars) to encode null data.
### Example: Using window transform to impute missing values

