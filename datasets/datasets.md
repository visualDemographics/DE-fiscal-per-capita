# Audited Datasets Data Dictionary

This directory contains analysis-ready, reproducible datasets produced deterministically by `src/data_preparation.py` from verified primary source registers in `rawdata/`.

---

## 1. `datasets/literature_empirical_benchmarks.csv`
Central database of all external empirical scalar benchmarks extracted from official primary reports and verified literature:
- `parameter_id`: Unique alphanumeric identifier (e.g., `BUND_AUSGABEN_2024`, `BAYERN_LFA_ABFLUSS_2024`, `DE_GEMEINDE_STEUERN_PRO_KOPF_2024`).
- `themenbereich`: Domain category (*Bundeshaushalt*, *Sozialversicherung*, *Staatshaushalt*, *Kommunalhaushalt*, *Demographie*).
- `indikator`: Clear description of the metric.
- `gruppe`: Administrative level or target group (`bund`, `bayern`, `muenchen`, `sozialversicherung`, `deutschland`).
- `wert`: Numeric standardized float.
- `einheit`: Physical/economic unit (`Milliarden_EUR`, `Millionen_Personen`, `EUR_pro_Kopf`).
- `exakter_quelltext_zitat`: Verbatim quotation from the primary source text or table.
- `lokale_datei`: Local path anchor to verified primary document in `literature/`.
- `methodischer_status`: Methodological data classification (`Amtliche_Registerstatistik`).

---

## 2. `datasets/fiscal_sankey_flows_per_capita.csv`
Contains the complete directed network graph for the 4-Layer Sankey visualization across 2023 and 2024:
- `jahr`: Budget year (`2023`, `2024`).
- `layer_source`: Originating layer (`Layer_1_Influx`, `Layer_2_Nominal`, `Layer_3_Effective`).
- `layer_target`: Destination layer (`Layer_2_Nominal`, `Layer_3_Effective`, `Layer_4_Buckets`).
- `source_node`: Identifier of the source node.
- `target_node`: Identifier of the target node.
- `wert_mrd_eur`: Absolute conserved physical flow volume in billions of Euros (€ bn). Kirchhoff flow conservation holds across all 4 layers ($\Delta = 0.000\text{ Mrd. €}$ across all stages: 1,272.986 Mrd. € in 2024).
- `wert_eur_pro_kopf`: Citizen-facing per-capita equivalent in Euros per resident, normalized by the specific sending/receiving sovereign population ($N_{\text{DE}}$, $N_{\text{BY}}$, or $N_{\text{MUC}}$).

---

## 3. `datasets/fiscal_per_capita_summary.csv`
Summary balance sheet comparing the four public tiers on an apples-to-apples basis:
- `jahr`: Budget year (`2023`, `2024`).
- `ebene`: Administrative tier:
  - `Bund_Kernhaushalt`: Federal core budget divided by German population ($N_{\text{DE}} = 83{,}577{,}140$ in 2024; $5{,}571.74\text{ €/resident}$).
  - `Sozialversicherungstraeger`: Statutory social insurance expenditures divided by German population ($N_{\text{DE}} = 83{,}577{,}140$ in 2024; $10{,}194.65\text{ €/resident}$).
  - `Freistaat_Bayern`: Free State of Bavaria state budget divided by Bavarian population ($N_{\text{BY}} = 13{,}248{,}928$ in 2024; $5{,}562.71\text{ €/resident}$).
  - `Landeshauptstadt_Muenchen`: Munich municipal budget divided by Munich population ($N_{\text{MUC}} = 1{,}505{,}005$ in 2024; $6{,}276.39\text{ €/resident}$ ordentlich, $7{,}005.96\text{ €/resident}$ Gesamtetat).
- `bevoelkerung_referenz`: Resident population denominator used for per-capita normalization (audited Zensus 2022 revised register).
- `gesamtvolumen_mrd_eur`: Total expenditure volume in € billion.
- `pro_kopf_eur`: Standardized outlay per resident in Euros.
