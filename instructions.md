I would like a sankey flow of federal, state of bavaria, and city of Munich breakdown of fiscal money per capita. 

- Layer 1: sources of influx of taxes and insurances separated by federal, state of Bavaria, and city of Munich
- Layer 2: totals per capita federal, state of Bavaria, city of Munich
- Layer 3: Final buckets per capita, e.g. schools, roads, universities, defense, pension, health etc.

---

## Evolved Implementation Prompts & Latest Insights

The initial 3-layer brief evolved through rigorous empirical modeling and visual debugging into a battle-tested 4-layer architecture. When replicating, extending, or building similar multi-level public finance flows, use the following structured prompt sequences:

### Prompt 1: The 4-Layer Architecture & Intergovernmental Transfer Bridge
> "Construct a 4-layer directional Sankey flow rather than a naive 3-layer design:
> - **Layer 1: Steuer- & Beitragsinflux** ($x = 0.001$): Primary tax revenues, statutory social insurance contributions, and municipal deficit financing grouped strictly by intake authority with unified sovereign tier colors.
> - **Layer 2: Nominale Gebietskörperschaften** ($x = 0.320$): Gross sovereign revenues prior to intergovernmental redistribution.
> - **Intermediate Transfer Bridge** (Layer 2 $\to$ Layer 3): Explicit directed ribbons routing tax subsidies to social insurances (*Bundeszuschüsse*), federal social cost reimbursements to Munich (*KdU & Grundsicherung SGB II/XII*), federal grants to Bavaria (*Bundeszuweisungen*), and state municipal allocations (*FAG/BayKiBiG*).
> - **Layer 3: Effektive Haushalte** ($x = 0.650$): Net operational spending capacities after transfer consolidation and statutory reserve adjustments.
> - **Layer 4: Finale Funktionale End-Buckets** ($x = 0.999$): Tangible citizen-facing public goods destinations (schools, healthcare, pensions, transit, defense, municipal levies)."

### Prompt 2: Physical Kirchhoff Flow Conservation & Dual-Unit Per-Capita Display
> "Preserve dimensional physical flow conservation across non-nested jurisdictional populations while keeping municipal and state flows visually legible:
> - **Dual-Unit Scaling & Kirchhoff Conservation**: Scale visual ribbon and node widths to citizen-facing per-capita volume (`wert_eur_pro_kopf` in `€/Kopf`), while enforcing strict Kirchhoff flow conservation ($\Delta = 0.000\text{ Mrd. €}$) in physical currency (`wert_mrd_eur` in `Mrd. €`) across all four layers:
>   $$\sum \text{Layer 1} \equiv \sum \text{Layer 2} \equiv \sum \text{Layer 3} \equiv \sum \text{Layer 4} = 1{,}271.341\text{ Mrd. € (2024)}$$
> - **Per-Capita Metric Annotations**: Compute per-capita indicators (`€/Kopf`) relative to each sending and receiving entity's statutory population ($N_{\text{DE}} = 83{,}577{,}140$, $N_{\text{BY}} = 13{,}248{,}928$, $N_{\text{MUC}} = 1{,}505{,}005$). Display both per-capita figures, physical volumes (`Mrd. €`), and population badges (`Basis: 83,6 Mio. EW`) directly on node labels, link text, and interactive tooltips."

### Prompt 3: Crossover Elimination, Closest-Port Geometry & Native Plotly Sort
> "Optimize graph topology to eliminate ribbon crossovers and visual clutter:
> - **Layer 2 & 3 Stacking**: Place *Social Insurance above Federal Core Budget* (*Sozialversicherung* above *Bund*). Because social insurances flow predominantly into healthcare and pensions, this places the largest national flows at the top of the canvas, preventing ribbons from crossing federal outlays.
> - **Closest-Port Attachment & Native Plotly Link Sort**: Configure `sort='input'` on both `go.Sankey.node` and `go.Sankey.link`, and pre-sort links by `(source_y, target_y)`. Ensure outgoing flows exit from the vertically closest port of the node bar to their destination tier (e.g., Bund exits: top $\to$ Insurance, middle $\to$ Federal core, lower $\to$ Bavaria, bottom $\to$ Munich).
> - **Transfer Ribbon Exit Alignment**: Route the Bavarian municipal grant ribbon to Munich exiting from the bottom of Layer 2 *Freistaat Bayern* and entering the middle of Layer 3 *Stadt München*, completely avoiding overlap with the horizontal *Länderfinanzausgleich* outflow ribbon.
> - **Monotonic Influx Attachments**: Within each sovereign cluster in Layer 1, order primary revenues strictly descending by volume and align link attachment points monotonically on Layer 2 receiving nodes."

### Prompt 4: Dynamic Functional Sorting & Parent-Color Harmonization
> "Enhance legibility and semantic recognition in the final destination layer:
> - **Strict Descending Sort**: Dynamically sort all Layer 4 end-buckets descending by per-capita outlay, annotated with both per-capita spending and percentage share of total per-capita outlays.
> - **Single-Parent Color Inheritance**: When a functional destination is funded predominantly by a single tier ($> 80\%$), inherit that tier's primary brand color (e.g., Defense $\to$ Federal Navy `#1e3a8a`, Hospitals $\to$ Social Insurance Teal `#0d9488`, Local Transit/Housing $\to$ Municipal Amber `#d97706`). Use distinctive neutral/slate accents for genuinely mixed multi-level buckets (e.g., Schools, Infrastructure)."

### Prompt 5: Sankey-Centric Research Consolidation
> "Consolidate all empirical accounting normalizations, causal waterfall insights, and demographic denominator audits directly into the 4-layer Sankey network (`sankey_fiscal_per_capita.png`, `.svg`, and `.html`). Avoid generating decoupled auxiliary panels or multi-panel grids that diffuse focus from the unified multi-tier flow."


