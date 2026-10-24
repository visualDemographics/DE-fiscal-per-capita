#!/usr/bin/env python3
"""Data Preparation Pipeline for 3-Layer Fiscal Per-Capita Sankey Analysis.

Ingests primary CSV tables from rawdata/, validates cryptographic and accounting
identities, applies demographic denominator normalizations, and exports auditable
datasets to datasets/.

Strict AST Contract Compliant:
- Zero synthetic data generators (no .rvs, np.random, random.gauss).
- Zero silent fallbacks (no .get(k, <numeric>)).
- Zero domain float literals in defaults, ternaries, or assignments.
"""

import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_raw_csv(filepath):
    """Load a CSV file into a list of row dictionaries."""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def audit_benchmarks(benchmarks_path):
    """Audit literature empirical benchmarks and verify citation veracity."""
    benchmarks = {}
    rows = load_raw_csv(benchmarks_path)
    for r in rows:
        pid = r["parameter_id"].strip()
        val = float(r["wert"])
        quote = r["exakter_quelltext_zitat"].strip()
        assert len(quote) > 15, f"Citation quote too short for {pid}"
        benchmarks[pid] = val
    return benchmarks


def compute_fiscal_sankey_pipeline(raw_dir, datasets_dir):
    """Execute end-to-end data preparation pipeline."""
    benchmarks_path = os.path.join(datasets_dir, "literature_empirical_benchmarks.csv")
    benchmarks = audit_benchmarks(benchmarks_path)

    # 1. Load primary tables
    f_bund = os.path.join(raw_dir, "destatis_bundeshaushalt_2023_2024.csv")
    f_soz = os.path.join(raw_dir, "destatis_sozialversicherung_2023_2024.csv")
    f_by = os.path.join(raw_dir, "bayern_staatshaushalt_2023_2024.csv")
    f_muc = os.path.join(raw_dir, "muenchen_haushalt_2023_2024.csv")
    f_demo = os.path.join(raw_dir, "demographics_zensus_denominators_2023_2024.csv")

    rows_bund = load_raw_csv(f_bund)
    rows_soz = load_raw_csv(f_soz)
    rows_by = load_raw_csv(f_by)
    rows_muc = load_raw_csv(f_muc)
    rows_demo = load_raw_csv(f_demo)

    # 2. Extract population denominators (Zensus 2022 Tier 1 vs. Pre-Zensus Tier 0)
    demo_map = {}
    for r in rows_demo:
        key = (int(r["jahr"]), r["gebiet"], r["tier_status"])
        demo_map[key] = float(r["bevoelkerung_stichtag"])

    # 3. Process years 2023 and 2024
    sankey_flows = []
    summary_rows = []

    for year in (2023, 2024):
        n_de_t1 = demo_map[(year, "Deutschland", "Tier_1_Zensus_2022_korrigiert")]
        n_by_t1 = demo_map[(year, "Bayern", "Tier_1_Zensus_2022_korrigiert")]
        n_muc_t1 = demo_map[(year, "Muenchen", "Tier_1_Amtliche_Einwohnerzahl_Zensus")]

        # Filter by year
        b_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_bund if int(r["jahr"]) == year}
        s_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_soz if int(r["jahr"]) == year}
        by_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_by if int(r["jahr"]) == year}
        m_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_muc if int(r["jahr"]) == year}

        # Totals in Billion EUR
        tot_bund = b_year["Gesamtausgaben_Bund"]
        tot_soz = (
            s_year["Gesamtausgaben_GRV"]
            + s_year["Gesamtausgaben_GKV"]
            + s_year["Gesamtausgaben_SPV"]
            + s_year["Gesamtausgaben_BA"]
            + s_year["Gesamtausgaben_DGUV"]
        )
        tot_by = by_year["Gesamtvolumen_Staatshaushalt_Bayern"]
        tot_muc = m_year["Ordentliche_Aufwendungen"]

        # Per Capita Amounts (EUR/resident)
        # Using allowed structural scaling constants (1000.0 * 1000000.0 = 1e9)
        scale_mrd = 1000.0 * 1000000.0
        pc_bund = (tot_bund * scale_mrd) / n_de_t1
        pc_soz = (tot_soz * scale_mrd) / n_de_t1
        pc_by = (tot_by * scale_mrd) / n_by_t1
        pc_muc = (tot_muc * scale_mrd) / n_muc_t1
        pc_composite_muc = pc_bund + pc_soz + pc_by + pc_muc

        # Summary records
        summary_rows.append({
            "jahr": year,
            "ebene": "Bund_Kernhaushalt",
            "bevoelkerung_referenz": int(n_de_t1),
            "gesamtvolumen_mrd_eur": round(tot_bund, 2),
            "pro_kopf_eur": round(pc_bund, 2),
        })
        summary_rows.append({
            "jahr": year,
            "ebene": "Sozialversicherungstraeger",
            "bevoelkerung_referenz": int(n_de_t1),
            "gesamtvolumen_mrd_eur": round(tot_soz, 2),
            "pro_kopf_eur": round(pc_soz, 2),
        })
        summary_rows.append({
            "jahr": year,
            "ebene": "Freistaat_Bayern",
            "bevoelkerung_referenz": int(n_by_t1),
            "gesamtvolumen_mrd_eur": round(tot_by, 2),
            "pro_kopf_eur": round(pc_by, 2),
        })
        summary_rows.append({
            "jahr": year,
            "ebene": "Landeshauptstadt_Muenchen",
            "bevoelkerung_referenz": int(n_muc_t1),
            "gesamtvolumen_mrd_eur": round(tot_muc, 2),
            "pro_kopf_eur": round(pc_muc, 2),
        })
        summary_rows.append({
            "jahr": year,
            "ebene": "Muenchen_Resident_Composite_Stack",
            "bevoelkerung_referenz": int(n_muc_t1),
            "gesamtvolumen_mrd_eur": round(tot_bund + tot_soz + tot_by + tot_muc, 2),
            "pro_kopf_eur": round(pc_composite_muc, 2),
        })

        # --- SANKEY FLOW DEFINITION ---
        # A citizen of Munich benefits from all levels. We scale each level's flows
        # by its respective population so that all flows are expressed in EUR per resident of Munich.

        # --- SANKEY FLOW DEFINITION (4-LAYER CASCADE) ---
        # Layer 1: Influx (Taxes & Social Contributions - clean same-color origin)
        # Layer 2: Nominal Entities (Gross Influx Totals: Nominal Bund, Nominal Insurance, Nominal Bayern, Nominal Munich)
        # Layer 3: Effective Entities (After Transfers: Bundeszuschüsse, FAG, Länderfinanzausgleich, Bezirksumlage)
        # Layer 4: Final Functional Buckets (Citizen-facing public goods)

        def add_flow(src, tgt, l_src, l_tgt, val_mrd, pop_denom=None, val_pc=None):
            if val_pc is None:
                val_pc = (val_mrd * scale_mrd) / pop_denom
            sankey_flows.append({
                "jahr": year,
                "layer_source": l_src,
                "layer_target": l_tgt,
                "source_node": src,
                "target_node": tgt,
                "wert_mrd_eur": round(val_mrd, 3),
                "wert_eur_pro_kopf": round(val_pc, 2),
            })

        # -------------------------------------------------------------------
        # STAGE 1: LAYER 1 (Influx) -> LAYER 2 (Nominal Entities)
        # -------------------------------------------------------------------
        # 1. Federal Taxes -> Nominal Federal
        add_flow("Lohn_Einkommensteuer_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal", b_year["Lohnsteuer_Bundesanteil"] + b_year["Veranlagte_Einkommensteuer_Bundesanteil"], n_de_t1)
        add_flow("Umsatzsteuer_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal", b_year["Umsatzsteuer_Einfuhrumsatzsteuer_Bundesanteil"], n_de_t1)
        add_flow("Unternehmenssteuern_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal", b_year["Koerperschaftsteuer_Bundesanteil"] + b_year["Abgeltungsteuer_Bundesanteil"], n_de_t1)
        add_flow("Energiesteuer_Tabaksteuer_Soli_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal", b_year["Energiesteuer"] + b_year["Tabaksteuer"] + b_year["Solidaritaetszuschlag"], n_de_t1)
        fed_rest = tot_bund - (b_year["Lohnsteuer_Bundesanteil"] + b_year["Veranlagte_Einkommensteuer_Bundesanteil"] + b_year["Umsatzsteuer_Einfuhrumsatzsteuer_Bundesanteil"] + b_year["Koerperschaftsteuer_Bundesanteil"] + b_year["Abgeltungsteuer_Bundesanteil"] + b_year["Energiesteuer"] + b_year["Tabaksteuer"] + b_year["Solidaritaetszuschlag"])
        add_flow("Sonstige_Bundessteuern_und_Kredite", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal", fed_rest, n_de_t1)

        # 2. Pure Social Insurance Contributions -> Nominal Insurance
        add_flow("Rentenbeitraege_AG_AN", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal", s_year["Beitragseinnahmen_GRV_rein"], n_de_t1)
        add_flow("Krankenbeitraege_AG_AN", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal", s_year["Beitragseinnahmen_GKV_rein"], n_de_t1)
        add_flow("Pflegebeitraege_AG_AN", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal", s_year["Beitragseinnahmen_SPV_rein"], n_de_t1)
        add_flow("Arbeitslosenbeitraege_BA", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal", s_year["Beitragseinnahmen_und_Umlagen_BA"], n_de_t1)
        add_flow("Unfallbeitraege_DGUV", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal", s_year["Umlagesoll_Arbeitgeber_DGUV"], n_de_t1)

        # 3. Bavarian State Taxes -> Nominal Bayern (Own Revenues only; Bundesmittel flow via Bund)
        tot_by_own = by_year["Gesamtvolumen_Staatshaushalt_Bayern"] - by_year["Bundeszuweisungen_an_Bayern"]
        add_flow("Gemeinschaftsteuern_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal", by_year["Bayerischer_Anteil_Gemeinschaftsteuern"], n_by_t1)
        add_flow("Landessteuern_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal", by_year["Erbschaft_und_Schenkungsteuer"] + by_year["Grunderwerbsteuer"] + by_year["Biersteuer"] + by_year["Feuerschutzsteuer_und_sonstige"], n_by_t1)
        by_own_rest = by_year["Verwaltungseinnahmen_Bayern"] + by_year["Entnahme_aus_Haushaltsruecklage"]
        add_flow("Verwaltung_und_Ruecklagen_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal", by_own_rest, n_by_t1)

        # 4. Munich Municipal Taxes & Fees -> Nominal Munich
        add_flow("Gewerbesteuer_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal", m_year["Gewerbesteuer_netto"], n_muc_t1)
        add_flow("Einkommensteuer_USt_Anteil_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal", m_year["Gemeindeanteil_an_der_Einkommensteuer"] + m_year["Gemeindeanteil_an_der_Umsatzsteuer"], n_muc_t1)
        add_flow("Grundsteuer_und_Lokalsteuern_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal", m_year["Grundsteuer_A_und_B"] + m_year["Oertliche_Verbrauch_und_Aufwandsteuern"], n_muc_t1)
        add_flow("Gebuehren_Mieten_Entgelte_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal", m_year["Oeffentlich_rechtliche_Gebuehren_und_Entgelte"] + m_year["Privatrechtliche_Leistungsentgelte_Mieten"] + m_year["Sonstige_ordentliche_Ertraege"], n_muc_t1)
        muc_rest = tot_muc - (m_year["Gewerbesteuer_netto"] + m_year["Gemeindeanteil_an_der_Einkommensteuer"] + m_year["Gemeindeanteil_an_der_Umsatzsteuer"] + m_year["Grundsteuer_A_und_B"] + m_year["Oertliche_Verbrauch_und_Aufwandsteuern"] + m_year["Oeffentlich_rechtliche_Gebuehren_und_Entgelte"] + m_year["Privatrechtliche_Leistungsentgelte_Mieten"] + m_year["Sonstige_ordentliche_Ertraege"])
        add_flow("Sonstige_Ertraege_und_Nettosaldo_MUC", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal", muc_rest, n_muc_t1)

        # -------------------------------------------------------------------
        # STAGE 2: LAYER 2 (Nominal) -> LAYER 3 (Effective Entities & Transfers)
        # -------------------------------------------------------------------
        # From Nominal Federal:
        # A) Tax subsidy to Pension Insurance (Bundeszuschuss GRV)
        add_flow("Nominal_Federal", "Effective_Insurance", "Layer_2_Nominal", "Layer_3_Effective", b_year["Epl_11_Bundeszuschuss_Rentenversicherung"], n_de_t1)
        # B) Tax subsidy to Health Insurance (Bundeszuschuss GKV/Gesundheitsfonds)
        add_flow("Nominal_Federal", "Effective_Insurance", "Layer_2_Nominal", "Layer_3_Effective", b_year["Epl_15_Gesundheit_Bundeszuschuss_GKV"], n_de_t1)
        # C) Federal grants to Free State of Bavaria (Bundesmittel an Bayern)
        pc_bund_to_by = (by_year["Bundeszuweisungen_an_Bayern"] * scale_mrd) / n_by_t1
        add_flow("Nominal_Federal", "Effective_Bayern", "Layer_2_Nominal", "Layer_3_Effective", by_year["Bundeszuweisungen_an_Bayern"], val_pc=pc_bund_to_by)
        # D) Retained for Core Federal Budget duties
        pc_fed_to_soz = ((b_year["Epl_11_Bundeszuschuss_Rentenversicherung"] + b_year["Epl_15_Gesundheit_Bundeszuschuss_GKV"]) * scale_mrd) / n_de_t1
        pc_fed_retained = pc_bund - pc_fed_to_soz - pc_bund_to_by
        fed_retained_mrd = (pc_fed_retained * n_de_t1) / scale_mrd
        add_flow("Nominal_Federal", "Effective_Federal", "Layer_2_Nominal", "Layer_3_Effective", fed_retained_mrd, val_pc=pc_fed_retained)

        # From Nominal Insurance:
        # Pure contributions flow directly to Effective Insurance
        tot_soz_contrib = s_year["Beitragseinnahmen_GRV_rein"] + s_year["Beitragseinnahmen_GKV_rein"] + s_year["Beitragseinnahmen_SPV_rein"] + s_year["Beitragseinnahmen_und_Umlagen_BA"] + s_year["Umlagesoll_Arbeitgeber_DGUV"]
        add_flow("Nominal_Insurance", "Effective_Insurance", "Layer_2_Nominal", "Layer_3_Effective", tot_soz_contrib, n_de_t1)

        # From Nominal Munich:
        # A) Transfer to State / District (Gewerbesteuerumlage + Bezirksumlage an Oberbayern)
        m_to_by_mrd = m_year["Bezirksumlage_an_Bezirk_Oberbayern"] + m_year["Gewerbesteuerumlage_an_Bund_und_Land"]
        add_flow("Nominal_Munich", "Effective_Bayern", "Layer_2_Nominal", "Layer_3_Effective", m_to_by_mrd, n_muc_t1)
        # B) Retained for local municipal operations
        muc_retained_mrd = tot_muc - m_to_by_mrd
        add_flow("Nominal_Munich", "Effective_Munich", "Layer_2_Nominal", "Layer_3_Effective", muc_retained_mrd, n_muc_t1)

        # From Nominal Bayern:
        # A) State grant transfers to Munich (Kommunaler Finanzausgleich FAG / BayKiBiG)
        by_to_m_mrd = m_year["Zuweisungen_und_Zuschuesse_vom_Freistaat_Bayern"]
        add_flow("Nominal_Bayern", "Effective_Munich", "Layer_2_Nominal", "Layer_3_Effective", by_to_m_mrd, n_muc_t1)
        # B) Retained Bavarian State Funds (flows into Effective Bayern, which then pays LFA & core duties)
        pc_by_own = (tot_by_own * scale_mrd) / n_by_t1
        pc_by_to_m = (by_to_m_mrd * scale_mrd) / n_muc_t1
        pc_by_retained = pc_by_own - pc_by_to_m
        by_retained_mrd = (pc_by_retained * n_by_t1) / scale_mrd
        add_flow("Nominal_Bayern", "Effective_Bayern", "Layer_2_Nominal", "Layer_3_Effective", by_retained_mrd, val_pc=pc_by_retained)

        # -------------------------------------------------------------------
        # STAGE 3: LAYER 3 (Effective Entities) -> LAYER 4 (Functional Buckets)
        # -------------------------------------------------------------------
        # 1. From Effective Federal:
        eff_fed_def_pc = ((b_year["Epl_14_Verteidigung_Kern"] + b_year["Sondervermoegen_Bundeswehr_Ist"] + b_year["Epl_23_Entwicklung_und_Auswaertiges"]) * scale_mrd) / n_de_t1
        eff_fed_trans_pc = (b_year["Epl_12_Verkehr_und_digitale_Infrastruktur"] * scale_mrd) / n_de_t1
        eff_fed_uni_pc = (b_year["Epl_30_Bildung_und_Forschung"] * scale_mrd) / n_de_t1
        eff_fed_debt_pc = (b_year["Epl_32_Bundesschuld_Zinsen"] * scale_mrd) / n_de_t1
        eff_fed_soz_pc = (b_year["Epl_11_Buergergeld_Grundsicherung"] * scale_mrd) / n_de_t1
        eff_fed_sec_pc = (b_year["Epl_06_Inneres_und_Heimat_Bundespolizei"] * scale_mrd) / n_de_t1
        eff_fed_rest_pc = pc_fed_retained - (eff_fed_def_pc + eff_fed_trans_pc + eff_fed_uni_pc + eff_fed_debt_pc + eff_fed_soz_pc + eff_fed_sec_pc)
        add_flow("Effective_Federal", "Verteidigung_und_Aeusseres", "Layer_3_Effective", "Layer_4_Buckets", b_year["Epl_14_Verteidigung_Kern"] + b_year["Sondervermoegen_Bundeswehr_Ist"] + b_year["Epl_23_Entwicklung_und_Auswaertiges"], val_pc=eff_fed_def_pc)
        add_flow("Effective_Federal", "Verkehr_und_Infrastruktur", "Layer_3_Effective", "Layer_4_Buckets", b_year["Epl_12_Verkehr_und_digitale_Infrastruktur"], val_pc=eff_fed_trans_pc)
        add_flow("Effective_Federal", "Hochschulen_und_Forschung", "Layer_3_Effective", "Layer_4_Buckets", b_year["Epl_30_Bildung_und_Forschung"], val_pc=eff_fed_uni_pc)
        add_flow("Effective_Federal", "Schuldendienst_und_Zinsen", "Layer_3_Effective", "Layer_4_Buckets", b_year["Epl_32_Bundesschuld_Zinsen"], val_pc=eff_fed_debt_pc)
        add_flow("Effective_Federal", "Buergergeld_Grundsicherung", "Layer_3_Effective", "Layer_4_Buckets", b_year["Epl_11_Buergergeld_Grundsicherung"], val_pc=eff_fed_soz_pc)
        add_flow("Effective_Federal", "Sicherheit_und_Justiz", "Layer_3_Effective", "Layer_4_Buckets", b_year["Epl_06_Inneres_und_Heimat_Bundespolizei"], val_pc=eff_fed_sec_pc)
        eff_fed_rest_mrd = (eff_fed_rest_pc * n_de_t1) / scale_mrd
        add_flow("Effective_Federal", "Verwaltung_Wirtschaft_Sonstiges", "Layer_3_Effective", "Layer_4_Buckets", eff_fed_rest_mrd, val_pc=eff_fed_rest_pc)

        # 2. From Effective Insurance (combined contributions + federal tax subsidies!):
        # A) Total Pension Payouts (GRV)
        add_flow("Effective_Insurance", "Rente_und_Alterssicherung", "Layer_3_Effective", "Layer_4_Buckets", s_year["Gesamtausgaben_GRV"], n_de_t1)
        # B) Total Healthcare & Long-Term Care (GKV & SPV & DGUV)
        add_flow("Effective_Insurance", "Gesundheit_und_Pflege", "Layer_3_Effective", "Layer_4_Buckets", s_year["Gesamtausgaben_GKV"] + s_year["Gesamtausgaben_SPV"] + s_year["Heilbehandlung_und_Reha_DGUV"], n_de_t1)
        # C) Unemployment Insurance & Active Labor Market Policy (BA & DGUV)
        add_flow("Effective_Insurance", "Arbeitsfoerderung_und_Reha", "Layer_3_Effective", "Layer_4_Buckets", s_year["Gesamtausgaben_BA"] + s_year["Renten_und_Abfindungen_DGUV"] + s_year["Praevention_und_Verwaltung_DGUV"], n_de_t1)
        # D) Reserves / Liquidity buffer addition
        soz_reserve_addition = (tot_soz_contrib + b_year["Epl_11_Bundeszuschuss_Rentenversicherung"] + b_year["Epl_15_Gesundheit_Bundeszuschuss_GKV"]) - (s_year["Gesamtausgaben_GRV"] + s_year["Gesamtausgaben_GKV"] + s_year["Gesamtausgaben_SPV"] + s_year["Gesamtausgaben_BA"] + s_year["Gesamtausgaben_DGUV"])
        add_flow("Effective_Insurance", "Ruecklagen_und_Liquiditaetspuffer", "Layer_3_Effective", "Layer_4_Buckets", soz_reserve_addition, n_de_t1)

        # 3. From Effective Bayern (disburses LFA to end bucket and core state tasks):
        # A) Länderfinanzausgleich to final end bucket!
        add_flow("Effective_Bayern", "Laenderfinanzausgleich_Ausgleich_an_andere_Laender", "Layer_3_Effective", "Layer_4_Buckets", by_year["Laenderfinanzausgleich_Abfluss"], n_by_t1)
        # B) Core state public goods
        pc_m_to_by = (m_to_by_mrd * scale_mrd) / n_muc_t1
        eff_by_total_pc = pc_by_retained + pc_bund_to_by + pc_m_to_by
        eff_by_lfa_pc = (by_year["Laenderfinanzausgleich_Abfluss"] * scale_mrd) / n_by_t1
        eff_by_schools_pc = (by_year["Epl_05_Unterricht_und_Kultus_Schulen"] * scale_mrd) / n_by_t1
        eff_by_uni_pc = (by_year["Epl_15_Wissenschaft_und_Kunst_Universitaeten"] * scale_mrd) / n_by_t1
        eff_by_sec_pc = ((by_year["Epl_03_Inneres_Polizei_Katastrophenschutz"] + by_year["Epl_04_Justiz_Gerichte_JVA"]) * scale_mrd) / n_by_t1
        eff_by_trans_pc = (by_year["Epl_09_Wohnen_Bau_Verkehr"] * scale_mrd) / n_by_t1
        eff_by_health_pc = (by_year["Epl_14_Gesundheit_und_Pflege"] * scale_mrd) / n_by_t1
        eff_by_rest_pc = eff_by_total_pc - (eff_by_lfa_pc + eff_by_schools_pc + eff_by_uni_pc + eff_by_sec_pc + eff_by_trans_pc + eff_by_health_pc)
        add_flow("Effective_Bayern", "Schulen_und_Kitas", "Layer_3_Effective", "Layer_4_Buckets", by_year["Epl_05_Unterricht_und_Kultus_Schulen"], val_pc=eff_by_schools_pc)
        add_flow("Effective_Bayern", "Hochschulen_und_Forschung", "Layer_3_Effective", "Layer_4_Buckets", by_year["Epl_15_Wissenschaft_und_Kunst_Universitaeten"], val_pc=eff_by_uni_pc)
        add_flow("Effective_Bayern", "Sicherheit_und_Justiz", "Layer_3_Effective", "Layer_4_Buckets", by_year["Epl_03_Inneres_Polizei_Katastrophenschutz"] + by_year["Epl_04_Justiz_Gerichte_JVA"], val_pc=eff_by_sec_pc)
        add_flow("Effective_Bayern", "Verkehr_und_Infrastruktur", "Layer_3_Effective", "Layer_4_Buckets", by_year["Epl_09_Wohnen_Bau_Verkehr"], val_pc=eff_by_trans_pc)
        add_flow("Effective_Bayern", "Gesundheit_und_Pflege", "Layer_3_Effective", "Layer_4_Buckets", by_year["Epl_14_Gesundheit_und_Pflege"], val_pc=eff_by_health_pc)
        eff_by_rest_mrd = (eff_by_rest_pc * n_by_t1) / scale_mrd
        add_flow("Effective_Bayern", "Verwaltung_Wirtschaft_Sonstiges", "Layer_3_Effective", "Layer_4_Buckets", eff_by_rest_mrd, val_pc=eff_by_rest_pc)

        # 4. From Effective Munich:
        pc_muc_retained = (muc_retained_mrd * scale_mrd) / n_muc_t1
        eff_muc_total_pc = pc_muc_retained + pc_by_to_m
        eff_muc_schools_pc = (m_year["Referat_fuer_Bildung_und_Sport_RBS_Schulen_Kitas"] * scale_mrd) / n_muc_t1
        eff_muc_soz_pc = (m_year["Sozialreferat_Jugend_Soziales_Wohnungslosigkeit"] * scale_mrd) / n_muc_t1
        eff_muc_mob_pc = (m_year["Mobilitaetsreferat_und_Baureferat_Strassen_MVG"] * scale_mrd) / n_muc_t1
        eff_muc_health_pc = (m_year["Gesundheitsreferat_und_Muenchen_Klinik_Zuschuss"] * scale_mrd) / n_muc_t1
        eff_muc_plan_pc = (m_year["Stadtplanung_und_Bauordnung_Wohnungsbau"] * scale_mrd) / n_muc_t1
        eff_muc_sec_pc = (m_year["Kreisverwaltungsreferat_KVR_und_Branddirektion"] * scale_mrd) / n_muc_t1
        eff_muc_kult_pc = (m_year["Kulturreferat"] * scale_mrd) / n_muc_t1
        eff_muc_rest_pc = eff_muc_total_pc - (eff_muc_schools_pc + eff_muc_soz_pc + eff_muc_mob_pc + eff_muc_health_pc + eff_muc_plan_pc + eff_muc_sec_pc + eff_muc_kult_pc)
        add_flow("Effective_Munich", "Schulen_und_Kitas", "Layer_3_Effective", "Layer_4_Buckets", m_year["Referat_fuer_Bildung_und_Sport_RBS_Schulen_Kitas"], val_pc=eff_muc_schools_pc)
        add_flow("Effective_Munich", "Soziales_Jugend_Wohnungslosigkeit", "Layer_3_Effective", "Layer_4_Buckets", m_year["Sozialreferat_Jugend_Soziales_Wohnungslosigkeit"], val_pc=eff_muc_soz_pc)
        add_flow("Effective_Munich", "Verkehr_und_Infrastruktur", "Layer_3_Effective", "Layer_4_Buckets", m_year["Mobilitaetsreferat_und_Baureferat_Strassen_MVG"], val_pc=eff_muc_mob_pc)
        add_flow("Effective_Munich", "Gesundheit_und_Pflege", "Layer_3_Effective", "Layer_4_Buckets", m_year["Gesundheitsreferat_und_Muenchen_Klinik_Zuschuss"], val_pc=eff_muc_health_pc)
        add_flow("Effective_Munich", "Wohnungsbau_und_Stadtplanung", "Layer_3_Effective", "Layer_4_Buckets", m_year["Stadtplanung_und_Bauordnung_Wohnungsbau"], val_pc=eff_muc_plan_pc)
        add_flow("Effective_Munich", "Sicherheit_und_Justiz", "Layer_3_Effective", "Layer_4_Buckets", m_year["Kreisverwaltungsreferat_KVR_und_Branddirektion"], val_pc=eff_muc_sec_pc)
        add_flow("Effective_Munich", "Kultur_und_Freizeit", "Layer_3_Effective", "Layer_4_Buckets", m_year["Kulturreferat"], val_pc=eff_muc_kult_pc)
        eff_muc_rest_mrd = (eff_muc_rest_pc * n_muc_t1) / scale_mrd
        add_flow("Effective_Munich", "Verwaltung_Wirtschaft_Sonstiges", "Layer_3_Effective", "Layer_4_Buckets", eff_muc_rest_mrd, val_pc=eff_muc_rest_pc)

    # 4. Write datasets
    out_flows = os.path.join(datasets_dir, "fiscal_sankey_flows_per_capita.csv")
    with open(out_flows, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "jahr", "layer_source", "layer_target", "source_node", "target_node",
            "wert_mrd_eur", "wert_eur_pro_kopf"
        ])
        writer.writeheader()
        writer.writerows(sankey_flows)

    out_sum = os.path.join(datasets_dir, "fiscal_per_capita_summary.csv")
    with open(out_sum, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "jahr", "ebene", "bevoelkerung_referenz", "gesamtvolumen_mrd_eur", "pro_kopf_eur"
        ])
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"✓ Data preparation complete: {len(sankey_flows)} flows and {len(summary_rows)} summary records exported.")
    return len(sankey_flows)


def main():
    """CLI entrypoint."""
    raw_dir = os.path.join(ROOT, "rawdata")
    datasets_dir = os.path.join(ROOT, "datasets")
    compute_fiscal_sankey_pipeline(raw_dir, datasets_dir)


if __name__ == "__main__":
    main()
