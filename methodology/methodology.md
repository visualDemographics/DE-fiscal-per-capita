# Methodological Framework: Multi-Level Fiscal Normalization & Accounting Boundaries

## 1. Multi-Level Federal Accounting Harmonization

When comparing fiscal flows across three governmental tiers (Federal Republic of Germany, Free State of Bavaria, and City of Munich) alongside the statutory social security funds (*Sozialversicherungsträger*), researchers must prevent three major accounting distortions:

### 1.1 The Intergovernmental Transfer Double-Counting Problem (*Zahlungen zwischen den Ebenen*)
In gross public budgets, funds frequently pass through multiple administrative tiers before being spent on tangible public goods:
1. **Federal Subsidies to Social Insurances (*Bundeszuschüsse zur Sozialversicherung*)**:
   - The Federal government transfers $> €112\text{ billion}$ annually from federal tax revenues to the Statutory Pension Insurance (*Deutsche Rentenversicherung*) and $\sim €14.5\text{ billion}$ to the Statutory Health Insurance (*Gesundheitsfonds*).
   - In our 3-Layer Sankey, this transfer is explicitly modeled as a flow from **Federal Taxes (Layer 1)** $\to$ **Social Insurance Funds (Layer 2)** $\to$ **Final Pension & Healthcare Outflows (Layer 3)**, ensuring that total public expenditure is not artificially inflated by counting both the tax revenue and the insurance payout as separate independent pools.
2. **Horizontal Fiscal Equalization (*Länderfinanzausgleich / Finanzkraftausgleich*)**:
   - Bavaria is the largest net contributor in Germany, paying out $\sim €9.1\text{ billion}$ (2023) to financially weaker states.
   - This outflow is accounted for as a dedicated deduction from Bavaria's raw tax influx in Layer 1, showing the net available budget for Bavarian public expenditures.
3. **Municipal Fiscal Equalization (*Kommunaler Finanzausgleich / FAG*)**:
   - The Free State of Bavaria transfers funds via *Schlüsselzuweisungen* to Bavarian municipalities.
   - For the City of Munich, these state transfers are mapped as a transition flow from Bavaria $\to$ Munich, linking the state budget to municipal public goods (schools, daycares, public transit).

### 1.2 Boundary Alignment: Standalone vs. Munich Composite Resident Stack
- **Standalone Regional Average**:
  - Federal outlays divided by German population: $\text{PerCapita}_{\text{Bund}} = \frac{\text{Budget}_{\text{Bund}}}{N_{\text{DE}}}$.
  - Bavarian state outlays divided by Bavarian population: $\text{PerCapita}_{\text{Bayern}} = \frac{\text{Budget}_{\text{Bayern}}}{N_{\text{BY}}}$.
  - Munich municipal outlays divided by Munich population: $\text{PerCapita}_{\text{München}} = \frac{\text{Budget}_{\text{München}}}{N_{\text{MUC}}}$.
- **Munich Composite Stack**:
  - A citizen living in Munich simultaneously benefits from and pays into all three levels:
    $$\text{PerCapita}_{\text{München, Composite}} = \text{PerCapita}_{\text{Bund}} + \text{PerCapita}_{\text{Sozialversicherung}} + \text{PerCapita}_{\text{Bayern}} + \text{PerCapita}_{\text{München}}$$
  - This provides the complete, true fiscal balance sheet of public money per resident.

---

## 2. Demographic Denominators & Zensus 2022 Revisions

In accordance with [`responsible-demographics`](../.agents/skills/responsible-demographics/SKILL.md), using outdated population projections distorts per-capita metrics:
- **Federal Germany ($N_{\text{DE}}$)**:
  - Pre-Zensus 2022 estimate: $84,669,000$
  - Official Zensus 2022 adjusted register: $83,445,000$ ($-1,224,000$ or $-1.45\%$)
- **Free State of Bavaria ($N_{\text{BY}}$)**:
  - Pre-Zensus 2022 estimate: $13,435,000$
  - Official Zensus 2022 adjusted register: $13,180,000$ ($-255,000$ or $-1.90\%$)
- **City of Munich ($N_{\text{MUC}}$)**:
  - Local municipal Melderegister (Hauptwohnsitz): $1,589,000$
  - Official Zensus 2022 count: $1,509,000$ ($-80,000$ or $-5.03\%$)

Both tiers are evaluated in sensitivity analysis, with Tier 1 (Zensus 2022) as the audited baseline.

---

## 3. Strict AST Code & Reproducibility Contract

1. All data transformations are fully deterministic in `src/data_preparation.py`.
2. Modeling and plotting logic resides in `src/modeling.py` with zero hardcoded values, zero synthetic distributions (`np.random`, `.rvs`), and zero silent `.get(key, 0.0)` fallbacks.
3. Every parameter from external statistical reports is registered with exact quotation and page coordinates in `datasets/literature_empirical_benchmarks.csv`.

