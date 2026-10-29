# Systematic Plot Documentation & Validity Audit

This document systematically details the empirical provenance, mathematical formulation, and validity classifications for the flagship visualization generated in `/plots/`, in strict compliance with the **Responsible Empirical Research Protocol** (`responsible-research`).

> [!IMPORTANT]
> **Exclusive Visualization Scope Notice**:
> In accordance with the core research objectives of this repository, the visualization assets and modeling pipeline are dedicated **exclusively to the 4-Layer Fiscal Per-Capita Sankey Flow Architecture** ([`sankey_fiscal_per_capita.png`](./sankey_fiscal_per_capita.png), [`sankey_fiscal_per_capita.svg`](./sankey_fiscal_per_capita.svg), and [`sankey_fiscal_interactive.html`](./sankey_fiscal_interactive.html)). All auxiliary sub-panels (Panels A–I and the 3x3 matrix) have been retired to focus entirely on the unified multi-level Sankey network.

---

## 1. Inventory of Generated Visualizations

| Figure Filename | Figure Title | Visual Architecture | Statistical Validity Tier | Input Dataset(s) |
| :--- | :--- | :--- | :--- | :--- |
| [`sankey_fiscal_per_capita.png`](./sankey_fiscal_per_capita.png) | **4-Layer Fiscal Per-Capita Sankey (2024 & 2023)** | High-Resolution Static Sankey Diagram (5200 × 4500 px) | Audited Administrative Synthesis (Kirchhoff Conserved) | [`datasets/fiscal_sankey_flows_per_capita.csv`](../datasets/fiscal_sankey_flows_per_capita.csv) |
| [`sankey_fiscal_per_capita.svg`](./sankey_fiscal_per_capita.svg) | **Vector Graphic Master Source** | Scalable Vector Graphic (SVG) | Audited Administrative Synthesis | [`datasets/fiscal_sankey_flows_per_capita.csv`](../datasets/fiscal_sankey_flows_per_capita.csv) |
| [`sankey_fiscal_interactive.html`](./sankey_fiscal_interactive.html) | **Interactive 4-Layer Fiscal Sankey Widget** | D3 / Plotly Web Application with Year Switcher | Audited Administrative Synthesis | [`datasets/fiscal_sankey_flows_per_capita.csv`](../datasets/fiscal_sankey_flows_per_capita.csv) |

---

## 2. In-Depth Methodological & Mathematical Audit

### Figure: `sankey_fiscal_per_capita.png` (and interactive HTML)

#### 2.1 Research Objective & Tier-by-Tier Sovereign Scope
The 4-layer fiscal Sankey diagram resolves the multi-level fragmentation of German public finances by tracing the multi-tier sovereign fiscal flows available to residents in the **City of Munich (*Landeshauptstadt München*)** in 2024 (with full longitudinal comparability to 2023). Under the **Tier-by-Tier Apples-to-Apples Policy (Option A)**, each public authority is evaluated within its genuine sovereign constituency:
1. **Federal Republic of Germany (*Bund*)**: Normalized by Germany's population ($N_{\text{DE}} = 83{,}577{,}140$).
2. **Statutory Social Insurances (*Sozialversicherungsträger*: GRV, GKV, SPV, BA, DGUV)**: Normalized by national insured population ($N_{\text{DE}} = 83{,}577{,}140$).
3. **Free State of Bavaria (*Freistaat Bayern*)**: Normalized by Bavaria's population ($N_{\text{BY}} = 13{,}248{,}928$).
4. **City of Munich (*Landeshauptstadt München*)**: Normalized by Munich's resident population ($N_{\text{MUC}} = 1{,}505{,}005$).

Residents of Munich simultaneously benefit from public goods provided across all four sovereign tiers (e.g. municipal schools and daycares funded locally, police and universities funded at the state level, federal highways and defense funded centrally, and healthcare/pensions funded through national social insurance). Each node carries an explicit population denominator badge (`Basis: 83,6 Mio. EW`, `Basis: 13,2 Mio. EW`, `Basis: 1,51 Mio. EW`) to prevent misleading stacked resident totals.

#### 2.2 Mathematical Formulation & Physical Ribbon Conservation
- **Per-Capita Visual Scaling & Dual-Unit Accounting**: Link ribbon and node bar visual widths are scaled proportionally to citizen-facing per-capita volume ($\text{wert\_eur\_pro\_kopf}$, in $\text{€/Kopf}$), so that municipal ($N_{\text{MUC}} = 1.51\text{ Mio.}$) and state ($N_{\text{BY}} = 13.25\text{ Mio.}$) public services remain visually legible alongside federal and social insurance tiers ($N_{\text{DE}} = 83.58\text{ Mio.}$), while exact physical budgetary volumes ($\text{wert\_mrd\_eur}$, in $\text{Mrd. €}$) are reported in parentheses on every node and link.
- **Kirchhoff Flow Conservation ($\Delta = 0.000\text{ Mrd. €}$)**:
  Every layer in the underlying physical ledger satisfies exact input-output conservation across all nodes:
  $$\sum \text{Layer 1 (Influx)} \equiv \sum \text{Layer 2 (Nominal)} \equiv \sum \text{Layer 3 (Effective)} \equiv \sum \text{Layer 4 (Buckets)} = 1{,}271.341\text{ Mrd. € (2024)}$$
- **Jurisdictional Per-Capita Normalization**:
  To prevent distorted synthetic denominator additions, each flow is normalized per capita relative to its statutory source and recipient constituency:
  $$\text{EUR/Kopf} = \frac{\text{Flow Volume (EUR)}}{N_{\text{Constituency}}}$$
  - **Federal & Social Insurance Baseline**: $N_{\text{DE}} = 83{,}577{,}140$ (Destatis Zensus 2022 revised register)
  - **Free State of Bavaria Baseline**: $N_{\text{BY}} = 13{,}248{,}928$ (LfStat Zensus 2022 revised register)
  - **City of Munich Baseline**: $N_{\text{MUC}} = 1{,}505{,}005$ (LfStat Zensus 2022 revised register)

---

#### 2.3 Layer-by-Layer Architecture

##### Layer 1: Steuer- & Beitragsinflux ($x = 0.001$)
Groups primary revenue collection and financing streams strictly descending by sovereign intake authority:
- **Statutory Social Insurance Contributions** (Teal `#0d9488`):
  - *Krankenbeiträge (AG & AN an GKV)*: $306.10\text{ Mrd. €}$ ($3{,}662.48\text{ €/Kopf}$)
  - *Rentenbeiträge (AG & AN an GRV)*: $305.80\text{ Mrd. €}$ ($3{,}658.90\text{ €/Kopf}$)
  - *Pflegebeiträge (AG & AN an SPV)*: $66.16\text{ Mrd. €}$ ($791.60\text{ €/Kopf}$)
  - *Arbeitslosenbeiträge (an BA)*: $40.58\text{ Mrd. €}$ ($485.54\text{ €/Kopf}$)
  - *Unfallbeiträge (Umlagesoll DGUV)*: $14.33\text{ Mrd. €}$ ($171.46\text{ €/Kopf}$)
  - *Subtotal Social Contributions*: **$732.97\text{ Mrd. €}$** ($8{,}769.98\text{ €/Kopf}$)
- **Federal Net Influx (BMF Table 1 & Table 7)** (Navy `#1e3a8a`):
  - *Umsatzsteuer Bund*: $145.34\text{ Mrd. €}$ ($1{,}738.99\text{ €/Kopf}$)
  - *Lohn- & Einkommensteuer Bund*: $137.61\text{ Mrd. €}$ ($1{,}646.50\text{ €/Kopf}$)
  - *Verwaltungseinnahmen & Beteiligungen Bund*: $65.65\text{ Mrd. €}$ ($785.50\text{ €/Kopf}$)
  - *Verbrauchs- & Bundessteuern (Energie, Tabak, Soli, Kfz, VersSt)*: $46.66\text{ Mrd. €}$ ($558.29\text{ €/Kopf}$)
  - *Unternehmenssteuern Bund (KSt, Abgeltungsteuer)*: $45.37\text{ Mrd. €}$ ($542.85\text{ €/Kopf}$)
  - *Nettokreditaufnahme & Finanzierungssaldo*: $25.04\text{ Mrd. €}$ ($299.60\text{ €/Kopf}$)
  - *Subtotal Federal Net Intake*: **$465.67\text{ Mrd. €}$** ($5{,}571.73\text{ €/Kopf}$)
- **Bavarian State Own Revenues** (Sky Blue `#0284c7`):
  - *Gemeinschaftsteuern Bayern (Landesanteil ESt, USt, KSt)*: $50.95\text{ Mrd. €}$ ($3{,}845.59\text{ €/Kopf}$)
  - *Landessteuern (Erbschaft-, Grunderwerb-, Biersteuer)*: $6.45\text{ Mrd. €}$ ($486.83\text{ €/Kopf}$)
  - *Verwaltungseinnahmen Freistaat*: $4.67\text{ Mrd. €}$ ($352.48\text{ €/Kopf}$)
  - *Rücklagenentnahme & Kredite Bayern*: $2.83\text{ Mrd. €}$ ($213.60\text{ €/Kopf}$)
  - *Subtotal Bavarian Own Revenues*: **$64.90\text{ Mrd. €}$** ($4{,}898.89\text{ €/Kopf}$)
- **Munich Municipal Own Revenues & Financing (Option B Reconciled)** (Amber `#d97706`):
  - *Gewerbesteuer (netto)*: $3.240\text{ Mrd. €}$ ($2{,}152.82\text{ €/Kopf}$)
  - *Gemeindeanteile an ESt & USt*: $1.830\text{ Mrd. €}$ ($1{,}215.94\text{ €/Kopf}$)
  - *Gebühren, Mieten & Entgelte*: $1.027\text{ Mrd. €}$ ($682.39\text{ €/Kopf}$)
  - *Städtischer Fehlbedarf / Kredite*: $0.892\text{ Mrd. €}$ ($592.69\text{ €/Kopf}$)
  - *SWM-Ausschüttung & Sonstige ordentliche Erträge*: $0.448\text{ Mrd. €}$ ($297.67\text{ €/Kopf}$)
  - *Grundsteuer & Lokalsteuern*: $0.364\text{ Mrd. €}$ ($241.86\text{ €/Kopf}$)
  - *Subtotal Munich Own Revenues & Financing*: **$7.801\text{ Mrd. €}$** ($5{,}183.37\text{ €/Kopf}$)

##### Layer 2: Nominale Gebietskörperschaften ($x = 0.320$)
Gross intake volumes prior to intergovernmental consolidation (with explicit sovereign intake badges):
- **Nominale Sozialversicherung**: $732.97\text{ Mrd. €}$ ($8{,}770\text{ €/Kopf}$ · Basis 83.6M EW)
- **Nominaler Bund**: $465.67\text{ Mrd. €}$ ($5{,}572\text{ €/Kopf}$ · Basis 83.6M EW)
- **Nominaler Freistaat Bayern**: $64.90\text{ Mrd. €}$ ($4{,}898\text{ €/Kopf}$ · Basis 13.2M EW)
- **Nominale Stadt München**: $7.80\text{ Mrd. €}$ ($5{,}183\text{ €/Kopf}$ · Basis 1.51M EW)

##### Intergovernmental Transfer Layer (Layer 2 $\to$ Layer 3)
Explicit directed link ribbons routing intergovernmental transfers from the closest portion of the sovereign node bars:
- **Federal Subsidies to Social Insurances (*Bundeszuschüsse*)**:
  - To Statutory Pension Insurance (GRV): **$116.00\text{ Mrd. €}$** ($1{,}387.94\text{ €/Kopf}$)
  - To Statutory Health Insurance (GKV Gesundheitsfonds): **$14.50\text{ Mrd. €}$** ($173.49\text{ €/Kopf}$)
  - *Combined Social Subsidy Ribbon (exits top of Fed bar)*: **$130.50\text{ Mrd. €}$** ($1{,}561.43\text{ €/Kopf}$)
- **Federal Grants to Bavaria (*Bundeszuweisungen*)**:
  - Federal allocations for joint tasks and transit (exits lower part of Fed bar): **$8.80\text{ Mrd. €}$** ($664.20\text{ €/Kopf}$)
- **Federal Social Reimbursements to Munich (*KdU & Grundsicherung SGB II/XII*)**:
  - Direct federal reimbursement for municipal social accommodation outlays (exits bottom of Fed bar): **$0.483\text{ Mrd. €}$** ($320.93\text{ €/Kopf}$)
- **Bavarian Gross Municipal Grants to Munich (*FAG & BayKiBiG*)**:
  - Gross key grants and early childhood subsidies (exits bottom of Bayern bar): **$+1.162\text{ Mrd. €}$** ($+772.09\text{ €/Kopf}$)
- **Consolidated Effective Spending**:
  - Federal retained core budget: **$325.89\text{ Mrd. €}$** ($3{,}899.24\text{ €/Kopf}$)
  - Bavarian retained state budget: **$63.74\text{ Mrd. €}$** ($4{,}810.80\text{ €/Kopf}$)
  - Munich effective municipal spending: **$9.446\text{ Mrd. €}$** ($6{,}276.39\text{ €/Kopf}$), composed of $7.801\text{ Mrd. €}$ own revenues + $1.162\text{ Mrd. €}$ state grants + $0.483\text{ Mrd. €}$ federal social reimbursements.

##### Layer 3: Effektive Haushalte ($x = 0.650$)
Net disposable spending capacity after transfer consolidation:
- **Effektive Sozialversicherung**: $863.47\text{ Mrd. €}$ ($10{,}331\text{ €/Kopf}$ · Basis 83.6M EW)
- **Effektiver Bund (Kernhaushalt)**: $325.89\text{ Mrd. €}$ ($3{,}899\text{ €/Kopf}$ · Basis 83.6M EW)
- **Effektiver Freistaat Bayern**: $72.54\text{ Mrd. €}$ ($5{,}475\text{ €/Kopf}$ · Basis 13.2M EW)
- **Effektive Stadt München**: $9.45\text{ Mrd. €}$ ($6{,}276\text{ €/Kopf}$ · Basis 1.51M EW)

##### Layer 4: Finale Funktionale End-Buckets ($x = 0.999$)
21 citizen-facing public goods destinations, dynamically sorted strictly descending by per-capita spending relative to total outlays ($25{,}982.04\text{ €/Kopf}$ in 2024 / $24{,}947.59\text{ €/Kopf}$ in 2023, as highlighted directly in the column header `Gesamtausgaben: 25.982 € / Kopf (1.271,3 Mrd. € · 100%)`), featuring multi-tier parenthetical breakdowns on all shared nodes:
1. **Gesundheit & Pflege**: $402.14\text{ Mrd. €}$ ($5{,}002.46\text{ €/Kopf}$, $19.25\%$) · *(SV 401.0 + BY 0.9 + MUC 0.2 Mrd. €)*
2. **Rente & Alterssicherung**: $397.40\text{ Mrd. €}$ ($4{,}754.89\text{ €/Kopf}$, $18.30\%$) · *(SV 397.4 Mrd. €)*
3. **Schulen & Kitas**: $18.16\text{ Mrd. €}$ ($2{,}723.99\text{ €/Kopf}$, $10.48\%$) · *(BY 15.9 + MUC 2.3 Mrd. €)*
4. **Soziales, Jugend & Familie**: $24.67\text{ Mrd. €}$ ($2{,}037.78\text{ €/Kopf}$, $7.84\%$) · *(Bund 14.4 + BY 8.4 + MUC 1.9 Mrd. €)*
5. **Wirtschaft, Klima & Verwaltung**: $40.58\text{ Mrd. €}$ ($1{,}542.28\text{ €/Kopf}$, $5.94\%$) · *(Bund 34.8 + BY 4.7 + MUC 1.2 Mrd. €)*
6. **Verkehr & Mobilität**: $43.44\text{ Mrd. €}$ ($1{,}409.22\text{ €/Kopf}$, $5.42\%$) · *(Bund 36.4 + BY 6.3 + MUC 0.7 Mrd. €)*
7. **Innere Sicherheit & Justiz**: $27.37\text{ Mrd. €}$ ($1{,}337.70\text{ €/Kopf}$, $5.15\%$) · *(Bund 15.4 + BY 11.5 + MUC 0.4 Mrd. €)*
8. **Hochschulen & Spitzenforschung**: $38.79\text{ Mrd. €}$ ($1{,}032.57\text{ €/Kopf}$, $3.97\%$) · *(Bund 29.8 + BY 8.9 Mrd. €)*
9. **Verteidigung & Äußeres**: $74.20\text{ Mrd. €}$ ($887.80\text{ €/Kopf}$, $3.42\%$) · *(Bund 74.2 Mrd. €)*
10. **Kommunale Verwaltung & IT (MUC)**: $1.295\text{ Mrd. €}$ ($860.46\text{ €/Kopf}$, $3.31\%$) · *(MUC 1.3 Mrd. €)*
11. **Länderfinanzausgleich (Nettoabfluss BY)**: $9.77\text{ Mrd. €}$ ($737.42\text{ €/Kopf}$, $2.84\%$) · *(BY 9.8 Mrd. €)*
12. **Bezirks- & Gewerbesteuerumlage (MUC)**: $1.061\text{ Mrd. €}$ ($704.98\text{ €/Kopf}$, $2.71\%$) · *(MUC 1.1 Mrd. €)*
13. **Bürgergeld & Grundsicherung**: $57.78\text{ Mrd. €}$ ($691.30\text{ €/Kopf}$, $2.66\%$) · *(Bund 57.8 Mrd. € net after 0.48 Mrd. € transfer to Munich)*
14. **Arbeitsförderung & Reha (BA)**: $53.64\text{ Mrd. €}$ ($641.80\text{ €/Kopf}$, $2.47\%$) · *(SV 53.6 Mrd. €)*
15. **Schuldendienst & Zinsen**: $34.22\text{ Mrd. €}$ ($409.44\text{ €/Kopf}$, $1.58\%$) · *(Bund 34.2 Mrd. €)*
16. **Wirtschaft & Landesverwaltung (BY)**: $5.41\text{ Mrd. €}$ ($408.33\text{ €/Kopf}$, $1.57\%$) · *(BY 5.4 Mrd. €)*
17. **Bundeszuweisungen an übrige Länder**: $24.80\text{ Mrd. €}$ ($296.73\text{ €/Kopf}$, $1.14\%$) · *(Bund 24.8 Mrd. €)*
18. **Kultur & Freizeit**: $0.284\text{ Mrd. €}$ ($188.70\text{ €/Kopf}$, $0.73\%$) · *(MUC 0.3 Mrd. €)*
19. **Rücklagen & Liquiditätspuffer**: $11.43\text{ Mrd. €}$ ($136.76\text{ €/Kopf}$, $0.53\%$) · *(SV 11.4 Mrd. €)*
20. **Wohnungsbau & Stadtplanung**: $4.19\text{ Mrd. €}$ ($123.24\text{ €/Kopf}$, $0.47\%$) · *(Bund 4.1 + MUC 0.1 Mrd. €)*
21. **Kommunaler Finanzausgleich (übrige Kommunen BY)**: $0.718\text{ Mrd. €}$ ($54.19\text{ €/Kopf}$, $0.21\%$) · *(BY 0.72 Mrd. €)*

---

## 3. Data Integrity & Verification Standards

1. **No Synthetic Fallbacks**: Zero artificial random distributions or imputed cells.
2. **Deterministic Reproducibility**: Generated via `python src/modeling.py` from audited datasets.
3. **Primary Document Grounding**: Every node is verified against official primary government PDFs archived in `literature/`.
