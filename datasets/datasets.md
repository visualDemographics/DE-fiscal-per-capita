# Audited Datasets Data Dictionary

This directory contains analysis-ready, reproducible datasets produced deterministically by `src/data_preparation.py` from verified primary source registers in `rawdata/`.

## 1. `datasets/literature_empirical_benchmarks.csv`
Central database of all external empirical scalar benchmarks extracted from official reports and literature:
- `parameter_id`: Unique alphanumeric identifier.
- `themenbereich`: Domain category (*Bundeshaushalt*, *Sozialversicherung*, *Staatshaushalt*, *Kommunalhaushalt*, *Demographie*).
- `indikator`: Clear description of the metric.
- `gruppe`: Administrative level or target group (`bund`, `bayern`, `muenchen`, `sozialversicherung`, `deutschland`).
- `wert`: Numeric standardized float.
- `einheit`: Physical/economic unit (`Milliarden_EUR`, `Millionen_Personen`).
- `exakter_quelltext_zitat`: Verbatim quotation from the primary source text or table.
- `lokale_datei`: Local path anchor.
- `methodischer_status`: Methodological data classification (`Amtliche_Registerstatistik`).

## 2. `datasets/fiscal_sankey_flows_per_capita.csv`
Contains the complete directed network graph for the 4-Layer Sankey visualization across 2023 and 2024:
- `jahr`: Budget year (`2023`, `2024`).
- `layer_source`: Originating layer (`Layer_1_Influx`, `Layer_2_Nominal`, `Layer_3_Effective`).
- `layer_target`: Destination layer (`Layer_2_Nominal`, `Layer_3_Effective`, `Layer_4_Buckets`).
- `source_node`: Identifier of the source node.
- `target_node`: Identifier of the target node.
- `wert_mrd_eur`: Absolute flow volume in billions of Euros (€ bn).
- `wert_eur_pro_kopf`: Flow normalized per capita (€/resident for a resident of Munich receiving services across all tiers). Exact Kirchhoff flow conservation is satisfied across all layers ($\Delta < 0{,}01\text{ €}$).

## 3. `datasets/fiscal_per_capita_summary.csv`
Summary balance sheet comparing the four public tiers and the composite stack:
- `jahr`: Budget year (`2023`, `2024`).
- `ebene`: Administrative tier (`Bund_Kernhaushalt`, `Sozialversicherungstraeger`, `Freistaat_Bayern`, `Landeshauptstadt_Muenchen`, `Muenchen_Resident_Composite_Stack`).
- `bevoelkerung_referenz`: Resident population denominator used for per-capita normalization (Zensus 2022 revised register).
- `gesamtvolumen_mrd_eur`: Total expenditure volume in € billion.
- `pro_kopf_eur`: Outlay per resident in Euros.

