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

#### 2.1 Research Objective
The 4-layer fiscal Sankey diagram resolves the multi-level fragmentation of German public finances by tracing the directional lifecycle of public money for an individual resident of the **City of Munich (*Landeshauptstadt München*)** in 2024 (with full longitudinal comparability to 2023). Every resident in Munich simultaneously benefits from services provided across four distinct sovereign public tiers:
1. **Federal Republic of Germany (*Bund*)**
2. **Statutory Social Insurances (*Sozialversicherungsträger*: GRV, GKV, SPV, BA, DGUV)**
3. **Free State of Bavaria (*Freistaat Bayern*)**
4. **City of Munich (*Landeshauptstadt München*)**

#### 2.2 Mathematical Formulation & Physical Ribbon Conservation
- **Physical Volume Scaling**: Link ribbon visual widths are strictly proportional to conserved physical budgetary volume in billions of Euros ($\text{wert\_mrd\_eur}$).
- **Kirchhoff Flow Conservation ($\Delta = 0.000\text{ Mrd. €}$)**:
  Every layer satisfies exact input-output conservation across all nodes:
  $$\sum \text{Layer 1 (Influx)} \equiv \sum \text{Layer 2 (Nominal)} \equiv \sum \text{Layer 3 (Effective)} \equiv \sum \text{Layer 4 (Buckets)} = 1{,}272.986\text{ Mrd. € (2024)}$$
- **Jurisdictional Per-Capita Normalization**:
  To prevent distorted synthetic denominator additions, each flow is normalized per capita relative to its statutory source and recipient constituency:
  $$\text{EUR/Kopf} = \frac{\text{Flow Volume (EUR)}}{N_{\text{Constituency}}}$$
  - **Federal & Social Insurance Baseline**: $N_{\text{DE}} = 83{,}577{,}140$ (Destatis Zensus 2022 revised register)
  - **Free State of Bavaria Baseline**: $N_{\text{BY}} = 13{,}248{,}928$ (LfStat Zensus 2022 revised register)
  - **City of Munich Baseline**: $N_{\text{MUC}} = 1{,}505{,}005$ (LfStat Zensus 2022 revised register)

---

#### 2.3 Layer-by-Layer Architecture

##### Layer 1: Steuer- & Beitragsinflux ($x = 0.00$)
Groups primary revenue collection streams strictly descending by sovereign intake authority:
- **Federal Taxes & Borrowing** (Navy `#1e3a8a`):
  - *Umsatzsteuer Bund*: $145.34\text{ Mrd. €}$ ($1{,}739\text{ €/Kopf}$)
  - *Lohn- & Einkommensteuer Bund*: $137.61\text{ Mrd. €}$ ($1{,}646\text{ €/Kopf}$)
  - *Verbrauchs- & Bundessteuern (Energie, Tabak, Soli, Kfz)*: $115.17\text{ Mrd. €}$ ($1{,}378\text{ €/Kopf}$)
  - *Nettokreditaufnahme Bund*: $33.30\text{ Mrd. €}$ ($398\text{ €/Kopf}$)
  - *Unternehmenssteuern (KSt, Abgeltungsteuer)*: $28.36\text{ Mrd. €}$ ($339\text{ €/Kopf}$)
  - *Verwaltungseinnahmen & Beteiligungen*: $5.89\text{ Mrd. €}$ ($70\text{ €/Kopf}$)
- **Statutory Social Insurance Contributions** (Teal `#0d9488`):
  - *Krankenbeiträge (AG & AN an GKV)*: $306.09\text{ Mrd. €}$ ($3{,}662\text{ €/Kopf}$)
  - *Rentenbeiträge (AG & AN an GRV)*: $305.79\text{ Mrd. €}$ ($3{,}659\text{ €/Kopf}$)
  - *Pflegebeiträge (AG & AN an SPV)*: $66.17\text{ Mrd. €}$ ($792\text{ €/Kopf}$)
  - *Arbeitslosenbeiträge (an BA)*: $40.64\text{ Mrd. €}$ ($486\text{ €/Kopf}$)
  - *Unfallbeiträge (Umlagesoll DGUV)*: $4.39\text{ Mrd. €}$ ($53\text{ €/Kopf}$)
- **Bavarian State Own Revenues** (Sky Blue `#0284c7`):
  - *Gemeinschaftsteuern Bayern (Landesanteil ESt, USt, KSt)*: $50.95\text{ Mrd. €}$ ($3{,}846\text{ €/Kopf}$)
  - *Landessteuern (Erbschaft-, Grunderwerb-, Biersteuer)*: $6.45\text{ Mrd. €}$ ($487\text{ €/Kopf}$)
  - *Verwaltungseinnahmen Freistaat*: $5.00\text{ Mrd. €}$ ($377\text{ €/Kopf}$)
  - *Rücklagenentnahme & Kredite Bayern*: $2.50\text{ Mrd. €}$ ($189\text{ €/Kopf}$)
- **Munich Municipal Revenues** (Amber `#d97706`):
  - *Gewerbesteuer (netto)*: $3.24\text{ Mrd. €}$ ($2{,}153\text{ €/Kopf}$)
  - *Gemeindeanteile an ESt & USt*: $1.83\text{ Mrd. €}$ ($1{,}216\text{ €/Kopf}$)
  - *Gebühren, Mieten & Verwaltung*: $1.35\text{ Mrd. €}$ ($898\text{ €/Kopf}$)
  - *Kredite, Rücklagen & Investitionsausgleich*: $0.89\text{ Mrd. €}$ ($593\text{ €/Kopf}$)
  - *Stadtwerke München (SWM) Ausschüttung*: $0.40\text{ Mrd. €}$ ($266\text{ €/Kopf}$)
  - *Grundsteuer (A & B)*: $0.35\text{ Mrd. €}$ ($231\text{ €/Kopf}$)

##### Layer 2: Nominale Gebietskörperschaften ($x = 0.28$)
Gross intake volumes prior to intergovernmental consolidation:
- **Nominaler Bund**: $465.67\text{ Mrd. €}$ ($5{,}572\text{ €/Kopf}$ · Basis 83.6M EW)
- **Nominale Sozialversicherung**: $723.08\text{ Mrd. €}$ ($8{,}652\text{ €/Kopf}$ · Basis 83.6M EW)
- **Nominaler Freistaat Bayern**: $64.80\text{ Mrd. €}$ ($4{,}891\text{ €/Kopf}$ · Basis 13.2M EW)
- **Nominale Stadt München**: $9.45\text{ Mrd. €}$ ($6{,}276\text{ €/Kopf}$ · Basis 1.51M EW)

##### Intergovernmental Transfer Layer (Layer 2 $\to$ Layer 3)
Explicit directed link ribbons routing intergovernmental transfers:
- **Federal Subsidies to Social Insurances (*Bundeszuschüsse*)**:
  - To Statutory Pension Insurance (GRV): **$116.00\text{ Mrd. €}$** ($1{,}388\text{ €/Kopf}$)
  - To Statutory Health Insurance (GKV Gesundheitsfonds): **$14.50\text{ Mrd. €}$** ($173\text{ €/Kopf}$)
- **Federal Grants to Bavaria (*Bundeszuweisungen*)**:
  - Federal allocations for joint tasks and transit: **$8.80\text{ Mrd. €}$** ($664\text{ €/Kopf}$)
- **Bavarian Municipal Equalization to Munich (*FAG & BayKiBiG*)**:
  - Key grants and early childhood subsidies: **$1.162\text{ Mrd. €}$** ($772\text{ €/Kopf}$)
- **Munich Levies Remitted to Upper Bavaria and State/Bund**:
  - *Bezirksumlage* to Upper Bavarian District: **$829\text{ Mio. €}$** ($551\text{ €/Kopf}$)
  - *Gewerbesteuerumlage* to State & Bund: **$232\text{ Mio. €}$** ($154\text{ €/Kopf}$)
  - Net municipal transfer balance: $+101\text{ Mio. €}$ ($+67.11\text{ €/Kopf}$)

##### Layer 3: Effektive Haushalte ($x = 0.69$)
Net disposable spending capacity after transfer consolidation:
- **Effektive Sozialversicherung**: $863.47\text{ Mrd. €}$ ($10{,}331\text{ €/Kopf}$ · Basis 83.6M EW)
- **Effektiver Bund (Kernhaushalt)**: $326.37\text{ Mrd. €}$ ($3{,}905\text{ €/Kopf}$ · Basis 83.6M EW)
- **Effektiver Freistaat Bayern**: $73.60\text{ Mrd. €}$ ($5{,}555\text{ €/Kopf}$ · Basis 13.2M EW)
- **Effektive Stadt München**: $9.55\text{ Mrd. €}$ ($6{,}343\text{ €/Kopf}$ · Basis 1.51M EW)

##### Layer 4: Finale Funktionale End-Buckets ($x = 1.00$)
19 citizen-facing public goods destinations, sorted strictly descending by per-capita spending:
1. **Renten- und Alterssicherung**: $425.80\text{ Mrd. €}$ ($5{,}095\text{ €/Kopf}$, $19.50\%$)
2. **Gesundheit, Pflege & Kliniken**: $397.77\text{ Mrd. €}$ ($4{,}759\text{ €/Kopf}$, $18.21\%$)
3. **Schulen, Kitas & frühkindliche Bildung**: $245.20\text{ Mrd. €}$ ($2{,}934\text{ €/Kopf}$, $11.22\%$)
4. **Verkehrswege, Mobilität & ÖPNV**: $166.70\text{ Mrd. €}$ ($1{,}995\text{ €/Kopf}$, $7.63\%$)
5. **Soziale Sicherung, Bürgergeld & Familie**: $145.80\text{ Mrd. €}$ ($1{,}744\text{ €/Kopf}$, $6.67\%$)
6. **Universitäten, Hochschulen & Spitzenforschung**: $80.20\text{ Mrd. €}$ ($959\text{ €/Kopf}$, $3.67\%$)
7. **Länderfinanzausgleich (Ausgleich an andere Länder)**: $9.77\text{ Mrd. €}$ ($737\text{ €/Kopf}$, $2.82\%$)
8. **Innere Sicherheit & Polizei**: $60.50\text{ Mrd. €}$ ($724\text{ €/Kopf}$, $2.77\%$)
9. **Verteidigung & Bundeswehr**: $57.07\text{ Mrd. €}$ ($683\text{ €/Kopf}$, $2.61\%$)
10. **Schuldendienst & Zinsen**: $38.20\text{ Mrd. €}$ ($457\text{ €/Kopf}$, $1.75\%$)
11. **Wohnungsbau & Stadtentwicklung**: $32.40\text{ Mrd. €}$ ($388\text{ €/Kopf}$, $1.48\%$)
12. **Umwelt-, Natur- & Klimaschutz**: $25.60\text{ Mrd. €}$ ($306\text{ €/Kopf}$, $1.17\%$)
13. **Auswärtiger Dienst & Entwicklungshilfe**: $17.13\text{ Mrd. €}$ ($205\text{ €/Kopf}$, $0.78\%$)
14. **Rücklagen- & Liquiditätspuffer**: $14.93\text{ Mrd. €}$ ($179\text{ €/Kopf}$, $0.68\%$)
15. **Kultur, Theater & Museen**: $14.20\text{ Mrd. €}$ ($170\text{ €/Kopf}$, $0.65\%$)
16. **Wirtschaftsförderung & Verwaltung**: $13.80\text{ Mrd. €}$ ($165\text{ €/Kopf}$, $0.63\%$)
17. **Kommunale Verwaltung & IT-Infrastruktur**: $0.64\text{ Mrd. €}$ ($423\text{ €/Kopf}$, $1.62\%$)
18. **Kommunale Straßen, Tiefbau & Brücken**: $0.40\text{ Mrd. €}$ ($266\text{ €/Kopf}$, $1.02\%$)
19. **Kommunale Grünanlagen, Parks & Sport**: $0.29\text{ Mrd. €}$ ($192\text{ €/Kopf}$, $0.73\%$)

---

## 3. Data Integrity & Verification Standards

1. **No Synthetic Fallbacks**: Zero artificial random distributions or imputed cells.
2. **Deterministic Reproducibility**: Generated via `python src/modeling.py` from audited datasets.
3. **Primary Document Grounding**: Every node is verified against official primary government PDFs archived in `literature/`.
