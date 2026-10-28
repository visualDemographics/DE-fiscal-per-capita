# Visual Artifact & Plotting Guidelines

## 1. Sovereign Tier Aesthetic & Color Unification Invariants
1. **Unified Tier Colors in Layer 1**: Every node and link originating in Layer 1 must be strictly color-coded by its sovereign intake authority:
   - **Statutory Social Insurance**: Teal (`#0d9488`, links `rgba(13, 148, 136, 0.45)`)
   - **Federal Republic (*Bund*)**: Navy (`#1e3a8a`, links `rgba(30, 58, 138, 0.45)`)
   - **Free State of Bavaria (*Bayern*)**: Sky Blue (`#0284c7`, links `rgba(2, 132, 199, 0.45)`)
   - **City of Munich (*München*)**: Amber (`#d97706`, links `rgba(217, 119, 6, 0.45)`)
   Never permit neutral gray fallbacks (`#475569`) on municipal deficit, credit financing, or utility dividend nodes.
2. **Closest-Port Ribbon Attachment & Anti-Crossing**: Outgoing ribbons must exit from the vertically closest port of the node bar to their destination tier (e.g. on `Nominal_Federal`, outgoing flows must exit strictly in order: Insurance $\to$ top, Federal $\to$ middle, Bavaria $\to$ lower, Munich $\to$ bottom).
3. **Native Plotly Link Sorting Invariant (`sort="input"`)**: Always set `sort="input"` on both `go.Sankey.node` and `go.Sankey.link`, and pre-sort links by `(source_y, target_y)`. This prevents d3-sankey's relaxation algorithm from re-ordering links or crossing ribbons, eliminating the need for brittle post-processing SVG mutations.
4. **Transfer Deduction & Kirchhoff Conservation**: Direct intergovernmental transfers routed to sub-national authorities (e.g. federal SGB II/XII social cost reimbursements to Munich) must be deducted from the corresponding federal functional end-bucket (Bürgergeld/Grundsicherung) in Layer 4, ensuring zero double counting and exact mathematical flow conservation ($\Delta = 0.000\text{ Mrd. €}$) across all layers.

## 2. Design System Reference
For complete color hex codes, badge coordinates, typography templates, and margin specifications, consult [`plots/styling_guide.md`](file:///Users/selle/Documents/GitHub/DE-fiscal-per-capita/plots/styling_guide.md).

## 3. Vector-First Rendering & Anti-Pixel-Surgery Invariant
1. **Never Perform Destructive In-Memory Canvas Surgery**: Never attempt to "patch" raster images (PNG, JPEG) by drawing opaque background-colored polygons (`base_draw.polygon`) or bounding-box clear zones to erase and manually redraw chart elements (ribbons, lines, bars). Destructive pixel clearing risks obliterating adjacent text labels, anti-aliased edges, node rects, and text halos.
2. **Simple Direct Conversion Over Workaround Tangents**: When a vector graphic (SVG) is verified, clean, and accurate but the raster export is flawed, do not spend turns reverse-engineering internal rendering engines, CDP/browser internals, or complex in-place PIL surgery. Either:
   - Use a simple, deterministic standalone conversion script/utility to render PNG from the verified SVG, or
   - Keep the native generator pipeline clean without invasive raster post-processing.
3. **Time-Boxing Low-Level Debugging**: If an export workaround exceeds 2–3 turns without a clean, minimal solution, stop the tangent, assess the direct path (e.g. converting from the clean vector source), and consult the user or propose a simple conversion approach.


