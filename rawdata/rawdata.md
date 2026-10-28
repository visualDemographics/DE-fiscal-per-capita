# Raw Data Manifest & Cryptographic Provenance

This directory stores unmodified primary source extracts collected via official statistical releases from the Federal Ministry of Finance (*BMF*), Federal Statistical Office (*Destatis*), Bavarian State Ministry of Finance (*StMFH*), Bavarian State Office for Statistics (*LfStat*), City of Munich (*Stadtkämmerei & Statistisches Amt München*), and statutory social insurance authorities (*DRV, BMAS, BMG, BA, DGUV*).

## Cryptographic Inventory

### Primary Source Tables in `rawdata/`

| File | Description | Bytes | SHA-256 Hash | Deep Source URL | Retrieval Date |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `bayern_staatshaushalt_2023_2024.csv` | Bavarian state budget revenues, tax receipts, and functional expenditures (Soll/Plan 2024, Ist 2023) | 6,014 | `02dc8670d05e015e15f800efb4c1301c4726bf204989d08d40f90aa6445baf7b` | [bayern_staatshaushalt_2023_2024](https://www.verkuendung-bayern.de/gvbl/2024-114/) | 2026-10-25 |
| `demographics_zensus_denominators_2023_2024.csv` | Official resident population denominators (Zensus 2022 revised vs. Pre-Zensus 2011 basis) | 2,242 | `78ef6e427ccb00929f2002f8232ce004a36732bf4fa66f4497023582ec8830ec` | [demographics_zensus_denominators_2023_2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/tabelle-geschlechtseintrag-2023.html) | 2026-10-25 |
| `destatis_bundeshaushalt_2023_2024.csv` | Federal budget actual outlays (Ist 2024), tax revenues, and net borrowing | 10,954 | `c9f4f8988afa8f074d1e1636e91cb0b46409d5ae5b739bb789d079dd189146e7` | [destatis_bundeshaushalt_2023_2024](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2025/01/Inhalte/Kapitel-3-Analysen/3-2-vorlaeufiger-abschluss-bundeshaushalt-2024.html) | 2026-10-25 |
| `destatis_sozialversicherung_2023_2024.csv` | Statutory social insurance contributions and expenditures (GRV, GKV, SPV, BA, DGUV) | 8,071 | `3a037e32de8967ab629dbb97187c4ca997ac79677331150a484ccf1ab1206767` | [destatis_sozialversicherung_2023_2024](https://www.bmas.de/DE/Service/Publikationen/Broschueren/a230-sozialbudget.html) | 2026-10-25 |
| `literature_empirical_benchmarks.csv` | Audited empirical benchmarks certified against primary government PDF reports | 9,464 | `0683be089bbea095a4611b22284da0d695a0c5bd62bc040d028ddcd2cde0fac3` | [literature_empirical_benchmarks](https://www.destatis.de/DE/Themen/Staat/Oeffentliche-Finanzen/Ausgaben-Einnahmen/Tabellen/laenderfinanzausgleich.html) | 2026-10-25 |
| `muenchen_haushalt_2023_2024.csv` | City of Munich municipal budget (Gesamtergebnisplan 2024) and municipal taxes | 8,102 | `ff98cac700fcdbcceb231edf979c5fd0daafcd1bea3f7ca68b782c79f19cb210` | [muenchen_haushalt_2023_2024](https://stadt.muenchen.de/infos/haushaltsplaene-vorjahre.html) | 2026-10-25 |

### Primary Source Documents in `literature/`

| Primary PDF Document | Bytes | SHA-256 Hash |
| :--- | :---: | :--- |
| `BMAS_2024_Sozialbudget_2023.pdf` | 964,936 | `4585a3bcae2b8ac529f4017154cef133dba600ac0e31f6ee9f421d80ca55f07c` |
| `BMF_2025_Steuereinnahmen_Dezember_2024.pdf` | 362,512 | `acfb4d496fcbd07b08a4d2b1e40b32562926542920eb7dbbf97abbb8aa04a6a4` |
| `BMF_2025_Vorlaeufiger_Abschluss_Bundeshaushalt_2024.pdf` | 571,970 | `592a4f4c9aac80f280b1a3ae65eca51e52e02105b5a2e4f93ea31d22d89e7105` |
| `Bayern_GVBl_2024_Haushaltsgesetz_2024_2025.pdf` | 769,604 | `e7a92d65d189852cc0cb6ee3463bdf7a9d3d887cd4680bf90aabce67bda57545` |
| `Destatis_2024_Qualitaetsbericht_Zensus_2022.pdf` | 680,526 | `0b2179b1e4c8973d6e5acf6acf0d4f2e09cffc8fe96677bcdc84a62560457d47` |
| `Destatis_2024_Statement_Zensus_2022.pdf` | 1,483,717 | `8eef44a3747fc99a1f993e771de41d587da10918c21e94a421746736d92e9321` |
| `LfStat_2024_Statistik_Kommunal_Muenchen_09162.pdf` | 1,654,075 | `5c27683caf381e6e3f4238a977d20653147f8547de22010ad401c1b6c16487bb` |
| `Muenchen_2024_Haushaltsplan_Band_1_Gesamthaushalt.pdf` | 5,783,166 | `db17489b563d0ca3048caf66a2e771eedfe09e1adfe15c77cbd0a291d25b2cd1` |

All records are audited against primary administrative registers under the [`responsible-research`](../.agents/skills/responsible-research/SKILL.md) protocol.
