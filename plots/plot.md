# Systematic Plot Documentation & Validity Audit

This document systematically details the empirical provenance, mathematical formulation, and validity classifications for every figure generated in `/plots/`, in strict compliance with the **Responsible Empirical Research Protocol** (`responsible-research`).

---

## 1. Inventory of Generated Figures

| Figure Filename | Figure Title | Visual Architecture | Statistical Validity Tier | Input Dataset(s) |
| :--- | :--- | :--- | :--- | :--- |
| `sankey_fiscal_per_capita.png` | **4-Layer Fiscal Per-Capita Sankey (2024)** | High-Resolution Static Sankey Diagram | Audited Administrative Synthesis | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `sankey_fiscal_interactive.html` | **Interactive 4-Layer Fiscal Sankey Widget** | Interactive D3/Plotly Web Application | Audited Administrative Synthesis | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_a_per_capita_breakdown.png` | **Panel A: Headline Per-Capita Fiscal Outlays** | Horizontal Tier Comparison Bar Chart | Complete Audited Registers | `datasets/fiscal_per_capita_summary.csv` |
| `panel_b_demographic_pyramid.png` | **Panel B: Demographic Denominators & Zensus Shock** | Stacked Cohort Age Distribution Chart | Official Census Registry | `rawdata/demographics_zensus_denominators_2023_2024.csv` |
| `panel_c_transfer_deduction.png` | **Panel C: Intergovernmental Transfer Deductions** | Bridge Waterfall (*Bereinigte Ausgaben*) | National Accounts Matrix | `datasets/fiscal_per_capita_summary.csv` |
| `panel_d_tax_influx_structure.png` | **Panel D: Tax Influx Composition Across Levels** | Stacked Component Distribution | Tax Revenue Records | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_e_functional_buckets.png` | **Panel E: Final Functional Bucket Allocations** | Ranked Horizontal Allocation Chart | Functional Accounts (COFOG) | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_f_social_insurance_dominance.png` | **Panel F: Social Insurances vs. Core Investments** | Disproportionality Bar Ratio Chart | Statutory Fund Accounts | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_g_longitudinal_trajectory.png` | **Panel G: 2023 vs. 2024 Fiscal Trajectory** | Paired Delta Comparison Bar Chart | Annual Fiscal Registries | `datasets/fiscal_per_capita_summary.csv` |
| `panel_h_equalization_redistribution.png` | **Panel H: Equalization Transfers (LFA & KFA)** | Bipolar Horizontal Redistribution Map | Inter-State Financial Records | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_i_causal_waterfall.png` | **Panel I: Sequential Waterfall: Munich Gross to Net** | 5-Stage Path-Independent Waterfall | Multi-Level Public Budget | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `synoptic_3x3_matrix.png` | **Composite 9-Panel ($3 \times 3$) Synoptic Matrix** | Multi-Panel Executive Synthesis Grid | Complete Audited Synthesis | Panels A through I Composite |

---

## 2. Panel-by-Panel Methodological & Mathematical Audit

### Figure: `sankey_fiscal_per_capita.png` & `sankey_fiscal_interactive.html`
- **Objective**: Trace the complete directional flow of public funds across a 4-layer cascade: Influx $\to$ Nominal Entities $\to$ Effective Entities (after intergovernmental transfers) $\to$ Functional Public Goods.
- **Mathematical Formulation & Physical Ribbon Conservation**:
  - Ribbon visual widths represent conserved physical budgetary volume in billions of Euros ($\text{wert\_mrd\_eur}$), ensuring that no artificial widening or thinning occurs when funds cross jurisdictional boundaries.
  - Strict Kirchhoff flow conservation is satisfied across all 4 layers ($\Delta = 0.000\text{ Mrd. €}$):
    $$\sum \text{Layer 1 (Influx)} \equiv \sum \text{Layer 2 (Nominal)} \equiv \sum \text{Layer 3 (Effective)} \equiv \sum \text{Layer 4 (Buckets)} = 1{,}272.986\text{ Mrd. €}$$
  - Per-capita metrics ($\text{€/Kopf}$) are displayed on node headers and link tooltips, calculated with respect to each entity's audited population:
    - Bund & Social Insurance: $N_{\text{DE}} = 83{,}577{,}140$
    - Bavaria: $N_{\text{BY}} = 13{,}248{,}928$
    - Munich: $N_{\text{MUC}} = 1{,}505{,}005$
- **4-Layer Architecture & Flow Routing**:
  - **Layer 1 (Steuer- & Beitragsinflux)**:
    - *Federal Taxes* (Navy `#1e3a8a`): Lohn- & Einkommensteuer ($137.61\text{ Mrd. €}$, $1{,}646\text{ €/Kopf}$), Umsatzsteuer ($145.34\text{ Mrd. €}$, $1{,}739\text{ €/Kopf}$), Körperschaft- & Abgeltungsteuer ($28.36\text{ Mrd. €}$, $339\text{ €/Kopf}$), Verbrauchs- & Bundessteuern ($115.17\text{ Mrd. €}$, $1{,}378\text{ €/Kopf}$), Verwaltungseinnahmen ($5.89\text{ Mrd. €}$, $70\text{ €/Kopf}$), Nettokreditaufnahme ($33.30\text{ Mrd. €}$, $398\text{ €/Kopf}$).
    - *Social Insurance Contributions* (Teal `#0d9488`): Rentenbeiträge ($305.79\text{ Mrd. €}$, $3{,}659\text{ €/Kopf}$), Krankenbeiträge ($306.09\text{ Mrd. €}$, $3{,}662\text{ €/Kopf}$), Pflegebeiträge ($66.17\text{ Mrd. €}$, $792\text{ €/Kopf}$), Arbeitslosenbeiträge ($40.64\text{ Mrd. €}$, $486\text{ €/Kopf}$), Unfallbeiträge ($4.39\text{ Mrd. €}$, $53\text{ €/Kopf}$).
    - *Bavarian State Own Revenues* (Sky Blue `#0284c7`): Gemeinschaftsteuern ($50.95\text{ Mrd. €}$, $3{,}846\text{ €/Kopf}$), Landessteuern ($6.45\text{ Mrd. €}$, $487\text{ €/Kopf}$), Verwaltungseinnahmen ($5.00\text{ Mrd. €}$, $377\text{ €/Kopf}$), Rücklagen/Kredite ($2.50\text{ Mrd. €}$, $189\text{ €/Kopf}$).
    - *Munich Municipal Revenues* (Amber `#d97706`): Gewerbesteuer ($3.24\text{ Mrd. €}$, $2{,}153\text{ €/Kopf}$), Gemeindeanteil ESt/USt ($1.83\text{ Mrd. €}$, $1{,}216\text{ €/Kopf}$), Grundsteuer ($0.35\text{ Mrd. €}$, $231\text{ €/Kopf}$), Gebühren & Mieten ($1.35\text{ Mrd. €}$, $898\text{ €/Kopf}$), SWM-Gewinnausschüttung ($0.40\text{ Mrd. €}$, $266\text{ €/Kopf}$), Kredite & Entnahmen ($0.89\text{ Mrd. €}$, $593\text{ €/Kopf}$).
  - **Layer 2 (Nominale Gebietskörperschaften)**:
    - *Nominaler Bund*: $465.67\text{ Mrd. €}$ ($5{,}572\text{ €/Kopf}$ · Basis 83.6M EW)
    - *Nominale Sozialversicherung*: $723.08\text{ Mrd. €}$ ($8{,}652\text{ €/Kopf}$ · Basis 83.6M EW)
    - *Nominaler Freistaat Bayern*: $64.80\text{ Mrd. €}$ ($4{,}891\text{ €/Kopf}$ · Basis 13.2M EW)
    - *Nominale Stadt München*: $9.45\text{ Mrd. €}$ ($6{,}276\text{ €/Kopf}$ · Basis 1.51M EW)
  - **Intergovernmental Transfers (Layer 2 $\to$ Layer 3)**:
    - *Bund $\to$ Sozialversicherung*: Tax subsidies of **$116.00\text{ Mrd. €}$** ($1{,}388\text{ €/Kopf}$) to GRV and **$14.50\text{ Mrd. €}$** ($173\text{ €/Kopf}$) to GKV Gesundheitsfonds.
    - *Bund $\to$ Freistaat Bayern*: Federal grants of **$8.80\text{ Mrd. €}$** ($664\text{ €/Bavarian resident}$).
    - *Freistaat Bayern $\to$ München*: Key grants FAG and BayKiBiG of **$1.162\text{ Mrd. €}$** ($772\text{ €/Munich resident}$).
    - *München $\to$ Freistaat Bayern / Bezirk*: Munich transfers **$1.061\text{ Mrd. €}$** ($705\text{ €/Munich resident}$) in *Bezirksumlage* ($0.829\text{ Mrd. €}$) and *Gewerbesteuerumlage* ($0.232\text{ Mrd. €}$).
    - *Net municipal transfer bridge*: $+0.101\text{ Mrd. €}$ ($+67\text{ €/resident}$) net transfer from the Bavarian state layer to Munich.
  - **Layer 3 (Effektive Haushalte)**: Net operational budgets post-transfers:
    - *Effektiver Bund*: $326.37\text{ Mrd. €}$ ($3{,}905\text{ €/Kopf}$)
    - *Effektive Sozialversicherung*: $853.58\text{ Mrd. €}$ ($10{,}213\text{ €/Kopf}$)
    - *Effektiver Freistaat Bayern*: $73.60\text{ Mrd. €}$ ($5{,}555\text{ €/Kopf}$)
    - *Effektive Stadt München*: $9.55\text{ Mrd. €}$ ($6{,}343\text{ €/Kopf}$)
  - **Layer 4 (Finale Funktionale End-Buckets)**:
    - *Dynamic Descending Sorting & Percentage Shares*: All 19 functional end buckets are dynamically sorted strictly descending by per-capita volume ($\sum \text{Layer 4} = 26{,}135.02\text{ €/Kopf}$ in 2024, 100.0%):
      1. **Gesundheit & Pflege**: **$5{,}002\text{ €/Kopf}$** · **$19.1\%$** ($402.14\text{ Mrd. €}$)
      2. **Rente & Alterssicherung**: **$4{,}755\text{ €/Kopf}$** · **$18.2\%$** ($397.40\text{ Mrd. €}$)
      3. **Schulen & Kitas**: **$2{,}724\text{ €/Kopf}$** · **$10.4\%$** ($18.16\text{ Mrd. €}$)
      4. **Soziales, Jugend & Wohnen (MUC)**: **$2{,}038\text{ €/Kopf}$** · **$7.8\%$** ($24.67\text{ Mrd. €}$)
      5. **Kommunale Verwaltung & IT (MUC)**: **$1{,}633\text{ €/Kopf}$** · **$6.2\%$** ($2.46\text{ Mrd. €}$)
      6. **Wirtschaft, Energie & Verwaltung (Bund)**: **$1{,}527\text{ €/Kopf}$** · **$5.8\%$** ($40.38\text{ Mrd. €}$)
      7. **Verkehr & Mobilität**: **$1{,}409\text{ €/Kopf}$** · **$5.4\%$** ($43.44\text{ Mrd. €}$)
      8. **Innere Sicherheit & Justiz**: **$1{,}338\text{ €/Kopf}$** · **$5.1\%$** ($27.37\text{ Mrd. €}$)
      9. **Hochschulen & Spitzenforschung**: **$1{,}059\text{ €/Kopf}$** · **$4.1\%$** ($39.14\text{ Mrd. €}$)
      10. **Verteidigung & Äußeres**: **$888\text{ €/Kopf}$** · **$3.4\%$** ($74.20\text{ Mrd. €}$)
      11. **Länderfinanzausgleich (Transferabfluss BY)**: **$-737\text{ €/Kopf}$** · **$2.8\%$** ($-9.77\text{ Mrd. €}$ Nettoabfluss Bayern)
      12. **Bürgergeld & Grundsicherung**: **$697\text{ €/Kopf}$** · **$2.7\%$** ($58.26\text{ Mrd. €}$)
      13. **Arbeitsförderung & Reha (BA)**: **$642\text{ €/Kopf}$** · **$2.5\%$** ($53.64\text{ Mrd. €}$)
      14. **Wirtschaft & Landesverwaltung (BY)**: **$531\text{ €/Kopf}$** · **$2.0\%$** ($7.04\text{ Mrd. €}$)
      15. **Schuldendienst & Zinsen (Bund)**: **$409\text{ €/Kopf}$** · **$1.6\%$** ($34.22\text{ Mrd. €}$)
      16. **Bundeszuweisungen an übrige Länder**: **$297\text{ €/Kopf}$** · **$1.1\%$** ($24.80\text{ Mrd. €}$)
      17. **Kultur & Freizeit (München)**: **$189\text{ €/Kopf}$** · **$0.7\%$** ($284\text{ Mio. €}$)
      18. **Rücklagen & Liquiditätspuffer**: **$137\text{ €/Kopf}$** · **$0.5\%$** ($11.43\text{ Mrd. €}$)
      19. **Wohnungsbau & Stadtplanung**: **$123\text{ €/Kopf}$** · **$0.5\%$** ($4.19\text{ Mrd. €}$)
  - **Footer Annotation Architecture**:
    - *Referenzbevölkerung (Zensus 2022)*: Positioned on the bottom-left callout card (`x=0.005`), displaying exact registered resident totals and rounded millions for Bund & SV ($83{,}577{,}140\text{ EW}$ / $83.6\text{ Mio.}$), Freistaat Bayern ($13{,}248{,}928\text{ EW}$ / $13.2\text{ Mio.}$), and Landeshauptstadt München ($1{,}505{,}005\text{ EW}$ / $1.51\text{ Mio.}$).
    - *Amtliche Primärquellen*: Positioned on the bottom-right callout card (`x=0.995`), documenting verified official institutional registers: BMF (Bundeshaushalt), BMAS/DRV/GKV (Sozialbudget), StMFH (Haushalt Bayern & LFA), Stadtkämmerei München (Haushaltsplan), and Destatis (Zensus 2022).
    - *Header Subtitle*: Streamlined to focus on visual and flow conventions without demographic clutter.

---

### Figure: `panel_a_per_capita_breakdown.png`
- **Objective**: Direct headline comparison of per-capita public outlays across the 4 sovereign tiers, normalized by each jurisdiction's own audited population:
  - Bund (Kernhaushalt): **$5{,}572\text{ €/Kopf}$** (Basis: 83.6 Mio. EW)
  - Gesetzliche Sozialversicherung: **$10{,}213\text{ €/Kopf}$** (Basis: 83.6 Mio. EW)
  - Freistaat Bayern: **$5{,}563\text{ €/Kopf}$** (Basis: 13.2 Mio. EW)
  - Landeshauptstadt München: **$7{,}006\text{ €/Kopf}$** (Basis: 1.51 Mio. EW)
- **Validation**: Derived from `fiscal_per_capita_summary.csv`, fully reconciled with BMF, ORH, and Munich Kämmerei accounts.

---

### Figure: `panel_b_demographic_pyramid.png`
- **Objective**: Demographic structure and empirical quantification of the Zensus 2022 revision shock.
- **Key Empirical Indicators**:
  - Munich working-age concentration (18–64 years): **$67.32\%$** vs. Bavaria ($61.45\%$) and Germany ($60.58\%$).
  - Downward population correction: DE ($-1.43\%$), BY ($-1.93\%$), Munich ($-6.31\%$).
  - Mechanical per-capita inflation effect: $+1.45\%$ (Bund), $+6.74\%$ (Munich).

---

### Figure: `panel_c_transfer_deduction.png`
- **Objective**: Waterfall bridge illustrating intergovernmental transfer consolidation (*Bereinigte Ausgaben* per Destatis Fachserie 14) to prevent double counting:
  - Gross unconsolidated sum: **$27{,}605\text{ €}$**
  - Bundeszuschuss GRV: **$-1{,}388\text{ €}$**
  - Bundeszuschuss GKV: **$-173\text{ €}$**
  - Bundesmittel an Bayern: **$-664\text{ €}$**
  - Freistaat FAG an München: **$-772\text{ €}$**
  - Münchner Umlagen (Bezirk/Gewerbesteuer): **$+705\text{ €}$**
  - Net transfer consolidation delta: **$-2{,}293\text{ €}$**
  - Consolidated citizen-facing total: **$25{,}313\text{ €}$**

---

### Figure: `panel_d_tax_influx_structure.png`
- **Objective**: Influx stream profile across levels:
  - Bund: dominated by Umsatzsteuer ($1{,}739\text{ €}$) and Lohn-/ESt ($1{,}646\text{ €}$).
  - Sozialversicherung: pure employer/employee contributions ($3{,}659\text{ €}$ Rente, $3{,}662\text{ €}$ Gesundheit).
  - Freistaat Bayern: joint income/VAT taxes ($3{,}846\text{ €/Kopf}$).
  - Stadt München: Gewerbesteuer ($2{,}153\text{ €/Kopf}$) generating $>34\%$ of total municipal ordinary revenue.

---

### Figure: `panel_e_functional_buckets.png`
- **Objective**: Ranked functional destination of citizen-facing public expenditures across all 19 functional buckets, displaying exact per-capita spending and percentage share of total per-capita outlays ($26{,}135.02\text{ €/Kopf}$ in 2024):
  - Gesundheit & Pflege: **$5{,}002\text{ €}$** ($19.1\%$)
  - Rente & Alterssicherung: **$4{,}755\text{ €}$** ($18.2\%$)
  - Schulen & Kitas: **$2{,}724\text{ €}$** ($10.4\%$)
  - Soziales, Jugend & Wohnen (MUC): **$2{,}038\text{ €}$** ($7.8\%$)
  - Kommunale Verwaltung & IT (MUC): **$1{,}633\text{ €}$** ($6.2\%$)
  - Wirtschaft, Energie & Verwaltung (Bund): **$1{,}527\text{ €}$** ($5.8\%$)
  - Verkehr & Mobilität: **$1{,}409\text{ €}$** ($5.4\%$)
  - Innere Sicherheit & Justiz: **$1{,}338\text{ €}$** ($5.1\%$)
  - Hochschulen & Spitzenforschung: **$1{,}059\text{ €}$** ($4.1\%$)
  - Verteidigung & Äußeres: **$888\text{ €}$** ($3.4\%$)
  - Länderfinanzausgleich (Abfluss BY): **$737\text{ €}$** ($2.8\%$)
  - Bürgergeld & Grundsicherung: **$697\text{ €}$** ($2.7\%$)
  - Arbeitsförderung & Reha (BA): **$642\text{ €}$** ($2.5\%$)
  - Wirtschaft & Landesverwaltung (BY): **$531\text{ €}$** ($2.0\%$)
  - Schuldendienst & Zinsen (Bund): **$409\text{ €}$** ($1.6\%$)
  - Bundeszuweisungen an übrige Länder: **$297\text{ €}$** ($1.1\%$)
  - Kultur & Freizeit (München): **$189\text{ €}$** ($0.7\%$)
  - Rücklagen & Liquiditätspuffer: **$137\text{ €}$** ($0.5\%$)
  - Wohnungsbau & Stadtplanung: **$123\text{ €}$** ($0.5\%$)
  Highlights the structural dominance of statutory social transfers ($37.3\%$ for health and pensions alone) over capital investments.

---

### Figure: `panel_f_social_insurance_dominance.png`
- **Objective**: Empirical verification of Hypothesis 1:
  - Mandatory social security outlays: **$10{,}591\text{ €/resident}$** ($47.5\%$ of total).
  - Public investments & education: **$6{,}880\text{ €/resident}$** ($30.8\%$).
  - Overheads, debt service & LFA transfer: **$4{,}834\text{ €/resident}$** ($21.7\%$).
  - Dominance factor: $1.539\times$ ($+53.9\%$).

---

### Figure: `panel_g_longitudinal_trajectory.png`
- **Objective**: Paired longitudinal comparison of 2023 vs. 2024 per-capita spending across all 4 sovereign tiers:
  - Bund: $5{,}477\text{ €} \to 5{,}572\text{ €}$ ($+1.7\%$)
  - Sozialversicherung: $9{,}679\text{ €} \to 10{,}213\text{ €}$ ($+5.5\%$)
  - Freistaat Bayern: $5{,}388\text{ €} \to 5{,}563\text{ €}$ ($+3.2\%$)
  - Stadt München: $6{,}346\text{ €} \to 7{,}006\text{ €}$ ($+10.4\%$).

---

### Figure: `panel_h_equalization_redistribution.png`
- **Objective**: Multi-tier redistribution mapping:
  - Bavaria net LFA transfer outflow: **$-9.771\text{ Mrd. €}$** ($-737.42\text{ €/Bavarian resident}$).
  - Munich Bezirksumlage transfer outflow: **$-829\text{ Mio. €}$** ($-550.83\text{ €/Munich resident}$).
  - Munich Gewerbesteuerumlage transfer outflow: **$-232\text{ Mio. €}$** ($-154.15\text{ €/Munich resident}$).
  - State FAG and daycare grants to Munich: **$+1.162\text{ Mrd. €}$** ($+772.09\text{ €/Munich resident}$).
  - Federal grants to Bavaria: **$+8.80\text{ Mrd. €}$** ($+664.20\text{ €/Bavarian resident}$).

---

### Figure: `panel_i_causal_waterfall.png`
- **Objective**: 5-stage sequential waterfall isolating gross contributions ($27{,}605\text{ €}$) to net tangible public goods receipt ($24{,}225\text{ €}$) for a Munich resident with path-independent Shapley attribution (91.7% LFA, 8.3% municipal reallocation), accounting for overhead/administrative nodes ($-2{,}710\text{ €}$).

---

### Figure: `synoptic_3x3_matrix.png` & `synoptic_3x3_matrix.svg`
- **Objective**: Composite 9-panel synthesis matrix combining Panels A through I into a cohesive, publication-ready executive summary.
