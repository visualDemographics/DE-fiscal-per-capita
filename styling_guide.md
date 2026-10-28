# Flagship Visual Styling & Aesthetics Guide
## 4-Layer Multi-Level Fiscal Sankey Architecture

This styling guide codifies the design system, color palette, typography, geometric link-ordering invariants, and rendering standards for the flagship visualization ([`sankey_fiscal_per_capita.png`](./sankey_fiscal_per_capita.png), [`sankey_fiscal_per_capita.svg`](./sankey_fiscal_per_capita.svg), and [`sankey_fiscal_interactive.html`](./sankey_fiscal_interactive.html)).

All production visualizations in this repository must adhere strictly to these aesthetic and technical specifications.

---

## 1. Visual Hierarchy & Canvas Geometry

### 1.1 Canvas Specifications
- **Dimensions**:
  - Base Layout: $2600 \times 2250$ px
  - High-Resolution Static Export: Scale factor 2 ($5200 \times 4500$ px at 300 DPI)
- **Background**: Soft cool gray `#f8fafc` (`paper_bgcolor` and `plot_bgcolor`).
- **Margins**: Left $50$ px, Right $50$ px, Top $160$ px, Bottom $190$ px.
- **Node Geometry**:
  - Thickness: $26$ px
  - Vertical Node Padding: $35$ px
  - Border Stroke: $0.8$ px solid `#0f172a` (Slate-900)

### 1.2 4-Layer Column Grid ($x$-Coordinates)
The visualization strictly separates the fiscal lifecycle into four distinct horizontal stages:
1. **Layer 1: Steuer- & Beitragsinflux** ($x = 0.001$): Primary taxes, contributions, and net borrowing.
2. **Layer 2: Nominale Gebietskörperschaften** ($x = 0.320$): Gross sovereign budgets prior to intergovernmental consolidation.
3. **Layer 3: Effektive Haushalte (konsolidiert)** ($x = 0.650$): Net operational spending capacities after intergovernmental transfers.
4. **Layer 4: Finale Funktionale End-Buckets** ($x = 0.999$): Citizen-facing public goods and statutory equalizations.

---

## 2. Sovereign Tier Color System

Every sovereign tier is assigned a distinct, authoritative color identity that remains consistent across all layers (nodes and links) to prevent visual ambiguity.

| Sovereign Tier | Primary Influx (L1) | Nominal Entity (L2) | Effective Entity (L3) | Influx Link (L1 $\to$ L2) | Core Retention Link (L2 $\to$ L3) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Statutory Social Insurance (*SV*)** | Teal `#0d9488` | Teal `#0d9488` | Dark Teal `#0f766e` | `rgba(13, 148, 136, 0.45)` | `rgba(13, 148, 136, 0.55)` |
| **Federal Republic (*Bund*)** | Navy `#1e3a8a` | Navy `#1e3a8a` | Dark Royal `#1e40af` | `rgba(30, 58, 138, 0.45)` | `rgba(30, 58, 138, 0.55)` |
| **Free State of Bavaria (*Bayern*)** | Sky Blue `#0284c7` | Sky Blue `#0284c7` | Deep Sky `#0369a1` | `rgba(2, 132, 199, 0.45)` | `rgba(2, 132, 199, 0.55)` |
| **City of Munich (*München*)** | Amber `#d97706` | Amber `#d97706` | Dark Amber `#b45309` | `rgba(217, 119, 6, 0.45)` | `rgba(217, 119, 6, 0.55)` |

> [!IMPORTANT]
> **Layer 1 Color Unification Invariant**:
> In Layer 1, all nodes and links must be assigned their tier color explicitly. Never allow neutral gray fallbacks (`#475569` or `rgba(100, 116, 139, ...)`) for deficits, credit intake, utility dividends (SWM), or fee revenues.

---

## 3. Intergovernmental Transfer Ribbons & Bridges

Transfers between sovereign tiers in Layer 2 $\to$ Layer 3 must be clearly distinguishable from straight-through retained core budget flows:

| Intergovernmental Transfer Flow | Source $\to$ Target | Visual Styling / Ribbon Color | Flow Volume (2024) | Per-Capita Equivalent | Ribbon Badge Background |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bundeszuschuss an SV** | Nominal Bund $\to$ Effective Insurance | Royal Purple `rgba(139, 92, 246, 0.75)` | $130.50\text{ Mrd. €}$ | $1{,}561\text{ €/Kopf}$ | `rgba(245, 243, 255, 0.96)`, Border `#8b5cf6` |
| **Bundesmittel an Bayern** | Nominal Bund $\to$ Effective Bayern | Indigo `rgba(99, 102, 241, 0.70)` | $8.80\text{ Mrd. €}$ | $664\text{ €/Kopf}$ | `rgba(224, 231, 255, 0.96)`, Border `#6366f1` |
| **Bundesmittel an München** | Nominal Bund $\to$ Effective Munich | Deep Indigo `rgba(79, 70, 229, 0.70)` | $0.483\text{ Mrd. €}$ | $321\text{ €/Kopf}$ | `rgba(238, 242, 255, 0.96)`, Border `#6366f1` |
| **Zuweisungen Bayern an München** | Nominal Bayern $\to$ Effective Munich | Cyan/Blue `rgba(14, 165, 233, 0.70)` | $1.162\text{ Mrd. €}$ | $772\text{ €/Kopf}$ | `rgba(254, 243, 199, 0.96)`, Border `#f59e0b` |

---

## 4. Layer 4 Functional End-Buckets

### 4.1 Single-Parent vs. Multi-Parent Color Inheritance
1. **Single-Parent Buckets**: Inherit the exact color of their originating Layer 3 parent tier:
   - *Rente & Alterssicherung*: Insurance Dark Teal `#0f766e`
   - *Arbeitsförderung & Reha*: Insurance Dark Teal `#0f766e`
   - *Rücklagen & Liquiditätspuffer*: Insurance Dark Teal `#0f766e`
   - *Verteidigung & Äußeres*: Federal Dark Royal `#1e40af`
   - *Bürgergeld & Grundsicherung*: Federal Dark Royal `#1e40af`
   - *Schuldendienst & Zinsen*: Federal Dark Royal `#1e40af`
   - *Bundeszuweisungen übrige Länder*: Federal Dark Royal `#1e40af`
   - *Länderfinanzausgleich (Nettoabfluss)*: Bavarian Deep Sky `#0369a1`
   - *Wirtschaft & Landesverwaltung (BY)*: Bavarian Deep Sky `#0369a1`
   - *Kommunaler Finanzausgleich (übrige Kommunen)*: Bavarian Deep Sky `#0369a1`
   - *Kommunale Verwaltung & IT (MUC)*: Munich Dark Amber `#b45309`
   - *Kultur & Freizeit (MUC)*: Munich Dark Amber `#b45309`
   - *Bezirks- & Gewerbesteuerumlage (MUC)*: Dedicated Outflow Crimson `#be123c`
2. **Multi-Parent Shared Buckets**: Assigned curated, highly distinct semantic colors:
   - *Gesundheit & Pflege (SV + BY + MUC)*: Emerald `#10b981`
   - *Schulen & Kitas (BY + MUC)*: Royal Blue `#3b82f6`
   - *Verkehr & Mobilität (Bund + BY + MUC)*: Orange-Gold `#f59e0b`
   - *Innere Sicherheit & Justiz (Bund + BY + MUC)*: Slate `#64748b`
   - *Soziales, Jugend & Wohnen (Bund + MUC)*: Rose `#db2777`
   - *Hochschulen & Spitzenforschung (Bund + BY)*: Indigo `#6366f1`
   - *Wohnungsbau & Stadtplanung (Bund + MUC)*: Purple `#8b5cf6`

---

## 5. Geometric Link-Ordering & Anti-Crossing Invariant

### 5.1 Closest-Port Attachment Rule
To ensure optimal visual ergonomics, outgoing ribbons must leave each node bar from the port vertically closest to their target tier:

```
Nominal_Federal Bar:
┌──────────────────────────────┐
│ [Top Port]     ──(slants up)─┼──> Effective_Insurance (Top Tier)
│ [Middle Port]  ──(straight)──┼──> Effective_Federal (Second Tier)
│ [Lower Port]   ──(slants dn)─┼──> Effective_Bayern (Third Tier)
│ [Bottom Port]  ──(slants dn)─┼──> Effective_Munich (Fourth Tier)
└──────────────────────────────┘

Nominal_Bayern Bar:
┌──────────────────────────────┐
│ [Top Port]     ──(straight)──┼──> Effective_Bayern (Third Tier)
│ [Bottom Port]  ──(slants dn)─┼──> Effective_Munich (Fourth Tier)
└──────────────────────────────┘

Effective_Munich Entry Bar:
┌──────────────────────────────┐
│ [Top Entry]    <─────────────┼── from Nominal_Federal (KdU / SGB Reimbursement)
│ [Middle Entry] <─────────────┼── from Nominal_Bayern (FAG / BayKiBiG Gross Grants)
│ [Bottom Entry] <─────────────┼── from Nominal_Munich (Own Municipal Taxes & Deficit)
└──────────────────────────────┘
```

### 5.2 Plotly Native Link Sort Configuration
To enforce this geometric order deterministically and prevent d3-sankey relaxation algorithms from inverting links:
```python
fig = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        sort="input",  # Preserves exact vertical node stack
        ...
    ),
    link=dict(
        sort="input",  # Preserves exact vertical port attachment order
        ...
    )
))
```
- **Rule**: Links must be provided in `sources`/`targets` strictly sorted by `(source_y, target_y)`.
- **Anti-Surgery Guarantee**: Setting `sort="input"` natively produces clean, non-crossing ribbons in SVG, PNG, and interactive HTML, eliminating the need for brittle regex path surgery or raster pixel patching.

---

## 6. Typography & Label System

### 6.1 Font Stack
- Primary Font: `Helvetica, Arial, sans-serif`
- Color: `#1e293b` (Slate-800) for body, `#0f172a` (Slate-900) for headings.

### 6.2 Node Label Templates
- **Layer 2 & 3 Sovereign Tiers**:
  ```html
  <b>Effektive Stadt München</b><br>
  <b>6.276 €/Kopf</b> (9.4 Mrd. €)<br>
  <span style='font-size:10px;color:#000000'>Basis: 1,51 Mio. EW</span>
  ```
- **Layer 4 Shared Citizen-Facing End-Buckets**:
  ```html
  <b>Schulen & Kitas</b><br>
  <b>2.724 €/Kopf</b> · <b>10.5%</b> (BY 15.9 + MUC 2.3 Mrd. €)
  ```
- **Layer 4 Single-Parent End-Buckets**:
  ```html
  <b>Verteidigung & Äußeres</b><br>
  <b>888 €/Kopf</b> · <b>3.4%</b> (74.20 Mrd. €)
  ```
- **Negative Outflow Buckets (Länderfinanzausgleich)**:
  ```html
  <b>Länderfinanzausgleich (Nettoabfluss BY)</b><br>
  <b>-737 €/Kopf</b> · <b>2.8%</b> (-9.77 Mrd. €)
  ```

---

## 7. Ribbon Badges & Layout Callouts

### 7.1 Layer 2 $\to$ 3 Transfer Ribbon Badges
Badges placed directly on transfer ribbons provide immediate numerical context without forcing the user to consult external tables:
- Horizontal Coordinate: $x = 0.485$ (centered between Layer 2 and Layer 3)
- Vertical Placement ($y$):
  - *Beitragseinnahmen SV*: $y = 0.865$
  - *Bundeszuschuss an SV*: $y = 0.675$
  - *Bundes-Kernhaushalt*: $y = 0.560$
  - *Bundesmittel an Bayern*: $y = 0.450$
  - *Bundesmittel an München*: $y = 0.370$
  - *Landeshaushalt Bayern*: $y = 0.285$
  - *Zuweisungen Bayern an München*: $y = 0.190$
  - *Kommunalhaushalt München*: $y = 0.090$
- Styling Invariant: `borderwidth=1.5`, `borderpad=5`, `bgcolor="rgba(..., 0.96)"` matched to the ribbon hue.

### 7.2 Header Column Labels ($y = 1.025$)
- Font: $13$ px bold Helvetica, with $11$ px muted subtitle (`#64748b`).
- Explicit uppercase column headers:
  - `LAYER 1: STEUER- & BEITRAGSINFLUX` (`#1e3a8a`)
  - `LAYER 2: NOMINALE GEBIETSKÖRPERSCHAFTEN` (`#0f172a`)
  - `LAYER 3: EFFEKTIVE HAUSHALTE (KONSOLIDIERT)` (`#0d9488`)
  - `LAYER 4: FINALE FUNKTIONALE END-BUCKETS` (`#475569`, right-aligned)

### 7.3 Footer Metadata Badges ($y = -0.075$)
- Left: **Referenzbevölkerung** with exact Destatis / LfStat Zensus 2022 population baselines.
- Right: **Amtliche Primärquellen** documenting official institutional registers (BMF, BMAS, StMFH, Stadtkämmerei München, Destatis).

---

## 8. Summary Checklist for Future Chart Iterations

When extending, modifying, or creating derivative figures in this repository:
- [ ] Are Layer 1 colors 100% unified by sovereign tier (no random gray nodes or links)?
- [ ] Do intergovernmental transfer links exit from the vertically closest port of the source node?
- [ ] Is `sort="input"` specified on both `go.Sankey.node` and `go.Sankey.link`?
- [ ] Are input links pre-sorted by `(source_y, target_y)`?
- [ ] Does Kirchhoff flow conservation hold across all 4 layers ($\Delta = 0.000\text{ Mrd. €}$)?
- [ ] Are direct transfers deducted from the corresponding functional end-bucket to prevent double counting?
- [ ] Is the raster export generated via clean native Plotly + Kaleido vector rendering without raster canvas surgery?
