# Interaction Params

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Dynamic Behaviors with Parameters
Source: https://vega.github.io/vega-lite/docs/parameter.html

```
// A Single View Specification
{
  ...,
  "params": [  // An array of named parameters.
    {"name": ..., ...}
  ],
  "mark": ...,
  "encoding": ...,
  ...
}

```

Parameters are the basic building block in Vega-Lites grammar of interaction. Parameters can either be simple variables or more complex selections that map user input (e.g., mouse clicks and drags) to data queries. Parameters can be used throughout the remainder of the chart specification to determine encoding rules, filter data points, determine data extents, or in expression strings. They can also optionally be bound to input widgets (e.g., sliders or drop down menus).
## Documentation Overview
- Defining a Parameter (#defining-a-parameter)
- Variable Parameters (#variable-parameters)
- Expression (#expr)
- Built-In Variable Parameters (#built-in-variable-parameters)
- Selection Parameters (#select)
- Using Parameters (#using-parameters)
- In Expression Strings (#in-expression-strings)
- As Predicates (#as-predicates)
- Data Extents (#data-extents)
- Selection Configuration (#config)
## Defining a Parameter
Both variable and selection parameters support the following properties:
| Property | Type | Description |
| --- | --- | --- |
| name | String | Required. A unique name for the variable parameter. Parameter names should be valid JavaScript identifiers: they should contain only alphanumeric characters (or $, or _) and may not start with a digit. Reserved keywords that may not be used as parameter names are datum, event, item, and parent. |
| value | Any | The initial value of the parameter. Default value: undefined |
| bind | Binding | Binds the parameter to an external input element such as a slider, selection list or radio button group. |

### Variable Parameters
Variables are the simplest form a parameter can take. Variable parameters allow for a value to be defined once and then reused throughout the rest of the specification. For example, here we define a `cornerRadius` parameter:
As the name suggests, variable values can be modified dynamically, either by binding the variable (bind.html) to input widgets (e.g., sliders or drop down menus), or by modifying the underlying signal in a Vega view API (https://vega.github.io/vega/docs/api/view/#signals). For example, here we include widgets to customize bar marks corner radius:
#### Expression
Besides setting the initial `value`, you can also create a parameter using an expression (`expr`).
| Property | Type | Description |
| --- | --- | --- |
| expr | Expr | An expression for the value of the parameter. This expression may include other parameters, in which case the parameter will automatically update in response to upstream parameter changes. |

For example, here we make the inner bars in a bullet chart depends on the chart height.
Note: Height is a built-in parameter, as described in the next section.
#### Built-In Variable Parameters
A few parameter names are automatically processed and/or reserved:
- Parameters for the specification `width`, `height`, `padding`, `autosize`, and `background` properties are automatically defined. Specifications may include definitions for these parameters in the top-level parameters array, in which case the definitions will be merged with any top-level specification property values, with precedence given to properties defined in the parameters array.
- The parameters names `datum`, `item`, `event`, `parent` are reserved for top-level variables within expressions. Specifications may not define parameters named `datum`, `item`, `event`, or `parent`.
- If you define a parameter named `cursor`, its value will automatically drive the CSS mouse cursor for the Vega-Lite view. For more details about `cursor` parameter, see the Vega documentation for the underlying `cursor` signal (https://vega.github.io/vega/docs/signals/#the-cursor-signal).
### Selection Parameters
Selection parameters, on the other hand, define data queries that are driven by direct manipulation user input (e.g., mouse clicks or drags). A parameter becomes a selection when the `select` property is specified. This property identifies properties of a selection including its type (`point` or `interval`), which determines the default events that trigger a selection and the resultant data query.
| Property | Type | Description |
| --- | --- | --- |
| select | String | PointSelection | IntervalSelection | Required. Determines the default event processing and data query for the selection. Vega-Lite currently supports two selection types: "point"  to select multiple discrete data values; the first value is selected on click and additional values toggled on shift-click. "interval"  to select a continuous range of data values on drag . |

For example, try the two types against the example selection (named `pts`) below: pointinterval.
While selection types provide useful defaults, you can set `select` to be a selection definition (selection.html) to override default selection behaviors and customize the interaction design. See the selection (selection.html) documentation for more information about the selection definition.
## Using Parameters
### In Expression Strings
Parameter names can be used directly in expression strings. For selection parameters, the parameter name references an object with properties corresponding to the data fields that participate in the selection (specified either by the `encodings` (#selection-props) or `fields` (#selection-props) property).
For instance, in the example below, the opacity of the point marks is driven by a bound (bind.html) variable parameter, and their size is determined by a clicked points `Miles_per_Gallon`.
### As Predicates
Predicates (predicate.html) are functions that return a boolean `true` or `false` value. While predicates can be explicitly written as expression strings (for example, `opacityVar == 25` or `sel.Miles_per_Gallon > 75`), it is often more convenient to treat a parameter as a predicate directly. When variable parameters are used as predicates, their values are coerced to booleans following JavaScripts conventions (https://www.w3schools.com/js/js_type_conversion.asp). For selection parameters, the predicate evaluates to `true` when the corresponding data point lies within the selection, and `false` otherwise.
For instance, in the example below, we use a variable parameter to toggle the color of points in the scatterplot and a selection parameter to resize points on hover. Notice: by default, empty selections are considered to contain all data values (and thus all points are large at the start, or when the mouse cursor moves into empty space). We can toggle this behavior by setting the optional `empty` property on the predicate: true (default)false.
See the `condition` (condition.html) documentation for more information.
As another example of using parameters as predicates, consider how we might use one view to filter the data shown in another view. Below, we show two scatterplots concatenated vertically. An interval selection (named `brush`) is defined in the first plot and is used to filter the points in the second. Thus, the `Acceleration x Displacement` scatterplot only visualizes points that fall within the brushed region.
### Data Extents
Selection parameters can additionally be used to define two types of data extents: binning logic or scale domains. Lets look at two examples of an interaction technique called overview+detail.
In the specification below, the bottom plot contains an interval selection named `brush`, which is used in the top plot to interactive re-bin data and zoom into the brushed region.
The specification below has a similar setup. However, in this case, the `brush` in the bottom view drives the `domain` of the top plots x-scale, to make it show only the selected interval.
An alternate way to construct either of these examples would be to first filter out the input data using the selection like so:
```
{
  "vconcat": [{
    "transform": [{"filter": {"param": "brush"}}],
    ...
  }]
}

```

However, setting the data extents (rather than filtering data out) yields superior interactive performance. Rather than testing whether each data value falls within the selection or not, the data extents (either the bin extents or scale domains) are changed directly to the brush extents.
If the selection is projected (selection.html#project) over multiple fields or encodings, one must be given as part of the data extent definition. Vega-Lite automatically infers this property if the selection is only projected over a single field or encoding. Thus, with the above example, the scale domain can be specified more explicitly as:
- `"scale": {"domain": {"param": "brush", "encoding": "x"}}` or
- `"scale": {"domain": {"param": "brush", "field": "date"}}`
Note: Bin extents can be explicitly specified using a similar syntax. For a selection to manipulate the scales of its own view, use the bind (bind.html#scale-binding) operator instead.
## Selection Configuration
```
// Top-level View Specification
{
  ...,
  "config": {          // Configuration Object
    "selection": { ... },   // - Selection Configuration
    ...
  }
}

```

The `selection` property of the `config` (config.html) object determines the default properties and transformations applied to the two types of selection parameters. The selection config can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| point | PointSelection | The default definition for a point selection. All properties and transformations for a point selection definition (except type ) may be specified here. For instance, setting point to {"on": "dblclick"} populates point selections on double-click by default. |
| interval | IntervalSelection | The default definition for an interval selection. All properties and transformations for an interval selection definition (except type ) may be specified here. For instance, setting interval to {"translate": false} disables the ability to move interval selections by default. |

## Initializing a Parameter
Source: https://vega.github.io/vega-lite/docs/param-value.html

Parameters can be initialized using the `value` property.
- For variable parameters, this `value` can be set to any valid JSON primitive type including booleans, numbers, or string.
- For selection parameters, `value` should specify mappings between projected channels or field names (project.html) to initial values.
- Point selections are initialized with an array of such mappings.
- Interval selections are initialized with a single object mapping to arrays of values.
## Examples
In the example below, we initalize the `"CylYr"` selection with two values by setting the values for the `"Cylinders"` and `"Years"` fields.
Similarly, we initialize the `"brush"` selection to the extent of the brush for the `x` and `y` encoding channels. The values specify the start and end of the interval selection.

## Selection Parameters
Source: https://vega.github.io/vega-lite/docs/selection.html

```
// A Single View Specification
{
  ...,
  "params": [  // An array of named parameters.
    {
      "name": ...,
      "select": { // Selection
        "type": ...,
        ...
      }
    }
  ],
  "mark": ...,
  "encoding": ...,
  ...
}

```

Selection parameters define data queries that are driven by direct manipulation user input (e.g., mouse clicks or drags). A parameter becomes a selection when the `select` property is specified. This page discusses different properties of a selection.
## Documentation Overview
- Common Selection Properties (#selection-props)
- `type` (#type)
- Selection Projection with `encodings` and `fields` (#project)
- Current Limitations (#current-limitations)
- `on` (#on)
- `clear` (#clear)
- `resolve` (#resolve)
- Point Selection Properties (#point)
- `toggle` (#toggle)
- Nearest (#nearest)
- Current Limitations (#current-limitations-1)
- Interval Selection Properties (#interval)
- `mark` (#mark)
- `translate` (#translate)
- `zoom` (#zoom)
## Common Selection Properties
For both selection types, the `select` object can take the following properties:
| Property | Type | Description |
| --- | --- | --- |
| type | String | Required. Determines the default event processing and data query for the selection. Vega-Lite currently supports two selection types: "point"  to select multiple discrete data values; the first value is selected on click and additional values toggled on shift-click. "interval"  to select a continuous range of data values on drag . |
| encodings | String[] | An array of encoding channels. The corresponding data field values must match for a data tuple to fall within the selection. See also: The projection with encodings and fields section in the documentation. |
| fields | String[] | An array of field names whose values must match for a data tuple to fall within the selection. See also: The projection with encodings and fields section in the documentation. |
| on | VegaEventStream | String | A Vega event stream (object or selector) that triggers the selection. For interval selections, the event stream must specify a start and end . See also: on examples in the documentation. |
| clear | VegaEventStream | String | Boolean | Clears the selection, emptying it of all values. This property can be a Event Stream or false to disable clear. Default value: dblclick . See also: clear examples in the documentation. |
| resolve | String | With layered and multi-view displays, a strategy that determines how selections data queries are resolved when applied in a filter transform, conditional encoding rule, or scale domain. One of: "global"  only one brush exists for the entire SPLOM. When the user begins to drag, any previous brushes are cleared, and a new one is constructed. "union"  each cell contains its own brush, and points are highlighted if they lie within any of these individual brushes. "intersect"  each cell contains its own brush, and points are highlighted only if they fall within all of these individual brushes. Default value: global . See also: resolve examples in the documentation. |

### `type`
A selections type (parameter.html#select) determines which data values fall within it by default:
- For `point` selections, only values that have been directly interacted with (e.g., those that have been clicked on) are considered to be selected.
- For `interval` selections, values that fall within both the horizontal (`x`) and vertical (`y`) extents are considered to be selected.
### Selection Projection with `encodings` and `fields`
In the scatterplot example below, highlight multiplea single: Cylinder(s) Origin(s).
With interval selections, we can use the projection to restrict the region to just the horizontal (`x`) and/or vertical (`y`) dimensions.
#### Current Limitations
- Selections projected over aggregated `fields`/`encodings` can only be used within the same view they are defined in.
- Interval selections can only be projected using `encodings`.
- Interval selections projected over binned or `timeUnit` fields remain continuous selections. Thus, if the visual encoding discretizes them, conditional encodings will no longer work. Instead, use a layered view as shown in the example below. The bar mark discretizes the binned `Acceleration` field. As a result, to highlight selected bars, we use a second layered view rather than a conditional color encoding within the same view.
### `on`
The `on` property modifies the event that triggers the selection.
For instance, a single rectangle in the heatmap below can now be selected on mouse hover instead.
### `clear`
The `clear` property identifies which events must fire to empty a selection of all selected values (the `empty` (selection.html#selection-properties) property can be used to further determine the behavior of empty selections).
The following visualization demonstrates the default clearing behavior: select a square on click and clear out the selection on double click.
The following example clears the brush when the mouse button is released.
Note, in the above example, clearing out the selection does not reset it to its initial value. Instead, when the mouse button is released, the selection is emptied of all values. This behavior is subtly different to when the selection is bound to scales (bind.html#scale-binding)  clearing the selection out now resets the view to use the initial scale domains. Try it out below: pan and zoom the plot, and then double click.
### `resolve`
When a selection is defined within a data-driven view (i.e., a view that is part of a facet (facet.html) or repeat (repeat.html)), the desired behaviour can be ambiguous. Consider the scatterplot matrix (SPLOM) example below, which has an interval selection named `brush`. Should there be only one brush across all cells, or should each cell have its own brush? In the latter case, how should points be highlighted in all the other cells?
The aptly named `resolve` property addresses this ambiguity, and can be set to one of the following values (click to apply it to the SPLOM example, and drag out an interval in different cells):
-
`global` (javascript:changeSpec('selection_resolution', 'selection_resolution_global')) (default)  only one brush exists for the entire SPLOM. When the user begins to drag, any previous brushes are cleared, and a new one is constructed.
-
`union` (javascript:changeSpec('selection_resolution', 'selection_resolution_union'))  each cell contains its own brush, and points are highlighted if they lie within any of these individual brushes.
-
`intersect` (javascript:changeSpec('selection_resolution', 'selection_resolution_intersect'))  each cell contains its own brush, and points are highlighted only if they fall within all of these individual brushes.
## Point Selection Properties
In addition to all common selection properties (#selection-props), point selections support the following properties:
| Property | Type | Description |
| --- | --- | --- |
| toggle | String | Boolean | Controls whether data values should be toggled (inserted or removed from a point selection) or only ever inserted into point selections. One of: true  the default behavior, which corresponds to "event.shiftKey" . As a result, data values are toggled when the user interacts with the shift-key pressed. false  disables toggling behaviour; the selection will only ever contain a single data value corresponding to the most recent interaction. A Vega expression which is re-evaluated as the user interacts. If the expression evaluates to true , the data value is toggled into or out of the point selection. If the expression evaluates to false , the point selection is first cleared, and the data value is then inserted. For example, setting the value to the Vega expression "true" will toggle data values without the user pressing the shift-key. Default value: true See also: toggle examples in the documentation. |
| nearest | Boolean | When true, an invisible voronoi diagram is computed to accelerate discrete selection. The data value nearest the mouse cursor is added to the selection. Default value: false , which means that data values must be interacted with directly (e.g., clicked on) to be added to the selection. See also: nearest examples documentation. |

### `toggle`
The `toggle` property customizes how user interaction can insert or remove data values from a point selection if they are or are not already members of the selection, respectively.
For example, you can highlight points in the scatterplot below by toggling them into the `paintbrush` selection when clicking with:
 `event.shiftKey` `event.altKey`.
### Nearest
The `nearest` propery accelerates user selection with an invisible voronoi diagram.
For example, in the scatterplot below, points nearestdirectly underneath the mouse cursor are highlighted as it moves.
The `nearest` transform also respects any position encoding projections (project.html) applied to the selection. For instance, in the example below, moving the mouse cursor back-and-forth snaps the vertical rule and label to the nearest `date` value.
#### Current Limitations
- The `nearest` property is not supported for multi-element mark types (i.e., `line` and `area`). For these mark types, consider layering a discrete mark type (e.g., `point`) with a 0-value `opacity` as in the last example above.
## Interval Selection Properties
In addition to all common selection properties (#selection-props), interval selections support the following properties:
| Property | Type | Description |
| --- | --- | --- |
| mark | Mark | An interval selection also adds a rectangle mark to depict the extents of the interval. The mark property can be used to customize the appearance of the mark. See also: mark examples in the documentation. |
| translate | String | Boolean | When truthy, allows a user to interactively move an interval selection back-and-forth. Can be true , false (to disable panning), or a Vega event stream definition which must include a start and end event to trigger continuous panning. Discrete panning (e.g., pressing the left/right arrow keys) will be supported in future versions. Default value: true , which corresponds to [pointerdown, window:pointerup] > window:pointermove! . This default allows users to clicks and drags within an interval selection to reposition it. See also: translate examples in the documentation. |
| zoom | String | Boolean | When truthy, allows a user to interactively resize an interval selection. Can be true , false (to disable zooming), or a Vega event stream definition . Currently, only wheel events are supported, but custom event streams can still be used to specify filters, debouncing, and throttling. Future versions will expand the set of events that can trigger this transformation. Default value: true , which corresponds to wheel! . This default allows users to use the mouse wheel to resize an interval selection. See also: zoom examples in the documentation. |

### `mark`
Every interval selection also adds a rectangle mark to the visualization, to depict the extents of the selected region.
The selections `mark` property can include the folloiwing properties to customize the appearance of this rectangle mark.
| Property | Type | Description |
| --- | --- | --- |
| cursor | String | The mouse cursor used over the interval mark. Any valid CSS cursor type can be used. |
| fill | Color | The fill color of the interval mark. Default value: "#333333" |
| fillOpacity | Number | The fill opacity of the interval mark (a value between 0 and 1 ). Default value: 0.125 |
| stroke | Color | The stroke color of the interval mark. Default value: "#ffffff" |
| strokeOpacity | Number | The stroke opacity of the interval mark (a value between 0 and 1 ). |
| strokeWidth | Number | The stroke width of the interval mark. |
| strokeDash | Number[] | An array of alternating stroke and space lengths, for creating dashed or dotted lines. |
| strokeDashOffset | Number | The offset (in pixels) with which to begin drawing the stroke dash array. |

For example, the spec below imagines two users, Alex and Morgan, who can each drag out an interval selection. To prevent collision between the two selections, Morgan must press the shift key while dragging out their interval (while Alex must not). Morgans interval is depicted with the default grey rectangle, and Morgans with a customized red rectangle.
### `translate`
The `translate` property allows a user to interactively move an interval selection back-and-forth.
For example, try to pan the brushscatterplot on dragshift-drag.
### `zoom`
The `zoom` property allows a user to interactively resize an interval selection.
For example, you can zoom the brushscatterplot on wheelshift-wheel.

## Binding a Parameter
Source: https://vega.github.io/vega-lite/docs/bind.html

Using the `bind` property, parameters can be bound in the following ways:
- Variable parameters and point selections can be bound to input elements (#input-element-binding).
- Point selections can also be bound to legends (#legend-binding).
- Interval selections can be bound to their own views scales (#scale-binding) to enable panning & zooming.
## Input Element Binding
For variable parameters and point selections, the `bind` property can follow the form of Vegas input element binding definition (https://vega.github.io/vega/docs/signals/#bind). Doing so generates an input element (per projected channel or field (selection.html#project) for selections) which can be used to interactively set the parameter value.
For example, in the specification below, we use a variety of variable parameters to interactively manipulate the `rect` mark.
Similarly, in the example below, the `org` selections selects a single `Origin` data value, and is bound to a dropdown menu with three options to choose from.
If multiple projections are specified, customized bindings can be specified by mapping the projected field/encoding to a binding definition. For example, the scatterplot below projects over both the `Cylinders` and `Year` fields, and uses a customize `range` slider for each one.
Note: When point selections are bound to input widgets, direct manipulation interaction (e.g., clicking or double clicking the visualization) is disabled by default. Such interaction can be re-enabled by explicitly specifying the `on` (selection.html#selection-props) and `clear` (clear.html) properties.
## Legend Binding
When a point selection is projected (project.html) over only one field or encoding channel, the `bind` property can be set to `"legend"` to populate the selection by interacting with the corresponding legend.
To customize the events that trigger legend interaction, expand the `bind` property to an object, with a single `legend` property that maps to a Vega event stream (https://vega.github.io/vega/docs/event-streams/).
Note: When a selection is bound to legends, direct manipulation interaction (e.g., clicking or double clicking the visualization) is disabled by default. Such interaction can be re-enabled by explicitly specifying the `on` (selection.html#selection-props) and `clear` (clear.html) properties.
Limitations: Currently, only binding to symbol legends (/vega-lite/docs/legend.html#legend-types) are supported.
## Scale Binding
With interval selections, the `bind` property can be set to the value `"scales"` to enable a two-way binding between the selection and the scales used within the same view. This binding first populates the interval selection with the scale domains, and then uses the selection to drive the scale domains. As a result, the view now functions like an interval selection and can be panned (translate.html) and zoomed (zoom.html).
In multi-view displays, binding shared scales will keep the views synchronized. For example, below we explicitly share the `x` scale between the two vertically concatenated views. Panning/zooming the bound interval selection in the first view also updates the second view.
A similar setup can be used to pan and zoom the cells of a scatterplot matrix:

## Predicate
Source: https://vega.github.io/vega-lite/docs/predicate.html

To test a data point in a filter transform (filter.html) or a `test` property in conditional encoding (/vega-lite/docs/condition.html), a predicate definition of the following forms must be specified:
-
a Vega expression (/vega-lite/docs/types.html#expression) string, where `datum` can be used to refer to the current data object. For example, `datum.b2 > 60` would test if the value in the field `b2` for each data point is over 60.
-
one of the field predicates (#field-predicate): `equal` (#field-equal-predicate), `lt` (#lt-predicate), `lte` (#lte-predicate), `gt` (#gt-predicate), `gte` (#gte-predicate), `range` (#range-predicate), `oneOf` (#one-of-predicate), or `valid` (#valid-predicate),
-
a parameter predicate (#parameter-predicate), which defines the names of a selection that the data point should belong to (or a logical composition of selections).
-
a logical composition (#composition) of (1), (2), or (3).
## Field Predicate
Test if a field in the data point satisfies certain conditions.
For a field predicate, a `field` must be provided along with one of the predicate properties: `equal` (#equal-predicate), `lt` (#lt-predicate) (less than), `lte` (#lte-predicate) (less than or equal), `gt` (#gt-predicate) (greater than), `gte` (#gte-predicate)(greater than or equal), `range` (#range-predicate), or `oneOf` (#one-of-predicate). Values of these operators can be primitive types (string, number, boolean) or a DateTime definition object (types.html#datetime) to describe time. In addition, `timeUnit` can be provided to further transform a temporal `field`.
| Property | Type | Description |
| --- | --- | --- |
| field | String | Required. Field to be tested. |
| timeUnit | TimeUnit | String | TimeUnitParams | Time unit for the field to be tested. |

### Field Equal Predicate
| Property | Type | Description |
| --- | --- | --- |
| equal | String | Number | Boolean | DateTime | ExprRef | Required. The value that the field should be equal to. |

For example, to check if the `car_color` fields value is equal to `"red"`, we can use the following predicate:
```
{"field": "car_color", "equal": "red"}

```

### Field Less Than Predicate
| Property | Type | Description |
| --- | --- | --- |
| lt | String | Number | DateTime | ExprRef | Required. The value that the field should be less than. |

For example, to check if the `height` fields value is less than `180`, we can use the following predicate:
```
{"field": "height", "lt": 180}

```

### Field Less Than or Equals Predicate
| Property | Type | Description |
| --- | --- | --- |
| lte | String | Number | DateTime | ExprRef | Required. The value that the field should be less than or equals to. |

For example, to check if the `Year` fields value is less than or equals to `"2000"`, we can use the following predicate:
```
{"timeUnit": "year", "field": "Year", "lte": "2000"}

```

### Field Greater Than Predicate
| Property | Type | Description |
| --- | --- | --- |
| gt | String | Number | DateTime | ExprRef | Required. The value that the field should be greater than. |

To check if the `state` fields value is greater than `"Arizona"` by string comparison, we can use the following predicate: (Note: Standard Javascript string comparison is done, ie., A < B, but B < a)
```
{"field": "state", "gt": "Arizona"}

```

### Field Greater Than or Equals Predicate
| Property | Type | Description |
| --- | --- | --- |
| gte | String | Number | DateTime | ExprRef | Required. The value that the field should be greater than or equals to. |

For example, to check if the `height` fields value is greater than or equals to `0`, we can use the following predicate:
```
{"field": "height", "gte": 0}

```

### Field Range Predicate
| Property | Type | Description |
| --- | --- | --- |
| range | Number[] | DateTime [] | Null[] | ExprRef [] | ExprRef | Required. An array of inclusive minimum and maximum values for a field value of a data item to be included in the filtered data. |

Examples
- `{"field": "x", "range": [0, 5]}}` checks if the `x` fields value is in range [0,5] (0  x  5)
- `{"timeUnit": "year", "field": "date", "range": [2006, 2008] }}` checks if the `date`s value is between year 2006 and 2008
- `{"field": "date", "range": [{"year": 2006, "month": "jan", "date": 1}, {"year": 2008, "month": "feb", "date": 20}] }}` checks if the `date`svalue is between Jan 1, 2006 and Feb 20, 2008.
### Field One-Of Predicate
| Property | Type | Description |
| --- | --- | --- |
| oneOf | String[] | Number[] | Boolean[] | DateTime [] | Required. A set of values that the field s value should be a member of, for a data item included in the filtered data. |

For example, `{"field": "car_color", "oneOf": ["red", "yellow"]}}` checks if the `car_color` fields value is `"red"` or `"yellow"`
### Field Valid Predicate
| Property | Type | Description |
| --- | --- | --- |
| valid | Boolean | Required. If set to true the fields value has to be valid, meaning both not null and not NaN . |

For example, `{"field": "car_color", "valid": true}}` checks if the `car_color` fields value is valid meaning it is both not `null` and not`NaN` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN).
## Parameter Predicate
For a parameter predicate, a `param` name must be provided.
| Property | Type | Description |
| --- | --- | --- |
| param | String | Required. Filter using a parameter name. |
| empty | Boolean | For selection parameters, the predicate of empty selections returns true by default. Override this behavior, by setting this property empty: false . |

For example, with `{"param": "brush"}`, only data values that fall within the selection named `brush` will remain in the dataset as shown below. Notice, by default, empty selections are considered to contain all data values (and thus, the bottom view begins as fully populated). We can toggle this behavior by setting the optional `empty` property on the predicate: true (default)false.
When you use a selection filter to dynamically filter the data, scale domains may change, which can lead to jumping titles. To prevent this, you can fix the `minExtent` of the axis whose scale domain changes. For example, to set the minimum extent to `30`, add `{"axis": {"minExtent": 30}}` to the corresponding encoding.
## Predicate Composition
We can also use the logical composition operators (`and`, `or`, `not`) to combine predicates.
Examples
- `{"and": [{"field": "height", "gt": 0}, {"field": "height", "lt": 180}]}` checks if the field `"height"` is between 0 and 180.
- `{"not": {"field": "x", "range": [0, 5]}}}` checks if the `x` fields value is not in range [0,5] (0  x  5).

