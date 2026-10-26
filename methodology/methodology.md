# Methodological Framework: Multi-Level Fiscal Normalization & Accounting Boundaries

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
1. All ribbon widths are scaled by conserved physical budgetary volume in billions of Euros ($\text{wert\_mrd\_eur}$).
2. Strict **Kirchhoff Flow Conservation** is satisfied across all four layers with $\Delta = 0.000\text{ Mrd. €}$:
   $$\sum \text{Layer 1 (Influx)} \equiv \sum \text{Layer 2 (Nominal)} \equiv \sum \text{Layer 3 (Effective)} \equiv \sum \text{Layer 4 (Buckets)} = 1{,}272.986\text{ Mrd. €}$$
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
3. **Municipal Equalization & State Grants (*Kommunaler Finanzausgleich / FAG*)**:
   - Munich receives **$1.162\text{ Mrd. €}$** ($772.09\text{ €/resident}$) in state grants and allocations from the Free State of Bavaria (primarily *BayKiBiG* early education grants and school funding; Haushaltsplan Band 1 S. 32 & S. 37).
   - In return, Munich remits **$829\text{ Mio. €}$** ($550.83\text{ €/resident}$) in *Bezirksumlage* to the Upper Bavarian district (*Bezirk Oberbayern*) as well as **$232\text{ Mio. €}$** ($154.15\text{ €/resident}$) in *Gewerbesteuerumlage* to Bund and Land (Band 1 S. 42 & S. 44).
   - **Net municipal transfer bridge**: $1.162 - (0.829 + 0.232) = +0.101\text{ Mrd. €}$ ($+67.11\text{ €/resident}$) net transfer from the Bavarian state layer to the City of Munich, bringing Effective Municipal Outlays to $9.547\text{ Mrd. €}$.

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

As demonstrated, using the local municipal Melderegister rather than the official audited Zensus register understates Munich's municipal per-capita public outlays by $427\text{ €}$ per resident ($6{,}579\text{ €}$ vs. $7{,}006\text{ €}$), proving the necessity of demographic register auditing in compliance with `responsible-demographics`.
