---
name: vega-lite-docs
description: "Author and debug Vega-Lite specifications for web data visualizations, including embedding with vega-embed. Use when a task needs Vega-Lite chart specs, encoding/channel choices, transforms, compositions (layer/facet/concat/repeat), interactions (params/selection), or axis/scale/legend configuration."
---

# Vega-Lite Docs

## Overview

Use this skill to turn datasets and chart requirements into accurate Vega-Lite specs, then embed them in web apps. Lean on the reference files for precise property names, defaults, and examples.

## Workflow

### 1) Clarify the chart intent and data
- Identify fields, data types (quantitative, temporal, ordinal, nominal), and grain.
- Confirm whether aggregations, bins, or time units are needed.
- Decide if a single view, layered chart, or faceted grid fits best.

### 2) Draft the spec skeleton
- Start with top-level fields: `data`, `mark`, `encoding`, optional `transform`, `config`.
- Prefer the simplest spec that matches the goal, then add detail.
- Use inline `values` for small data or `url` + `format` for external data.

Example skeleton:

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {"url": "data.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"field": "category", "type": "nominal"},
    "y": {"field": "value", "type": "quantitative"}
  }
}
```

### 3) Refine encodings and transforms
- Add `aggregate`, `bin`, `timeUnit`, and `stack` only when required.
- Use `transform` for calculated fields, filtering, and reshaping.
- Validate channel compatibility with mark type and data types.

### 4) Compose and present
- Use `layer`, `facet`, `concat`, or `repeat` for multi-view layouts.
- Control scales, axes, and legends for readability and consistent design.
- Add `tooltip`, `title`, and formatting for clarity.

### 5) Add interaction and embed
- Use `params`/`selection` for hover/brush/filter interactions.
- Embed with `vega-embed` and pass the spec directly in JS/TS.

## Reference Map

Use these files as needed (only load the ones relevant to the request):
- `references/intro-and-embed.md` - getting started, ecosystem, and embed usage.
- `references/spec-core.md` - top-level spec, data, mark, config, invalid data.
- `references/encoding-and-fields.md` - channels, field defs, types, sort/stack/bandposition, constants, datetime.
- `references/presentation.md` - axis, legend, scale, format, header, title, tooltip, gradients.
- `references/marks.md` - mark types and mark-specific properties.
- `references/transforms.md` - transform pipeline and all transform types.
- `references/composition.md` - layer/concat/facet/repeat and resolve rules.
- `references/interaction-params.md` - parameters, selections, bindings, predicates.
- `references/geo.md` - projections for geospatial charts.

## Script

- `scripts/fetch_vega_lite_docs.py` refreshes the reference files from the official docs (requires network access).
