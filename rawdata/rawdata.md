# Raw Data Manifest & Cryptographic Provenance

This directory stores unmodified primary source extracts collected via official statistical releases from the Federal Ministry of Finance (*BMF*), Federal Statistical Office (*Destatis*), Bavarian State Ministry of Finance (*StMFH*), Bavarian State Office for Statistics (*LfStat*), City of Munich (*Stadtkämmerei & Statistisches Amt München*), and statutory social insurance authorities (*DRV, BMG, BA, DGUV*).

## Cryptographic Inventory

| File | Description | Bytes | SHA-256 Hash | Source URL / Authority | Retrieval Date |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `bayern_staatshaushalt_2023_2024.csv` | Bavarian state budget revenues and functional expenditures (2023–2024) | 5,161 | `08e80e0c5971e53d0beb7497164c08f6896bbe60fdd50d6e349b9149bd253ee8` | StMFH Bayern & ORH Jahresbericht 2024/2025 | 2026-10-24 |
| `demographics_zensus_denominators_2023_2024.csv` | Official resident population denominators (Zensus 2022 vs. Fortschreibung) | 1,885 | `2877220427fa1ddb70e9710d384369a002fcccb1f27517de420f92af24a68b5c` | Destatis, LfStat Bayern, Stat. Amt München | 2026-10-24 |
| `destatis_bundeshaushalt_2023_2024.csv` | Federal budget tax revenues and functional expenditures (2023–2024) | 8,817 | `9acff992afb343869002592f1c64a0493c5f5d0f97db8520c43e528138bebff1` | BMF Bundeshaushalt & Monatsberichte | 2026-10-24 |
| `destatis_sozialversicherung_2023_2024.csv` | Statutory social insurance branches (GRV, GKV, SPV, BA, DGUV) (2023–2024) | 7,144 | `e17b804207c2176a687019a0d0756dad8e4ce68fbce8e2be63e30003eaa4c552` | Destatis, BMAS, DRV, BMG, BA, DGUV | 2026-10-24 |
| `literature_empirical_benchmarks.csv` | Empirical literature benchmarks and certified register extracts | 10,194 | `8a4d27e60aaf43f39409f39b534cdc1ae3d373e175a3f60a750a021142f97423` | BMF, Destatis, DRV, BMG, StMFH, München | 2026-10-25 |
| `muenchen_haushalt_2023_2024.csv` | City of Munich municipal budget and functional allocations (2023–2024) | 7,328 | `c5e49b6e10f12f18c9349c914678571951a8c198747fec0b645c04bdd6a71a42` | Stadtkämmerei München (Haushaltsplan/Jahresabschluss) | 2026-10-24 |

All records are audited against administrative registers under the [`responsible-research`](../.agents/skills/responsible-research/SKILL.md) protocol.
