# Empirical Research Goal & Scope

> [!IMPORTANT]
> **Exclusive Analytical & Visualization Focus**:
> This repository is dedicated **exclusively to the 4-Layer Fiscal Per-Capita Sankey Architecture** ([`sankey_fiscal_per_capita.png`](../plots/sankey_fiscal_per_capita.png), [`.svg`](../plots/sankey_fiscal_per_capita.svg), and interactive [`.html`](../plots/sankey_fiscal_interactive.html)). All empirical pipelines, accounting normalizations, and visualization codes serve solely to construct and audit this unified multi-level Sankey network. Intermediate auxiliary sub-panels and matrices have been explicitly retired.

## Research Scope & Motivation
This investigation establishes a unified, multi-level empirical per-capita fiscal breakdown for the Federal Republic of Germany (*Bund*), the Free State of Bavaria (*Freistaat Bayern*), and the City of Munich (*Landeshauptstadt München*), spanning the 2023–2024 budgetary reporting period.

By following the **Responsible Empirical Research Protocol** (`responsible-research`) and demographic standardization principles (`responsible-demographics`), this analysis constructs a 4-layer Sankey flow:
- **Layer 1: Sources of Influx**:
  - Federal tax revenues (federal share of joint taxes *Gemeinschaftsteuern* like income tax and VAT, plus pure federal taxes like energy, tobacco, and solidarity surcharge) and statutory social insurance contributions (*Gesetzliche Renten-, Kranken-, Pflege-, Arbeitslosen- und Unfallversicherung*).
  - Bavarian state tax revenues (state share of joint taxes, state taxes like *Grunderwerbsteuer*, minus net horizontal equalisation outflow *Länderfinanzausgleich*).
  - Munich municipal tax revenues (*Gewerbesteuer*, municipal shares of income tax and VAT, property tax *Grundsteuer*, and local fees).
- **Layer 2: Sovereign Tiers Nominal**:
  - Nominal budgetary intake points normalized per capita across all four public institutions: Federal Core Budget (*Bund Kernhaushalt*), Statutory Social Insurance (*Sozialversicherungsträger*), Free State of Bavaria (*Freistaat Bayern*), and City of Munich (*Landeshauptstadt München*).
- **Layer 3: Effective Spending Authorities**:
  - Intergovernmental transfer consolidation explicitly mapping federal subsidies (*Bundeszuschüsse* to pension and health insurance), federal allocations to Bavaria (*Bundeszuweisungen*), direct federal social cost reimbursements to Munich (*KdU & Grundsicherung SGB II/XII*), and Bavarian municipal fiscal equalization (*Schlüsselzuweisungen / FAG* to Munich).
  - Yields the true net operational spending authority of each tier without double-counting (with Munich's statutory levies *Bezirksumlage* and *Gewerbesteuerumlage* isolated into Layer 4).
- **Layer 4: Final Functional Buckets**:
  - Tracing resource allocation into tangible public goods and citizen services:
    - Old-Age & Survivors Pensions (*Rentenversicherung & Beamtenversorgung*)
    - Health & Long-Term Care (*Krankenversicherung, Pflegeversicherung, Krankenhausinvestitionen*)
    - Schools & Early Childhood Education (*Schulgebäude, Kitas, Lehrpersonal*)
    - Universities, Higher Education & Scientific Research (*Universitäten TUM/LMU, DFG, Max-Planck-Gesellschaft*)
    - National Defense & Foreign Affairs (*Bundeswehr, Sondervermögen, Internationale Zusammenarbeit*)
    - Transport & Infrastructure (*Autobahnen, Bundesschienenwege/DB, Staatsstraßen, MVG/ÖPNV, Kommunale Straßen*)
    - Public Safety, Police & Justice (*Landespolizei Bayern, Bundespolizei, Justizwesen, KVR/Feuerwehr*)
    - Labor, Social Support & Municipal Housing (*Bürgergeld, BA-Arbeitsmarktförderung, Sozialhilfe, Wohnungsbau*)
    - Public Debt Service & Administration (*Bundesschuld-Zinsen, Kommunale Verwaltung*)

## Administrative Entities & Jurisdictions
1. **Federal Republic of Germany (Bund)**: Central national government and statutory social insurance funds (*Sozialversicherungsträger*).
2. **Free State of Bavaria (Freistaat Bayern)**: Federal state (*Bundesland*) responsible for schools, police, universities, and regional transport.
3. **City of Munich (Landeshauptstadt München)**: Independent municipal district (*Kreisfreie Großstadt*) responsible for local daycares, school infrastructure, municipal hospitals (*München Klinik*), local transit, and municipal utilities.

## Skill Contract Waiver & Unit of Analysis Specification (Option A)
In accordance with formal repository design specifications:
- **Skill Contract Waiver**: The 9-panel $3 \times 3$ synoptic matrix, Shapley waterfall permutations, and TOST sample tests are formally waived in favor of the closed-system 4-layer Kirchhoff-conserved Sankey flow diagram ([`plots/sankey_fiscal_per_capita.png`](../plots/sankey_fiscal_per_capita.png)). Macro public finance flows require topological conservation and intergovernmental transfer bridges rather than sample regression panels.
- **Unit of Analysis (Tier-by-Tier Status Quo)**: Each sovereign tier's budget is normalized by its own statutory resident population ($N_{\text{DE}} = 83{,}577{,}140$, $N_{\text{BY}} = 13{,}248{,}928$, $N_{\text{MUC}} = 1{,}505{,}005$ in 2024), preserving constitutional boundaries without misleading stacked denominator additions.
- **Kirchhoff Flow Conservation**: Ribbon widths represent conserved physical volume in billions of Euros ($\Delta = 0.000\text{ Mrd. €}$ across all four layers), while per-capita indicators and sovereign population badges are displayed on each node and tooltip.

