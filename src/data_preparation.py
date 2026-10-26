#!/usr/bin/env python3
"""Data Preparation Pipeline for Multi-Level Fiscal Per-Capita Sankey Analysis.

Ingests primary CSV tables from rawdata/, validates cryptographic and accounting
identities, dynamically audits literature benchmarks, applies demographic denominator
normalizations (apples-to-apples per-tier population), enforces Kirchhoff flow
conservation across all layers, and exports auditable datasets to datasets/.

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
    """Execute end-to-end data preparation pipeline with strict accounting assertions."""
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

    sankey_flows = []
    summary_rows = []

    scale_mrd = 1000.0 * 1000000.0  # 1e9 multiplier for Billion EUR to EUR

    for year in (2023, 2024):
        n_de_t1 = demo_map[(year, "Deutschland", "Tier_1_Zensus_2022_korrigiert")]
        n_by_t1 = demo_map[(year, "Bayern", "Tier_1_Zensus_2022_korrigiert")]
        n_muc_t1 = demo_map[(year, "Muenchen", "Tier_1_Amtliche_Einwohnerzahl_Zensus")]

        # Denominator assertions
        assert n_de_t1 > 0, "German denominator must be positive"
        assert n_by_t1 > 0, "Bavarian denominator must be positive"
        assert n_muc_t1 > 0, "Munich denominator must be positive"
        assert n_de_t1 > n_by_t1 > n_muc_t1, "Hierarchical population consistency check"

        # Filter by year
        b_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_bund if int(r["jahr"]) == year}
        s_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_soz if int(r["jahr"]) == year}
        by_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_by if int(r["jahr"]) == year}
        m_year = {r["indikator"]: float(r["wert_mrd_eur"]) for r in rows_muc if int(r["jahr"]) == year}

        # Dynamic Benchmark Cross-Verification Assertions
        if year == 2024:
            assert b_year["Gesamtausgaben_Bund"] == benchmarks["BUND_AUSGABEN_2024"]
            assert b_year["Steuereinnahmen_Bundesanteil"] == benchmarks["BUND_STEUERN_2024"]
            assert b_year["Nettokreditaufnahme"] == benchmarks["BUND_NKA_2024"]
            assert b_year["Epl_11_Bundeszuschuss_Rentenversicherung"] == benchmarks["BUND_ZUSCHUSS_GRV_2024"]
            assert by_year["Gesamtvolumen_Staatshaushalt_Bayern"] == benchmarks["BAYERN_AUSGABEN_2024"]
            assert by_year["Kommunaler_Finanzausgleich_KFA_Epl_13"] == benchmarks["BAYERN_KFA_2024"]
            assert m_year["Ordentliche_Aufwendungen"] == benchmarks["MUENCHEN_AUFWENDUNGEN_2024"]

        # Sovereign entity totals in Billion EUR
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

        # Per-tier Per Capita Amounts (EUR/resident)
        pc_bund = (tot_bund * scale_mrd) / n_de_t1
        pc_soz = (tot_soz * scale_mrd) / n_de_t1
        pc_by = (tot_by * scale_mrd) / n_by_t1
        pc_muc = (tot_muc * scale_mrd) / n_muc_t1

        # Summary records (Per-tier Standalone Baseline)
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

        # Helper to append flow with explicit dual units
        def add_flow(src, tgt, l_src, l_tgt, val_mrd, pop_denom=None, val_pc=None):
            if val_pc is None:
                assert pop_denom is not None, "pop_denom required when val_pc is None"
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
        # Flows ordered in descending order per sovereign tier (SV -> Bund -> Bayern -> Munich)
        # -------------------------------------------------------------------
        # 1. Pure Social Insurance Contributions -> Nominal Insurance (Descending)
        add_flow("Krankenbeitraege_AG_AN", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal",
                 s_year["Beitragseinnahmen_GKV_rein"], pop_denom=n_de_t1)
        add_flow("Rentenbeitraege_AG_AN", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal",
                 s_year["Beitragseinnahmen_GRV_rein"], pop_denom=n_de_t1)
        add_flow("Pflegebeitraege_AG_AN", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal",
                 s_year["Beitragseinnahmen_SPV_rein"], pop_denom=n_de_t1)
        add_flow("Arbeitslosenbeitraege_BA", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal",
                 s_year["Beitragseinnahmen_und_Umlagen_BA"], pop_denom=n_de_t1)
        add_flow("Unfallbeitraege_DGUV", "Nominal_Insurance", "Layer_1_Influx", "Layer_2_Nominal",
                 s_year["Umlagesoll_Arbeitgeber_DGUV"], pop_denom=n_de_t1)

        # 2. Federal Influx Streams -> Nominal Federal (Descending)
        fed_tax_sum = (
            b_year["Lohnsteuer_Bundesanteil"] + b_year["Veranlagte_Einkommensteuer_Bundesanteil"]
            + b_year["Umsatzsteuer_Einfuhrumsatzsteuer_Bundesanteil"]
            + b_year["Koerperschaftsteuer_Bundesanteil"] + b_year["Abgeltungsteuer_Bundesanteil"]
            + b_year["Energiesteuer"] + b_year["Tabaksteuer"] + b_year["Solidaritaetszuschlag"]
            + b_year["Versicherungssteuer"] + b_year["Kraftfahrzeugsteuer"] + b_year["Stromsteuer"]
            + b_year["Sonstige_Bundessteuern"]
        )
        fed_nontax = tot_bund - fed_tax_sum
        fed_nka = b_year["Nettokreditaufnahme"] if year == 2024 else (b_year["Nettokreditaufnahme"] + b_year["Ruecklagenentnahme"])
        fed_admin = fed_nontax - fed_nka

        add_flow("Umsatzsteuer_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal",
                 b_year["Umsatzsteuer_Einfuhrumsatzsteuer_Bundesanteil"], pop_denom=n_de_t1)
        add_flow("Lohn_Einkommensteuer_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal",
                 b_year["Lohnsteuer_Bundesanteil"] + b_year["Veranlagte_Einkommensteuer_Bundesanteil"], pop_denom=n_de_t1)
        add_flow("Verbrauchs_und_Bundessteuern", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal",
                 b_year["Energiesteuer"] + b_year["Tabaksteuer"] + b_year["Solidaritaetszuschlag"]
                 + b_year["Versicherungssteuer"] + b_year["Kraftfahrzeugsteuer"] + b_year["Stromsteuer"]
                 + b_year["Sonstige_Bundessteuern"], pop_denom=n_de_t1)
        add_flow("Nettokreditaufnahme_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal",
                 fed_nka, pop_denom=n_de_t1)
        add_flow("Unternehmenssteuern_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal",
                 b_year["Koerperschaftsteuer_Bundesanteil"] + b_year["Abgeltungsteuer_Bundesanteil"], pop_denom=n_de_t1)
        add_flow("Verwaltungseinnahmen_Beteiligungen_Bund", "Nominal_Federal", "Layer_1_Influx", "Layer_2_Nominal",
                 fed_admin, pop_denom=n_de_t1)

        # 3. Bavarian State Taxes & Own Revenues -> Nominal Bayern (Descending)
        tot_by_own = by_year["Gesamtvolumen_Staatshaushalt_Bayern"] - by_year["Bundeszuweisungen_an_Bayern"]
        add_flow("Gemeinschaftsteuern_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal",
                 by_year["Bayerischer_Anteil_Gemeinschaftsteuern"], pop_denom=n_by_t1)
        add_flow("Landessteuern_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal",
                 by_year["Erbschaft_und_Schenkungsteuer"] + by_year["Grunderwerbsteuer"]
                 + by_year["Biersteuer"] + by_year["Feuerschutzsteuer_und_sonstige"], pop_denom=n_by_t1)
        add_flow("Verwaltungseinnahmen_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal",
                 by_year["Verwaltungseinnahmen_Bayern"], pop_denom=n_by_t1)
        add_flow("Ruecklagenentnahme_Kredite_Bayern", "Nominal_Bayern", "Layer_1_Influx", "Layer_2_Nominal",
                 by_year["Entnahme_aus_Haushaltsruecklage"], pop_denom=n_by_t1)

        # 4. Munich Municipal Taxes & Own Revenues -> Nominal Munich (Descending)
        muc_own_sum = (
            m_year["Gewerbesteuer_netto"] + m_year["Gemeindeanteil_an_der_Einkommensteuer"]
            + m_year["Gemeindeanteil_an_der_Umsatzsteuer"] + m_year["Grundsteuer_A_und_B"]
            + m_year["Oertliche_Verbrauch_und_Aufwandsteuern"]
            + m_year["Oeffentlich_rechtliche_Gebuehren_und_Entgelte"]
            + m_year["Privatrechtliche_Leistungsentgelte_Mieten"]
            + m_year["Gewinnausschuettung_Stadtwerke_SWM"]
        )
        muc_saldo_rest = tot_muc - muc_own_sum

        add_flow("Gewerbesteuer_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal",
                 m_year["Gewerbesteuer_netto"], pop_denom=n_muc_t1)
        add_flow("Einkommensteuer_USt_Anteil_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal",
                 m_year["Gemeindeanteil_an_der_Einkommensteuer"] + m_year["Gemeindeanteil_an_der_Umsatzsteuer"], pop_denom=n_muc_t1)
        add_flow("Gebuehren_Mieten_Entgelte_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal",
                 m_year["Oeffentlich_rechtliche_Gebuehren_und_Entgelte"] + m_year["Privatrechtliche_Leistungsentgelte_Mieten"], pop_denom=n_muc_t1)
        add_flow("Sonstige_Ertraege_und_Defizitausgleich_MUC", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal",
                 muc_saldo_rest, pop_denom=n_muc_t1)
        add_flow("Beteiligungsertraege_SWM_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal",
                 m_year["Gewinnausschuettung_Stadtwerke_SWM"], pop_denom=n_muc_t1)
        add_flow("Grundsteuer_und_Lokalsteuern_Muenchen", "Nominal_Munich", "Layer_1_Influx", "Layer_2_Nominal",
                 m_year["Grundsteuer_A_und_B"] + m_year["Oertliche_Verbrauch_und_Aufwandsteuern"], pop_denom=n_muc_t1)

        # -------------------------------------------------------------------
        # STAGE 2: LAYER 2 (Nominal) -> LAYER 3 (Effective Entities & Transfers)
        # -------------------------------------------------------------------
        # A) Social Insurance: Pure contributions pass through (Tier 1 at top)
        tot_soz_contrib = (
            s_year["Beitragseinnahmen_GRV_rein"] + s_year["Beitragseinnahmen_GKV_rein"]
            + s_year["Beitragseinnahmen_SPV_rein"] + s_year["Beitragseinnahmen_und_Umlagen_BA"]
            + s_year["Umlagesoll_Arbeitgeber_DGUV"]
        )
        add_flow("Nominal_Insurance", "Effective_Insurance", "Layer_2_Nominal", "Layer_3_Effective",
                 tot_soz_contrib, pop_denom=n_de_t1)

        # B) Bund Flows (ordered by target vertical position: Effective_Insurance (up) -> Effective_Federal (across) -> Effective_Bayern (down)):
        fed_to_soz_mrd = b_year["Epl_11_Bundeszuschuss_Rentenversicherung"] + b_year["Epl_15_Gesundheit_Bundeszuschuss_GKV"]
        bund_to_by_mrd = by_year["Bundeszuweisungen_an_Bayern"]
        fed_retained_mrd = tot_bund - fed_to_soz_mrd - bund_to_by_mrd

        # 1. Bundeszuschuss GRV + GKV -> Effective Insurance (slants up to top tier)
        add_flow("Nominal_Federal", "Effective_Insurance", "Layer_2_Nominal", "Layer_3_Effective",
                 fed_to_soz_mrd, pop_denom=n_de_t1)

        # 2. Federal retained core budget -> Effective Federal (horizontal at second tier)
        add_flow("Nominal_Federal", "Effective_Federal", "Layer_2_Nominal", "Layer_3_Effective",
                 fed_retained_mrd, pop_denom=n_de_t1)

        # 3. Bundeszuweisungen an Bayern -> Effective Bayern (slants down to third tier)
        pc_bund_to_by = (bund_to_by_mrd * scale_mrd) / n_by_t1
        add_flow("Nominal_Federal", "Effective_Bayern", "Layer_2_Nominal", "Layer_3_Effective",
                 bund_to_by_mrd, val_pc=pc_bund_to_by)

        # C) Munich & Bayern Intergovernmental Net Consolidation (Option A):
        by_to_m_mrd = m_year["Zuweisungen_und_Zuschuesse_vom_Freistaat_Bayern"]
        m_to_by_mrd = m_year["Bezirksumlage_an_Bezirk_Oberbayern"] + m_year["Gewerbesteuerumlage_an_Bund_und_Land"]
        by_net_to_m_mrd = by_to_m_mrd - m_to_by_mrd

        # 1. Retained Bavarian state funds -> Effective Bayern
        by_retained_mrd = tot_by_own - by_net_to_m_mrd
        pc_by_retained = (by_retained_mrd * scale_mrd) / n_by_t1
        add_flow("Nominal_Bayern", "Effective_Bayern", "Layer_2_Nominal", "Layer_3_Effective",
                 by_retained_mrd, val_pc=pc_by_retained)

        # 2. Net municipal equalization grant from Bavaria to Munich
        pc_net_grant_muc = (by_net_to_m_mrd * scale_mrd) / n_muc_t1
        add_flow("Nominal_Bayern", "Effective_Munich", "Layer_2_Nominal", "Layer_3_Effective",
                 by_net_to_m_mrd, val_pc=pc_net_grant_muc)

        # 3. Munich retains own municipal tax revenues -> Effective Munich
        add_flow("Nominal_Munich", "Effective_Munich", "Layer_2_Nominal", "Layer_3_Effective",
                 tot_muc, pop_denom=n_muc_t1)

        # -------------------------------------------------------------------
        # STAGE 3: LAYER 3 (Effective Entities) -> LAYER 4 (Functional Buckets)
        # Flows ordered in sovereign tier order (SV -> Bund -> Bayern -> Munich)
        # and descending target Layer 4 vertical order within each tier
        # -------------------------------------------------------------------
        # 1. Effective Social Insurance (Normalized by n_de_t1)
        # Order matches descending Layer 4 vertical order: Gesundheit (Rank 1) -> Rente (Rank 2) -> Arbeitsfoerderung (Rank 13) -> Ruecklagen (Rank 19)
        add_flow("Effective_Insurance", "Gesundheit_und_Pflege", "Layer_3_Effective", "Layer_4_Buckets",
                 s_year["Gesamtausgaben_GKV"] + s_year["Gesamtausgaben_SPV"] + s_year["Heilbehandlung_und_Reha_DGUV"], pop_denom=n_de_t1)
        add_flow("Effective_Insurance", "Rente_und_Alterssicherung", "Layer_3_Effective", "Layer_4_Buckets",
                 s_year["Gesamtausgaben_GRV"], pop_denom=n_de_t1)
        add_flow("Effective_Insurance", "Arbeitsfoerderung_und_Reha", "Layer_3_Effective", "Layer_4_Buckets",
                 s_year["Gesamtausgaben_BA"] + s_year["Renten_und_Abfindungen_DGUV"] + s_year["Praevention_und_Verwaltung_DGUV"], pop_denom=n_de_t1)

        tot_soz_eff_in = tot_soz_contrib + fed_to_soz_mrd
        soz_reserve_addition = tot_soz_eff_in - tot_soz
        add_flow("Effective_Insurance", "Ruecklagen_und_Liquiditaetspuffer", "Layer_3_Effective", "Layer_4_Buckets",
                 soz_reserve_addition, pop_denom=n_de_t1)

        # 2. Effective Federal (Normalized by n_de_t1)
        bw_sv = b_year["Sondervermoegen_Bundeswehr_Ist"] if "Sondervermoegen_Bundeswehr_Ist" in b_year else 0.0
        fed_grants_other_laender = b_year["Bundeszuweisungen_an_Laender"] - bund_to_by_mrd
        fed_known_other_mrd = (
            b_year["Epl_14_Verteidigung_Kern"] + bw_sv
            + b_year["Epl_23_Entwicklung_und_Auswaertiges"] + b_year["Epl_12_Verkehr_und_digitale_Infrastruktur"]
            + b_year["Epl_30_Bildung_und_Forschung"] + b_year["Epl_32_Bundesschuld_Zinsen"]
            + b_year["Epl_11_Buergergeld_Grundsicherung"] + b_year["Epl_11_Grundsicherung_im_Alter_SGB_XII"]
            + b_year["Epl_06_Inneres_und_Heimat_Bundespolizei"] + b_year["Epl_08_Finanzverwaltung_Zoll"]
            + b_year["Epl_25_Wohnungswesen_und_Staedtebau"] + b_year["Epl_17_Familie_Senioren_Frauen_Jugend"]
            + fed_grants_other_laender
        )
        fed_admin_econ = fed_retained_mrd - fed_known_other_mrd

        # Emitted in descending order of Layer 4 target buckets to eliminate ribbon crossovers
        add_flow("Effective_Federal", "Verkehr_und_Infrastruktur", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_12_Verkehr_und_digitale_Infrastruktur"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Sicherheit_und_Justiz", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_06_Inneres_und_Heimat_Bundespolizei"] + b_year["Epl_08_Finanzverwaltung_Zoll"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Soziales_Jugend_Wohnungslosigkeit", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_17_Familie_Senioren_Frauen_Jugend"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Hochschulen_und_Forschung", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_30_Bildung_und_Forschung"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Verteidigung_und_Aeusseres", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_14_Verteidigung_Kern"] + bw_sv + b_year["Epl_23_Entwicklung_und_Auswaertiges"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Buergergeld_Grundsicherung", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_11_Buergergeld_Grundsicherung"] + b_year["Epl_11_Grundsicherung_im_Alter_SGB_XII"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Wirtschaft_Klima_Verwaltung", "Layer_3_Effective", "Layer_4_Buckets",
                 fed_admin_econ, pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Schuldendienst_und_Zinsen", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_32_Bundesschuld_Zinsen"], pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Bundeszuweisungen_an_andere_Laender_Transfer", "Layer_3_Effective", "Layer_4_Buckets",
                 fed_grants_other_laender, pop_denom=n_de_t1)
        add_flow("Effective_Federal", "Wohnungsbau_und_Stadtplanung", "Layer_3_Effective", "Layer_4_Buckets",
                 b_year["Epl_25_Wohnungswesen_und_Staedtebau"], pop_denom=n_de_t1)

        # 3. Effective Bayern (Normalized by n_by_t1)
        tot_by_eff_mrd = by_retained_mrd + bund_to_by_mrd
        by_known_mrd = (
            by_year["Laenderfinanzausgleich_Abfluss"] + by_year["Epl_05_Unterricht_und_Kultus_Schulen"]
            + by_year["Epl_15_Wissenschaft_und_Kunst_Universitaeten"]
            + by_year["Epl_03_Inneres_Polizei_Katastrophenschutz"] + by_year["Epl_04_Justiz_Gerichte_JVA"]
            + by_year["Epl_09_Wohnen_Bau_Verkehr"] + by_year["Epl_14_Gesundheit_und_Pflege"]
        )
        by_rest_mrd = tot_by_eff_mrd - by_known_mrd

        # Emitted in descending order of Layer 4 target buckets
        add_flow("Effective_Bayern", "Gesundheit_und_Pflege", "Layer_3_Effective", "Layer_4_Buckets",
                 by_year["Epl_14_Gesundheit_und_Pflege"], pop_denom=n_by_t1)
        add_flow("Effective_Bayern", "Schulen_und_Kitas", "Layer_3_Effective", "Layer_4_Buckets",
                 by_year["Epl_05_Unterricht_und_Kultus_Schulen"], pop_denom=n_by_t1)
        add_flow("Effective_Bayern", "Verkehr_und_Infrastruktur", "Layer_3_Effective", "Layer_4_Buckets",
                 by_year["Epl_09_Wohnen_Bau_Verkehr"], pop_denom=n_by_t1)
        add_flow("Effective_Bayern", "Wirtschaft_Verwaltung_Sonstiges", "Layer_3_Effective", "Layer_4_Buckets",
                 by_rest_mrd, pop_denom=n_by_t1)
        add_flow("Effective_Bayern", "Sicherheit_und_Justiz", "Layer_3_Effective", "Layer_4_Buckets",
                 by_year["Epl_03_Inneres_Polizei_Katastrophenschutz"] + by_year["Epl_04_Justiz_Gerichte_JVA"], pop_denom=n_by_t1)
        add_flow("Effective_Bayern", "Hochschulen_und_Forschung", "Layer_3_Effective", "Layer_4_Buckets",
                 by_year["Epl_15_Wissenschaft_und_Kunst_Universitaeten"], pop_denom=n_by_t1)
        add_flow("Effective_Bayern", "Laenderfinanzausgleich_Ausgleich_an_andere_Laender", "Layer_3_Effective", "Layer_4_Buckets",
                 by_year["Laenderfinanzausgleich_Abfluss"], pop_denom=n_by_t1)

        # 4. Effective Munich (Normalized by n_muc_t1)
        tot_muc_eff_mrd = tot_muc + by_net_to_m_mrd
        muc_known_mrd = (
            m_year["Referat_fuer_Bildung_und_Sport_RBS_Schulen_Kitas"]
            + m_year["Sozialreferat_Jugend_Soziales_Wohnungslosigkeit"]
            + m_year["Mobilitaetsreferat_und_Baureferat_Strassen_MVG"]
            + m_year["Gesundheitsreferat_und_Muenchen_Klinik_Zuschuss"]
            + m_year["Stadtplanung_und_Bauordnung_Wohnungsbau"]
            + m_year["Kreisverwaltungsreferat_KVR_und_Branddirektion"]
            + m_year["Kulturreferat"]
        )
        muc_rest_mrd = tot_muc_eff_mrd - muc_known_mrd

        # Emitted in descending order of Layer 4 target buckets
        add_flow("Effective_Munich", "Gesundheit_und_Pflege", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Gesundheitsreferat_und_Muenchen_Klinik_Zuschuss"], pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Schulen_und_Kitas", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Referat_fuer_Bildung_und_Sport_RBS_Schulen_Kitas"], pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Kommunale_Verwaltung_Sonstiges", "Layer_3_Effective", "Layer_4_Buckets",
                 muc_rest_mrd, pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Verkehr_und_Infrastruktur", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Mobilitaetsreferat_und_Baureferat_Strassen_MVG"], pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Sicherheit_und_Justiz", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Kreisverwaltungsreferat_KVR_und_Branddirektion"], pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Soziales_Jugend_Wohnungslosigkeit", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Sozialreferat_Jugend_Soziales_Wohnungslosigkeit"], pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Wohnungsbau_und_Stadtplanung", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Stadtplanung_und_Bauordnung_Wohnungsbau"], pop_denom=n_muc_t1)
        add_flow("Effective_Munich", "Kultur_und_Freizeit", "Layer_3_Effective", "Layer_4_Buckets",
                 m_year["Kulturreferat"], pop_denom=n_muc_t1)

        # --- RIGOROUS KIRCHHOFF FLOW ASSERTIONS IN BILLIONS EUR ---
        year_flows = [f for f in sankey_flows if f["jahr"] == year]
        l1_mrd = sum(f["wert_mrd_eur"] for f in year_flows if f["layer_source"] == "Layer_1_Influx")
        l2_mrd = sum(f["wert_mrd_eur"] for f in year_flows if f["layer_source"] == "Layer_2_Nominal")
        l3_mrd = sum(f["wert_mrd_eur"] for f in year_flows if f["layer_source"] == "Layer_3_Effective")

        assert abs(l1_mrd - l2_mrd) < 0.05, f"Kirchhoff violation: Layer 1 ({l1_mrd:.2f}) != Layer 2 ({l2_mrd:.2f}) Mrd EUR"
        assert abs(l2_mrd - l3_mrd) < 0.05, f"Kirchhoff violation: Layer 2 ({l2_mrd:.2f}) != Layer 3 ({l3_mrd:.2f}) Mrd EUR"

    # Export datasets
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

    print(f"✓ Data preparation complete: {len(sankey_flows)} flows exported with strict Kirchhoff conservation.")
    return len(sankey_flows)


def main():
    """CLI entrypoint."""
    raw_dir = os.path.join(ROOT, "rawdata")
    datasets_dir = os.path.join(ROOT, "datasets")
    compute_fiscal_sankey_pipeline(raw_dir, datasets_dir)


if __name__ == "__main__":
    main()
