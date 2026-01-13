# Intro And Embed

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Overview
Source: https://vega.github.io/vega-lite/docs/index.html

Vega-Lite is a high-level grammar for interactive graphics. It provides a concise JSON syntax for supporting rapid generation of interactive multi-view visualizations to support analysis. Vega-Lite can serve as a declarative format for describing and creating data visualizations. To use Vega-Lite, our compiler compiles a Vega-Lite specification into a lower-level, more detailed Vega (https://vega.github.io/vega) specifications and rendered using Vegas compiler.
This documentation describes the JSON specification language (spec.html) and how to use Vega-Lite visualizations (/vega-lite/usage/embed.html) in a web application.     Search
## Table of Contents
Below is an overview of the documentation for Vega-Lite properties. See the specification page (spec.html) for an overview of Vega-Lite specifications.
- Overview (/vega-lite/docs/index.html)
- Table of Contents (/vega-lite/docs/index.html#toc)
- View Specification (/vega-lite/docs/spec.html)
- Documentation Overview (/vega-lite/docs/spec.html#documentation-overview)
- Common Properties of Specifications (/vega-lite/docs/spec.html#common)
- Top-Level Specifications (/vega-lite/docs/spec.html#top-level)
- Single View Specifications (/vega-lite/docs/spec.html#single)
- Layered and Multi-view Specifications (/vega-lite/docs/spec.html#layered-and-multi-view-specifications)
- View Configuration (/vega-lite/docs/spec.html#config)
- Title (/vega-lite/docs/title.html)
- Title Properties Object (/vega-lite/docs/title.html#props)
- Title Config (/vega-lite/docs/title.html#config)
- Width / Height (/vega-lite/docs/size.html)
- Documentation Overview (/vega-lite/docs/size.html#documentation-overview)
- Width and Height of Single and Layered Plots (/vega-lite/docs/size.html#width-and-height-of-single-and-layered-plots)
- Width and Height of Multi-View Displays (/vega-lite/docs/size.html#width-and-height-of-multi-view-displays)
- Data / Datasets (/vega-lite/docs/data.html)
- Documentation Overview (/vega-lite/docs/data.html#documentation-overview)
- Types of Data Sources (/vega-lite/docs/data.html#types-of-data-sources)
- Format (/vega-lite/docs/data.html#format)
- Data Generators (/vega-lite/docs/data.html#data-generators)
- Datasets (/vega-lite/docs/data.html#datasets)
- Transform (/vega-lite/docs/transform.html)
- View-level Transform Property (/vega-lite/docs/transform.html#view-level-transform-property)
- Aggregate (/vega-lite/docs/aggregate.html)
- Documentation Overview (/vega-lite/docs/aggregate.html#documentation-overview)
- Aggregate in Encoding Field Definition (/vega-lite/docs/aggregate.html#encoding)
- Aggregate Transform (/vega-lite/docs/aggregate.html#transform)
- Supported Aggregation Operations (/vega-lite/docs/aggregate.html#ops)
- Argmin / Argmax (/vega-lite/docs/aggregate.html#argmax)
- Bin (/vega-lite/docs/bin.html)
- Documentation Overview (/vega-lite/docs/bin.html#documentation-overview)
- Binning in Encoding Field Definition (/vega-lite/docs/bin.html#encoding)
- Bin Transform (/vega-lite/docs/bin.html#transform)
- Bin Parameters (/vega-lite/docs/bin.html#bin-parameters)
- Ordinal Bin (/vega-lite/docs/bin.html#ordinal-bin)
- Calculate (/vega-lite/docs/calculate.html)
- Calculate Transform Definition (/vega-lite/docs/calculate.html#calculate-transform-definition)
- Example (/vega-lite/docs/calculate.html#example)
- Density (/vega-lite/docs/density.html)
- Density Transform Definition (/vega-lite/docs/density.html#density-transform-definition)
- Usage (/vega-lite/docs/density.html#usage)
- Extent (/vega-lite/docs/extent.html)
- Extent Transform Definition (/vega-lite/docs/extent.html#extent-transform-definition)
- Usage (/vega-lite/docs/extent.html#usage)
- Example (/vega-lite/docs/extent.html#example)
- Filter (/vega-lite/docs/filter.html)
- Flatten (/vega-lite/docs/flatten.html)
- Flatten Transform Definition (/vega-lite/docs/flatten.html#flatten-transform-definition)
- Usage (/vega-lite/docs/flatten.html#usage)
- Examples (/vega-lite/docs/flatten.html#examples)
- Fold (/vega-lite/docs/fold.html)
- Fold Transform Definition (/vega-lite/docs/fold.html#fold-transform-definition)
- Usage (/vega-lite/docs/fold.html#usage)
- Example (/vega-lite/docs/fold.html#example)
- Impute (/vega-lite/docs/impute.html)
- Documentation Overview (/vega-lite/docs/impute.html#documentation-overview)
- Impute in Encoding Field Definition (/vega-lite/docs/impute.html#encoding)
- Impute Transform (/vega-lite/docs/impute.html#transform)
- Join Aggregate (/vega-lite/docs/joinaggregate.html)
- Documentation Overview (/vega-lite/docs/joinaggregate.html#documentation-overview)
- Join Aggregate Field Definition (/vega-lite/docs/joinaggregate.html#join-aggregate-field-definition)
- Join Aggregate Transform Definition (/vega-lite/docs/joinaggregate.html#join-aggregate-transform-definition)
- Examples (/vega-lite/docs/joinaggregate.html#ops)
- Loess (/vega-lite/docs/loess.html)
- Loess Transform Definition (/vega-lite/docs/loess.html#loess-transform-definition)
- Usage (/vega-lite/docs/loess.html#usage)
- Example (/vega-lite/docs/loess.html#example)
- Lookup (/vega-lite/docs/lookup.html)
- Lookup Transform (/vega-lite/docs/lookup.html#lookup-transform)
- Pivot (/vega-lite/docs/pivot.html)
- Pivot Transform Definition (/vega-lite/docs/pivot.html#pivot-transform-definition)
- Usage (/vega-lite/docs/pivot.html#usage)
- Example (/vega-lite/docs/pivot.html#example)
- Quantile (/vega-lite/docs/quantile.html)
- Quantile Transform Definition (/vega-lite/docs/quantile.html#quantile-transform-definition)
- Usage (/vega-lite/docs/quantile.html#usage)
- Regression (/vega-lite/docs/regression.html)
- Regression Transform Definition (/vega-lite/docs/regression.html#regression-transform-definition)
- Usage (/vega-lite/docs/regression.html#usage)
- Example (/vega-lite/docs/regression.html#example)
- Sample (/vega-lite/docs/sample.html)
- Sample Transform Definition (/vega-lite/docs/sample.html#sample-transform-definition)
- Usage (/vega-lite/docs/sample.html#usage)
- Example (/vega-lite/docs/sample.html#example)
- Stack (/vega-lite/docs/stack.html)
- Documentation Overview (/vega-lite/docs/stack.html#documentation-overview)
- Stack in Encoding Field Definition (/vega-lite/docs/stack.html#encoding)
- Stack Transform (/vega-lite/docs/stack.html#transform)
- Time Unit (/vega-lite/docs/timeunit.html)
- Documentation Overview (/vega-lite/docs/timeunit.html#documentation-overview)
- Time Unit in Encoding Field Definition (/vega-lite/docs/timeunit.html#encoding)
- Time Unit Transform (/vega-lite/docs/timeunit.html#transform)
- UTC time (/vega-lite/docs/timeunit.html#utc)
- Time Unit Parameters (/vega-lite/docs/timeunit.html#params)
- Window (/vega-lite/docs/window.html)
- Documentation Overview (/vega-lite/docs/window.html#documentation-overview)
- Window Field Definition (/vega-lite/docs/window.html#window-field-definition)
- Window Transform Definition (/vega-lite/docs/window.html#window-transform-definition)
- Window Only Operation Reference (/vega-lite/docs/window.html#ops)
- Examples (/vega-lite/docs/window.html#examples)
- Mark (/vega-lite/docs/mark.html)
- Documentation Overview (/vega-lite/docs/mark.html#documentation-overview)
- Mark Types (/vega-lite/docs/mark.html#types)
- Mark Definition Object (/vega-lite/docs/mark.html#mark-def)
- Mark Config (/vega-lite/docs/mark.html#config)
- Mark Style Config (/vega-lite/docs/mark.html#style-config)
- Arc (/vega-lite/docs/arc.html)
- Documentation Overview (/vega-lite/docs/arc.html#documentation-overview)
- Arc Mark Properties (/vega-lite/docs/arc.html#properties)
- Examples (/vega-lite/docs/arc.html#examples)
- Arc Config (/vega-lite/docs/arc.html#arc-config)
- Faceted Pie Charts (/vega-lite/docs/arc.html#faceted-pie-charts)
- Area (/vega-lite/docs/area.html)
- Documentation Overview (/vega-lite/docs/area.html#documentation-overview)
- Area Mark Properties (/vega-lite/docs/area.html#properties)
- Examples (/vega-lite/docs/area.html#examples)
- Area Config (/vega-lite/docs/area.html#config)
- Bar (/vega-lite/docs/bar.html)
- Documentation Overview (/vega-lite/docs/bar.html#documentation-overview)
- Bar Mark Properties (/vega-lite/docs/bar.html#properties)
- Examples (/vega-lite/docs/bar.html#examples)
- Bar Config (/vega-lite/docs/bar.html#config)
- Box Plot (/vega-lite/docs/boxplot.html)
- Documentation Overview (/vega-lite/docs/boxplot.html#documentation-overview)
- Box Plot Mark Properties (/vega-lite/docs/boxplot.html#properties)
- Types of Box Plot (/vega-lite/docs/boxplot.html#boxplot-types)
- Dimension & Orientation (/vega-lite/docs/boxplot.html#dims-orient)
- The Parts of Box Plots (/vega-lite/docs/boxplot.html#parts)
- Color, Size, and Opacity Encoding Channels (/vega-lite/docs/boxplot.html#color-size-and-opacity-encoding-channels)
- Tooltip Encoding Channels (/vega-lite/docs/boxplot.html#tooltip-encoding-channels)
- Mark Config (/vega-lite/docs/boxplot.html#config)
- Box Plot with Pre-Calculated Summaries (/vega-lite/docs/boxplot.html#box-plot-with-pre-calculated-summaries)
- Circle (/vega-lite/docs/circle.html)
- Circle Mark Properties (/vega-lite/docs/circle.html#properties)
- Examples (/vega-lite/docs/circle.html#examples)
- Circle Config (/vega-lite/docs/circle.html#config)
- Error Band (/vega-lite/docs/errorband.html)
- Documentation Overview (/vega-lite/docs/errorband.html#documentation-overview)
- Error Band Mark Properties (/vega-lite/docs/errorband.html#properties)
- Comparing the usage of Error Band to the usage of Error Bar (/vega-lite/docs/errorband.html#compare-to-errorbar)
- Using Error Band to Aggregate Raw Data (/vega-lite/docs/errorband.html#raw-usage)
- Using Error Band to Visualize Aggregated Data (/vega-lite/docs/errorband.html#pre-aggregated-usage)
- Dimension (/vega-lite/docs/errorband.html#dimension)
- The Parts of Error Band (/vega-lite/docs/errorband.html#parts)
- Color, and Opacity Encoding Channels (/vega-lite/docs/errorband.html#color-and-opacity-encoding-channels)
- Tooltip Encoding Channels (/vega-lite/docs/errorband.html#config)
- Mark Config (/vega-lite/docs/errorband.html#mark-config)
- Error Bar (/vega-lite/docs/errorbar.html)
- Documentation Overview (/vega-lite/docs/errorbar.html#documentation-overview)
- Error Bar Mark Properties (/vega-lite/docs/errorbar.html#properties)
- Using Error Bars to Aggregate Raw Data (/vega-lite/docs/errorbar.html#raw-usage)
- Using Error Bars to Visualize Aggregated Data (/vega-lite/docs/errorbar.html#pre-aggregated-usage)
- Dimension & Orientation (/vega-lite/docs/errorbar.html#dimension--orientation)
- The Parts of Error Bars (/vega-lite/docs/errorbar.html#parts)
- Color, and Opacity Encoding Channels (/vega-lite/docs/errorbar.html#color-and-opacity-encoding-channels)
- Tooltip Encoding Channels (/vega-lite/docs/errorbar.html#tooltip-encoding-channels)
- Mark Config (/vega-lite/docs/errorbar.html#config)
- Geoshape (/vega-lite/docs/geoshape.html)
- Geoshape Config (/vega-lite/docs/geoshape.html#config)
- Image (/vega-lite/docs/image.html)
- Documentation Overview (/vega-lite/docs/image.html#documentation-overview)
- Image Mark Properties (/vega-lite/docs/image.html#properties)
- Examples (/vega-lite/docs/image.html#examples)
- Image Config (/vega-lite/docs/image.html#image-config)
- Line (/vega-lite/docs/line.html)
- Documentation Overview (/vega-lite/docs/line.html#documentation-overview)
- Line Mark Properties (/vega-lite/docs/line.html#properties)
- Examples (/vega-lite/docs/line.html#examples)
- Line Config (/vega-lite/docs/line.html#config)
- Point (/vega-lite/docs/point.html)
- Documentation Overview (/vega-lite/docs/point.html#documentation-overview)
- Point Mark Properties (/vega-lite/docs/point.html#properties)
- Examples (/vega-lite/docs/point.html#examples)
- Point Config (/vega-lite/docs/point.html#config)
- Rect (/vega-lite/docs/rect.html)
- Documentation Overview (/vega-lite/docs/rect.html#documentation-overview)
- Rect Mark Properties (/vega-lite/docs/rect.html#properties)
- Examples (/vega-lite/docs/rect.html#examples)
- Rect Config (/vega-lite/docs/rect.html#config)
- Rule (/vega-lite/docs/rule.html)
- Documentation Overview (/vega-lite/docs/rule.html#documentation-overview)
- Rule Mark Properties (/vega-lite/docs/rule.html#properties)
- Examples (/vega-lite/docs/rule.html#examples)
- Rule Config (/vega-lite/docs/rule.html#config)
- Square (/vega-lite/docs/square.html)
- Square Mark Properties (/vega-lite/docs/square.html#properties)
- Example: Scatterplot with Square (/vega-lite/docs/square.html#example-scatterplot-with-square)
- Square Config (/vega-lite/docs/square.html#config)
- Text (/vega-lite/docs/text.html)
- Documentation Overview (/vega-lite/docs/text.html#documentation-overview)
- Text Mark Properties (/vega-lite/docs/text.html#properties)
- Examples (/vega-lite/docs/text.html#examples)
- Text Config (/vega-lite/docs/text.html#config)
- Tick (/vega-lite/docs/tick.html)
- Documentation Overview (/vega-lite/docs/tick.html#documentation-overview)
- Tick Mark Properties (/vega-lite/docs/tick.html#properties)
- Examples (/vega-lite/docs/tick.html#examples)
- Tick Config (/vega-lite/docs/tick.html#config)
- Trail (/vega-lite/docs/trail.html)
- Documentation Overview (/vega-lite/docs/trail.html#documentation-overview)
- Trail Mark Properties (/vega-lite/docs/trail.html#properties)
- Examples (/vega-lite/docs/trail.html#examples)
- Trail Config (/vega-lite/docs/trail.html#config)
- Encoding (/vega-lite/docs/encoding.html)
- Encoding Channels (/vega-lite/docs/encoding.html#channels)
- Channel Definition (/vega-lite/docs/encoding.html#channel-definition)
- Position Channels (/vega-lite/docs/encoding.html#position)
- Position Offset Channels (/vega-lite/docs/encoding.html#position-offset)
- Polar Position Channels (/vega-lite/docs/encoding.html#polar)
- Geographic Position Channels (/vega-lite/docs/encoding.html#geo)
- Mark Property Channels (/vega-lite/docs/encoding.html#mark-prop)
- Text and Tooltip Channels (/vega-lite/docs/encoding.html#text)
- Hyperlink Channel (/vega-lite/docs/encoding.html#href)
- Description Channel (/vega-lite/docs/encoding.html#description)
- Level of Detail Channel (/vega-lite/docs/encoding.html#detail)
- Key Channel (/vega-lite/docs/encoding.html#key)
- Order Channel (/vega-lite/docs/encoding.html#order)
- Facet Channels (/vega-lite/docs/encoding.html#facet)
- Aggregate (/vega-lite/docs/aggregate.html)
- Documentation Overview (/vega-lite/docs/aggregate.html#documentation-overview)
- Aggregate in Encoding Field Definition (/vega-lite/docs/aggregate.html#encoding)
- Aggregate Transform (/vega-lite/docs/aggregate.html#transform)
- Supported Aggregation Operations (/vega-lite/docs/aggregate.html#ops)
- Argmin / Argmax (/vega-lite/docs/aggregate.html#argmax)
- Axis (/vega-lite/docs/axis.html)
- Documentation Overview (/vega-lite/docs/axis.html#documentation-overview)
- Axis Properties (/vega-lite/docs/axis.html#axis-properties)
- Axis Config (/vega-lite/docs/axis.html#config)
- Band Position (/vega-lite/docs/bandposition.html)
- Examples (/vega-lite/docs/bandposition.html#examples)
- Bin (/vega-lite/docs/bin.html)
- Documentation Overview (/vega-lite/docs/bin.html#documentation-overview)
- Binning in Encoding Field Definition (/vega-lite/docs/bin.html#encoding)
- Bin Transform (/vega-lite/docs/bin.html#transform)
- Bin Parameters (/vega-lite/docs/bin.html#bin-parameters)
- Ordinal Bin (/vega-lite/docs/bin.html#ordinal-bin)
- Condition (/vega-lite/docs/condition.html)
- Conditional Field Definition (/vega-lite/docs/condition.html#field)
- Conditional Value Definition (/vega-lite/docs/condition.html#value)
- Datum (/vega-lite/docs/datum.html)
- Examples (/vega-lite/docs/datum.html#examples)
- Field (/vega-lite/docs/field.html)
- Format (/vega-lite/docs/format.html)
- Formatting Text Marks and Tooltips (/vega-lite/docs/format.html#formatting-text-marks-and-tooltips)
- Formatting Axis, Legend, and Header Labels (/vega-lite/docs/format.html#formatting-axis-legend-and-header-labels)
- Header (/vega-lite/docs/header.html)
- Documentation Overview (/vega-lite/docs/header.html#documentation-overview)
- Header Properties (/vega-lite/docs/header.html#header-properties)
- Header Config (/vega-lite/docs/header.html#config)
- Impute (/vega-lite/docs/impute.html)
- Documentation Overview (/vega-lite/docs/impute.html#documentation-overview)
- Impute in Encoding Field Definition (/vega-lite/docs/impute.html#encoding)
- Impute Transform (/vega-lite/docs/impute.html#transform)
- Legend (/vega-lite/docs/legend.html)
- Legend Types (/vega-lite/docs/legend.html#legend-types)
- Combined Legend (/vega-lite/docs/legend.html#combined-legend)
- Legend Properties (/vega-lite/docs/legend.html#legend-properties)
- Legend Config (/vega-lite/docs/legend.html#config)
- Scale (/vega-lite/docs/scale.html)
- Documentation Overview (/vega-lite/docs/scale.html#documentation-overview)
- Scale Types (/vega-lite/docs/scale.html#type)
- Scale Domains (/vega-lite/docs/scale.html#domain)
- Scale Ranges (/vega-lite/docs/scale.html#range)
- Common Scale Properties (/vega-lite/docs/scale.html#continuous)
- Continuous Scales (/vega-lite/docs/scale.html#continuous-scales)
- Discrete Scales (/vega-lite/docs/scale.html#discrete)
- Discretizing Scales (/vega-lite/docs/scale.html#discretizing)
- Disabling Scale (/vega-lite/docs/scale.html#disable)
- Configuration (/vega-lite/docs/scale.html#config)
- Stack (/vega-lite/docs/stack.html)
- Documentation Overview (/vega-lite/docs/stack.html#documentation-overview)
- Stack in Encoding Field Definition (/vega-lite/docs/stack.html#encoding)
- Stack Transform (/vega-lite/docs/stack.html#transform)
- Sort (/vega-lite/docs/sort.html)
- Documentation Overview (/vega-lite/docs/sort.html#documentation-overview)
- Sorting Continuous Fields (/vega-lite/docs/sort.html#sorting-continuous-fields)
- Sorting Discrete Fields (/vega-lite/docs/sort.html#sorting-discrete-fields)
- Time Unit (/vega-lite/docs/timeunit.html)
- Documentation Overview (/vega-lite/docs/timeunit.html#documentation-overview)
- Time Unit in Encoding Field Definition (/vega-lite/docs/timeunit.html#encoding)
- Time Unit Transform (/vega-lite/docs/timeunit.html#transform)
- UTC time (/vega-lite/docs/timeunit.html#utc)
- Time Unit Parameters (/vega-lite/docs/timeunit.html#params)
- Type (/vega-lite/docs/type.html)
- Quantitative (/vega-lite/docs/type.html#quantitative)
- Temporal (/vega-lite/docs/type.html#temporal)
- Ordinal (/vega-lite/docs/type.html#ordinal)
- Nominal (/vega-lite/docs/type.html#nominal)
- GeoJSON (/vega-lite/docs/type.html#geojson)
- Value (/vega-lite/docs/value.html)
- Projection (/vega-lite/docs/projection.html)
- Documentation Overview (/vega-lite/docs/projection.html#documentation-overview)
- Projection Properties (/vega-lite/docs/projection.html#projection-properties)
- Projection Types (/vega-lite/docs/projection.html#projection-types)
- Projection Configuration (/vega-lite/docs/projection.html#config)
- View Composition (/vega-lite/docs/composition.html)
- Documentation Overview (/vega-lite/docs/composition.html#documentation-overview)
- Faceting (/vega-lite/docs/composition.html#faceting)
- Layering (/vega-lite/docs/composition.html#layering)
- Concatenation (/vega-lite/docs/composition.html#concatenation)
- Repeating (/vega-lite/docs/composition.html#repeating)
- Resolution (/vega-lite/docs/composition.html#resolution)
- Facet (/vega-lite/docs/facet.html)
- Documentation Overview (/vega-lite/docs/facet.html#documentation-overview)
- Facet Operator (/vega-lite/docs/facet.html#facet-operator)
- Facet, Row, and Column Encoding Channels (/vega-lite/docs/facet.html#facet-row-and-column-encoding-channels)
- Resolve (/vega-lite/docs/facet.html#resolve)
- Facet Configuration (/vega-lite/docs/facet.html#config)
- Layer (/vega-lite/docs/layer.html)
- Example (/vega-lite/docs/layer.html#example)
- Concat (/vega-lite/docs/concat.html)
- Documentation Overview (/vega-lite/docs/concat.html#documentation-overview)
- Horizontal Concatenation (/vega-lite/docs/concat.html#hconcat)
- Vertical Concatenation (/vega-lite/docs/concat.html#vconcat)
- General (Wrappable) Concatenation (/vega-lite/docs/concat.html#concat)
- Resolve (/vega-lite/docs/concat.html#resolve)
- Concat Configuration (/vega-lite/docs/concat.html#config)
- Repeat (/vega-lite/docs/repeat.html)
- Documentation Overview (/vega-lite/docs/repeat.html#documentation-overview)
- Repeat Operator (/vega-lite/docs/repeat.html#repeat-operator)
- Row/Column/Layer Repeat Mapping (/vega-lite/docs/repeat.html#repeat-mapping)
- Examples (/vega-lite/docs/repeat.html#examples)
- Resolve (/vega-lite/docs/repeat.html#resolve)
- Repeat Configuration (/vega-lite/docs/repeat.html#config)
- Resolve (/vega-lite/docs/resolve.html)
- Example (/vega-lite/docs/resolve.html#example)
- Parameter (/vega-lite/docs/parameter.html)
- Documentation Overview (/vega-lite/docs/parameter.html#documentation-overview)
- Defining a Parameter (/vega-lite/docs/parameter.html#defining-a-parameter)
- Using Parameters (/vega-lite/docs/parameter.html#using-parameters)
- Selection Configuration (/vega-lite/docs/parameter.html#config)
- Value (/vega-lite/docs/param-value.html)
- Examples (/vega-lite/docs/param-value.html#examples)
- Expr (/vega-lite/docs/parameter.html)
- Documentation Overview (/vega-lite/docs/parameter.html#documentation-overview)
- Defining a Parameter (/vega-lite/docs/parameter.html#defining-a-parameter)
- Using Parameters (/vega-lite/docs/parameter.html#using-parameters)
- Selection Configuration (/vega-lite/docs/parameter.html#config)
- Bind (/vega-lite/docs/bind.html)
- Input Element Binding (/vega-lite/docs/bind.html#input-element-binding)
- Legend Binding (/vega-lite/docs/bind.html#legend-binding)
- Scale Binding (/vega-lite/docs/bind.html#scale-binding)
- Select (/vega-lite/docs/selection.html)
- Documentation Overview (/vega-lite/docs/selection.html#documentation-overview)
- Common Selection Properties (/vega-lite/docs/selection.html#selection-props)
- Point Selection Properties (/vega-lite/docs/selection.html#point)
- Interval Selection Properties (/vega-lite/docs/selection.html#interval)
- Config (/vega-lite/docs/config.html)
- Top-level Configuration (/vega-lite/docs/config.html#top-level-config)
- Format Configuration (/vega-lite/docs/config.html#format)
- Guide Configurations (/vega-lite/docs/config.html#axis-config)
- Mark Configurations (/vega-lite/docs/config.html#mark-config)
- Style Configuration (/vega-lite/docs/config.html#style-configuration)
- Scale and Scale Range Configuration (/vega-lite/docs/config.html#scale-config)
- Projection Configuration (/vega-lite/docs/config.html#projection-config)
- Selection Configuration (/vega-lite/docs/config.html#selection-config)
- Title Configuration (/vega-lite/docs/config.html#title-config)
- View & View Composition Configuration (/vega-lite/docs/config.html#view-config)
- Locale Configuration (/vega-lite/docs/config.html#aria-config)
- ARIA Configuration (/vega-lite/docs/config.html#aria-configuration)
- Property Types (/vega-lite/docs/types.html)
- Documentation Overview (/vega-lite/docs/types.html#documentation-overview)
- Primitive Types (/vega-lite/docs/types.html#primitive-types)
- Special Object Types (/vega-lite/docs/types.html#special-object-types)
- Date Time (/vega-lite/docs/datetime.html)
- Gradient (/vega-lite/docs/gradient.html)
- Linear Gradient (/vega-lite/docs/gradient.html#linear-gradient)
- Radial Gradient (/vega-lite/docs/gradient.html#radial-gradient)
- Gradient Stop (/vega-lite/docs/gradient.html#gradient-stop)
- Predicate (/vega-lite/docs/predicate.html)
- Field Predicate (/vega-lite/docs/predicate.html#field-predicate)
- Parameter Predicate (/vega-lite/docs/predicate.html#selection-predicate)
- Predicate Composition (/vega-lite/docs/predicate.html#composition)
- Tooltip (/vega-lite/docs/tooltip.html)
- Documentation Overview (/vega-lite/docs/tooltip.html#documentation-overview)
- Tooltip Based on Encoding (/vega-lite/docs/tooltip.html#encoding)
- Tooltip Based on Underlying Data Point (/vega-lite/docs/tooltip.html#data)
- Tooltip channel (/vega-lite/docs/tooltip.html#channel)
- Tooltip image (/vega-lite/docs/tooltip.html#tooltip-image)
- Disable tooltips (/vega-lite/docs/tooltip.html#disable-tooltips)
- Vega Tooltip plugin (/vega-lite/docs/tooltip.html#plugin)
- Invalid Data (/vega-lite/docs/invalid-data.html)
- Documentation Overview (/vega-lite/docs/invalid-data.html#documentation-overview)
- Mark Invalid Mode (/vega-lite/docs/invalid-data.html#mark-invalid-mode)
- Scale Output for Invalid Values (/vega-lite/docs/invalid-data.html#scale-output-for-invalid-values)
- Other solutions (/vega-lite/docs/invalid-data.html#other-solutions)

## Introduction to Vega-Lite
Source: https://vega.github.io/vega-lite/tutorials/getting_started.html

This tutorial will guide through the process of writing a visualization specification in Vega-Lite. We will walk you through all main components of Vega-Lite by adding each of them to an example specification one-by-one. After creating the example visualization, we will also guide you how to embed the final visualization on a web page.
We suggest that you follow along the tutorial by building a visualization in the online editor (https://vega.github.io/editor/#/custom/vega-lite). Extend your specification in the editor as you read through this tutorial. If something does not work as expected, compare your specifications with ones inside this tutorial.
## Tutorial Overview
- Tutorial Overview (#tutorial-overview)
- The Data (#the-data)
- Encoding Data with Marks (#encoding-data-with-marks)
- Data Transformation: Aggregation (#data-transformation-aggregation)
- Customize your Visualization (#customize-your-visualization)
- Publish your Visualization Online (#embed)
- Next Steps (#next-steps)
## The Data
Lets say you have a tabular data set with a categorical variable in the first column `a` and a numerical variable in the second column `b`.
| a | b |
| --- | --- |
| C | 2 |
| C | 7 |
| C | 4 |
| D | 1 |
| D | 2 |
| D | 6 |
| E | 8 |
| E | 4 |
| E | 7 |

We can represent this data as a JSON array (http://www.json.org/) in which each row is an object in the array.
```
[
  {"a": "C", "b": 2},
  {"a": "C", "b": 7},
  {"a": "C", "b": 4},
  {"a": "D", "b": 1},
  {"a": "D", "b": 2},
  {"a": "D", "b": 6},
  {"a": "E", "b": 8},
  {"a": "E", "b": 4},
  {"a": "E", "b": 7}
]

```

To visualize this data with Vega-Lite, we can add it directly to the `data` property in a Vega-Lite specification.
```
{
  "data": {
    "values": [
      {"a": "C", "b": 2},
      {"a": "C", "b": 7},
      {"a": "C", "b": 4},
      {"a": "D", "b": 1},
      {"a": "D", "b": 2},
      {"a": "D", "b": 6},
      {"a": "E", "b": 8},
      {"a": "E", "b": 4},
      {"a": "E", "b": 7}
    ]
  }
}

```

The `data` (/vega-lite/docs/data.html) property defines the data source of the visualization. In this example, we embed the data inline by directly setting `values` property. Vega-Lite also supports other types of data sources (/vega-lite/docs/data.html) besides inline data.
## Encoding Data with Marks
Now we have a data source but we havent defined yet how the data should be visualized.
Basic graphical elements in Vega-Lite are marks (/vega-lite/docs/mark.html). Marks provide basic shapes whose properties (such as position, size, and color) can be used to visually encode data, either from a data field (or a variable), or a constant value.
To show the data as a point, we can set the `mark` property to `point`.
Now, it looks like we get a point. In fact, Vega-Lite renders one point for each object in the array, but they are all overlapping since we have not specified each points position.
To visually separate the points, data variables can be mapped to visual properties of a mark. For example, we can encode (/vega-lite/docs/encoding.html) the variable `a` of the data with `x` channel, which represents the x-position of the points. We can do that by adding an `encoding` object with its key `x` mapped to a channel definition that describes variable `a`.
```
...
"encoding": {
  "x": {"field": "a", "type": "nominal"}
}
...

```

The `encoding` (/vega-lite/docs/encoding.html) object is a key-value mapping between encoding channels (such as `x`, `y`) and definitions of the mapped data fields. The channel definition describes the fields name (`field`) and its data type (/vega-lite/docs/type.html) (`type`). In this example, we map the values for field `a` to the encoding channel `x` (the x-location of the points) and set `a`s data type to `nominal`, since it represents categories. (See the documentation for more information about data types (/vega-lite/docs/type.html).)
In the visualization above, Vega-Lite automatically adds an axis with labels for the different categories as well as an axis title. However, 3 points in each category are still overlapping. So far, we have only defined a visual encoding for the field `a`. We can also map the field `b` to the `y` channel.
```
...
"y": {"field": "b", "type": "quantitative"}
...

```

This time we set the field type to be `quantitative` because the values in field `b` are numeric.
Now we can see the raw data points. Note that Vega-Lite automatically adds grid lines to the y-axis to facilitate comparison of the `b` values.
## Data Transformation: Aggregation
Vega-Lite also supports data transformation such as aggregation. By adding `"aggregate": "average"` to the definition of the `y` channel, we can see the average value of `a` in each category. For example, the average value of category `D` is `(1 + 2 + 6)/3 = 9/3 = 3`.
Great! You computed the aggregate values for each category and visualized the resulting value as a point. Typically aggregated values for categories are visualized using bar charts. To create a bar chart, we have to change the mark type from `point` to `bar`.
```
- "mark": "point"
+ "mark": "bar"

```

Since the quantitative value is on `y`, you automatically get a vertical bar chart. If we swap the `x` and `y` channel, we get a horizontal bar chart instead.
## Customize your Visualization
Vega-Lite automatically provides default properties for the visualization. You can further customize these values by adding more properties. For example, to change the title of the x-axis from `Average of b` to `Mean of b`, we can set the title property of the axis in the `x` channel.
## Publish your Visualization Online
You have learned about basic components of a Vega-Lite specification. Now, lets see how to publish your visualization.
You can use Vega-Embed (https://github.com/vega/vega-embed) to embed your Vega-Lite visualization in a webpage. For example, you can create a web page with the following content:
```
<!doctype html>
<html>
  <head>
    <title>Vega-Lite Bar Chart</title>
    <meta charset="utf-8" />

    <script src="https://cdn.jsdelivr.net/npm/vega@6.2.0"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@6.4.1"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@7.0.2"></script>

    <style media="screen">
      /* Add space between Vega-Embed links  */
      .vega-actions a {
        margin-right: 5px;
      }
    </style>
  </head>
  <body>
    <h1>Template for Embedding Vega-Lite Visualization</h1>
    <!-- Container for the visualization -->
    <div id="vis"></div>

    <script>
      // Assign the specification to a local variable vlSpec.
      var vlSpec = {
        $schema: 'https://vega.github.io/schema/vega-lite/v6.json',
        data: {
          values: [
            {a: 'C', b: 2},
            {a: 'C', b: 7},
            {a: 'C', b: 4},
            {a: 'D', b: 1},
            {a: 'D', b: 2},
            {a: 'D', b: 6},
            {a: 'E', b: 8},
            {a: 'E', b: 4},
            {a: 'E', b: 7},
          ],
        },
        mark: 'bar',
        encoding: {
          y: {field: 'a', type: 'nominal'},
          x: {
            aggregate: 'average',
            field: 'b',
            type: 'quantitative',
            axis: {
              title: 'Average of b',
            },
          },
        },
      };

      // Embed the visualization in the container with id `vis`
      vegaEmbed('#vis', vlSpec);
    </script>
  </body>
</html>

```

In this webpage, we first load the dependencies for Vega-Lite (Vega-Embed, Vega, and Vega-Lite) in the `<head/>` tag of the document. We also create an HTML `<div/>` element with id `vis` to serve as a container for the visualization.
In the JavaScript code, we create a variable `vlSpec` that holds the Vega-Lite specification in JSON format. The `vegaEmbed` method translates a Vega-Lite specification into a Vega specification and then calls the Vega Runtime (https://vega.github.io/vega/usage/) to display visualization in the container `<div/>` element.
If viewed in a browser, this page displays our bar chart like on our demo page (/vega-lite/demo.html). You can also fork our Vega-Lite Block example (https://bl.ocks.org/domoritz/455e1c7872c4b38a58b90df0c3d7b1b9).
## Next Steps
Now you can create a website that embeds a Vega-Lite specification. If you want to learn more about Vega-Lite, please feel free to:
- Read the next tutorial (/vega-lite/tutorials/explore.html).
- See the examples gallery (/vega-lite/examples/).
- Build your own visualizations in the online editor (https://vega.github.io/editor/#/custom/vega-lite).
- Browse through the documentation (/vega-lite/docs/).
- See the list of applications (/vega-lite/ecosystem.html) that you can use Vega-Lite with.

## Embedding Vega-Lite
Source: https://vega.github.io/vega-lite/usage/embed.html

Fork our Vega-Lite Block (https://bl.ocks.org/domoritz/455e1c7872c4b38a58b90df0c3d7b1b9) if you want to quickly publish a Vega-Lite visualization on the web.
The easiest way to use Vega-Lite on your own web page is with Vega-Embed (https://github.com/vega/vega-embed), a library we built to make the process as painless as possible.
## Get Vega-Lite and other dependencies
To embed a Vega-Lite specification on your web page first load the required libraries. You can get Vega, Vega-Lite, and Vega-Embed via a CDN, NPM, or manually download them.
### CDN
For production deployments you will likely want to serve your own files or use a content delivery network (CDN) (https://en.wikipedia.org/wiki/Content_delivery_network). Vega-Lite releases are hosted on jsDelivr (https://www.jsdelivr.com/package/npm/vega-lite):
```
<script src="https://cdn.jsdelivr.net/npm/vega@6.2.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@6.4.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@7.0.2"></script>

```

If you want to automatically use the latest versions of Vega-Lite, Vega, and Vega-Embed, you can specify only the major version.
```
<script src="https://cdn.jsdelivr.net/npm/vega@6"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@6"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@7"></script>

```

### NPM
If you prefer to host the dependencies yourself, we suggest that you use npm to install the libraries (Vega (https://www.npmjs.com/package/vega), Vega-Lite (https://www.npmjs.com/package/vega-lite), and Vega-Embed (https://www.npmjs.com/package/vega-embed)) to get the latest stable version. To install with npm, simply install it as you would any other npm module.
```
npm install vega
npm install vega-lite
npm install vega-embed

```

You can learn more about NPM on the official website (https://docs.npmjs.com/getting-started/what-is-npm).
### Download
Alternatively, you can download the latest Vega-Lite release (https://github.com/vega/vega-lite/releases/latest) and add it to your project manually. In this case, you will also have to download Vega (https://github.com/vega/vega/releases/latest), and Vega-Embed (https://github.com/vega/vega-embed/releases/latest).
## Start using Vega-Lite with Vega-Embed
The next step after getting the libraries is to create a DOM element that the visualization will be attached to.
```
<div id="vis"></div>

```

Then use Vega-Embeds provided function to embed your spec.
```
// More argument info at https://github.com/vega/vega-embed
vegaEmbed('#vis', yourVlSpec);

```

Vega-Embed automatically adds links to export an image, view the source, and open the specification in the online editor. These links can be individually disabled. For more information, read the Vega-Embed documentation (https://github.com/vega/vega-embed).
Here is the final HTML file in the easiest way to embed Vega-Lite (assuming that you use the CDN approach (#cdn) from above). See the output in your browser (/vega-lite/demo.html).
```
<!doctype html>
<html>
  <head>
    <title>Embedding Vega-Lite</title>
    <script src="https://cdn.jsdelivr.net/npm/vega@6.2.0"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@6.4.1"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@7.0.2"></script>
  </head>
  <body>
    <div id="vis"></div>

    <script type="text/javascript">
      var yourVlSpec = {
        $schema: 'https://vega.github.io/schema/vega-lite/v6.json',
        description: 'A simple bar chart with embedded data.',
        data: {
          values: [
            {a: 'A', b: 28},
            {a: 'B', b: 55},
            {a: 'C', b: 43},
            {a: 'D', b: 91},
            {a: 'E', b: 81},
            {a: 'F', b: 53},
            {a: 'G', b: 19},
            {a: 'H', b: 87},
            {a: 'I', b: 52},
          ],
        },
        mark: 'bar',
        encoding: {
          x: {field: 'a', type: 'ordinal'},
          y: {field: 'b', type: 'quantitative'},
        },
      };
      vegaEmbed('#vis', yourVlSpec);
    </script>
  </body>
</html>

```

## Vega-Lite Ecosystem
Source: https://vega.github.io/vega-lite/ecosystem.html

This is an incomplete list of integrations, applications, and extensions of the Vega-Lite language and compiler. If you want to add a tool or library, edit this file and send us a pull request (https://github.com/vega/vega-lite/blob/main/site/ecosystem.md).
We mark featured plugins and tools with a .
## Tools for Authoring Vega-Lite Visualizations
-  Vega-Editor (https://vega.github.io/editor/), the online editor for Vega and Vega-Lite. You can also get an output Vega spec from a given Vega-Lite spec as well.
-  Vega Viewer (https://github.com/RandomFractals/vscode-vega-viewer), a VSCode extension for interactive preview of Vega and Vega-Lite maps and graphs.
- vega-desktop (https://github.com/kristw/vega-desktop), a desktop app that lets you open `.vg.json` and `.vl.json` to see visualizations just like you open image files with an image viewer. This is useful for creating visualizations with Vega/Vega-Lite locally (https://medium.com/@kristw/create-visualizations-with-vega-on-your-machine-using-your-preferred-editor-529e1be875c0).
-  Voyager (2) (https://github.com/vega/voyager), visualization tool for exploratory data analysis that blends a Tableau-style specification interface (formerly Polestar (https://github.com/vega/polestar)) with chart recommendations (formerly the Voyager visualization browser) and generates Vega-Lite visualizations.
- Bayes (https://bayes.com) - A creative data exploration and storytelling tool. Easily create and publish Vega-Lite visualizations.
- data.world Chart Builder (https://data.world/integrations/chart-builder), a chart builder that imports data from queries in data.world. The generated specs can be saved locally or uploaded back to data.world. Project is open source (https://github.com/datadotworld/chart-builder).
- ColorBrewer-Lite (https://github.com/vis-au/colorbrewer), a fork of the ColorBrewer project that allows importing Vega-Lite specifications into the ColorBrewer interface to pick effective color schemes in situ for any color encoding.
- Emacs Vega View (https://github.com/applied-science/emacs-vega-view), a tool that allows one to view Vega visualizations directly within emacs, currently supporting specs written in JSON, elisp or clojure.
- Codimd (https://github.com/hackmdio/codimd), realtime collaborative markdown notes editor with support of various diagram syntaxes including Vega-Lite (https://hackmd.io/c/codimd-documentation/%2F%40codimd%2Fextra-supported-syntax#Vega-Lite).
- Ivy (http://ivy-vis.netlify.app/), an Integrated Visualization Editing environment that wraps Vega-Lite (among other declarative visualization grammars) as templates to facilitate reuse, exploration, and opportunistic creation. Includes an in-app reproduction of Polestar (https://github.com/vega/polestar).
- Deneb (https://deneb-viz.github.io), a Power BI custom visual with an editor for Vega-Lite or Vega specifications.
- VizLinter (https://vizlinter.idvxlab.com/), an online editor that detects and fixes encoding issues based on vega-lite-linter.
- Datapane (https://github.com/datapane/datapane), a Python framework for building interactive reports from open-source visualization formats such as Vega-Lite.
- Graphpad (https://www.figma.com/community/widget/1027276088284051809), an editor for creating Vega-Lite or Vega visualizations in the Figma and Figjam collaborative design/whiteboarding tools.
- Datadog (https://www.datadoghq.com/), the monitoring and security platform, has a browser editor for Vega-Lite visualizations in several places: in dashboards and notebooks through the Wildcard Widget (https://www.datadoghq.com/blog/wildcard-widget/), and in low-code apps through custom charts (https://docs.datadoghq.com/actions/app_builder/components/custom_charts/).
## Tools for Scaling Vega-Lite Visualizations
- altair-transform (https://github.com/altair-viz/altair-transform), a Python library for pre-evaluating Altair/Vega-Lite transforms with Pandas.
- ibis-vega-transform (https://github.com/Quansight/ibis-vega-transform), a Python library and JupyterLab extension for evaluating Altair/Vega-Lite transforms with external databases using Ibis (https://ibis-project.org/).
- StatisticalGraphics.jl (https://sl-solution.github.io/StatisticalGraphics.jl/stable/Plots/), a Julia library for statistical graphics.
-  VegaFusion (https://vegafusion.io/), a Rust library and Python API that provides server-side acceleration for interactive Altair/Vega-Lite visualizations using Apache Arrow (https://arrow.apache.org/) and DataFusion (https://arrow.apache.org/datafusion/).
- Scalable Vega (https://github.com/vega/scalable-vega), a demo of how to scale Vega to large datasets by implementing a custom transform that accepts SQL queries and requests data from an external database.
## Plug-ins for Vega-Lite
-  Tooltips for Vega and Vega-Lite (https://github.com/vega/vega-lite-tooltip)
- Leaflet Tile Map integration for Vega and Vega-Lite (https://github.com/nyurik/leaflet-vega)
## Bindings for Programming Languages
-  Altair (https://altair-viz.github.io) exposes a Python API for building statistical visualizations that follows Vega-Lite syntax.
-  Vega-Lite API (https://github.com/vega/vega-lite-api) is a JavaScript API for creating Vega-Lite JSON specifications.
-  elm-vegaLite (https://package.elm-lang.org/packages/gicentre/elm-vegalite/latest) generates Vega-Lite specifications in the pure functional language Elm (https://elm-lang.org).
- Altair wrapper in R (https://vegawidget.github.io/altair/)
- ipyvega (https://github.com/vega/ipyvega) supports Vega and Vega-Lite charts in Jupyter Notebooks.
- VegaLite (Elixir bindings) (https://github.com/elixir-nx/vega_lite).
-  VegaLite.jl (https://github.com/queryverse/VegaLite.jl) are Julia bindings to Vega and Vega-Lite.
- Deneb.jl (https://github.com/brucala/Deneb.jl) is a convenient Julia API for creating Vega-Lite visualizations.
- Vega-Lite bindings for R (https://github.com/hrbrmstr/vegalite), create Vega-Lite visualizations in R.
- vegaliteR (https://github.com/timelyportfolio/vegaliteR), vega-lite htmlwidget for R.
- Vegas (https://github.com/aishfenton/Vegas) brings visualizations to Scala and Spark using Vega-Lite.
- Smile (https://haifengl.github.io/) is a machine learning engine for JVM using Vega-Lite.
- vegawidget (https://vegawidget.github.io/vegawidget), low-level interface in R to render Vega and Vega-Lite specifications as htmlwidgets, including functions to interact with data, events, and signals in Shiny (https://shiny.rstudio.com).
- vegabrite (https://vegawidget.github.io/vegabrite), functional interface for building up Vega-Lite specifications in R. Built on top of the lower-level interface provided by vegawidget
- Hanami (https://github.com/jsa-aerial/hanami) A Clojure(Script) library for creating domain specific interactive visualization applications. Exposes a parameterized template system that uses recursive transformation to finished Vega-Lite and Vega specs. Built with reagent (https://reagent-project.github.io/) (react) and re-com (https://github.com/Day8/re-com) enabled.
- Vizard (https://github.com/yieldbot/vizard) tiny REPL client to visualize Clojure data in browser w/ Vega-Lite.
- Oz (https://github.com/metasoarous/oz) is a Vega & Vega-Lite based visualization and scientific document toolkit for Clojure & ClojureScript (Reagent). Originally a fork of Vizard, Oz adds support for Vega, publishing/sharing, markdown & hiccup extensions for embedding Vega-Lite & Vega visualizations in html documents, static html output, and Jupyter notebooks.
- Vizsla (https://github.com/gjmcn/vizsla) is a simple JavaScript API for Vega-Lite.
- Vega node for Node-RED Dashboard (https://flows.nodered.org/node/node-red-node-ui-vega) supports Vega and Vega-Lite visualizations on the Node-RED (https://nodered.org/) flow-based programming tool.
- hvega (https://hackage.haskell.org/package/hvega) generates Vega-Lite specifications in Haskell and is based on Elm-Vega.
- Vega-Lite bindings for Rust (https://github.com/procyon-rs/vega_lite_3.rs), create vega-lite v3, or v4 (https://github.com/procyon-rs/vega_lite_4.rs), vizualizations in Rust A high-level like Altair in under construction at procyon (https://github.com/procyon-rs/procyon)
- Vega.rb (https://github.com/ankane/vega) brings Vega and Vega-Lite to Ruby.
- Jekyll Diagrams (https://github.com/zhustec/jekyll-diagrams) A Jekyll plugin with support for Vega & Vega-Lite and others diagramming libraries.
- Liquid Diagrams (https://github.com/zhustec/liquid-diagrams) A Liquid plugin with support for Vega & Vega-Lite and others diagramming libraries.
- Vega-Lite-Linter (https://github.com/idvxlab/vega-lite-linter) is a python package to help users detect and fix encoding issues.
- VegaLite (https://github.com/JoshDavid/VegaLite) is a library for Dyalog APL (https://www.dyalog.com) to build and render Vega-Lite specifications from your data.
- React Spectrum Charts (https://github.com/adobe/react-spectrum-charts) are declarative visualization components from Adobe using Vega and Vega-Lite.
- vega-view (https://github.com/cuprous-au/vega-view) displays nushell (https://www.nushell.sh/) tables using Vega-Lite in a webview.
## Programming / Data Science Environment that supports Vega-Lite
-  JupyterLab (https://github.com/jupyterlab/jupyterlab), an extensible environment for interactive and reproducible computing, based on the Jupyter Notebook and Architecture.
- nteract (https://github.com/nteract/nteract), interactive notebook application with Vega and Vega-Lite renderer.
-  Observable (https://beta.observablehq.com/), an interactive JavaScript notebook. Embed example (https://beta.observablehq.com/@domoritz/hello-vega-embed) and exploration example (https://beta.observablehq.com/@mbostock/exploring-data-with-vega-lite).
- data.world (https://data.world), upload `.vg.json` and `.vl.json` files along side your raw data, or embed Vega (https://docs.data.world/tutorials/markdown/#vega-and-vega-lite) directly into comments and summary markdown.
- nextjournal (https://nextjournal.com/), scientific computing environment with support for data visualizations including Vega-Lite (https://nextjournal.com/blog/plotting-with-vega-lite-in-nextjournal)
- Liminoid (https://liminoid.io/), toolkit for building interactive analytics applications with Python and WebAssembly. Can pass Python data to JavaScript callbacks which render Vega/Vega-Lite specifications.
- Neptune.ai (https://neptune.ai), machine learning experiment tracking tool with Vega-Lite and Altair visualizations.
- Livebook (https://github.com/elixir-nx/livebook), Interactive and collaborative code notebooks with Vega-Lite visualizations.
- Hex (https://hex.tech) is a data science platform that uses Vega-Lite visualizations.
## Tools that use Vega-Lite
- Lyra (https://github.com/vega/lyra), an interactive, graphical Visualization Design Environment (VDE)
-  PdVega (https://altair-viz.github.io/pdvega/), lets you create interactive Vega-Lite plots for Pandas. Uses ipyvega (https://github.com/vega/ipyvega).
- Turi Create (https://github.com/apple/turicreate) Apples tool to simplify the development of custom machine learning models.
- mondrian-rest-ui (https://github.com/jazzido/mondrian-rest-ui), an experimental UI for `mondrian-rest` (https://github.com/jazzido/mondrian-rest) inspired by Polestar (https://github.com/vega/polestar) and CubesViewer (https://github.com/jjmontesl/cubesviewer).
- Django Chartflo (https://github.com/synw/django-chartflo), charts for the lazy ones in Django
- Vega-Lite for PowerBI (https://github.com/Microsoft/vegalite-for-powerbi/) is an example of a PowerBI custom visual built with Vega-Lite.
- Sci-Hub stats browser (https://github.com/greenelab/scihub) provides coverage and usage statistics for Sci-Hub.
- github-repo-stats (https://github.com/jgehrcke/github-repo-stats), a GitHub Action for advanced repository traffic analysis and reporting.
- Iris (https://hackernoon.com/a-conversational-agent-for-data-science-4ae300cdc220), a conversational agent for data science.
- dashcard (https://github.com/scottcame/dashcard): a simple Bootstrap (https://getbootstrap.com/)-based UI for dynamic dashboarding using Vega-Lite and Mondrian (https://community.hds.com/docs/DOC-1009853) via a REST API (https://github.com/ojbc/mondrian-rest).
- histbook (https://github.com/diana-hep/histbook), a versatile, high-performance histogram toolkit for Numpy.
- Olmsted (https://github.com/matsengrp/olmsted): a web application for biologists to explore and visualize the adapative immune system using deep sequenced B-cell receptor data. The app uses Vegas interactive capabilities in the context of a React/Redux application to allow users to drill down into the data at multiple levels of granularity, and is currently being used by HIV researchers in the quest for a vaccine. Demo available here (https://olmstedviz.org).
- Lens.org (https://www.lens.org/): Provides free search and analysis for millions of patents and scholarly works. Simplified interface for creating Vega-Lite data visualisations.
- DataVoyager.jl (https://github.com/queryverse/DataVoyager.jl), a Julia package that exposes the Voyager (2) (https://github.com/vega/voyager) UI to the Julia programming language.
- ProfileVega.jl (https://github.com/davidanthoff/ProfileVega.jl), a Julia profile visualization tool that uses Vega-Lite.
- Voyager clone (https://matyunya-simple-voyager-clone.ellx.app), a basic Voyager clone with step-by-step tutorial made with Ellx (https://ellx.io).
- NL4DV (https://nl4dv.github.io/nl4dv/), a Python toolkit that generates analytic specifications (attributes + tasks + Vega-Lite visualizations) from natural language (NL) queries, helping people prototype NL systems for data visualization.
- Saite (https://github.com/jsa-aerial/saite) Interactive exploratory graphics and ad hoc visualization application for Clojure(Script). Built on top of Hanami (https://github.com/jsa-aerial/hanami).
- Datablocks (https://datablocks.pro), a node-based editor for exploring, analyzing and transforming data without code.
- Rath (https://github.com/Kanaries/Rath) An augmented analysis tool including auto-EDA, pattern discovery, multi-dimensional visualization recommendation, and interactive dashboards generation.
- MarkText (https://github.com/marktext/marktext): An open-source markdown editor that supports Vega-Lite.
- Scalene (https://github.com/plasma-umass/scalene): A CPU+GPU+memory profiler for Python.
- CSrankings (https://csrankings.org): a metrics-based ranking of top computer science institutions around the world.
- Kibana (https://github.com/elastic/kibana): a browser-based analytics and search dashboard for Elasticsearch that supports authoring and embedding Vega and Vega-Lite visualizations (https://www.elastic.co/guide/en/kibana/current/vega.html).
- PyGWalker (https://github.com/Kanaries/pygwalker) A python library that turns your data into an interactive visual exploration app with one line of code.
- GWalkR (https://github.com/Kanaries/GWalkR) An R library that turns your dataframe into an interactive visual exploration app in RStudio.
- graphic-walker (https://github.com/Kanaries/graphic-walker), an open-source alternative to Tableau, is a versatile visualization tool for data exploration and no-code Vega-Lite editing, that can be easily embedded as a component in web apps.
## Tools for Embedding Vega-Lite Visualizations
-  Vega-Embed (https://github.com/vega/vega-embed), a convenience wrapper for Vega and Vega-Lite.
-  Flourish (https://flourish.studio/2018/05/29/vega-lite-in-flourish/) - Visualization and Storytelling Platform
- Visdown (http://visdown.com), a web app to create Vega-Lite visualizations in Markdown. Specs are written in YAML (http://www.yaml.org/) (not JSON) within `code` blocks.
- vega-element (https://www.webcomponents.org/element/PolymerVis/vega-element) is a Polymer web component to embed Vega or Vega-Lite visualization using custom HTML tags.
- marked-vega (https://www.webcomponents.org/element/PolymerVis/marked-vega) is a Polymer web component to parse image/code markdowns into Vega and Vega-Lite charts.
- gulp-marked-vega (https://github.com/e2fyi/gulp-marked-vega) is a gulp plugin (comes with a cli tool also) to replace marked-vega (https://www.webcomponents.org/element/PolymerVis/marked-vega) markdown syntax with base64 embedded image tags, so that any standard markdown parser can render the Vega and Vega-Lite charts without modifying their render rules.
- idyll-vega-lite (https://github.com/idyll-lang/idyll-vega-lite) is a component that allows you to embed Vega-Lite graphics inside of Idyll markup (https://idyll-lang.org), an interactive markup language.
- generator-veeg (https://github.com/millette/generator-veeg) is a Vega and Vega-Lite boilerplate generator for Yeoman (https://yeoman.io/).
- Kroki (https://kroki.io/) is a service to render Vega and Vega-Lite as PNG, SVG, or PDF.
- vega_embed_flutter (https://pub.dev/packages/vega_embed_flutter), a flutter-web widget to embed Vega-Lite specs into flutter-web apps.
- vegalite-wordpress-plugin (https://github.com/wikimedia/vegalite-wordpress-plugin) enables viewing and editing Vega-Lite in a WordPress site.

