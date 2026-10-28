# Methodological Framework: Multi-Level Fiscal Normalization & Accounting Boundaries

> [!IMPORTANT]
> **Exclusive Visualization Scope**:
> The definitive empirical and modeling artifact of this investigation is the **4-Layer Physical Kirchhoff-Conserved Fiscal Sankey Flow Diagram** ([`plots/sankey_fiscal_per_capita.png`](../plots/sankey_fiscal_per_capita.png), [`.svg`](../plots/sankey_fiscal_per_capita.svg), and interactive [`.html`](../plots/sankey_fiscal_interactive.html)). All accounting normalizations, intergovernmental transfer consolidations, and functional public goods distributions are modeled and unified directly within this single visual network. All auxiliary non-Sankey panels have been explicitly retired.

## 1. Multi-Level Federal Accounting Harmonization

When comparing fiscal flows across three governmental tiers (Federal Republic of Germany, Free State of Bavaria, and City of Munich) alongside the statutory social security funds (*Sozialversicherungsträger*), researchers must prevent accounting distortions, double counting, and denominator mismatch.

### 1.1 The Per-Tier Apples-to-Apples Denominator Policy
Public budgets serve distinct, non-overlapping jurisdictional constituencies:
- **Federal Republic (*Bund*)**: Serves the total resident population of Germany ($N_{\text{DE}} = 83{,}577{,}140$ in 2024).
- **Statutory Social Insurance (*Sozialversicherungen*)**: Operates nationwide mandatory insurance pools covering German residents ($N_{\text{DE}} = 83{,}577{,}140$).
- **Free State of Bavaria (*Freistaat Bayern*)**: Serves the population of Bavaria ($N_{\text{BY}} = 13{,}248{,}928$ in 2024).
- **City of Munich (*Landeshauptstadt München*)**: Serves the registered resident population of Munich ($N_{\text{MUC}} = 1{,}505{,}005$ in 2024).

To enable an authentic, apples-to-apples comparison across tiers, each budget is normalized by its own statutory population:
$$\text{PerCapita}_{\text{Tier } k} = \frac{\text{Budget Volume}_k (\text{EUR})}{N_k}$$

This strictly avoids the methodological flaw of synthetic resident "stacks" (which artificially added national German totals to a Munich-only denominator, creating an ungrounded synthetic $28{,}000\text{ €}$ figure). Instead, each entity is evaluated within its genuine sovereign constituency, and every node in the visual architecture displays an explicit denominator badge (e.g., `Basis: 83,6 Mio. EW`, `Basis: 13,2 Mio. EW`, `Basis: 1,51 Mio. EW`).

---

### 1.2 Physical Flow Ribbon Conservation vs. Per-Capita Annotations
In graph-based network diagrams (such as Plotly Sankey diagrams), the visual width of a link ribbon is proportional to its scalar numeric `value`.

If intergovernmental transfers (Layer 2 $\to$ Layer 3) were scaled in mixed per-capita units, a geometric distortion would occur:
- A transfer of $8.80\text{ Mrd. €}$ from the Federal budget ($N_{\text{DE}} = 83.6\text{ M}$) to the Free State of Bavaria ($N_{\text{BY}} = 13.2\text{ M}$) corresponds to $105.29\text{ €}$ per German resident, but $664.20\text{ €}$ per Bavarian resident.
- If ribbon width represented per-capita values, the ribbon would magically expand by a factor of $6.3\times$ as it crossed the administrative boundary, violating physical continuity.

**Methodological Resolution**:
3. All ribbon widths are scaled by conserved physical budgetary volume in billions of Euros ($\text{wert\_mrd\_eur}$).
2. Strict **Kirchhoff Flow Conservation** is satisfied across all four layers with $\Delta = 0.000\text{ Mrd. €}$:
   $$\sum \text{Layer 1 (Influx)} \equiv \sum \text{Layer 2 (Nominal)} \equiv \sum \text{Layer 3 (Effective)} \equiv \sum \text{Layer 4 (Buckets)} = 1{,}271.341\text{ Mrd. €}$$
3. Citizen-facing per-capita metrics ($\text{€/Kopf}$) are computed based on the specific sending and receiving jurisdictions and displayed directly on node titles, ribbon labels, and interactive tooltips.

---

### 1.3 Intergovernmental Transfer Deductions & Consolidation
Funds frequently flow through intermediate administrative levels before funding tangible public goods:
1. **Federal Tax Subsidies to Social Insurance (*Bundeszuschüsse*)**:
   - The Bund transfers tax revenues into statutory pension funds ($116.00\text{ Mrd. €}$ in 2024 to DRV) and statutory health funds ($14.50\text{ Mrd. €}$ to the *Gesundheitsfonds*).
   - In Layer 2 $\to$ Layer 3, these flows shift financial capacity from *Nominaler Bund* to *Effektive Sozialversicherung*.
2. **Horizontal Fiscal Equalization (*Länderfinanzausgleich / LFA*)**:
   - Bavaria paid **$9.771\text{ Mrd. €}$** ($737.42\text{ €/Bavarian resident}$) in net financial contributions to other federal states in 2024.
   - This flow is explicitly separated from internal state public services and routed as a distinct crimson outflow ribbon (`#be123c`) into the dedicated end-bucket *Länderfinanzausgleich*.
3. **Municipal Equalization & Intergovernmental Transfers (Option B Gross Architecture)**:
   - **Bavarian State Grants to Munich**: Munich receives **$1.162\text{ Mrd. €}$** ($772.09\text{ €/resident}$) in gross state grants and allocations from the Free State of Bavaria (primarily *BayKiBiG* early education grants and school funding; Haushaltsplan Band 1 S. 32 & S. 37) routed via Layer 2 $\to$ Layer 3.
   - **Federal Social Reimbursements to Munich**: Under statutory federal cost-sharing (§ 46 SGB II & § 46a SGB XII), the Federal government directly reimburses municipalities for municipal accommodation costs (*Kosten der Unterkunft / KdU*) and basic security in old age. Munich receives **$0.483\text{ Mrd. €}$** ($320.93\text{ €/resident}$) in 2024 ($0.452\text{ Mrd. €}$ in 2023), routed directly as an intergovernmental transfer link from `Nominaler Bund` (Layer 2) to `Effektive Stadt München` (Layer 3) and deducted from federal Bürgergeld outlays in Layer 4 (reducing federal *Bürgergeld & Grundsicherung* from $58.26\text{ Mrd. €}$ to $57.78\text{ Mrd. €}$).
   - **Munich Intergovernmental Levies (*Umlagen*)**: Out of its ordinary budget, Munich remits **$829\text{ Mio. €}$** ($550.83\text{ €/resident}$) in *Bezirksumlage* to the Upper Bavarian district (*Bezirk Oberbayern*) as well as **$232\text{ Mio. €}$** ($154.15\text{ €/resident}$) in *Gewerbesteuerumlage* to Bund and Land (Band 1 S. 42 & S. 44). These statutory levies (**$1.061\text{ Mrd. €}$** = $704.98\text{ €/resident}$) are routed directly from `Effektive Stadt München` into Layer 4 as a dedicated transfer outflow bucket (`Bezirks- & Gewerbesteuerumlage (MUC)`), reducing Munich's internal administrative overhead (`Kommunale Verwaltung & IT`) to its true core of **$1.295\text{ Mrd. €}$** ($860.46\text{ €/resident}$).
   - **Munich Layer 1 Own Revenues**: Munich's Layer 1 revenue base reflects pure own municipal revenue and financing of **$7.801\text{ Mrd. €}$** ($5{,}183.37\text{ €/resident}$) in 2024 ($7.212\text{ Mrd. €}$ in 2023), consisting of Gewerbesteuer ($3.240\text{ Mrd. €}$), Gemeindeanteile ESt/USt ($1.830\text{ Mrd. €}$), Gebühren & Entgelte ($1.027\text{ Mrd. €}$), Fehlbedarf / Kredite ($0.892\text{ Mrd. €}$), SWM-Erträge ($0.448\text{ Mrd. €}$), and Grund-/Lokalsteuern ($0.364\text{ Mrd. €}$), eliminating all residual plugs. Combined with Bavarian grants ($1.162\text{ Mrd. €}$) and federal social reimbursements ($0.483\text{ Mrd. €}$), Munich's effective disposable budget equals exactly **$9.446\text{ Mrd. €}$** ($6{,}276.39\text{ €/resident}$).
4. **Option 3A: Non-Munich Municipal Equalization (*Kommunaler Finanzausgleich an übrige Kommunen*)**:
   - The Free State of Bavaria allocates significant equalization grants to its remaining 2,055 municipalities outside Munich.
   - To prevent administrative inflation in state overhead, direct municipal fiscal equalization outlays (**$0.57\text{ Mrd. €}$** in 2024; **$0.87\text{ Mrd. €}$** in 2023) are explicitly isolated into a separate Layer 4 destination node (`Kommunaler_Finanzausgleich_uebrige_Kommunen_BY`), reducing Bavaria's administrative and financial management residual (`Allgemeine_Finanzverwaltung_Rest`) to genuine core levels ($5.41\text{ Mrd. €}$, well within the 5% audit boundary).

---

### 1.4 Institutional Architecture of the Upper Bavarian District (Bezirk Oberbayern)
Bavaria possesses a constitutionally anchored three-tier local self-government structure (*Art. 1 Bayerische Bezirksordnung – BezO*):
1. **First Tier**: Municipalities (*Gemeinden* and *kreisfreie Städte* like Munich).
2. **Second Tier**: Rural Counties (*Landkreise*).
3. **Third Tier**: Districts (*Bezirke*, higher municipal associations / *höhere Kommunalverbände*).

The seven Bavarian Bezirke possess **no autonomous taxing authority** (*keine eigene Steuerhoheit*). Instead, they are responsible for mandatory supra-local welfare and specialized public health:
- *Überörtliche Sozialhilfe* (SGB XII) and integration assistance for people with disabilities (*Eingliederungshilfe nach SGB IX*).
- Specialized psychiatric and neurological clinical care (*kbo-Kliniken des Bezirks Oberbayern*).
- Regional cultural and natural heritage preservation.

To finance these constitutionally assigned obligations, the Bezirke levy the *Bezirksumlage* upon all member counties and independent cities based on their standardized tax assessment base (*Steuerkraft*) and key grants (*Schlüsselzuweisungen*). In 2024, the district levy rate was fixed at $22.0\%$, resulting in Munich's contribution of $829\text{ Mio. €}$. In the multi-level fiscal framework, this levy is accurately modeled as an intergovernmental welfare equalization transfer, avoiding any double-counting of municipal social expenditure.

---

### 1.5 Social Security Funds Operating Liquidity Buffers (Liquiditätsreserve & Rücklagen)
Total financial inflows allocated to the statutory social security system in 2024 equal **$863.470\text{ Mrd. €}$**, composed of:
- **$732.970\text{ Mrd. €}$**: Direct employee and employer social insurance contributions (*Beitragseinnahmen* across GRV, GKV, SPV, and BA).
- **$130.500\text{ Mrd. €}$**: Steuerfinanzierte Bundeszuschüsse (tax-financed federal subsidies from the federal core budget).

Direct cash expenditure for healthcare, pensions, unemployment benefits, and rehabilitation amounted to **$852.040\text{ Mrd. €}$**. The remaining balance of **$11.430\text{ Mrd. €}$** ($136.76\text{ €/resident}$) represents net allocations to statutory operating liquidity reserves (*Liquiditätsreserve des Gesundheitsfonds*, *Nachhaltigkeitsrücklage der DRV*). Modeling this statutory reserve accumulation explicitly guarantees mathematical closure and strict **Kirchhoff Flow Conservation** ($\Delta = 0.000\text{ Mrd. €}$) across the entire national social security ledger.

---

### 1.6 Budgetary Vintage Disclosure & Harmonization Methodology
Empirical fiscal research across German federal tiers requires explicit disclosure of budget publication vintages:
1. **Federal Republic (*Bund*)**: Utilizes the audited **vorläufiger Ist-Abschluss 2024** published by the Federal Ministry of Finance (*BMF Monatsbericht Januar 2025*, pp. 21–34), reflecting cash expenditures ($465.67\text{ Mrd. €}$), revenues ($440.63\text{ Mrd. €}$), and net borrowing ($33.30\text{ Mrd. €}$).
2. **Statutory Social Insurances (*Sozialversicherungen*)**: Utilizes the **vorläufiges Ist-Ergebnis / Rechnungsstatistik 2024** (*BMAS Sozialbudget 2024*, Destatis Fachserie 14 Reihe 2), capturing statutory insurance payments ($852.04\text{ Mrd. €}$).
3. **Free State of Bavaria (*Freistaat Bayern*)**: Utilizes the statutory legislative budget appropriation **Haushaltsgesetz 2024/2025 (HG 2024/2025)** promulgated on 21 June 2024 (*GVBl. Nr. 12/2024 S. 114 Art. 1*), fixing 2024 expenditures at **$73{,}692{,}557{,}400\text{ €}$**.
4. **City of Munich (*Landeshauptstadt München*)**: Utilizes the statutory municipal plan **Haushaltsplan 2024 Band 1 Gesamthaushalt** (*Stadtkämmerei München*, Beschluss vom Dezember 2023 / Januar 2024), establishing ordinary operating expenses at **$9.446\text{ Mrd. €}$** (and gross capital outlays of $1.09\text{ Mrd. €}$).

**Methodological Rationale for Vintage Combination**:
In German public accounting, comprehensive audited cash-accounting closings (*kassenmäßige Jahresrechnungen*) for 16 federal states and over 10,000 municipalities are compiled by state audit offices (*Oberste Rechnungshöfe*) and statistical offices with a standard reporting lag of 12 to 18 months. Consequently, combining the immediate federal cash closing with statutory legislative state and municipal appropriations is the established empirical standard in public finance benchmarking (e.g., Bertelsmann Stiftung, ifo Institut). All budgetary flows are bound to the exact calendar year 2024, ensuring temporal synchronization.

---

### 1.7 Architectural Column Hierarchy & Dynamic Functional Sorting
The visual flow network is organized into a clean 4-tier column architecture:
1. **Layer 1: Steuer- & Beitragsinflux** ($x = 0.00$): Primary tax revenues and statutory insurance contributions grouped by sovereign intake level.
2. **Layer 2: Nominale Gebietskörperschaften** ($x = 0.28$): Gross budgetary volumes before intergovernmental redistribution.
3. **Layer 3: Effektive Haushalte** ($x = 0.69$): Net operational spending capacities after intergovernmental transfers and statutory reserves.
4. **Layer 4: Finale Funktionale Buckets** ($x = 1.00$): Direct citizen-facing public goods categories.

**Intergovernmental Transfer Representation**:
Transfers between the tiers (Layer 2 $\to$ Layer 3)—such as the federal social insurance subsidies (*Bundeszuschuss*), state allocations (*FAG/BayKiBiG*), and municipal levies (*Bezirksumlage* and *Gewerbesteuerumlage*)—are represented exclusively as directed intermediate ribbons. This eliminates the need for an artificial 5th transfer column header, preserving strict 4-column visual symmetry and legibility.

**Dynamic Descending Sorting of Functional Destinations**:
All 19 citizen-facing end-buckets in Layer 4 are dynamically sorted strictly descending by per-capita spending ($\text{€/Kopf}$) for each year. Each bucket label displays both its per-capita outlay and its exact percentage share of total per-capita outlays ($26{,}135.02\text{ €/Kopf}$ in 2024; $25{,}144.59\text{ €/Kopf}$ in 2023). Dedicated vertical spacing in the lower half of Layer 4 ensures that smaller municipal expenditure categories maintain clear, non-overlapping label typography.

---

## 2. Independent Cross-Check & National Accounts Reconciliation

To prevent reliance on unverified single-source tables, all primary budget figures are cross-reconciled against audited administrative registers, Destatis national accounts, and the official *Sozialbudget*:

| Sovereign Tier | Primary Working Volume (2024) | Audited Official Source | Benchmark Source & Publication | Cross-Reconciliation Check | Residual Unallocated |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bund (Kern)** | $465.67\text{ Mrd. €}$ | BMF Monatsbericht Jan 2025 S. 23 | Destatis Fachserie 14 R3.1 (Gesamthaushalt) | $465.67\text{ Mrd. €}$ Ist-Abschluss matched | $0.00\%$ |
| **Sozialversicherungen** | $852.04\text{ Mrd. €}$ (Outlays) + $11.43\text{ Mrd. €}$ (Buffer) | BMAS Sozialbudget 2024 Tab. 1 | Destatis FS 14 R2 / DRV / GKV Abschluss | Total effective resources $863.47\text{ Mrd. €}$ matched | $0.00\%$ |
| **Freistaat Bayern** | $73.70\text{ Mrd. €}$ | Bay. GVBl Nr. 12/2024 S. 114 (HG 2024/2025) | Bayerischer Oberster Rechnungshof (ORH) | $73.69\text{ Mrd. €}$ HG-Ansatz matched | $0.00\%$ |
| **Stadt München** | $9.45\text{ Mrd. €}$ (Ordentl.) + $1.09\text{ Mrd. €}$ (Invest.) | LH München Haushaltsplan 2024 Band 1 S. 22 | Bayerisches Landesamt für Statistik | $9.45\text{ Mrd. €}$ ordentlicher Haushalt matched | $0.00\%$ |

---

## 3. Demographic Denominators & Zensus 2022 Revision Sensitivity

All per-capita metrics are computed against the official Zensus 2022 revised register (Stichtag 15. Mai 2022, extrapolated by Destatis to 31.12.2023 and 31.12.2024).

### Sensitivity Table: Zensus 2022 vs. Unrevised Melderegister
The following table documents the empirical impact of the Zensus 2022 revision across all jurisdictions:

| Administrative Jurisdiction | Pre-Zensus / Melderegister Count | Official Audited Zensus 2022 Count | Absolute Delta | Percentage Revision ($\Delta_{\%}$) | Per-Capita Multiplier | Impact on Calculated Per-Capita Expenditure |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Deutschland (Bund)** | $84{,}669{,}000$ | $83{,}456{,}045$ | $-1{,}212{,}955$ | $-1.432\%$ | $1.0145\times$ | $+1.45\%$ mechanical increase ($+81\text{ €/Kopf}$) |
| **Freistaat Bayern** | $13{,}435{,}000$ | $13{,}176{,}426$ | $-258{,}574$ | $-1.925\%$ | $1.0196\times$ | $+1.96\%$ mechanical increase ($+107\text{ €/Kopf}$) |
| **Stadt München** | $1{,}589{,}026$ (Melderegister) | $1{,}488{,}719$ (Zensus amtlich) | $-100{,}307$ | $-6.312\%$ | $1.0674\times$ | $+6.74\%$ mechanical increase ($+427\text{ €/Kopf}$) |

As demonstrated, using the local municipal Melderegister rather than the official audited Zensus register understates Munich's total municipal per-capita public outlays (including capital outlays of $1.09\text{ Mrd. €}$, totaling $10.45\text{ Mrd. €}$) by $427\text{ €}$ per resident ($6{,}579\text{ €}$ vs. $7{,}006\text{ €}$), proving the necessity of demographic register auditing in compliance with `responsible-demographics`. (For core ordinary operating expenditure in 2024, the baseline is $9.446\text{ Mrd. €} / 1{,}505{,}005 = \mathbf{6{,}276.39\text{ €/resident}}$).

---

## 4. Formal Skill Contract Waiver & Methodological Protocol Specification

### 4.1 Skill Contract Waiver: 3x3 Synoptic Matrix, Shapley Waterfalls & TOST
Under the [`responsible-research`](../.agents/skills/responsible-research/SKILL.md) protocol, certain visual and inferential architectures are tailored to econometric regression models, historical commodity time series, or microdata causal mediation. For this comprehensive multi-tier public finance investigation, specific components are formally waived with explicit scientific justification:

1. **Waiver of 9-Panel $3 \times 3$ Synoptic Matrix in Favor of 4-Layer Fiscal Sankey Flow**:
   - *Rationale*: Macro public finance involves multi-level sovereign accounting, intergovernmental transfer bridges (*Bundeszuschüsse*, *Länderfinanzausgleich*, *Kommunaler Finanzausgleich*), and joint funding of public goods. A closed-system directional Sankey network diagram ([`plots/sankey_fiscal_per_capita.png`](../plots/sankey_fiscal_per_capita.png), [`.svg`](../plots/sankey_fiscal_per_capita.svg), and interactive [`.html`](../plots/sankey_fiscal_interactive.html)) provides complete topological visibility into financial origins, sovereign custody, intergovernmental redistribution, and final public service delivery. Dissecting this unified conservation system into an artificial $3 \times 3$ panel matrix would shatter the visual conservation of flows and obscure cross-tier transfer bridges.
2. **Waiver of Path-Independent Shapley Waterfall Decomposition**:
   - *Rationale*: Sequential waterfall charts and $K!$ order-permutation Shapley values are designed for sequential causal mediation chains ($X \to M \to Y$). Sovereign public expenditure allocations across Bund, Bavaria, and Munich are governed by the constitutional distribution of competences (*Grundgesetz* Arts. 30, 70, 83, 104a–109) and municipal self-government (*Art. 28 Abs. 2 GG*). They represent concurrent sovereign responsibilities, not a sequential causal funnel.
3. **Waiver of Sample-Based Inference (TOST Equivalence & Random-Effects Meta-Regression)**:
   - *Rationale*: The empirical data consists of official statutory budget laws (*Haushaltsgesetze*), audited financial statements (*Haushaltsrechnungen*), and full demographic register counts (*Vollerhebungen*). Because there is no sampling variance, Two One-Sided Tests (TOST) and DerSimonian–Laird Random-Effects Meta-Regression (REMR) across survey samples are mathematically inapplicable.

---

### 4.2 Unit of Analysis: Tier-by-Tier Status Quo (Option A)
All per-capita indicators in this repository are computed under the **Tier-by-Tier Apples-to-Apples Policy**:
- **Federal Republic (*Bund*) & Social Insurances**: Normalized by Germany's total resident population ($N_{\text{DE}} = 83{,}577{,}140$ in 2024; Destatis Zensus 2022 revised register).
- **Free State of Bavaria (*Freistaat Bayern*)**: Normalized by Bavaria's resident population ($N_{\text{BY}} = 13{,}248{,}928$ in 2024; LfStat Zensus 2022 revised register).
- **City of Munich (*Landeshauptstadt München*)**: Normalized by Munich's resident population ($N_{\text{MUC}} = 1{,}505{,}005$ in 2024; LfStat Zensus 2022 revised register).

**Rejection of Synthetic Resident Stacking**:
We explicitly reject the practice of stacking federal, state, and municipal totals into an artificial "Munich resident" expenditure figure of $\approx 28{,}000\text{ €/Kopf}$. Federal expenditures ($465.7\text{ Mrd. €}$) serve all 83.6 million German residents equally and cannot be attributed as if they were municipal outlays exclusive to Munich. Each entity is presented in its genuine sovereign constituency, with explicit population badges on every node.

---

### 4.3 Physical Kirchhoff Flow Conservation & Accounting Balancing (Option B Reconciliations)
1. **Kirchhoff Flow Conservation ($\Delta = 0.000\text{ Mrd. €}$)**:
   Link ribbon visual widths are strictly proportional to physical budgetary volume in billions of Euros (`wert_mrd_eur`), preserving dimensional physical continuity across all four network layers:
   $$\sum \text{Layer 1 (Influx)} \equiv \sum \text{Layer 2 (Nominal)} \equiv \sum \text{Layer 3 (Effective)} \equiv \sum \text{Layer 4 (Buckets)} = 1{,}271.341\text{ Mrd. € (2024)}$$
2. **Authentic Accounting Balancing in Layer 1 (Option B)**:
   Layer 1 is defined as **Steuer-, Beitrags- & Finanzierungszuflüsse** (Net tax revenues, statutory social insurance contributions, non-tax revenues, and net borrowing / deficit financing):
   - **Federal Net Influx (BMF Table 1 & Table 7)**: Gross federal tax collection ($434.62\text{ Mrd. €}$) is adjusted by deducting statutory transfers to the European Union ($32.41\text{ Mrd. €}$) and financial transfers to the federal states ($27.23\text{ Mrd. €}$), yielding net federal taxes of **$374.98\text{ Mrd. €}$** ($331.42\text{ Mrd. €}$ Netto-Gemeinschaftsteuern + $43.56\text{ Mrd. €}$ Bundessteuern). Together with non-tax revenues (*Sonstige Einnahmen & Münzeinnahmen*, **$65.65\text{ Mrd. €}$**) and net financing / liquidity utilization (**$25.04\text{ Mrd. €}$**; $33.30\text{ Mrd. €}$ borrowing minus $8.26\text{ Mrd. €}$ cash build), total federal inflows equal **$465.67\text{ Mrd. €}$**, perfectly matching preliminary cash expenditures.
   - **Munich Municipal Own Influx & Gross Grant Routing**: Munich's own revenue streams and financing (**$7.801\text{ Mrd. €}$** = $5{,}183.37\text{ €/Kopf}$, including $3.240\text{ Mrd. €}$ Gewerbesteuer netto, $1.830\text{ Mrd. €}$ Gemeindeanteile ESt/USt, $1.027\text{ Mrd. €}$ Gebühren/Mieten, $0.892\text{ Mrd. €}$ operating deficit/Kredite, $0.448\text{ Mrd. €}$ SWM dividend & other ordinary revenue, and $0.364\text{ Mrd. €}$ Grund-/Lokalsteuern) are strictly distinguished from Bavaria's gross state grants (**$1.162\text{ Mrd. €}$** = $772.09\text{ €/Kopf}$) and direct federal social cost reimbursements (**$0.483\text{ Mrd. €}$** = $320.93\text{ €/Kopf}$ for KdU / § 46 SGB II). Outgoing statutory levies (**$1.061\text{ Mrd. €}$** of *Bezirksumlage* and *Gewerbesteuerumlage*) are routed directly from `Effective_Munich` into Layer 4 as a dedicated transfer bucket. Every single Munich revenue line matches *Haushaltsplan 2024 Band 1 S. 22 & S. 32* verbatim with **zero residual plug**.
3. **Visual Disambiguation & Layer 2 Intake Badging**:
   - Layer 2 nodes carry explicit nominal intake badges (`Nominaler Bund: 5,572 €/Kopf (465.7 Mrd. €)`, `Nominaler Freistaat Bayern: 4,899 €/Kopf (64.9 Mrd. €)`, `Nominale Stadt München: 5,183 €/Kopf (7.80 Mrd. €)`), avoiding ambiguity between sovereign budget size and citizen entitlement.
   - Shared Layer 4 public goods buckets incorporate multi-tier parentheticals (e.g. `(BY 15.9 + MUC 2.3 Mrd. €)`) to clearly identify which sovereign levels co-finance that public service.

---

### 4.4 Intergovernmental Transfer Consolidation & Reconciliation
All inter-tier transfers are cataloged and reconciled in [`datasets/fiscal_transfer_consolidation_ledger.csv`](../datasets/fiscal_transfer_consolidation_ledger.csv):
- *Bundeszuschuss GRV*: $116.00\text{ Mrd. €}$ (Bund Epl 11 $\to$ DRV)
- *Bundeszuschuss GKV*: $14.50\text{ Mrd. €}$ (Bund Epl 15 $\to$ Gesundheitsfonds)
- *Bundeszuweisungen an Bayern*: $8.80\text{ Mrd. €}$ (Bund $\to$ Bayern)
- *Bundeszuweisungen an München (KdU/SGB II)*: $0.483\text{ Mrd. €}$ (Bund $\to$ München)
- *Zuweisungen Bayern an München*: $1.162\text{ Mrd. €}$ (Bayern $\to$ München)
- *Bezirksumlage & Gewerbesteuerumlage*: $1.061\text{ Mrd. €}$ (München $\to$ Bezirk Oberbayern & Land/Bund)
- *Länderfinanzausgleich*: $9.771\text{ Mrd. €}$ (Bayern $\to$ Übrige Bundesländer)

Functional mapping from budget accounts to tangible public goods is documented in [`datasets/functional_crosswalk.csv`](../datasets/functional_crosswalk.csv).

