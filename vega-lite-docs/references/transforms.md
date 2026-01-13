# Transforms

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Transformation
Source: https://vega.github.io/vega-lite/docs/transform.html

Data transformations in Vega-Lite are described via either view-level (spec.html#common) transforms (the `transform` property) or field transforms inside `encoding` (encoding.html#field-transform) (`bin`, `timeUnit`, `aggregate`, `sort`, and `stack`).
When both types of transforms are specified, the view-level `transform`s are executed first based on the order in the array. Then the inline transforms are executed in this order: `bin`, `timeUnit`, `aggregate`, `sort`, and `stack`.
## View-level Transform Property
```
{
  "data": ... ,
  "transform": [
     ...
  ],
  "mark": ... ,
  "encoding": ... ,
  ...
}

```

The View-level `transform` object is an array of objects describing transformations. The transformations are executed in the order in which they are specified in the array. Vega-Lites `transform` supports the following types of transformations:
- Aggregate (aggregate.html#transform)
- Bin (bin.html#transform)
- Calculate (calculate.html)
- Density (density.html)
- Extent (extent.html)
- Filter (filter.html)
- Flatten (flatten.html)
- Fold (fold.html)
- Impute (impute.html)
- Join Aggregate (joinaggregate.html)
- Lookup (lookup.html)
- Pivot (pivot.html)
- Quantile (quantile.html)
- Regression (regression.html) and Loess Regression (loess.html)
- Sample (sample.html)
- Stack (stack.html)
- Time Unit (timeunit.html#transform)
- Window (window.html)

## Calculate Transform
Source: https://vega.github.io/vega-lite/docs/calculate.html

The formula transform extends data objects with new fields (columns) according to an expression (types.html#expression).
```
// Any View Specification
{
  ...
  "transform": [
    {"calculate": ..., "as" ...} // Calculate Transform
     ...
  ],
  ...
}

```

## Calculate Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| calculate | String | Required. A expression string. Use the variable datum to refer to the current data object. |
| as | String | Required. The field for storing the computed formula value. |

## Example
This example uses `calculate` to derive a new field, and then `filter`s the data based on the new field.

## Filter Transform
Source: https://vega.github.io/vega-lite/docs/filter.html

The filter transform removes objects from a data stream based on a provided filter expression or filter object.
```
// Any View Specification
{
  ...
  "transform": [
    {"filter": ...} // Filter Transform
     ...
  ],
  ...
}

```

Vega-Lite filter transforms must have the `filter` property describing the predicate for the filtering condition.
| Property | Type | Description |
| --- | --- | --- |
| filter | Predicate | Required. The filter property must be a predication definition, which can take one of the following forms: 1) an expression string, where datum can be used to refer to the current data object. For example, {filter: "datum.b2 > 60"} would make the output data includes only items that have values in the field b2 over 60. 2) one of the field predicates : equal , lt , lte , gt , gte , range , oneOf , or valid , 3) a selection predicate , which define the names of a selection that the data point should belong to (or a logical composition of selections). 4) a logical composition of (1), (2), or (3). |

## Aggregation
Source: https://vega.github.io/vega-lite/docs/aggregate.html

To aggregate data in Vega-Lite, users can either use the `aggregate` property of an encoding field definition (#encoding) or the `aggregate` transform inside the `transform` (#transform) array. Aggregate summarizes a table as one record for each group. To preserve the original table structure and instead add a new column with the aggregate values, use the join aggregate (joinaggregate.html) transform.
## Documentation Overview
- Aggregate in Encoding Field Definition (#encoding)
- Aggregate Transform (#transform)
- Aggregated Field Definition for Aggregate Transform (#aggregate-op-def)
- Supported Aggregation Operations (#ops)
- Argmin / Argmax (#argmax)
- Example: Labeling Line Chart (#example-labeling-line-chart)
## Aggregate in Encoding Field Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "aggregate": ..., // aggregate
      "field": ...,
      "type": "quantitative",
      ...
    },
    "y": ...,
    ...
  },
  ...
}

```

The `aggregate` property of a field definition (encoding.html#field-def) can be used to compute aggregate summary statistics (e.g., median, min, max) over groups of data.
If at least one fields in the specified encoding channels contain `aggregate`, the resulting visualization will show aggregate data. In this case, all fields without aggregation function specified are treated as group-by fields1 in the aggregation process.
For example, the following bar chart aggregates mean of `Acceleration`, grouped by the number of `Cylinders`.
Note: aggregated fields are quantitative by default while unaggregated (group by) fields in aggregated encodings are nominal by default.
The `detail` channel can be used to specify additional summary and group-by fields without mapping the field(s) to any visual properties. For example, the following plots add `Origin` as a group by field.
1The group-by fields are also known as independent/condition variables (https://en.wikipedia.org/wiki/Dependent_and_independent_variables) in statistics and dimensions (https://en.wikipedia.org/wiki/Dimension_(data_warehouse)) in Business Intelligence. Similarly, the aggregate fields are known as dependent variables (https://en.wikipedia.org/wiki/Dependent_and_independent_variables) and measures (https://en.wikipedia.org/wiki/Measure_(data_warehouse)).
## Aggregate Transform
```
// Any View Specification
{
  ...
  "transform": [
    {
      // Aggregate Transform
      "aggregate": [{"op": ..., "field": ..., "as": ...}],
      "groupby": [...]
    }
     ...
  ],
  ...
}

```

For example, here is the same bar chart which aggregates mean of Acceleration, grouped by the number of Cylinders, but this time using the `aggregate` property as part of the `transform`.
An `aggregate` transform in the `transform` (transform.html) array has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| aggregate | AggregatedFieldDef [] | Required. Array of objects that define fields to aggregate. |
| groupby | String[] | The data fields to group by. If not specified, a single group containing all data objects will be used. |

### Aggregated Field Definition for Aggregate Transform
| Property | Type | Description |
| --- | --- | --- |
| op | String | Required. The aggregation operation to apply to the fields (e.g., "sum" , "average" , or "count" ). See the full list of supported aggregation operations for more information. |
| field | String | The data field for which to compute aggregate function. This is required for all aggregation operations except "count" . |
| as | String | Required. The output field names to use for each aggregated field. |

Note: It is important you `parse` (data.html#format) your data types explicitly, especially if you are likely to have `null` values in your dataset and automatic type inference will fail.
## Supported Aggregation Operations
The supported aggregation operations are:
| Operation | Description |
| --- | --- |
| count | The total count of data objects in the group. Note: count operates directly on the input objects and return the same value regardless of the provided field. |
| valid | The count of field values that are not null , undefined or NaN . |
| values | A list of data objects in the group. |
| missing | The count of null or undefined field values. |
| distinct | The count of distinct field values. |
| sum | The sum of field values. |
| product | The product of field values. |
| mean | The mean (average) field value. |
| average | The mean (average) field value. Identical to mean . |
| variance | The sample variance of field values. |
| variancep | The population variance of field values. |
| stdev | The sample standard deviation of field values. |
| stdevp | The population standard deviation of field values. |
| stderr | The standard error of field values. |
| median | The median field value. |
| q1 | The lower quartile boundary of field values. |
| q3 | The upper quartile boundary of field values. |
| ci0 | The lower boundary of the bootstrapped 95% confidence interval of the mean field value. |
| ci1 | The upper boundary of the bootstrapped 95% confidence interval of the mean field value. |
| min | The minimum field value. |
| max | The maximum field value. |
| argmin | An input data object containing the minimum field value. Note: When used inside encoding, argmin must be specified as an object. (See below for an example.) |
| argmax | An input data object containing the maximum field value. Note: When used inside encoding, argmax must be specified as an object. (See below for an example.) |

## Argmin / Argmax
Sometimes, you may not want to find the minimum or maximum of a field, but instead the value from a field that corresponds to the minimum or maximum value in another field. In these cases you can use the argmin and argmax aggregates.
The argmax and argmin operation can be specified in an encoding field definition by setting `aggregate` to an object with `argmax/min` describing the field to maximize/minimize. For example, the following plot shows the production budget of the movie that has the highest US Gross in each major genre.
This is equivalent to specifying argmax in an aggregate transform and encode its nested data.
### Example: Labeling Line Chart
`argmax` can be useful for getting the last value in a line for label placement.

## Join Aggregate
Source: https://vega.github.io/vega-lite/docs/joinaggregate.html

The joinaggregate transform extends the input data objects with aggregate values in a new field. Aggregation is performed and the results are then joined with the input data. This transform can be helpful for creating derived values that combine both raw data and aggregate calculations, such as percentages of group totals. This transform is a special case of the window (window.html) transform where the `frame` is always `[null, null]`. Compared with the regular aggregate (aggregate.html) transform, joinaggregate preserves the original table structure and augments records with aggregate values rather than summarizing the data in one record for each group.
## Documentation Overview
- Join Aggregate Field Definition (#join-aggregate-field-definition)
- Join Aggregate Transform Definition (#join-aggregate-transform-definition)
- Join Aggregate Transform Field Definition (#field-def)
- Examples (#ops)
- Percent of Total (#percent-of-total)
- Difference from Mean (#difference-from-mean)
- Text Color with Contrast (#text-color-with-contrast)
## Join Aggregate Field Definition
```
// Any View Specification
{
  ...
  "transform": [
    {
      // Join Aggregate Transform
      "joinaggregate": [{
          "op": ...,
          "field": ...,
          "as": ...
      }],
      "groupby": [
        "..."
      ]
    }
     ...
  ],
  ...
}

```

## Join Aggregate Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| joinaggregate | JoinAggregateFieldDef[] | Required. The definition of the fields in the join aggregate, and what calculations to use. |
| groupby | String[] | The data fields for partitioning the data objects into separate groups. If unspecified, all data points will be in a single group. |

### Join Aggregate Transform Field Definition
| Property | Type | Description |
| --- | --- | --- |
| op | String | Required. The aggregation operation to apply (e.g., "sum" , "average" or "count" ). See the list of all supported operations here . |
| field | String | The data field for which to compute the aggregate function. This can be omitted for functions that do not operate over a field such as "count" . |
| as | String | Required. The output name for the join aggregate operation. |

## Examples
Below are some common use cases for the join aggregate transform.
### Percent of Total
Here we use the join aggregate transform to derive the global sum so that we can calculate percentage.
### Difference from Mean
One example is to show the exemplar movies from a movie collection. Here exemplar is defined by having a score of 2.5 points higher than the global average.
Another example is to show the exemplar movies based on the release year average. Here exemplar is defined by having a score 2.5 points higher than the annual average for its release year (instead of the global average).
Rather than filtering the above two examples we can also calculate a residual by deriving the mean using the join aggregate transform first.
### Text Color with Contrast
Here, we layer text on a table heatmap. The text is black or white depending on the values of `num_cars`. One issue with this specification is that we have to know the range of `num_cars` ahead of time to determine a suitable threshold (e.g. `40`).
We can use a joinaggregate with a calculate to determine the threshold dynamically.

## Window
Source: https://vega.github.io/vega-lite/docs/window.html

The window transform performs calculations over sorted groups of data objects. These calculations including ranking, lead/lag analysis, and aggregates such as running sums and averages. Calculated values are written back to the input data stream. If you only want to set the same aggregated value in a new field, you can use the simpler join aggregate (joinaggregate.html) transform.
## Documentation Overview
- Window Field Definition (#window-field-definition)
- Window Transform Definition (#window-transform-definition)
- Window Transform Field Definition (#field-def)
- Sort Field Definition (#sort-field-def)
- Window Only Operation Reference (#ops)
- Examples (#examples)
- Cumulative Frequency Distribution (#cumulative-frequency-distribution)
- Rank Chart (#rank-chart)
- Top K (#top-k)
- Cumulative Running Average (#cumulative-running-average)
- Percent of Total (#percent-of-total)
- Using window transform to impute missing values (#using-window-transform-to-impute-missing-values)
## Window Field Definition
```
// Any View Specification
{
  ...
  "transform": [
    {
      // Window Transform
      "window": [{
          "op": ...,
          "field": ...,
          "param": ...,
          "as": ...
      }],
      "sort": [
        {"field": ..., "order": ...}
      ],
      "ignorePeers": ...,
      "groupby": [
        "..."
      ],
      "frame": [...,...]
    }
     ...
  ],
  ...
}

```

## Window Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| window | WindowFieldDef [] | Required. The definition of the fields in the window, and what calculations to use. |
| frame | (Null | Number)[] | A frame specification as a two-element array indicating how the sliding window should proceed. The array entries should either be a number indicating the offset from the current data object, or null to indicate unbounded rows preceding or following the current data object. The default value is [null, 0] , indicating that the sliding window includes the current object and all preceding objects. The value [-5, 5] indicates that the window should include five objects preceding and five objects following the current object. Finally, [null, null] indicates that the window frame should always include all data objects. If you this frame and want to assign the same value to add objects, you can use the simpler join aggregate transform . The only operators affected are the aggregation operations and the first_value , last_value , and nth_value window operations. The other window operations are not affected by this. Default value: : [null, 0] (includes the current object and all preceding objects) |
| ignorePeers | Boolean | Indicates if the sliding window frame should ignore peer values (data that are considered identical by the sort criteria). The default is false, causing the window frame to expand to include all peer values. If set to true, the window frame will be defined by offset values only. This setting only affects those operations that depend on the window frame, namely aggregation operations and the first_value, last_value, and nth_value window operations. Default value: false |
| groupby | String[] | The data fields for partitioning the data objects into separate windows. If unspecified, all data points will be in a single window. |
| sort | SortField [] | A sort field definition for sorting data objects within a window. If two data objects are considered equal by the comparator, they are considered peer values of equal rank. If sort is not specified, the order is undefined: data objects are processed in the order they are observed and none are considered peers (the ignorePeers parameter is ignored and treated as if set to true ). |

### Window Transform Field Definition
| Property | Type | Description |
| --- | --- | --- |
| op | String | String | Required. The window or aggregation operation to apply within a window (e.g., "rank" , "lead" , "sum" , "average" or "count" ). See the list of all supported operations here . |
| param | Number | Parameter values for the window functions. Parameter values can be omitted for operations that do not accept a parameter. See the list of all supported operations and their parameters here . |
| field | String | The data field for which to compute the aggregate or window function. This can be omitted for window functions that do not operate over a field such as "count" , "rank" , "dense_rank" . |
| as | String | Required. The output name for the window operation. |

### Sort Field Definition
| Property | Type | Description |
| --- | --- | --- |
| field | String | Required. The name of the field to sort. |
| order | String | Null | Whether to sort the field in ascending or descending order. One of "ascending" (default), "descending" , or null (do not sort). |

## Window Only Operation Reference
The valid operations include all aggregate operations (aggregate.html#ops) plus the following window operations.
| Operation | Parameter | Description |
| --- | --- | --- |
| row_number | None | Assigns each data object a consecutive row number, starting from 1. |
| rank | None | Assigns a rank order value to each data object in a window, starting from 1. Peer values are assigned the same rank. Subsequent rank scores incorporate the number of prior values. For example, if the first two values tie for rank 1, the third value is assigned rank 3. |
| dense_rank | None | Assigns dense rank order values to each data object in a window, starting from 1. Peer values are assigned the same rank. Subsequent rank scores do not incorporate the number of prior values. For example, if the first two values tie for rank 1, the third value is assigned rank 2. |
| percent_rank | None | Assigns a percentage rank order value to each data object in a window. The percent is calculated as (rank - 1) / (group_size - 1) . |
| cume_dist | None | Assigns a cumulative distribution value between 0 and 1 to each data object in a window. |
| ntile | Number | Assigns a quantile (e.g., percentile) value to each data object in a window. Accepts an integer parameter indicating the number of buckets to use (e.g., 100 for percentiles, 5 for quintiles). |
| lag | Number | Assigns a value from the data object that precedes the current object by a specified number of positions. If no such object exists, assigns null . Accepts an offset parameter (default 1 ) that indicates the number of positions. This operation must have a corresponding entry in the fields parameter array. |
| lead | Number | Assigns a value from the data object that follows the current object by a specified number of positions. If no such object exists, assigns null . Accepts an offset parameter (default 1 ) that indicates the number of positions. This operation must have a corresponding entry in the fields parameter array. |
| first_value | None | Assigns a value from the first data object in the current sliding window frame. This operation must have a corresponding entry in the fields parameter array. |
| last_value | None | Assigns a value from the last data object in the current sliding window frame. This operation must have a corresponding entry in the fields parameter array. |
| nth_value | Number | Assigns a value from the nth data object in the current sliding window frame. If no such object exists, assigns null . Requires a non-negative integer parameter that indicates the offset from the start of the window frame. This operation must have a corresponding entry in the fields parameter array. |

## Examples
Below are some common use cases for the window transform.
### Cumulative Frequency Distribution
Here we use the window transform with `frame: [null, 0]` to accumulate count in a cumulative frequency distribution plot.
See also: layered histogram and cumulative histogram (../examples/layer_cumulative_histogram.html)
### Rank Chart
We can also use `rank` operator to calculate ranks over time.
### Top K
Here we use window transform to derive the total number of students along with the rank of the current student to determine the top K students and display their score.
Also see this example (https://vega.github.io/vega-lite/examples/window_top_k_others.html) for a top-K plot with others.
### Cumulative Running Average
Here we use window transform to visualize how the average MPG for vehicles have changed over the years.
### Percent of Total
The window transform can be used to compute an aggregate and attach it to all records in order to derive a percent of total, however, a simpler approach is to use the join aggregate (joinaggregate.html) transform instead.
### Using window transform to impute missing values

## Binning
Source: https://vega.github.io/vega-lite/docs/bin.html

Binning discretizes numeric values into a set of bins. A common use case is to create a histogram (#histogram).
There are two ways to define binning in Vega-Lite: the `bin` property in encoding field definitions (#encoding) and the `bin` transform (#transform).
## Documentation Overview
- Binning in Encoding Field Definition (#encoding)
- Example: Histogram (#histogram)
- Example: Histogram with Ordinal Scale (#histogram-ordinal)
- Example: Binned color (#example-binned-color)
- Example: Using Vega-Lite with Binned data (#binned)
- Bin Transform (#transform)
- Example: Histogram with Bin Transform (#example-histogram-with-bin-transform)
- Bin Parameters (#bin-parameters)
- Example: Customizing Max Bins (#example-customizing-max-bins)
- Ordinal Bin (#ordinal-bin)
## Binning in Encoding Field Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "bin": ..., // bin
      "field": ...,
      "type": "quantitative",
      ...
    },
    "y": ...,
    ...
  },
  ...
}

```

You can directly bin an `encoding` field by using the `bin` property in a field definition (encoding.html#field).
| Property | Type | Description |
| --- | --- | --- |
| bin | Boolean | BinParams | String | Null | A flag for binning a quantitative field, an object defining binning parameters , or indicating that the data for x or y channel are binned before they are imported into Vega-Lite ( "binned" ). If true , default binning parameters will be applied. If "binned" , this indicates that the data for the x (or y ) channel are already binned. You can map the bin-start field to x (or y ) and the bin-end field to x2 (or y2 ). The scale and axis will be formatted similar to binning in Vega-Lite. To adjust the axis ticks based on the bin step, you can also set the axiss tickMinStep property. Default value: false See also: bin documentation. |

### Example: Histogram
Mapping binned values and its count to a `bar` mark produces a histogram.
### Example: Histogram with Ordinal Scale
While binned field has `"quantitative"` type by default, setting the binned fields `type` to `"ordinal"` produces a histogram with an ordinal scale.
### Example: Binned color
You can use binning to discretize color scales. Vega-Lite automatically creates legends with range labels.
### Example: Using Vega-Lite with Binned data
If you have data that is already binned outside of Vega-Lite, setting the `bin` property to `"binned"` will trigger Vega-Lite to render scales and axes similar to setting the `bin` property in encoding field definitions. Note that you have to specify field names that encode the start and end of each bin. To adjust the axis ticks based on the bin step, you can set `bin` to e.g. `{"binned": true, "step": 2}`.
## Bin Transform
```
// Any View Specification
{
  ...
  "transform": [
    {"bin": ..., "field": ..., "as" ...} // Bin Transform
     ...
  ],
  ...
}

```

The `bin` transform in the `transform` array has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| bin | Boolean | BinParams | Required. An object indicating bin properties, or simply true for using default bin parameters. |
| field | String | Required. The data field to bin. |
| as | String | String[] | Required. The output fields at which to write the start and end bin values. This can be either a string or an array of strings with two elements denoting the name for the fields for bin start and bin end respectively. If a single string (e.g., "val" ) is provided, the end field will be "val_end" . |

### Example: Histogram with Bin Transform
Instead of using the `bin` property of a field definition, you can also use a bin transform to derive a new field (e.g., `bin_IMDB_Rating`), and encode the new field with bin property of a field definition set to `binned` instead.
While binning in `transform` is more verbose than in `encoding`, it can be useful if you want to perform additional calculation before encoding the data.
## Bin Parameters
If `bin` is `true`, default binning properties are used. To customize binning properties, you can set `bin` to a bin definition object, which can have the following properties:
| Property | Type | Description |
| --- | --- | --- |
| anchor | Number | A value in the binned domain at which to anchor the bins, shifting the bin boundaries if necessary to ensure that a boundary aligns with the anchor value. Default value: the minimum bin extent value |
| base | Number | The number base to use for automatic bin determination (default is base 10). Default value: 10 |
| divide | Number[] | Scale factors indicating allowable subdivisions. The default value is [5, 2], which indicates that for base 10 numbers (the default base), the method may consider dividing bin sizes by 5 and/or 2. For example, for an initial step size of 10, the method can check if bin sizes of 2 (= 10/5), 5 (= 10/2), or 1 (= 10/(5*2)) might also satisfy the given constraints. Default value: [5, 2] |
| extent | Array | A two-element ( [min, max] ) array indicating the range of desired bin values. |
| maxbins | Number | Maximum number of bins. Default value: 6 for row , column and shape channels; 10 for other channels |
| minstep | Number | A minimum allowable step size (particularly useful for integer values). |
| nice | Boolean | If true, attempts to make the bin boundaries use human-friendly boundaries, such as multiples of ten. Default value: true |
| step | Number | An exact step size to use between bins. Note: If provided, options such as maxbins will be ignored. |
| steps | Number[] | An array of allowable step sizes to choose from. |

### Example: Customizing Max Bins
Setting the `maxbins` parameter changes the maximum number of output bins. There will often be fewer bins since the domain get sliced at nicely-rounded values.
## Ordinal Bin
Usually, you should set the type of binned encodings to be quantitative. Vega-Lite automatically creates axes and legends that best represent binned data. However, if you want to sort the bins or skip empty bins, you can set the type to ordinal.
For example, this following plot shows binned values sort by count.

## Time Unit
Source: https://vega.github.io/vega-lite/docs/timeunit.html

Time unit is used to discretize times in Vega-Lite. It can be used (1) with the `timeUnit` property of encoding field definitions (#encoding), (2) as a standalone transform (#transform), or (3) with the `timeUnit` property of a field predicate (predicate.html#field-predicate).
Vega-Lite supports the following time units:
- `"year"` - Gregorian (https://en.wikipedia.org/wiki/Gregorian_calendar) calendar years.
- `"quarter"` - Three-month intervals, starting in one of January, April, July, and October.
- `"month"` - Calendar months (January, February, etc.).
- `"date"` - Calendar day of the month (January 1, January 2, etc.).
- `"week"` - Sunday-based weeks. Days before the first Sunday of the year are considered to be in week 0, the first Sunday of the year is the start of week 1, the second Sunday week 2, etc..
- `"day"` - Day of the week (Sunday, Monday, etc.).
- `"dayofyear"` - Day of the year (1, 2, ..., 365, etc.).
- `"hours"` - Hours of the day (12:00am, 1:00am, etc.).
- `"minutes"` - Minutes in an hour (12:00, 12:01, etc.).
- `"seconds"` - Seconds in a minute (12:00:00, 12:00:01, etc.).
- `"milliseconds"` - Milliseconds in a second.
Vega-Lite time units can also be a string of consecutive time units to indicate desired intervals of time. For example, `yearmonthdate` indicates chronological time sensitive to year, month, and date (but not to hours, minutes, or seconds). The specifier `monthdate` is sensitive to month and date, but not year, which can be useful for binning time values to look at seasonal patterns only.
- By default, all time units represent date time using local time.
- To use UTC time, you can add the `utc` prefix (e.g., `"utcyear"`, `"utcyearmonth"`).
- For timeUnit in encoding, you can also add `"binned"` prefix (e.g., `"binnedyearmonth"` or `"binnedutcyearmonth"`) for Chronological time units (i.e., units that are truncated date times, as opposed to circle time units, which bin data to parts of date times).
## Documentation Overview
- Time Unit in Encoding Field Definition (#encoding)
- Time Units Band (#time-units-band)
- Time Unit with Ordinal Fields (#time-unit-with-ordinal-fields)
- Time Unit Transform (#transform)
- UTC time (#utc)
- Input (#input)
- Output (#output)
- Time Unit Parameters (#params)
- Example: Customizing Step (#example-customizing-step)
## Time Unit in Encoding Field Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "timeUnit": ...,               // time unit
      "field": ...,
      "type": "temporal",
      ...
    },
    "y": ...,
    ...
  },
  ...
}

```

A field definition can include a `timeUnit` property. For example, the chart below shows temperature in Seattle aggregated by month.

Using `timeUnit` with rect-based marks (including `bar`, `rect`, and `image`) will treat time units as intervals.

You can also add `"binned"` prefix if your data has already been binned and want Vega-Lite to apply the right formatting, including the right bands for the interval, to your charts.
By default, bar marks are placed from the beginning of a time interval (e.g., month) to the end of the interval.
Setting `bandPosition` (bandposition.html) to `0` moves the bar to center-align with ticks.

### Time Units Band
By default, Vega-Lite encodes fields with timeUnit using the initial position of a time unit (which is equivalent to having `band` = 0). However, one can set the `band` property to be `0.5` to use place each data point in the middle of each time unit band.

### Time Unit with Ordinal Fields
By default, fields with time units have temporal type and thus use time scales. However, time units can be also used with a discrete scale. For example, you can cast the field to have an `"ordinal"` type.

## Time Unit Transform
```
// Any View Specification
{
  ...,
  "transform": [
    {"timeUnit": ..., "field": ..., "as": ...} // TimeUnit Transform
     ...
  ],
  ...
}

```

A `timeUnit` transform in the `transform` array has the following properties:
| Property | Type | Description |
| --- | --- | --- |
| timeUnit | TimeUnit | TimeUnitTransformParams | Required. The timeUnit. |
| field | String | Required. The data field to apply time unit. |
| as | String | Required. The output field to write the timeUnit value. |

In the example below, we use the time unit transform to extract the month component of the dates. We can then visualize the hottest temperature. Note that Vega-Lite will not automatically format the axis if the `timeUnit` is applied outside `encoding` so we have to format it manually. For this reason, you should prefer time units as part of encoding definitions.

## UTC time
### Input
To parse data in local time or UTC time, there are three cases:
- Times are parsed as UTC time if the date strings are in ISO format (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse). Note that in JavaScript date strings without time are interpreted as UTC but date strings with time and without timezone as local.

If you dont want to re-bin the data, you can also add `"binned"` prefix.

- If that is not the case, by default, times are assumed to be local.

- To parse inline data or url data without ISO format as UTC time, we need to specify the `format` to be `utc` with time format:

### Output
By default, Vega-Lite will output data in local time (even when input is parsed as UTC time). To output data in UTC time, we can specify either a UTC time unit or scale:
- UTC time unit when input data is in local time.

- UTC scale type when you have input data in UTC time.

## Time Unit Parameters
To customize time unit properties, you can set `timeUnit` to be a time unit definition object. It can have the following properties.
| Property | Type | Description |
| --- | --- | --- |
| unit | TimeUnit | Defines how date-time values should be binned. |
| maxbins | Number | If no unit is specified, maxbins is used to infer time units. |
| step | Number | The number of steps between bins, in terms of the least significant unit provided. |
| utc | Boolean | True to use UTC timezone. Equivalent to using a utc prefixed TimeUnit . |
| binned | Boolean | Whether the data has already been binned to this time unit. If true, Vega-Lite will only format the data, marks, and guides, without applying the timeUnit transform to re-bin the data again. |

### Example: Customizing Step
The `step` parameter can be used to specify a bin size with respect to the smallest denominator in the time unit provided. The following example shows sum of distance traveled for each 5-minute interval.

## Density
Source: https://vega.github.io/vega-lite/docs/density.html

The density transform performs one-dimensional kernel density estimation (https://en.wikipedia.org/wiki/Kernel_density_estimation) over an input data stream and generates a new data stream of samples of the estimated densities.
```
// Any View Specification
{
  ...
  "transform": [
    {"density": ...} // Density Transform
     ...
  ],
  ...
}

```

## Density Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| density | String | Required. The data field for which to perform density estimation. |
| groupby | String[] | The data fields to group by. If not specified, a single group containing all data objects will be used. |
| cumulative | Boolean | A boolean flag indicating whether to produce density estimates (false) or cumulative density estimates (true). Default value: false |
| counts | Boolean | A boolean flag indicating if the output values should be probability estimates (false) or smoothed counts (true). Default value: false |
| bandwidth | Number | The bandwidth (standard deviation) of the Gaussian kernel. If unspecified or set to zero, the bandwidth value is automatically estimated from the input data using Scotts rule. |
| extent | Number[] | A [min, max] domain from which to sample the distribution. If unspecified, the extent will be determined by the observed minimum and maximum values of the density value field. |
| minsteps | Number | The minimum number of samples to take along the extent domain for plotting the density. Default value: 25 |
| maxsteps | Number | The maximum number of samples to take along the extent domain for plotting the density. Default value: 200 |
| resolve | String | Indicates how parameters for multiple densities should be resolved. If "independent" , each density may have its own domain extent and dynamic number of curve sample steps. If "shared" , the KDE transform will ensure that all densities are defined over a shared domain and curve steps, enabling stacking. Default value: "shared" |
| steps | Number | The exact number of samples to take along the extent domain for plotting the density. If specified, overrides both minsteps and maxsteps to set an exact number of uniform samples. Potentially useful in conjunction with a fixed extent to ensure consistent sample points for stacked densities. |
| as | String[] | The output fields for the sample value and corresponding density estimate. Default value: ["value", "density"] |

## Usage
```
{"density": "measure", "groupby": ["key"]}

```

Performs density estimation for the `"measure"` field, with separate estimations performed for each group of records with a distinct `"key"` field value. The output data is of the form:
```
[
  {"key": "a", "value": 1, "density": 0.02},
  ...
]

```

### Example: Density Plot
### Example: Stacked Density Estimates
To plot a stacked graph of estimates, use a shared `extent` and a fixed number of subdivision `steps` to ensure that the points for each area align well. In addition, setting `counts` to true multiplies the densities by the number of data points in each group, preserving proportional differences:
### Example: Faceted Density Estimates
Density estimates of body mass in grams for different penguin species:

## Regression
Source: https://vega.github.io/vega-lite/docs/regression.html

The regression transform fits two-dimensional regression models (https://en.wikipedia.org/wiki/Regression_analysis) to smooth and predict data. This transform can fit multiple models for input data (one per group) and generates new data objects that represent points for summary trend lines. Alternatively, this transform can be used to generate a set of objects containing regression model parameters, one per group.
This transform supports parametric models for the following functional forms:
- linear (`linear`): y = a + b * x
- logarithmic (`log`): y = a + b * log(x)
- exponential (`exp`): y = a * e^(b * x)
- power (`pow`): y = a * x^b
- quadratic (`quad`): y = a + b * x + c * x^2
- polynomial (`poly`): y = a + b * x + ... + k * x^(order)
All models are fit using ordinary least squares (https://en.wikipedia.org/wiki/Ordinary_least_squares). For non-parametric locally weighted regression, see the loess (loess.html) transform.
```
// Any View Specification
{
  ...
  "transform": [
    {"regression": ...} // Regression Transform
     ...
  ],
  ...
}

```

## Regression Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| regression | String | Required. The data field of the dependent variable to predict. |
| on | String | Required. The data field of the independent variable to use a predictor. |
| groupby | String[] | The data fields to group by. If not specified, a single group containing all data objects will be used. |
| method | String | The functional form of the regression model. One of "linear" , "log" , "exp" , "pow" , "quad" , or "poly" . Default value: "linear" |
| order | Number | The polynomial order (number of coefficients) for the poly method. Default value: 3 |
| extent | Number[] | A [min, max] domain over the independent (x) field for the starting and ending points of the generated trend line. |
| params | Boolean | A boolean flag indicating if the transform should return the regression model parameters (one object per group), rather than trend line points. The resulting objects include a coef array of fitted coefficient values (starting with the intercept term and then including terms of increasing order) and an rSquared value (indicating the total variance explained by the model). Default value: false |
| as | String[] | The output field names for the smoothed points generated by the regression transform. Default value: The field names of the input x and y values. |

## Usage
```
{"regression": "y", "on": "x"}

```

Generate a linear regression trend line that models field `"y"` as a function of `"x"`. The output data stream can then be visualized with a line mark, and takes the form:
```
[
  {"x": 1, "y": 2.3},
  {"x": 2, "y": 2.7},
  {"x": 3, "y": 3.0},
  ...
]

```

If the `groupby` parameter is provided, separate trend lines will be fit per-group, and the output records will additionally include all groupby field values.
## Example

## Loess
Source: https://vega.github.io/vega-lite/docs/loess.html

The loess transform (for locally-estimated scatterplot smoothing) uses locally-estimated regression (https://en.wikipedia.org/wiki/Local_regression) to produce a trend line. Loess performs a sequence of local weighted regressions over a sliding window of nearest-neighbor points. For standard parametric regression options, see the regression (regression.html) transform.
```
// Any View Specification
{
  ...
  "transform": [
    {"loess": ...} // Loess Transform
     ...
  ],
  ...
}

```

## Loess Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| loess | String | Required. The data field of the dependent variable to smooth. |
| on | String | Required. The data field of the independent variable to use a predictor. |
| groupby | String[] | The data fields to group by. If not specified, a single group containing all data objects will be used. |
| bandwidth | Number | A bandwidth parameter in the range [0, 1] that determines the amount of smoothing. Default value: 0.3 |
| as | String[] | The output field names for the smoothed points generated by the loess transform. Default value: The field names of the input x and y values. |

## Usage
```
{"loess": "y", "on": "x", "bandwidth": 0.5}

```

Generate a loess trend line that models field `"y"` as a function of `"x"`, using a bandwidth parameter of `0.5`. The output data stream can then be visualized with a line mark, and takes the form:
```
[
  {"x": 1, "y": 2.3},
  {"x": 2, "y": 2.9},
  {"x": 3, "y": 2.7},
  ...
]

```

If the `groupby` parameter is provided, separate trend lines will be fit per-group, and the output records will additionally include all groupby field values.
## Example

## Quantile
Source: https://vega.github.io/vega-lite/docs/quantile.html

The quantile transform calculates empirical quantile (https://en.wikipedia.org/wiki/Quantile) values for an input data stream. If a groupby parameter is provided, quantiles are estimated separately per group. Among other uses, the quantile transform is useful for creating quantile-quantile (Q-Q) plots (https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot).
```
// Any View Specification
{
  ...
  "transform": [
    {"quantile": ...} // Quantile Transform
     ...
  ],
  ...
}

```

## Quantile Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| quantile | String | Required. The data field for which to perform quantile estimation. |
| groupby | String[] | The data fields to group by. If not specified, a single group containing all data objects will be used. |
| probs | Number[] | An array of probabilities in the range (0, 1) for which to compute quantile values. If not specified, the step parameter will be used. |
| step | Number | A probability step size (default 0.01) for sampling quantile values. All values from one-half the step size up to 1 (exclusive) will be sampled. This parameter is only used if the probs parameter is not provided. |
| as | String[] | The output field names for the probability and quantile values. Default value: ["prob", "value"] |

## Usage
```
{"quantile": "measure", "probs": [0.25, 0.5, 0.75]}

```

Computes the quartile (https://en.wikipedia.org/wiki/Quartile) boundaries for the `"measure"` field. The output data is of the form:
```
[
  {prob: 0.25, value: 1.34},
  {prob: 0.5, value: 5.82},
  {prob: 0.75, value: 9.31},
];

```

```
{"quantile": "measure", "step": 0.05}

```

Computes quantiles for the `"measure"` field over equal-sized probability steps. The output data is of the form:
```
[{prob: 0.025, value: 0.01}, {prob: 0.075, value: 0.02}, ...{prob: 0.975, value: 0.2}];

```

### Example: Quantile-Quantile Plot
A quantile-quantile plot comparing input data to theoretical distributions:

## Sample
Source: https://vega.github.io/vega-lite/docs/sample.html

The sample transform filters random rows from the data source to reduce its size. As input data objects are added and removed, the sampled values may change in first-in, first-out manner. This transform uses reservoir sampling (https://en.wikipedia.org/wiki/Reservoir_sampling) to maintain a representative sample of the stream.
```
// Any View Specification
{
  ...
  "transform": [
    {"sample": ...} // Sample Transform
     ...
  ],
  ...
}

```

## Sample Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| sample | Number | Required. The maximum number of data objects to include in the sample. Default value: 1000 |

## Usage
```
{"sample": 500}

```

Filters a data stream to a random sample of at most 500 data objects.
## Example
Comparison between plots of the complete data and sampled data.

## Lookup Transform
Source: https://vega.github.io/vega-lite/docs/lookup.html

The lookup transform extends a primary data source by looking up values from another data source. It is similar to a one sided join.
```
// Any View Specification
{
  ...
  "transform": [
    {"lookup": ..., "from" ..., "as": ..., "default": ...} // Lookup Transform
     ...
  ],
  ...
}

```

## Lookup Transform
For each data object in the main data source, the transform finds matching objects in the secondary data source. An object matches if the value in the field specified by `lookup` is the same as the field specified in the `from.key`.
| Property | Type | Description |
| --- | --- | --- |
| lookup | String | Required. Key in primary data source. |
| from | LookupData | LookupSelection | Required. Data source or selection for secondary data reference. |
| as | String | String[] | The output fields on which to store the looked up data values. For data lookups, this property may be left blank if from.fields has been specified (those field names will be used); if from.fields has not been specified, as must be a string. For selection lookups, this property is optional: if unspecified, looked up values will be stored under a property named for the selection; and if specified, it must correspond to from.fields . |
| default | Any | The default value to use if lookup fails. Default value: null |

### Lookup Data
The secondary data reference (set with `from`) can be object that specifies how the lookup key should be matched to a second data source and what fields should be added.
| Property | Type | Description |
| --- | --- | --- |
| data | Data | Required. Secondary data source to lookup in. |
| key | String | Required. Key in data to lookup. |
| fields | String[] | Fields in foreign data or selection to lookup. If not specified, the entire object is queried. |

#### Example
This example uses `lookup` to add the properties `age` and `height` to the main data source. The `person` field in the main data source is matched to the `name` field in the secondary data source.

### Lookup Selection
The secondary data reference (set with `from`) can also be a selection parameter name.
| Property | Type | Description |
| --- | --- | --- |
| param | String | Required. Selection parameter name to look up. |

#### Example: Interactive Index Chart

## Fold
Source: https://vega.github.io/vega-lite/docs/fold.html

The fold transform collapses (or folds) one or more data fields into two properties: a key property (containing the original data field name) and a value property (containing the data value).
The fold transform is useful for mapping matrix or cross-tabulation data into a standardized format.
This transform generates a new data stream in which each data object consists of the key and value properties as well as all the original fields of the corresponding input data object.
Note: The `fold` transform only applies to a list of known fields (set using the `fields` parameter). If your data objects instead contain array-typed fields, you may wish to use the flatten (flatten.html) transform instead.
```
// Any View Specification
{
  ...
  "transform": [
    {"fold": ...} // Fold Transform
     ...
  ],
  ...
}

```

## Fold Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| fold | String[] | Required. An array of data fields indicating the properties to fold. |
| as | String[] | The output field names for the key and value properties produced by the fold transform. Default value: ["key", "value"] |

## Usage
```
{"fold": ["gold", "silver"]}

```

This example folds the `"gold"` and `"silver"` properties. Given the input data
```
[
  {"country": "USA", "gold": 10, "silver": 20},
  {"country": "Canada", "gold": 7, "silver": 26}
]

```

this example produces the output:
```
[
  {"key": "gold", "value": 10, "country": "USA", "gold": 10, "silver": 20},
  {"key": "silver", "value": 20, "country": "USA", "gold": 10, "silver": 20},
  {"key": "gold", "value": 7, "country": "Canada", "gold": 7, "silver": 26},
  {"key": "silver", "value": 26, "country": "Canada", "gold": 7, "silver": 26}
]

```

## Example

## Flatten
Source: https://vega.github.io/vega-lite/docs/flatten.html

The flatten transform maps array-valued fields to a set of individual data objects, one per array entry. This transform generates a new data stream in which each data object consists of an extracted array value as well as all the original fields of the corresponding input data object.
```
// Any View Specification
{
  ...
  "transform": [
    {"flatten": ...} // Flatten Transform
     ...
  ],
  ...
}

```

## Flatten Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| flatten | String[] | Required. An array of one or more data fields containing arrays to flatten. If multiple fields are specified, their array values should have a parallel structure, ideally with the same length. If the lengths of parallel arrays do not match, the longest array will be used with null values added for missing entries. |
| as | String[] | The output field names for extracted array values. Default value: The field name of the corresponding array field |

## Usage
```
{"flatten": ["foo", "bar"]}

```

This example flattens the `"foo"` and `"bar"` array-valued fields. Given the input data
```
[
  {"key": "alpha", "foo": [1, 2], "bar": ["A", "B"]},
  {"key": "beta", "foo": [3, 4, 5], "bar": ["C", "D"]}
]

```

this example produces the output:
```
[
  {"key": "alpha", "foo": 1, "bar": "A"},
  {"key": "alpha", "foo": 2, "bar": "B"},
  {"key": "beta", "foo": 3, "bar": "C"},
  {"key": "beta", "foo": 4, "bar": "D"},
  {"key": "beta", "foo": 5, "bar": null}
]

```

## Examples
Below are some examples to demonstrate the usage of the flatten transform.
### Basic Example
In this example, `flatten` is used on two fields simultaneously. `null` values are added to the shorter array.
### Advanced Example: Coordinated Views with Nested Time Series
Here, a single field is flattened and then used to plot the line chart corresponding to the circle chart above.

## Pivot
Source: https://vega.github.io/vega-lite/docs/pivot.html

The pivot transform maps unique values from a field to new aggregated fields (columns) in the output stream. The transform requires both a field to pivot on (providing new field names) and a field of values to aggregate to populate the new cells. In addition, any number of groupby fields can be provided to further subdivide the data into output data objects (rows).
Pivot transforms are useful for creating matrix or cross-tabulation data, acting as an inverse to the fold (fold.html) transform.
## Pivot Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| pivot | String | Required. The data field to pivot on. The unique values of this field become new field names in the output stream. |
| value | String | Required. The data field to populate pivoted fields. The aggregate values of this field become the values of the new pivoted fields. |
| groupby | String[] | The optional data fields to group by. If not specified, a single group containing all data objects will be used. |
| limit | Number | An optional parameter indicating the maximum number of pivoted fields to generate. The default ( 0 ) applies no limit. The pivoted pivot names are sorted in ascending order prior to enforcing the limit. Default value: 0 |
| op | String | The aggregation operation to apply to grouped value field values. Default value: sum |

## Usage
For the following input data:
```
[
  {"country": "Norway", "type": "gold", "count": 14},
  {"country": "Norway", "type": "silver", "count": 14},
  {"country": "Norway", "type": "bronze", "count": 11},
  {"country": "Germany", "type": "gold", "count": 14},
  {"country": "Germany", "type": "silver", "count": 10},
  {"country": "Germany", "type": "bronze", "count": 7},
  {"country": "Canada", "type": "gold", "count": 11},
  {"country": "Canada", "type": "silver", "count": 8},
  {"country": "Canada", "type": "bronze", "count": 10}
]

```

The pivot transform
```
{
  "pivot": "type",
  "groupby": ["country"],
  "value": "count"
}

```

produces the output:
```
[
  {"country": "Norway", "gold": 14, "silver": 14, "bronze": 11},
  {"country": "Germany", "gold": 14, "silver": 10, "bronze": 7},
  {"country": "Canada", "gold": 11, "silver": 8, "bronze": 10}
]

```

## Example

## Impute
Source: https://vega.github.io/vega-lite/docs/impute.html

To impute missing data in Vega-Lite, you can either use the `impute` transform, either via an encoding field definition (#encoding) or via an `transform` (#transform) array.
The impute transform groups data and determines missing values of the `key` field within each group. For each missing value in each group, the impute transform will produce a new tuple with the `impute`d field generated based on a specified imputation `method` (by using a constant `value` or by calculating statistics such as mean within each group).
## Documentation Overview
- Impute in Encoding Field Definition (#encoding)
- Specifying the Key Values to be Imputed (#specifying-the-key-values-to-be-imputed)
- Impute Transform (#transform)
## Impute in Encoding Field Definition
```
// A Single View or a Layer Specification
{
  ...,
  "mark/layer": ...,
  "encoding": {
    "x": {
      "field": ...,
      "type": "quantitative",
      "impute": {...},               // Impute
      ...
    },
    "y": ...,
    ...
  },
  ...
}

```

An encoding field definition (encoding.html#field-def) can include an `impute` definition object to generate new data objects in place of the missing data.
The `impute` definition object can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| frame | (Null | Number)[] | A frame specification as a two-element array used to control the window over which the specified method is applied. The array entries should either be a number indicating the offset from the current data object, or null to indicate unbounded rows preceding or following the current data object. For example, the value [-5, 5] indicates that the window should include five objects preceding and five objects following the current object. Default value: : [null, null] indicating that the window includes all objects. |
| keyvals | Any [] | ImputeSequence | Defines the key values that should be considered for imputation. An array of key values or an object defining a number sequence . If provided, this will be used in addition to the key values observed within the input data. If not provided, the values will be derived from all unique values of the key field. For impute in encoding , the key field is the x-field if the y-field is imputed, or vice versa. If there is no impute grouping, this property must be specified. |
| method | String | The imputation method to use for the field value of imputed data objects. One of "value" , "mean" , "median" , "max" or "min" . Default value: "value" |
| value | Any | The field value to use when the imputation method is "value" . |

For `impute` in encoding, the grouping fields and the key field (for identifying missing values) are automatically determined. Values are automatically grouped by the specified fields of mark property channels (encoding.html#mark-prop), key channel (encoding.html#key) and detail channel (encoding.html#detail). If x-field is `impute`d, y-field is the key field. Basically, any missing y-value in each group will lead to a new tuple imputed, and vice versa.
In this example, we `impute` the `y`-field (`"b"`), so the `x`-field (`"a"`) will be used as the `"key"`. The values are then grouped by the field `"c"` of the `color` encoding. The impute transform then determines missing key values within each group. In this case, the data tuple where `"a"` is `3` and `"c"` is `1` is missing, so a new tuple with `"a"` = `3`, `"c"` = `1`, and `"b"` = `0` will be added.
Besides imputing with a constant `value`, we can also use a `method` (such as `"mean"`) on existing data points to generate the missing data.
The `frame` property of `impute` can be used to control the window over which the specified `method` is applied. Here, the `frame` is `[-2, 2]` which indicates that the window for calculating mean includes two objects preceding and two objects following the current object.
### Specifying the Key Values to be Imputed
The `keyvals` property provides additional key values that should be considered for imputation. If not provided, all of the values will be derived from all unique values of the `key` field. If there is no grouping field (e.g., no `color` in the examples given above), then `keyvals` must be specified. Otherwise, the impute transform will have no effect on the data.
The `keyvals` property can be an array:
Alternatively, the `keyvals` property can be an object (#sequence-def) defining a sequence, which can contain the following properties:
| Property | Type | Description |
| --- | --- | --- |
| start | Number | The starting value of the sequence. Default value: 0 |
| stop | Number | Required. The ending value(exclusive) of the sequence. |
| step | Number | The step value between sequence entries. Default value: 1 or -1 if stop < start |

## Impute Transform
An impute transform can also be specified as a part of the `transform` array.
```
// A View Specification
{
  ...
  "transform": [
    ...
    {
      // Impute Transform
      "impute": ...,
      "key": ...,
      "keyvals": ...,
      "groupby": [...],
      "frame": [...],
      "method": ...,
      "value": ...
    }
    ...
  ],
  ...
}

```

| Property | Type | Description |
| --- | --- | --- |
| impute | String | Required. The data field for which the missing values should be imputed. |
| key | String | Required. A key field that uniquely identifies data objects within a group. Missing key values (those occurring in the data but not in the current group) will be imputed. |
| keyvals | Any [] | ImputeSequence | Defines the key values that should be considered for imputation. An array of key values or an object defining a number sequence . If provided, this will be used in addition to the key values observed within the input data. If not provided, the values will be derived from all unique values of the key field. For impute in encoding , the key field is the x-field if the y-field is imputed, or vice versa. If there is no impute grouping, this property must be specified. |
| groupby | String[] | An optional array of fields by which to group the values. Imputation will then be performed on a per-group basis. |
| frame | (Null | Number)[] | A frame specification as a two-element array used to control the window over which the specified method is applied. The array entries should either be a number indicating the offset from the current data object, or null to indicate unbounded rows preceding or following the current data object. For example, the value [-5, 5] indicates that the window should include five objects preceding and five objects following the current object. Default value: : [null, null] indicating that the window includes all objects. |
| method | String | The imputation method to use for the field value of imputed data objects. One of "value" , "mean" , "median" , "max" or "min" . Default value: "value" |
| value | Any | The field value to use when the imputation method is "value" . |

For example, the same chart with `impute` in encoding above ("#encoding-impute-value") can be created using the `impute` transform. Here, we have to manually specify the `key` and `groupby` fields, which were inferred automatically for `impute` in `encoding`.
Similarly `keyvals` must be specified if the `groupby` property is not specified.

## Extent
Source: https://vega.github.io/vega-lite/docs/extent.html

The extent transform finds the extent of a field and stores the result in a parameter (/vega-lite/docs/parameter.html).
```
// Any View Specification
{
  ...
  "transform": [
    {"extent": ..., "param": ...} // Extent Transform
     ...
  ],
  ...
}

```

## Extent Transform Definition
| Property | Type | Description |
| --- | --- | --- |
| extent | String | Required. The field of which to get the extent. |
| param | String | Required. The output parameter produced by the extent transform. |

## Usage
Given the following data:
```
"data": {
  "values": [
    {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
    {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
    {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
  ]
}

```

And the transform:
```
"transform": [
  {"extent": "b", "param": "b_extent"}
]

```

this example produces the param `b_extent` with the value `[19, 91]`.
## Example

