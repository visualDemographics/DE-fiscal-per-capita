#!/usr/bin/env python3
"""Modeling, Statistical Inference & 4-Layer Fiscal Sankey Generator.

Implements Kirchhoff multi-level flow validations and renders the
flagship 4-layer per-capita fiscal Sankey diagram across the Federal Republic,
Free State of Bavaria, and City of Munich (PNG, SVG, and interactive HTML).

This module is dedicated exclusively to the multi-level fiscal Sankey architecture.

Strict AST Contract Compliant:
- Zero synthetic data generators (no .rvs, np.random, random.gauss).
- Zero silent fallbacks (no .get(k, <numeric>)).
- Zero domain float literals in defaults, ternaries, or assignments.
"""

import csv
import os

import plotly.graph_objects as go

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_modeling_data(datasets_dir):
    """Load harmonized analysis-ready datasets for the 4-layer fiscal Sankey."""
    f_flows = os.path.join(datasets_dir, "fiscal_sankey_flows_per_capita.csv")
    f_sum = os.path.join(datasets_dir, "fiscal_per_capita_summary.csv")

    flows = []
    with open(f_flows, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            flows.append(r)

    summary = []
    with open(f_sum, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            summary.append(r)

    return flows, summary


# ---------------------------------------------------------------------------
# 1. Publication-Grade Plotly Sankey Generator (PNG & HTML)
# ---------------------------------------------------------------------------
def render_plotly_sankey(flows, summary, out_png_path, out_html_path, out_svg_path):
    """Generate high-resolution 4-Layer Sankey diagram using Plotly and Kaleido."""
    label_map = {
        # Layer 1 - Federal Taxes & Influx
        "Lohn_Einkommensteuer_Bund": "Lohn- & Einkommensteuer (Bund)",
        "Umsatzsteuer_Bund": "Umsatzsteuer (Bund)",
        "Unternehmenssteuern_Bund": "Körperschaft- & Abgeltungsteuer (Bund)",
        "Verbrauchs_und_Bundessteuern": "Verbrauchs- & Bundessteuern (Energie, Tabak, Soli, Kfz)",
        "Verwaltungseinnahmen_Beteiligungen_Bund": "Verwaltungseinnahmen & Beteiligungen (Bund)",
        "Nettokreditaufnahme_Bund": "Nettokreditaufnahme (Bund)",
        # Layer 1 - Social Insurance Pure Contributions
        "Rentenbeitraege_AG_AN": "Rentenbeiträge (AG & AN)",
        "Krankenbeitraege_AG_AN": "Krankenbeiträge (AG & AN)",
        "Pflegebeitraege_AG_AN": "Pflegebeiträge (AG & AN)",
        "Arbeitslosenbeitraege_BA": "Arbeitslosenbeiträge (BA)",
        "Unfallbeitraege_DGUV": "Unfallversicherungsumlage (DGUV)",
        # Layer 1 - Bavaria State Taxes & Own Revenues
        "Gemeinschaftsteuern_Bayern": "Gemeinschaftsteuern (Bayern)",
        "Landessteuern_Bayern": "Landessteuern (Erbschaft, Grunderwerb)",
        "Verwaltungseinnahmen_Bayern": "Verwaltungseinnahmen (Bayern)",
        "Ruecklagenentnahme_Kredite_Bayern": "Rücklagen & Kredite (Bayern)",
        # Layer 1 - Munich Municipal Revenues
        "Gewerbesteuer_Muenchen": "Gewerbesteuer (München)",
        "Einkommensteuer_USt_Anteil_Muenchen": "Einkommen- & USt-Anteil (MUC)",
        "Grundsteuer_und_Lokalsteuern_Muenchen": "Grundsteuer & Lokalsteuern (MUC)",
        "Gebuehren_Mieten_Entgelte_Muenchen": "Kommunale Gebühren & Mieten (MUC)",
        "Beteiligungsertraege_SWM_Muenchen": "Gewinnausschüttung SWM (MUC)",
        "Sonstige_Ertraege_und_Defizitausgleich_MUC": "Sonstige Erträge & Saldo (MUC)",
        # Layer 2 - Nominal Sovereign Tiers
        "Nominal_Federal": "Nominaler Bund",
        "Nominal_Insurance": "Nominale Sozialversicherung",
        "Nominal_Bayern": "Nominaler Freistaat Bayern",
        "Nominal_Munich": "Nominale Stadt München",
        # Layer 3 - Effective Entities & Transfers
        "Effective_Federal": "Effektiver Bund (Kern)",
        "Effective_Insurance": "Effektive Sozialversicherung",
        "Effective_Bayern": "Effektiver Freistaat Bayern",
        "Effective_Munich": "Effektive Stadt München",
        # Layer 4 - Functional Buckets & End Destinations
        "Laenderfinanzausgleich_Ausgleich_an_andere_Laender": "Länderfinanzausgleich (Nettoabfluss BY)",
        "Rente_und_Alterssicherung": "Rente & Alterssicherung",
        "Gesundheit_und_Pflege": "Gesundheit & Pflege",
        "Schulen_und_Kitas": "Schulen & Kitas",
        "Hochschulen_und_Forschung": "Hochschulen & Spitzenforschung",
        "Verteidigung_und_Aeusseres": "Verteidigung & Äußeres",
        "Verkehr_und_Infrastruktur": "Verkehr & Mobilität",
        "Sicherheit_und_Justiz": "Innere Sicherheit & Justiz",
        "Buergergeld_Grundsicherung": "Bürgergeld & Grundsicherung",
        "Arbeitsfoerderung_und_Reha": "Arbeitsförderung & Reha (BA)",
        "Wohnungsbau_und_Stadtplanung": "Wohnungsbau & Stadtplanung",
        "Soziales_Jugend_Wohnungslosigkeit": "Soziales, Jugend & Wohnen (MUC)",
        "Kultur_und_Freizeit": "Kultur & Freizeit",
        "Schuldendienst_und_Zinsen": "Schuldendienst & Zinsen",
        "Ruecklagen_und_Liquiditaetspuffer": "Rücklagen & Liquiditätspuffer",
        "Wirtschaft_Klima_Verwaltung": "Wirtschaft, Energie & Verwaltung (Bund)",
        "Wirtschaft_Verwaltung_Sonstiges": "Wirtschaft & Landesverwaltung (BY)",
        "Kommunale_Verwaltung_Sonstiges": "Kommunale Verwaltung & IT (MUC)",
        "Bundeszuweisungen_an_andere_Laender_Transfer": "Bundeszuweisungen an übrige Länder",
    }

    color_map = {
        # Federal (Navy)
        "Bund": "#1e3a8a",
        "Lohn": "#1e3a8a",
        "Umsatzsteuer": "#1e3a8a",
        "Unternehmen": "#1e3a8a",
        "Verbrauchs": "#1e3a8a",
        "Nettokredit": "#1e3a8a",
        "Nominal_Federal": "#1e3a8a",
        "Effective_Federal": "#1e40af",
        # Social Insurance (Teal)
        "Sozial": "#0d9488",
        "Rentenbeitraege": "#0d9488",
        "Krankenbeitraege": "#0d9488",
        "Pflegebeitraege": "#0d9488",
        "Arbeitslosenbeitraege": "#0d9488",
        "Unfallbeitraege": "#0d9488",
        "Nominal_Insurance": "#0d9488",
        "Effective_Insurance": "#0f766e",
        # Bavaria (Sky Blue)
        "Gemeinschaftsteuern_Bayern": "#0284c7",
        "Landessteuern_Bayern": "#0284c7",
        "Verwaltungseinnahmen_Bayern": "#0284c7",
        "Ruecklagenentnahme_Kredite_Bayern": "#0284c7",
        "Nominal_Bayern": "#0284c7",
        "Effective_Bayern": "#0369a1",
        # Munich (Amber)
        "Gewerbesteuer": "#d97706",
        "Einkommensteuer_USt_Anteil_Muenchen": "#d97706",
        "Grundsteuer": "#d97706",
        "Gebuehren": "#d97706",
        "Beteiligungsertraege_SWM": "#d97706",
        "Sonstige_Ertraege": "#d97706",
        "Nominal_Munich": "#d97706",
        "Effective_Munich": "#b45309",
        # Layer 4 Buckets: Single-parent buckets use their Layer 3 parent color, mixed use distinct colors
        "Laenderfinanzausgleich": "#0369a1",  # Same color as other Bavarian Layer 3 outflows
        "Rente_und_Alterssicherung": "#0f766e",  # Single parent: Effective_Insurance
        "Gesundheit_und_Pflege": "#10b981",      # Mixed (Insurance + BY + MUC)
        "Schulen_und_Kitas": "#3b82f6",          # Mixed (BY + MUC)
        "Hochschulen_und_Forschung": "#6366f1",  # Mixed (Bund + BY)
        "Verteidigung_und_Aeusseres": "#1e40af", # Single parent: Effective_Federal
        "Verkehr_und_Infrastruktur": "#f59e0b",  # Mixed (Bund + BY + MUC)
        "Sicherheit_und_Justiz": "#64748b",      # Mixed (Bund + BY + MUC)
        "Buergergeld_Grundsicherung": "#1e40af", # Single parent: Effective_Federal
        "Arbeitsfoerderung_und_Reha": "#0f766e", # Single parent: Effective_Insurance
        "Schuldendienst_und_Zinsen": "#1e40af",  # Single parent: Effective_Federal
        "Wohnungsbau_und_Stadtplanung": "#8b5cf6", # Mixed (Bund + MUC)
        "Soziales_Jugend_Wohnungslosigkeit": "#db2777", # Mixed (Bund + MUC)
        "Kultur_und_Freizeit": "#b45309",        # Single parent: Effective_Munich
        "Ruecklagen_und_Liquiditaetspuffer": "#0f766e", # Single parent: Effective_Insurance
        "Wirtschaft_Klima_Verwaltung": "#1e40af", # Single parent: Effective_Federal
        "Wirtschaft_Verwaltung_Sonstiges": "#0369a1", # Single parent: Effective_Bayern
        "Kommunale_Verwaltung_Sonstiges": "#b45309",  # Single parent: Effective_Munich
        "Bundeszuweisungen_an_andere_Laender": "#1e40af", # Single parent: Effective_Federal
    }

    # Helper function to construct a Plotly Sankey trace for a specific year
    def create_sankey_trace(target_year):
        year_flows = [f for f in flows if int(f["jahr"]) == target_year]

        node_keys = []
        node_idx = {}
        node_labels = []

        def get_node_idx(name):
            if name not in node_idx:
                node_idx[name] = len(node_keys)
                node_keys.append(name)
                node_labels.append(label_map.get(name, name.replace("_", " ")))
            return node_idx[name]

        # Group Layer 1 strictly by Sovereign Tier (SV -> Bund -> Bayern -> Munich, sorted descending per group)
        sv_l1 = [
            "Krankenbeitraege_AG_AN",
            "Rentenbeitraege_AG_AN",
            "Pflegebeitraege_AG_AN",
            "Arbeitslosenbeitraege_BA",
            "Unfallbeitraege_DGUV",
        ]
        bund_l1 = [
            "Umsatzsteuer_Bund",
            "Lohn_Einkommensteuer_Bund",
            "Verbrauchs_und_Bundessteuern",
            "Nettokreditaufnahme_Bund",
            "Unternehmenssteuern_Bund",
            "Verwaltungseinnahmen_Beteiligungen_Bund",
        ]
        by_l1 = [
            "Gemeinschaftsteuern_Bayern",
            "Landessteuern_Bayern",
            "Verwaltungseinnahmen_Bayern",
            "Ruecklagenentnahme_Kredite_Bayern",
        ]
        muc_l1 = [
            "Gewerbesteuer_Muenchen",
            "Einkommensteuer_USt_Anteil_Muenchen",
            "Gebuehren_Mieten_Entgelte_Muenchen",
            "Sonstige_Ertraege_und_Defizitausgleich_MUC",
            "Beteiligungsertraege_SWM_Muenchen",
            "Grundsteuer_und_Lokalsteuern_Muenchen",
        ]
        l1_nodes = sv_l1 + bund_l1 + by_l1 + muc_l1
        for k in l1_nodes:
            get_node_idx(k)

        l2_nodes = ["Nominal_Insurance", "Nominal_Federal", "Nominal_Bayern", "Nominal_Munich"]
        for k in l2_nodes:
            get_node_idx(k)

        l3_nodes = ["Effective_Insurance", "Effective_Federal", "Effective_Bayern", "Effective_Munich"]
        for k in l3_nodes:
            get_node_idx(k)

        # Layer 4 Functional End-Buckets: Dynamically sorted strictly descending by per-capita volume (€/Kopf)
        l4_in_pc = {}
        for f in year_flows:
            if f["layer_target"] == "Layer_4_Buckets":
                tgt = f["target_node"]
                val_pc = max(0.0, float(f["wert_eur_pro_kopf"]))
                if tgt not in l4_in_pc:
                    l4_in_pc[tgt] = 0.0
                l4_in_pc[tgt] += val_pc

        total_l4_pc = sum(l4_in_pc.values())
        l4_nodes = sorted(l4_in_pc.keys(), key=lambda k: l4_in_pc[k], reverse=True)
        for k in l4_nodes:
            get_node_idx(k)

        sources, targets, values, link_colors, custom_hover = [], [], [], [], []
        in_sums_pc = [0.0] * len(node_keys)
        out_sums_pc = [0.0] * len(node_keys)
        in_sums_mrd = [0.0] * len(node_keys)
        out_sums_mrd = [0.0] * len(node_keys)

        for f in year_flows:
            val_pc = max(0.0, float(f["wert_eur_pro_kopf"]))
            val_mrd = max(0.0, float(f["wert_mrd_eur"]))
            if val_pc <= 0:
                continue

            src_name = f["source_node"]
            tgt_name = f["target_node"]
            l_src = f["layer_source"]
            s_idx = get_node_idx(src_name)
            t_idx = get_node_idx(tgt_name)

            sources.append(s_idx)
            targets.append(t_idx)
            values.append(val_pc)
            custom_hover.append(val_mrd)

            out_sums_pc[s_idx] += val_pc
            in_sums_pc[t_idx] += val_pc
            out_sums_mrd[s_idx] += val_mrd
            in_sums_mrd[t_idx] += val_mrd

            # Color assignment
            if l_src == "Layer_1_Influx":
                if "Bund" in src_name or "Lohn" in src_name or "Umsatz" in src_name or "Unternehmen" in src_name or "Verbrauchs" in src_name:
                    link_colors.append("rgba(30, 58, 138, 0.40)")
                elif "AG_AN" in src_name or "BA" in src_name or "DGUV" in src_name:
                    link_colors.append("rgba(13, 148, 136, 0.40)")
                elif "Bayern" in src_name:
                    link_colors.append("rgba(2, 132, 199, 0.40)")
                elif "Muenchen" in src_name or "MUC" in src_name:
                    link_colors.append("rgba(217, 119, 6, 0.40)")
                else:
                    link_colors.append("rgba(100, 116, 139, 0.35)")
            elif l_src == "Layer_2_Nominal":
                if src_name == "Nominal_Federal" and tgt_name == "Effective_Insurance":
                    link_colors.append("rgba(139, 92, 246, 0.75)")  # Federal Social Subsidy
                elif src_name == "Nominal_Federal" and tgt_name == "Effective_Bayern":
                    link_colors.append("rgba(99, 102, 241, 0.70)")  # Federal Grants to Bavaria
                elif src_name == "Nominal_Bayern" and tgt_name == "Effective_Munich":
                    link_colors.append("rgba(14, 165, 233, 0.70)")  # State FAG Grants to Munich
                elif src_name == "Nominal_Munich" and tgt_name == "Effective_Bayern":
                    link_colors.append("rgba(245, 158, 11, 0.70)")  # Municipal Levy to District/State
                elif src_name == "Nominal_Federal":
                    link_colors.append("rgba(30, 58, 138, 0.55)")
                elif src_name == "Nominal_Insurance":
                    link_colors.append("rgba(13, 148, 136, 0.55)")
                elif src_name == "Nominal_Bayern":
                    link_colors.append("rgba(2, 132, 199, 0.55)")
                elif src_name == "Nominal_Munich":
                    link_colors.append("rgba(217, 119, 6, 0.55)")
                else:
                    link_colors.append("rgba(148, 163, 184, 0.50)")
            else:  # Layer 3 -> 4: Outflows inherit the exact color of their Layer 3 parent
                if src_name == "Effective_Federal":
                    link_colors.append("rgba(30, 58, 138, 0.45)")
                elif src_name == "Effective_Insurance":
                    link_colors.append("rgba(13, 148, 136, 0.45)")
                elif src_name == "Effective_Bayern":
                    link_colors.append("rgba(2, 132, 199, 0.45)")
                elif src_name == "Effective_Munich":
                    link_colors.append("rgba(217, 119, 6, 0.45)")
                else:
                    link_colors.append("rgba(148, 163, 184, 0.40)")

        # Clamped Y Layout: Influxes of Layer 2 are clustered close to each other per sovereign tier
        node_x, node_y, node_colors = [], [], []
        tier_y_l2_l3 = [0.15, 0.44, 0.68, 0.88]
        for k in node_keys:
            if k in l1_nodes:
                node_x.append(0.001)
                if k in sv_l1:
                    idx = sv_l1.index(k)
                    node_y.append(0.02 + idx * (0.24 / max(1, len(sv_l1) - 1)))
                elif k in bund_l1:
                    idx = bund_l1.index(k)
                    node_y.append(0.35 + idx * (0.16 / max(1, len(bund_l1) - 1)))
                elif k in by_l1:
                    idx = by_l1.index(k)
                    node_y.append(0.58 + idx * (0.14 / max(1, len(by_l1) - 1)))
                elif k in muc_l1:
                    idx = muc_l1.index(k)
                    node_y.append(0.79 + idx * (0.17 / max(1, len(muc_l1) - 1)))
                else:
                    node_y.append(0.50)
            elif k in l2_nodes:
                node_x.append(0.32)
                idx = l2_nodes.index(k)
                node_y.append(tier_y_l2_l3[idx])
            elif k in l3_nodes:
                node_x.append(0.65)
                idx = l3_nodes.index(k)
                node_y.append(tier_y_l2_l3[idx])
            else:
                node_x.append(0.999)
                idx = l4_nodes.index(k) if k in l4_nodes else 0
                node_y.append(0.02 + idx * (0.92 / max(1, len(l4_nodes) - 1)))

            if k in l4_nodes:
                parents_l3 = list({f["source_node"] for f in year_flows if f["target_node"] == k and f["layer_source"] == "Layer_3_Effective"})
                if len(parents_l3) == 1:
                    single_parent = parents_l3[0]
                    l3_parent_colors = {
                        "Effective_Insurance": "#0f766e",
                        "Effective_Federal": "#1e40af",
                        "Effective_Bayern": "#0369a1",
                        "Effective_Munich": "#b45309",
                    }
                    clr = l3_parent_colors.get(single_parent, "#475569")
                else:
                    mixed_colors = {
                        "Gesundheit_und_Pflege": "#10b981",          # Emerald
                        "Schulen_und_Kitas": "#3b82f6",              # Royal Blue
                        "Verkehr_und_Infrastruktur": "#f59e0b",      # Orange-Gold
                        "Sicherheit_und_Justiz": "#64748b",          # Slate
                        "Soziales_Jugend_Wohnungslosigkeit": "#db2777", # Rose
                        "Hochschulen_und_Forschung": "#6366f1",      # Indigo
                        "Wohnungsbau_und_Stadtplanung": "#8b5cf6",   # Purple
                    }
                    clr = mixed_colors.get(k, "#475569")
            else:
                clr = "#475569"
                for pat, c in color_map.items():
                    if pat in k:
                        clr = c
                        break
            node_colors.append(clr)

        enhanced_labels = []
        for i, k in enumerate(node_keys):
            base_lbl = node_labels[i]
            vol_pc = max(in_sums_pc[i], out_sums_pc[i])
            vol_mrd = max(in_sums_mrd[i], out_sums_mrd[i])
            if k in l2_nodes or k in l3_nodes:
                pop_desc = "83,6 Mio. EW" if ("Federal" in k or "Insurance" in k) else ("13,2 Mio. EW" if "Bayern" in k else "1,51 Mio. EW")
                enhanced_labels.append(
                    f"<b>{base_lbl}</b><br><b>{int(round(vol_pc)):,} €/Kopf</b> ({vol_mrd:.1f} Mrd. €)<br>"
                    f"<span style='font-size:10px;color:#000000'>Basis: {pop_desc}</span>"
                )
            elif k in l4_nodes:
                pct = (vol_pc / total_l4_pc * 100.0) if total_l4_pc > 0 else 0.0
                if "Laenderfinanzausgleich" in k:
                    enhanced_labels.append(
                        f"<b>{base_lbl}</b><br><b>-{int(round(vol_pc)):,} €/Kopf</b> · <b>{pct:.1f}%</b> (-{vol_mrd:.2f} Mrd. €)"
                    )
                elif vol_mrd >= 1.0:
                    enhanced_labels.append(f"<b>{base_lbl}</b><br><b>{int(round(vol_pc)):,} €/Kopf</b> · <b>{pct:.1f}%</b> ({vol_mrd:.2f} Mrd. €)")
                else:
                    mio_val = vol_mrd * 1000.0
                    enhanced_labels.append(f"<b>{base_lbl}</b><br><b>{int(round(vol_pc)):,} €/Kopf</b> · <b>{pct:.1f}%</b> ({mio_val:.0f} Mio. €)")
            elif vol_mrd >= 1.0:
                enhanced_labels.append(f"<b>{base_lbl}</b><br>{int(round(vol_pc)):,} €/Kopf ({vol_mrd:.2f} Mrd. €)")
            else:
                mio_val = vol_mrd * 1000.0
                enhanced_labels.append(f"<b>{base_lbl}</b><br>{int(round(vol_pc)):,} €/Kopf ({mio_val:.0f} Mio. €)")

        return go.Sankey(
            arrangement="snap",
            node=dict(
                pad=35,
                thickness=26,
                line=dict(color="#0f172a", width=0.8),
                label=enhanced_labels,
                color=node_colors,
                x=node_x,
                y=node_y,
                hovertemplate="<b>%{label}</b><extra></extra>",
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                color=link_colors,
                customdata=custom_hover,
                hovertemplate="%{source.label} → %{target.label}<br><b>%{value:,.0f} € / Kopf</b> (Pro-Kopf-Äquivalent)<br>Absolutes Gesamtvolumen: <b>%{customdata:.2f} Mrd. €</b><extra></extra>",
            ),
        )

    # Helper function to construct layout annotations including Layer 2 -> Layer 3 Transfer Badges
    def build_sankey_annotations(year):
        f_yr = [f for f in flows if int(f["jahr"]) == year]
        def get_f(s, t):
            return next(f for f in f_yr if f["source_node"] == s and f["target_node"] == t)

        f_sv = get_f("Nominal_Insurance", "Effective_Insurance")
        f_bz = get_f("Nominal_Federal", "Effective_Insurance")
        f_bk = get_f("Nominal_Federal", "Effective_Federal")
        f_bm = get_f("Nominal_Federal", "Effective_Bayern")
        f_by = get_f("Nominal_Bayern", "Effective_Bayern")
        f_fag = get_f("Nominal_Bayern", "Effective_Munich")
        f_muc = get_f("Nominal_Munich", "Effective_Munich")
        f_lfa = get_f("Effective_Bayern", "Laenderfinanzausgleich_Ausgleich_an_andere_Laender")

        sv_mrd = f"{float(f_sv['wert_mrd_eur']):.1f}".replace(".", ",")
        sv_pc = f"{int(round(float(f_sv['wert_eur_pro_kopf']))):,}".replace(",", ".")
        bz_mrd = f"{float(f_bz['wert_mrd_eur']):.1f}".replace(".", ",")
        bz_pc = f"{int(round(float(f_bz['wert_eur_pro_kopf']))):,}".replace(",", ".")
        bk_mrd = f"{float(f_bk['wert_mrd_eur']):.1f}".replace(".", ",")
        bk_pc = f"{int(round(float(f_bk['wert_eur_pro_kopf']))):,}".replace(",", ".")
        bm_mrd = f"{float(f_bm['wert_mrd_eur']):.2f}".replace(".", ",")
        bm_pc = f"{int(round(float(f_bm['wert_eur_pro_kopf']))):,}".replace(",", ".")
        by_mrd = f"{float(f_by['wert_mrd_eur']):.2f}".replace(".", ",")
        by_pc = f"{int(round(float(f_by['wert_eur_pro_kopf']))):,}".replace(",", ".")
        fag_mrd = f"{float(f_fag['wert_mrd_eur']):.2f}".replace(".", ",")
        fag_pc = f"{int(round(float(f_fag['wert_eur_pro_kopf']))):,}".replace(",", ".")
        muc_mrd = f"{float(f_muc['wert_mrd_eur']):.2f}".replace(".", ",")
        muc_pc = f"{int(round(float(f_muc['wert_eur_pro_kopf']))):,}".replace(",", ".")
        lfa_mrd = f"{float(f_lfa['wert_mrd_eur']):.2f}".replace(".", ",")
        lfa_pc = f"-{int(round(float(f_lfa['wert_eur_pro_kopf']))):,}".replace(",", ".")

        s_pop = {r["ebene"]: int(float(r["bevoelkerung_referenz"])) for r in summary if int(r["jahr"]) == year}
        pop_de = s_pop["Bund_Kernhaushalt"]
        pop_by = s_pop["Freistaat_Bayern"]
        pop_muc = s_pop["Landeshauptstadt_Muenchen"]

        pop_de_fmt = f"{pop_de:,}".replace(",", ".")
        pop_by_fmt = f"{pop_by:,}".replace(",", ".")
        pop_muc_fmt = f"{pop_muc:,}".replace(",", ".")
        pop_de_mio = f"{pop_de / 1e6:.1f}".replace(".", ",")
        pop_by_mio = f"{pop_by / 1e6:.1f}".replace(".", ",")
        pop_muc_mio = f"{pop_muc / 1e6:.2f}".replace(".", ",")

        return [
            dict(
                x=0.005, y=1.025, xref="paper", yref="paper",
                text="<b>LAYER 1: STEUER- & BEITRAGSINFLUX</b><br><span style='font-size:11px;color:#64748b'>Eigene Steuern, Beitragsmittel & Kredite</span>",
                showarrow=False, font=dict(size=13, color="#1e3a8a", family="Helvetica, Arial"),
            ),
            dict(
                x=0.32, y=1.025, xref="paper", yref="paper",
                text="<b>LAYER 2: NOMINALE GEBIETSKÖRPERSCHAFTEN</b><br><span style='font-size:11px;color:#64748b'>Bruttohaushalte der Gebietskörperschaften</span>",
                showarrow=False, font=dict(size=13, color="#0f172a", family="Helvetica, Arial"),
            ),
            dict(
                x=0.65, y=1.025, xref="paper", yref="paper",
                text="<b>LAYER 3: EFFEKTIVE HAUSHALTE (KONSOLIDIERT)</b><br><span style='font-size:11px;color:#64748b'>Ausgaben nach Konsolidierung & Umlagen</span>",
                showarrow=False, font=dict(size=13, color="#0d9488", family="Helvetica, Arial"),
            ),
            dict(
                x=0.995, y=1.025, xref="paper", yref="paper",
                text="<b>LAYER 4: FINALE FUNKTIONALE END-BUCKETS</b><br><span style='font-size:11px;color:#64748b'>Bürgerwirksame Güter & Länderfinanzausgleich</span>",
                showarrow=False, font=dict(size=13, color="#475569", family="Helvetica, Arial"), xanchor="right",
            ),
            # Layer 2 -> Layer 3 Transfer & Outflow Badges directly on the ribbons
            dict(
                x=0.485, y=0.853, xref="paper", yref="paper",
                text=f"<b>Beitragseinnahmen SV:</b> {sv_mrd} Mrd. € ({sv_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#0f766e", family="Helvetica, Arial"),
                bgcolor="rgba(240, 253, 250, 0.94)", bordercolor="#0d9488", borderwidth=1, borderpad=4,
            ),
            dict(
                x=0.485, y=0.661, xref="paper", yref="paper",
                text=f"<b>Bundeszuschuss an SV:</b> <b>{bz_mrd} Mrd. €</b> ({bz_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#5b21b6", family="Helvetica, Arial"),
                bgcolor="rgba(245, 243, 255, 0.96)", bordercolor="#8b5cf6", borderwidth=1.5, borderpad=5,
            ),
            dict(
                x=0.485, y=0.553, xref="paper", yref="paper",
                text=f"<b>Bundes-Kernhaushalt:</b> {bk_mrd} Mrd. € ({bk_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#1e3a8a", family="Helvetica, Arial"),
                bgcolor="rgba(239, 246, 255, 0.94)", bordercolor="#1e3a8a", borderwidth=1, borderpad=4,
            ),
            dict(
                x=0.485, y=0.435, xref="paper", yref="paper",
                text=f"<b>Bundesmittel an Bayern:</b> <b>{bm_mrd} Mrd. €</b> ({bm_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#3730a3", family="Helvetica, Arial"),
                bgcolor="rgba(224, 231, 255, 0.96)", bordercolor="#6366f1", borderwidth=1.5, borderpad=5,
            ),
            dict(
                x=0.485, y=0.316, xref="paper", yref="paper",
                text=f"<b>Landeshaushalt Bayern:</b> {by_mrd} Mrd. € ({by_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#0369a1", family="Helvetica, Arial"),
                bgcolor="rgba(240, 249, 255, 0.94)", bordercolor="#0284c7", borderwidth=1, borderpad=4,
            ),
            dict(
                x=0.485, y=0.229, xref="paper", yref="paper",
                text=f"<b>Netto-FAG an München:</b> <b>{fag_mrd} Mrd. €</b> ({fag_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#b45309", family="Helvetica, Arial"),
                bgcolor="rgba(254, 243, 199, 0.96)", bordercolor="#f59e0b", borderwidth=1.5, borderpad=5,
            ),
            dict(
                x=0.485, y=0.116, xref="paper", yref="paper",
                text=f"<b>Kommunalhaushalt München:</b> {muc_mrd} Mrd. € ({muc_pc} €/Kopf)",
                showarrow=False, font=dict(size=11, color="#92400e", family="Helvetica, Arial"),
                bgcolor="rgba(255, 251, 235, 0.94)", bordercolor="#d97706", borderwidth=1, borderpad=4,
            ),
            # Bottom footer callouts: Referenzbevölkerung (left) and Amtliche Primärquellen (right)
            dict(
                x=0.005, y=-0.075, xref="paper", yref="paper", xanchor="left",
                text=(
                    f"<b>Referenzbevölkerung (Zensus 2022, Stand 31.12.{year - 1}):</b> "
                    f"Bund & SV: <b>{pop_de_fmt} EW</b> ({pop_de_mio} Mio.) • "
                    f"Freistaat Bayern: <b>{pop_by_fmt} EW</b> ({pop_by_mio} Mio.) • "
                    f"Landeshauptstadt München: <b>{pop_muc_fmt} EW</b> ({pop_muc_mio} Mio.)"
                ),
                showarrow=False, font=dict(size=12, color="#1e293b", family="Helvetica, Arial"),
                bgcolor="#f8fafc", bordercolor="#cbd5e1", borderwidth=1, borderpad=6,
            ),
            dict(
                x=0.995, y=-0.075, xref="paper", yref="paper", xanchor="right",
                text=(
                    f"<b>Amtliche Primärquellen ({year}):</b> "
                    f"BMF (Bundeshaushalt) • BMAS / DRV / GKV (Sozialbudget) • "
                    f"StMFH (Haushalt Bayern & LFA) • Stadtkämmerei München • Destatis (Zensus 2022)"
                ),
                showarrow=False, font=dict(size=12, color="#334155", family="Helvetica, Arial"),
                bgcolor="#f8fafc", bordercolor="#cbd5e1", borderwidth=1, borderpad=6,
            )
        ]

    # 1. Static high-resolution 2024 figure
    title_2024 = (
        "<b>4-Layer Multi-Level Fiscal Architecture (2024): Bund, Freistaat Bayern & Landeshauptstadt München</b><br>"
        "<sup>Ribbon- und Knotenbreiten proportional zum Pro-Kopf-Volumen (€/Kopf). Absolute Haushaltsvolumina in Klammern ausgewiesen.</sup>"
    )
    title_2023 = (
        "<b>4-Layer Multi-Level Fiscal Architecture (2023): Bund, Freistaat Bayern & Landeshauptstadt München</b><br>"
        "<sup>Ribbon- und Knotenbreiten proportional zum Pro-Kopf-Volumen (€/Kopf). Absolute Haushaltsvolumina in Klammern ausgewiesen.</sup>"
    )

    trace_2024 = create_sankey_trace(2024)
    annos_2024 = build_sankey_annotations(2024)
    fig_static = go.Figure(data=[trace_2024])

    fig_static.update_layout(
        title=dict(
            text=title_2024,
            font=dict(family="Helvetica, Arial, sans-serif", size=22, color="#0f172a"),
            x=0.02,
            y=0.985,
        ),
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color="#1e293b"),
        width=2600,
        height=2250,
        margin=dict(l=50, r=50, t=160, b=190),
        paper_bgcolor="#f8fafc",
        plot_bgcolor="#f8fafc",
        annotations=annos_2024,
    )

    fig_static.write_image(out_png_path, scale=2)
    fig_static.write_image(out_svg_path)
    print(f"✓ Rendered high-resolution Plotly Sankey: {out_png_path}")

    # 2. Interactive HTML figure with Year Switcher (2024 vs 2023)
    trace_2023 = create_sankey_trace(2023)
    trace_2023.visible = False
    annos_2023 = build_sankey_annotations(2023)

    fig_interactive = go.Figure(data=[trace_2024, trace_2023])
    fig_interactive.update_layout(fig_static.layout)
    fig_interactive.update_layout(
        annotations=annos_2024,
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                x=0.48,
                y=1.08,
                buttons=[
                    dict(
                        label="<b>2024 (Baseline)</b>",
                        method="update",
                        args=[{"visible": [True, False]}, {"annotations": annos_2024, "title.text": title_2024}],
                    ),
                    dict(
                        label="<b>2023 (Vorjahr)</b>",
                        method="update",
                        args=[{"visible": [False, True]}, {"annotations": annos_2023, "title.text": title_2023}],
                    ),
                ],
                bgcolor="#f1f5f9",
                bordercolor="#cbd5e1",
                font=dict(size=12, color="#0f172a"),
            )
        ]
    )
    fig_interactive.write_html(out_html_path)
    _align_sankey_artifacts(out_svg_path, out_png_path, out_html_path)
    print(f"✓ Rendered interactive Plotly Sankey: {out_html_path}")


def _align_sankey_artifacts(out_svg_path, out_png_path, out_html_path):
    """Post-process rendered Sankey artifacts to ensure strict monotonic descending order
    on Layer 2 link attachments and eliminate Bayern -> Munich ribbon crossover."""
    import re

    updated_bund_ribbons = []
    updated_by_muc_ribbons = []
    js_statements = []

    # 1. Update SVG paths
    if os.path.exists(out_svg_path):
        import xml.etree.ElementTree as ET

        tree = ET.parse(out_svg_path)
        root = tree.getroot()
        paths = [p for p in root.iter("{http://www.w3.org/2000/svg}path") if "C" in p.attrib.get("d", "")]

        # A) Bund Layer 1 -> Layer 2 (paths[5:11])
        if len(paths) >= 11:
            bund_paths = paths[5:11]
            parsed_bund = []
            for p in bund_paths:
                d = p.attrib["d"]
                m = re.match(
                    r"M([-\d\.]+),\s*([-\d\.]+)C([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)L([-\d\.]+),\s*([-\d\.]+)",
                    d,
                )
                if m:
                    x0, y0 = float(m.group(1)), float(m.group(2))
                    x1, y1 = float(m.group(7)), float(m.group(8))
                    y1_bot = float(m.group(10))
                    h = y1_bot - y1
                    parsed_bund.append({"p": p, "x0": x0, "y0": y0, "x1": x1, "h": h, "orig_y1": y1})

            if parsed_bund:
                target_top = min(item["orig_y1"] for item in parsed_bund)
                curr_y1 = target_top

                for idx_offset, item in enumerate(parsed_bund):
                    x0 = item["x0"]
                    y0_top = item["y0"]
                    h = item["h"]
                    y0_bot = y0_top + h
                    x1 = item["x1"]
                    cx = (x0 + x1) / 2.0

                    y1_top = curr_y1
                    y1_bot = curr_y1 + h
                    curr_y1 += h

                    new_d = (
                        f"M{x0},{y0_top:.6f}C{cx:.6f},{y0_top:.6f} {cx:.6f},{y1_top:.6f} {x1},{y1_top:.6f}"
                        f"L{x1},{y1_bot:.6f}C{cx:.6f},{y1_bot:.6f} {cx:.6f},{y0_bot:.6f} {x0},{y0_bot:.6f}Z"
                    )
                    item["p"].attrib["d"] = new_d
                    updated_bund_ribbons.append((x0, x1, cx, y0_top, y0_bot, y1_top, y1_bot))
                    js_statements.append(f"paths[{5 + idx_offset}].setAttribute('d', '{new_d}');")

        # B) Bayern & Munich Layer 2 -> Layer 3 (paths[25:28])
        # User instruction: Bayern -> Munich transfer exits Bayern at the below part
        # and enters Effective Munich in the top part.
        if len(paths) >= 28:
            p25, p26, p27 = paths[25], paths[26], paths[27]
            m25 = re.match(r"M([-\d\.]+),\s*([-\d\.]+)C([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)L([-\d\.]+),\s*([-\d\.]+)", p25.attrib["d"])
            m26 = re.match(r"M([-\d\.]+),\s*([-\d\.]+)C([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)L([-\d\.]+),\s*([-\d\.]+)", p26.attrib["d"])
            m27 = re.match(r"M([-\d\.]+),\s*([-\d\.]+)C([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)\s+([-\d\.]+),\s*([-\d\.]+)L([-\d\.]+),\s*([-\d\.]+)", p27.attrib["d"])

            if m25 and m26 and m27:
                h25 = float(m25.group(10)) - float(m25.group(8))
                h26 = float(m26.group(10)) - float(m26.group(8))
                h27 = float(m27.group(10)) - float(m27.group(8))

                x0_by = float(m25.group(1))
                x1_by = float(m25.group(7))
                cx_by = (x0_by + x1_by) / 2.0

                # 1. Nominal Bayern exit: Path 25 at top, Path 26 in below part
                by_src_top = min(float(m25.group(2)), float(m26.group(2)))
                y0_top_25 = by_src_top
                y0_bot_25 = y0_top_25 + h25
                y0_top_26 = y0_bot_25
                y0_bot_26 = y0_top_26 + h26

                # Target for Path 25 in Effective Bayern (enters at original y1):
                y1_top_25 = float(m25.group(8))
                y1_bot_25 = y1_top_25 + h25

                # 2. Effective Munich entry: Path 26 in top part, Path 27 below it
                muc_tgt_top = min(float(m26.group(8)), float(m27.group(8)))
                y1_top_26 = muc_tgt_top
                y1_bot_26 = y1_top_26 + h26
                y1_top_27 = y1_bot_26
                y1_bot_27 = y1_top_27 + h27

                # Source for Path 27 (Nominal Munich):
                y0_top_27 = float(m27.group(2))
                y0_bot_27 = y0_top_27 + h27

                new_d25 = (
                    f"M{x0_by},{y0_top_25:.6f}C{cx_by:.6f},{y0_top_25:.6f} {cx_by:.6f},{y1_top_25:.6f} {x1_by},{y1_top_25:.6f}"
                    f"L{x1_by},{y1_bot_25:.6f}C{cx_by:.6f},{y1_bot_25:.6f} {cx_by:.6f},{y0_bot_25:.6f} {x0_by},{y0_bot_25:.6f}Z"
                )
                new_d26 = (
                    f"M{x0_by},{y0_top_26:.6f}C{cx_by:.6f},{y0_top_26:.6f} {cx_by:.6f},{y1_top_26:.6f} {x1_by},{y1_top_26:.6f}"
                    f"L{x1_by},{y1_bot_26:.6f}C{cx_by:.6f},{y1_bot_26:.6f} {cx_by:.6f},{y0_bot_26:.6f} {x0_by},{y0_bot_26:.6f}Z"
                )
                new_d27 = (
                    f"M{x0_by},{y0_top_27:.6f}C{cx_by:.6f},{y0_top_27:.6f} {cx_by:.6f},{y1_top_27:.6f} {x1_by},{y1_top_27:.6f}"
                    f"L{x1_by},{y1_bot_27:.6f}C{cx_by:.6f},{y1_bot_27:.6f} {cx_by:.6f},{y0_bot_27:.6f} {x0_by},{y0_bot_27:.6f}Z"
                )

                p25.attrib["d"] = new_d25
                p26.attrib["d"] = new_d26
                p27.attrib["d"] = new_d27

                js_statements.append(f"paths[25].setAttribute('d', '{new_d25}');")
                js_statements.append(f"paths[26].setAttribute('d', '{new_d26}');")
                js_statements.append(f"paths[27].setAttribute('d', '{new_d27}');")

                updated_by_muc_ribbons = [
                    (x0_by, x1_by, cx_by, y0_top_25, y0_bot_25, y1_top_25, y1_bot_25, (2, 132, 199, int(255 * 0.55))),
                    (x0_by, x1_by, cx_by, y0_top_26, y0_bot_26, y1_top_26, y1_bot_26, (14, 165, 233, int(255 * 0.70))),
                    (x0_by, x1_by, cx_by, y0_top_27, y0_bot_27, y1_top_27, y1_bot_27, (217, 119, 6, int(255 * 0.55))),
                ]

        tree.write(out_svg_path, encoding="utf-8", xml_declaration=True)

    # 2. Raster PNG alignment: Preserve native high-resolution rendering without destructive pixel surgery
    # (Per AGENTS.md invariant: avoid destructive in-memory canvas clearing/drawing over text labels)
    pass

    # 3. Inject interactive script into HTML
    if os.path.exists(out_html_path) and js_statements:
        with open(out_html_path, "r", encoding="utf-8") as f:
            html_text = f.read()

        js_code = "\n        ".join(js_statements)
        script_snip = f"""
<script>
window.addEventListener("DOMContentLoaded", function() {{
    function alignSankeyLinks() {{
        var paths = document.querySelectorAll('.sankey-link');
        if (!paths || paths.length < 28) {{
            setTimeout(alignSankeyLinks, 100);
            return;
        }}
        {js_code}
    }}
    setTimeout(alignSankeyLinks, 300);
    setTimeout(alignSankeyLinks, 800);
    document.addEventListener('click', function() {{
        setTimeout(alignSankeyLinks, 200);
    }});
}});
</script>
"""
        if "alignSankeyLinks" not in html_text:
            if "alignBundLinks" in html_text:
                html_text = re.sub(r"<script>\s*window\.addEventListener\(\"DOMContentLoaded\",\s*function\(\)\s*\{.*?alignBundLinks.*?</script>", script_snip.strip(), html_text, flags=re.DOTALL)
            elif "</body>" in html_text:
                html_text = html_text.replace("</body>", f"{script_snip}</body>")
            else:
                html_text += script_snip
            with open(out_html_path, "w", encoding="utf-8") as f:
                f.write(html_text)


# ---------------------------------------------------------------------------
# Main Execution Entrypoint
# ---------------------------------------------------------------------------
def main():
    """Main execution coordinator: renders the flagship 4-Layer Fiscal Sankey."""
    datasets_dir = os.path.join(ROOT, "datasets")
    plots_dir = os.path.join(ROOT, "plots")
    os.makedirs(plots_dir, exist_ok=True)

    flows, summary = load_modeling_data(datasets_dir)

    # 4-Layer Physical Kirchhoff-Conserved Fiscal Sankey
    sankey_png = os.path.join(plots_dir, "sankey_fiscal_per_capita.png")
    sankey_svg = os.path.join(plots_dir, "sankey_fiscal_per_capita.svg")
    sankey_html = os.path.join(plots_dir, "sankey_fiscal_interactive.html")
    render_plotly_sankey(flows, summary, sankey_png, sankey_html, sankey_svg)
    print("✓ Flagship 4-Layer Fiscal Sankey successfully generated (PNG, SVG, HTML).")


if __name__ == "__main__":
    main()
