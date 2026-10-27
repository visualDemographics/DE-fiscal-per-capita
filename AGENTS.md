# Visual Artifact & Plotting Guidelines

## Vector-First Rendering & Anti-Pixel-Surgery Invariant
1. **Never Perform Destructive In-Memory Canvas Surgery**: Never attempt to "patch" raster images (PNG, JPEG) by drawing opaque background-colored polygons (`base_draw.polygon`) or bounding-box clear zones to erase and manually redraw chart elements (ribbons, lines, bars). Destructive pixel clearing risks obliterating adjacent text labels, anti-aliased edges, node rects, and text halos.
2. **Simple Direct Conversion Over Workaround Tangents**: When a vector graphic (SVG) is verified, clean, and accurate but the raster export is flawed, do not spend turns reverse-engineering internal rendering engines, CDP/browser internals, or complex in-place PIL surgery. Either:
   - Use a simple, deterministic standalone conversion script/utility to render PNG from the verified SVG, or
   - Keep the native generator pipeline clean without invasive raster post-processing.
3. **Time-Boxing Low-Level Debugging**: If an export workaround exceeds 2–3 turns without a clean, minimal solution, stop the tangent, assess the direct path (e.g. converting from the clean vector source), and consult the user or propose a simple conversion approach.

