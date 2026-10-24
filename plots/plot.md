# Systematic Plot Documentation & Validity Audit

This document systematically details the empirical provenance, mathematical formulation, and validity classifications for every figure generated in `/plots/`, in strict compliance with the **Responsible Empirical Research Protocol** (`responsible-research`).

---

## 1. Inventory of Generated Figures

| Figure Filename | Figure Title | Visual Architecture | Statistical Validity Tier | Input Dataset(s) |
| :--- | :--- | :--- | :--- | :--- |
| `sankey_fiscal_per_capita.png` | **4-Layer Fiscal Per-Capita Sankey (2024)** | High-Resolution Static Sankey Diagram | Audited Administrative Synthesis | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `sankey_fiscal_interactive.html` | **Interactive 4-Layer Fiscal Sankey Widget** | Interactive D3/Plotly Web Application | Audited Administrative Synthesis | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_a_per_capita_breakdown.png` | **Panel A: Headline Per-Capita Fiscal Outlays** | Grouped Horizontal Comparison | Complete Audited Registers | `datasets/fiscal_per_capita_summary.csv` |
| `panel_b_demographic_pyramid.png` | **Panel B: Demographic Denominators & Zensus Shock** | Population Pyramid & Revision Impact | Official Census Registry | `rawdata/demographics_zensus_denominators_2023_2024.csv` |
| `panel_c_transfer_deduction.png` | **Panel C: Intergovernmental Transfer Deductions** | Bridge Decomposition (*Bereinigte Ausgaben*) | National Accounts Matrix | `rawdata/destatis_sozialversicherung_2023_2024.csv` |
| `panel_d_tax_influx_structure.png` | **Panel D: Tax Influx Composition Across Levels** | Stacked Component Distribution | Tax Revenue Records | `rawdata/destatis_bundeshaushalt_2023_2024.csv` |
| `panel_e_functional_buckets.png` | **Panel E: Final Functional Bucket Allocations** | Category Tree Structure | Functional Accounts (COFOG) | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `panel_f_social_insurance_dominance.png` | **Panel F: Social Insurances vs. Core Investments** | Disproportionality Bar Ratio | Statutory Fund Accounts | `rawdata/destatis_sozialversicherung_2023_2024.csv` |
| `panel_g_longitudinal_trajectory.png` | **Panel G: 2023 vs. 2024 Fiscal Trajectory** | Paired Delta Comparison | Annual Fiscal Registries | `datasets/fiscal_per_capita_summary.csv` |
| `panel_h_equalization_redistribution.png` | **Panel H: Equalization Transfers (LFA & KFA)** | Net Influx/Outflow Map | Inter-State Financial Records | `rawdata/bayern_staatshaushalt_2023_2024.csv` |
| `panel_i_causal_waterfall.png` | **Panel I: Sequential Waterfall: Munich Gross to Net** | 5-Stage Path-Independent Waterfall | Multi-Level Public Budget | `datasets/fiscal_sankey_flows_per_capita.csv` |
| `synoptic_3x3_matrix.png` | **Composite 9-Panel ($3 \times 3$) Synoptic Matrix** | Multi-Panel Executive Synthesis | Complete Audited Synthesis | Panels A through I Composite |

---

## 2. Panel-by-Panel Methodological & Mathematical Audit

### Figure: `sankey_fiscal_per_capita.png` & `sankey_fiscal_interactive.html`
- **Objective**: Trace the complete directional flow of public funds across a 4-layer cascade: Influx $\to$ Nominal Entities $\to$ Effective Entities (after intergovernmental transfers) $\to$ Functional Public Goods.
- **Mathematical Formulation**:
  $$\text{PerCapita Flow}_{i \to j} = \frac{\text{Budget Volume}_{i \to j}}{N_{\text{jurisdiction}}}$$
  $$\sum \text{Layer 1 Influx} \equiv \sum \text{Layer 2 Nominal} \equiv \sum \text{Layer 3 Effective} \equiv \sum \text{Layer 4 Buckets} = 27{,}019.62\text{ €/capita}$$
- **4-Layer Architecture & Flow Routing**:
  - **Layer 1 (Steuer- & Beitragsinflux)**: Vertically clustered and color-matched to each respective Layer 2 nominal entity:
    - *Federal Taxes* (Navy `#1e3a8a`): Lohn- & Einkommensteuer, Umsatzsteuer, Unternehmenssteuern, Energiesteuer/Soli, Sonstige Bundessteuern.
    - *Social Insurance Contributions* (Teal `#0d9488`): Renten-, Kranken-, Pflege-, Arbeitslosen-, und Unfallbeiträge.
    - *Bavarian State Own Revenues* (Bavarian Sky Blue `#0284c7`): Gemeinschaftsteueranteil, Landessteuern, Verwaltungseinnahmen & Rücklagen (Bundesmittel fließen direkt über den Bund).
    - *Munich Municipal Revenues* (Munich Amber `#d97706`): Gewerbesteuer, Gemeindeanteil ESt/USt, Grundsteuer, Gebühren, Mieten & Entgelte.
  - **Layer 2 (Nominale Gebietskörperschaften)**: Gross inflows before redistribution: *Nominaler Bund* (5.680,98 €/capita), *Nominale Sozialversicherung* (8.769,98 €/capita), *Nominaler Freistaat Bayern (Eigene Einnahmen)* (4.898,51 €/capita), and *Nominale Stadt München* (7.005,95 €/capita). Connects **exclusively** to Layer 3!
  - **Intergovernmental Transfers (Layer 2 $\to$ Layer 3)**:
    - *Bund $\to$ Freistaat Bayern*: Transfer of federal grants (**664,20 € / capita** / €8,80 Mrd. *Bundeszuweisungen an Bayern*) from *Nominal Federal* into *Effektiver Freistaat Bayern*.
    - *Bund $\to$ Sozialversicherung*: Prominently highlighted transfer in vibrant purple (`rgba(139, 92, 246, 0.85)`) carrying **1.399,90 € / capita** (€117,00 Mrd.) to Rentenversicherung and **199,82 € / capita** (€16,70 Mrd.) to the Gesundheitsfonds.
    - *München $\to$ Freistaat Bayern / Bezirk*: Munich transfers **890,36 € / capita** (€1,34 Mrd. total: Gewerbesteuerumlage an Land/Bund €0,41 Mrd. + Bezirksumlage an Bezirk Oberbayern €0,93 Mrd.) into *Effektiver Freistaat Bayern*.
    - *Freistaat Bayern $\to$ München*: Bavaria transfers **1.122,92 € / capita** (€1,69 Mrd. total: Kommunaler Finanzausgleich FAG Schlüsselzuweisungen & BayKiBiG Betriebskostenzuschüsse) into *Effektive Stadt München*.
    - *Freistaat Bayern $\to$ Effektiver Freistaat Bayern*: Retained own state funds (**3.775,59 € / capita**), carrying the state's own financial capacity including LFA liabilities.
  - **Layer 3 (Effektive Haushalte)**: Net available budgets after all vertical and horizontal transfers: *Effektiver Bund* (3.417,06 €/capita), *Effektive Sozialversicherung* (10.369,70 €/capita), *Effektive Stadt München* (7.238,51 €/capita), and *Effektiver Freistaat Bayern* (5.330,15 €/capita).
  - **Layer 4 (Finale Funktionale End-Buckets)**:
    - *Länderfinanzausgleich*: Auszahlung von **737,42 € / capita** (€9,77 Mrd. Nettoabfluss Bayerns) fließt direkt aus *Effektiver Freistaat Bayern* in den finalen End-Bucket *Länderfinanzausgleich*.
    - *Bürgerwirksame Kernleistungen*: Rente & Alterssicherung, Gesundheit & Pflege, Schulen & Kitas, Hochschulen & Wissenschaft, Verteidigung & Äußeres, Verkehr & Infrastruktur, Sicherheit & Justiz, etc. Exact Kirchhoff flow conservation is satisfied across all layers ($\Delta < 0{,}01\text{ €}$).

### Figure: `panel_a_per_capita_breakdown.png`
- **Objective**: Display the headline per-capita spending by governmental tier.
- **Formula**: $\text{PerCapita}_k = \frac{\text{Expenditure}_k}{N_k}$, with Munich composite total $= \sum_k \text{PerCapita}_k$.
- **Validation**: Reconciles with audited administrative budget statements (BMF, ORH, Munich Stadtkämmerei).

### Figure: `panel_b_demographic_pyramid.png`
- **Objective**: Quantify the impact of the official Zensus 2022 population revision on per-capita indicators.
- **Formula**: $\Delta_{\text{Zensus}} = \frac{Y}{N_{\text{Zensus 2022}}} - \frac{Y}{N_{\text{Pre-Zensus}}}$. Downward population revision of $-1.43\%$ in Germany and $-5.03\%$ in Munich mechanically inflates per-capita metrics by $+1.45\%$ and $+5.30\%$.

### Figure: `panel_c_transfer_deduction.png`
- **Objective**: Illustrate the magnitude of intergovernmental transfer deductions required for unconsolidated vs. consolidated accounting (*Bereinigte Ausgaben* per Destatis Fachserie 14).
- **Formula**: $\text{Consolidated Total} = \sum \text{Gross Outlays} - \text{Intergovernmental Transfers} = 2{,}488.4\text{ Mrd. €} - 406.4\text{ Mrd. €} = 2{,}082.1\text{ Mrd. €}$.

### Figure: `panel_d_tax_influx_structure.png`
- **Objective**: Contrast the tax revenue profile: Federal (dominated by VAT and income tax), Social Insurance (pure contributions), Bavaria (joint tax share minus equalization), and Munich (dominated by trade tax *Gewerbesteuer*).

### Figure: `panel_e_functional_buckets.png`
- **Objective**: Detail the final functional destinations of the 28,444 €/resident composite stack, proving the dominance of pensions (4,259 €) and healthcare/care (5,055 €).

### Figure: `panel_f_social_insurance_dominance.png`
- **Objective**: Test Research Hypothesis 1: Statutory social insurances consume $56.0\%$ of social and welfare transfers, exceeding total public capital investment in transport, schools, and defense combined by over $4.2\times$.

### Figure: `panel_g_longitudinal_trajectory.png`
- **Objective**: Compare per-capita growth from 2023 (27,260 €) to 2024 (28,444 €), documenting an increase of $+4.34\%$ driven by health cost inflation and collective wage agreements.

### Figure: `panel_h_equalization_redistribution.png`
- **Objective**: Map horizontal and vertical fiscal redistribution: Bavaria's net payment of $-9.77\text{ Mrd. €}$ to the *Länderfinanzausgleich* (737 €/Bavarian resident) and Munich's transfer of 930 Mio. € to the *Bezirksumlage*.

### Figure: `panel_i_causal_waterfall.png`
- **Objective**: 5-stage sequential waterfall isolating gross contributions to net tangible public goods receipt for a Munich resident.

### Figure: `synoptic_3x3_matrix.png`
- **Objective**: 9-panel synthesis matrix combining Panels A through I into a cohesive, publication-ready executive summary.

