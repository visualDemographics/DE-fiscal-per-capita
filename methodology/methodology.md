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
   - Bavaria transfers $1.69\text{ Mrd. €}$ ($1{,}122.92\text{ €/resident}$) in municipal key grants (*Schlüsselzuweisungen*) and daycare operational grants (*BayKiBiG*) to Munich.
   - Munich transfers $930\text{ Mio. €}$ ($617.94\text{ €/resident}$) in *Bezirksumlage* to the Upper Bavarian district (*Bezirk Oberbayern*) and $410\text{ Mio. €}$ in *Gewerbesteuerumlage*.

---

## 2. Independent Cross-Check & National Accounts Reconciliation

To prevent reliance on unverified single-source tables, all primary budget figures are cross-reconciled against audited administrative registers, Destatis national accounts, and the official *Sozialbudget*:

| Sovereign Tier | Primary Working Volume (2024) | Audited Official Source | Benchmark Source & Publication | Cross-Reconciliation Check | Residual Unallocated |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bund (Kern)** | $465.67\text{ Mrd. €}$ | BMF Monatsbericht Jan 2025 S. 23 | Destatis Fachserie 14 R3.1 (Gesamthaushalt) | $465.67\text{ Mrd. €}$ Ist-Abschluss matched | $0.00\%$ |
| **Sozialversicherungen** | $723.08\text{ Mrd. €}$ (rein) | BMAS Sozialbudget 2024 Tab. 1 | DRV/GKV/SPV/BA Jahresrechnungen | Total gross outlays $853.58\text{ Mrd. €}$ incl. Bundeszuschuss | $0.00\%$ |
| **Freistaat Bayern** | $73.70\text{ Mrd. €}$ | Bay. GVBl Nr. 12/2024 (Haushaltsgesetz) | Bayerischer Oberster Rechnungshof (ORH) | $73.70\text{ Mrd. €}$ Gesamtausgaben matched | $0.00\%$ |
| **Stadt München** | $10.54\text{ Mrd. €}$ | LH München Haushaltsplan 2024 Band 1 | Bayerisches Landesamt für Statistik | $9.45\text{ Mrd. €}$ ordentlich + $1.09\text{ Mrd. €}$ Investitionen | $0.00\%$ |

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
