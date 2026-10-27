# Raw Data Manifest & Cryptographic Provenance

This directory stores unmodified primary source extracts collected via official statistical releases from the Federal Ministry of Finance (*BMF*), Federal Statistical Office (*Destatis*), Bavarian State Ministry of Finance (*StMFH*), Bavarian State Office for Statistics (*LfStat*), City of Munich (*Stadtkämmerei & Statistisches Amt München*), and statutory social insurance authorities (*DRV, BMAS, BMG, BA, DGUV*).

## Cryptographic Inventory

| File | Description | Bytes | SHA-256 Hash | Deep Source URL | Retrieval Date |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `bayern_staatshaushalt_2023_2024.csv` | Bavarian state budget revenues, tax receipts, and functional expenditures (Soll/Plan 2024, Ist 2023) | 6,014 | `02dc8670d05e015e15f800efb4c1301c4726bf204989d08d40f90aa6445baf7b` | [bayern_staatshaushalt_2023_2024](https://www.verkuendung-bayern.de/gvbl/2024-114/) | 2026-10-25 |
| `demographics_zensus_denominators_2023_2024.csv` | Official resident population denominators (Zensus 2022 revised vs. Pre-Zensus 2011 basis) | 2,242 | `78ef6e427ccb00929f2002f8232ce004a36732bf4fa66f4497023582ec8830ec` | [demographics_zensus_denominators_2023_2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/tabelle-geschlechtseintrag-2023.html) | 2026-10-25 |
| `destatis_bundeshaushalt_2023_2024.csv` | Federal budget actual outlays (Ist 2024), tax revenues, and net borrowing | 9,849 | `9d81409a07c66055f51bf93f413330c508165e3b153f04084da1e44e55e3cf61` | [destatis_bundeshaushalt_2023_2024](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2025/01/Inhalte/Kapitel-3-Analysen/3-2-vorlaeufiger-abschluss-bundeshaushalt-2024.html) | 2026-10-25 |
| `destatis_sozialversicherung_2023_2024.csv` | Statutory social insurance contributions and expenditures (GRV, GKV, SPV, BA, DGUV) | 8,071 | `3a037e32de8967ab629dbb97187c4ca997ac79677331150a484ccf1ab1206767` | [destatis_sozialversicherung_2023_2024](https://www.bmas.de/DE/Service/Publikationen/Broschueren/a230-sozialbudget.html) | 2026-10-25 |
| `literature_empirical_benchmarks.csv` | Audited empirical benchmarks certified against primary government PDF reports | 9,786 | `2bf0511faa22468dce52fbfec0fafc2ba487d5b9c82aa47aef5790ef40f1efd9` | [literature_empirical_benchmarks](https://www.destatis.de/DE/Themen/Staat/Oeffentliche-Finanzen/Ausgaben-Einnahmen/Tabellen/laenderfinanzausgleich.html) | 2026-10-25 |
| `muenchen_haushalt_2023_2024.csv` | City of Munich municipal budget (Gesamtergebnisplan 2024) and municipal taxes | 8,102 | `ff98cac700fcdbcceb231edf979c5fd0daafcd1bea3f7ca68b782c79f19cb210` | [muenchen_haushalt_2023_2024](https://stadt.muenchen.de/infos/haushaltsplaene-vorjahre.html) | 2026-10-25 |

All records are audited against primary administrative registers under the [`responsible-research`](../.agents/skills/responsible-research/SKILL.md) protocol.
