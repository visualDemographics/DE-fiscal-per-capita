# Raw Data Manifest & Cryptographic Provenance

This directory stores unmodified primary source extracts collected via official statistical releases from the Federal Ministry of Finance (*BMF*), Federal Statistical Office (*Destatis*), Bavarian State Ministry of Finance (*StMFH*), Bavarian State Office for Statistics (*LfStat*), City of Munich (*Stadtkämmerei & Statistisches Amt München*), and statutory social insurance authorities (*DRV, BMG, BA, DGUV*).

## Cryptographic Inventory

| File | Description | Bytes | SHA-256 Hash | Source URL / Authority | Retrieval Date |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `bayern_staatshaushalt_2023_2024.csv` | Bavarian state budget revenues and functional expenditures (2023–2024) | 5,161 | `08e80e0c5971e53d0beb7497164c08f6896bbe60fdd50d6e349b9149bd253ee8` | StMFH Bayern & ORH Jahresbericht 2024/2025 | 2026-10-24 |
| `demographics_zensus_denominators_2023_2024.csv` | Official resident population denominators (Zensus 2022 vs. Fortschreibung) | 1,885 | `2877220427fa1ddb70e9710d384369a002fcccb1f27517de420f92af24a68b5c` | Destatis, LfStat Bayern, Stat. Amt München | 2026-10-24 |
| `destatis_bundeshaushalt_2023_2024.csv` | Federal budget tax revenues and functional expenditures (2023–2024) | 8,587 | `479c89d7612f71835560d8efa5b08e9ce2ff7b87befb355c6a12efa63c1855f6` | BMF Bundeshaushalt & Monatsberichte | 2026-10-24 |
| `destatis_sozialversicherung_2023_2024.csv` | Statutory social insurance branches (GRV, GKV, SPV, BA, DGUV) (2023–2024) | 7,144 | `e17b804207c2176a687019a0d0756dad8e4ce68fbce8e2be63e30003eaa4c552` | Destatis, BMAS, DRV, BMG, BA, DGUV | 2026-10-24 |
| `literature_empirical_benchmarks.csv` | Empirical literature benchmarks and certified register extracts | 10,110 | `6bcbbb3fe877a0f8c143004741491123728e5a026f57a8e6c59ad08129da5c4e` | BMF, Destatis, DRV, BMG, StMFH, München | 2026-10-25 |
| `muenchen_haushalt_2023_2024.csv` | City of Munich municipal budget and functional allocations (2023–2024) | 6,321 | `f8e2f9801519051c987c6ced0ce4f0dff498d05d26d9ecc407b487aece0de0c2` | Stadtkämmerei München (Haushaltsplan/Jahresabschluss) | 2026-10-24 |

All records are audited against administrative registers under the [`responsible-research`](../.agents/skills/responsible-research/SKILL.md) protocol.
