# Geo

Generated from https://vega.github.io/vega-lite/ on 2026-01-11.

## Projection
Source: https://vega.github.io/vega-lite/docs/projection.html

A cartographic projection maps longitude and latitude pairs to x, y coordinates. As with Vega, one can use projections in Vega-Lite to layout both geographic points (such as locations on a map) represented by longitude and latitude coordinates, or to project geographic regions (such as countries and states) represented using the GeoJSON format. Projections are specified at the unit specification level, alongside encoding. Geographic coordinate data can then be mapped to `longitude` and `latitude` channels (encoding.html#geo) (and `longitude2` and `latitude2` for ranged marks).
For example, this example chart shows all airports in the United States by projecting `latitude`, `longitude` as `x`, `y` coordinates using the albersUsa projection.

See the example gallery for more examples with geographic projection (../examples/#maps-geographic-displays).
## Documentation Overview
- Projection Properties (#projection-properties)
- Projection Types (#projection-types)
- Projection Configuration (#config)
## Projection Properties
| Property | Type | Description |
| --- | --- | --- |
| type | String | ExprRef | The cartographic projection to use. This value is case-insensitive, for example "albers" and "Albers" indicate the same projection type. You can find all valid projection types in the documentation . Default value: equalEarth |
| center | Array | ExprRef | The projections center, a two-element array of longitude and latitude in degrees. Default value: [0, 0] |
| clipAngle | Number | ExprRef | The projections clipping circle radius to the specified angle in degrees. If null , switches to antimeridian cutting rather than small-circle clipping. |
| clipExtent | Array | ExprRef | The projections viewport clip extent to the specified bounds in pixels. The extent bounds are specified as an array [[x0, y0], [x1, y1]] , where x0 is the left-side of the viewport, y0 is the top, x1 is the right and y1 is the bottom. If null , no viewport clipping is performed. |
| fit | Fit | Fit[] | ExprRef |  |
| parallels | Number[] | ExprRef | For conic projections, the two standard parallels that define the map layout. The default depends on the specific conic projection used. |
| pointRadius | Number | ExprRef | The default radius (in pixels) to use when drawing GeoJSON Point and MultiPoint geometries. This parameter sets a constant default value. To modify the point radius in response to data, see the corresponding parameter of the GeoPath and GeoShape transforms. Default value: 4.5 |
| precision | Number | ExprRef | The threshold for the projections adaptive resampling to the specified value in pixels. This value corresponds to the DouglasPeucker distance . If precision is not specified, returns the projections current resampling precision which defaults to 0.5  0.70710... . |
| rotate | Array | Array | ExprRef | The projections three-axis rotation to the specified angles, which must be a two- or three-element array of numbers [ lambda , phi , gamma ] specifying the rotation angles in degrees about each spherical axis. (These correspond to yaw, pitch and roll.) Default value: [0, 0, 0] |
| scale | Number | ExprRef | The projections scale (zoom) factor, overriding automatic fitting. The default scale is projection-specific. The scale factor corresponds linearly to the distance between projected points; however, scale factor values are not equivalent across projections. |
| translate | Array | ExprRef | The projections translation offset as a two-element array [tx, ty] . |

If you want to explore the various available properties in more depth, Vegas projection documentation hosts a useful demo (https://vega.github.io/vega/docs/projections/)
In addition to the shared properties above, the following properties are supported for specific projection types in the d3-geo-projection (https://github.com/d3/d3-geo-projection) library: `coefficient` (https://github.com/d3/d3-geo-projection#hammer_coefficient), `distance` (https://github.com/d3/d3-geo-projection#satellite_distance), `fraction` (https://github.com/d3/d3-geo-projection#bottomley_fraction), `lobes` (https://github.com/d3/d3-geo-projection#berghaus_lobes), `parallel` (https://github.com/d3/d3-geo-projection#armadillo_parallel), `radius` (https://github.com/d3/d3-geo-projection#gingery_radius), `ratio` (https://github.com/d3/d3-geo-projection#hill_ratio), `spacing` (https://github.com/d3/d3-geo-projection#lagrange_spacing), `tilt` (https://github.com/d3/d3-geo-projection#satellite_tilt).
Note: All properties (#properties) of projections are optional with defaults as defined in the Vega projection properties (https://vega.github.io/vega/docs/projections/#properties). Because of this, marks that dont have explicitly defined projections may implicitly derive a projection. Implicit projections will be added for any `geoshape` (geoshape.html) mark, any encoding with field of `geojson` (type.html#geojson) type, and encoding with `latitude` (encoding.html#geo) or `longitude` (encoding.html#geo) channels.
## Projection Types
Vega-Lite includes all cartographic projections provided by the d3-geo (https://github.com/d3/d3-geo#) library.
| Type | Description |
| --- | --- |
| albers | The Albers equal-area conic projection. This is a U.S.-centric configuration of "conicEqualArea" . |
| albersUsa | A U.S.-centric composite with projections for the lower 48 states, Hawaii, and Alaska (scaled to 0.35 times the true relative area). |
| azimuthalEqualArea | The azimuthal equal-area projection. |
| azimuthalEquidistant | The azimuthal equidistant projection. |
| conicConformal | The conic conformal projection. The parallels default to [30, 30] resulting in flat top. |
| conicEqualArea | The Albers equal-area conic projection. |
| conicEquidistant | The conic equidistant projection. |
| equalEarth | The Equal Earth projection, by Bojan Savric et al., 2018. |
| equirectangular | The equirectangular (plate carree) projection, akin to use longitude, latitude directly. |
| gnomonic | The gnomonic projection. |
| identity | The identity projection. Also supports additional boolean reflectX and reflectY parameters. |
| mercator | The spherical Mercator projection. Uses a default clipExtent such that the world is projected to a square, clipped to approximately 85 latitude. |
| orthographic | The orthographic projection. |
| stereographic | The stereographic projection. |
| transverseMercator | The transverse spherical Mercator projection. Uses a default clipExtent such that the world is projected to a square, clipped to approximately 85 latitude. |

## Projection Configuration
```
// Top-level View Specification
{
  ...,
  "config": {          // Configuration Object
    "projection": { ... },   // - Projection Configuration
    ...
  }
}

```

The `projection` property of the `config` (config.html) object determines the default properties and transformations applied to different types of projections (projection.html). The projection config can contain any of the projection properties as specified above (#properties).

