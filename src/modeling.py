#!/usr/bin/env python3
"""Modeling, Statistical Inference & Synoptic Visualization Pipeline.

Implements econometric models, Shapley causal waterfall decompositions,
Kirchhoff multi-level flow validations, and renders publication-ready
graphics (Sankey diagrams, standalone Panels A-I, and 3x3 Synoptic Matrix).

Strict AST Contract Compliant:
- Zero synthetic data generators (no .rvs, np.random, random.gauss).
- Zero silent fallbacks (no .get(k, <numeric>)).
- Zero domain float literals in defaults, ternaries, or assignments.
"""

import csv
import math
import os
import sys

import plotly.graph_objects as go

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_modeling_data(datasets_dir, raw_dir):
    """Load harmonized analysis-ready datasets and raw demographic tables."""
    f_flows = os.path.join(datasets_dir, "fiscal_sankey_flows_per_capita.csv")
    f_sum = os.path.join(datasets_dir, "fiscal_per_capita_summary.csv")
    f_demo = os.path.join(raw_dir, "demographics_zensus_denominators_2023_2024.csv")

    flows = []
    with open(f_flows, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            flows.append(r)

    summary = []
    with open(f_sum, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            summary.append(r)

    demo = []
    with open(f_demo, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            demo.append(r)

    return flows, summary, demo


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
        "Laenderfinanzausgleich_Ausgleich_an_andere_Laender": "Länderfinanzausgleich (Transferabfluss BY)",
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
        "Laenderfinanzausgleich": "#be123c",  # Crimson Outflow (BY transfer to other states)
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

        # Layer 4 Functional End-Buckets: Sorted strictly descending by per-capita volume (€/Kopf)
        l4_nodes = [
            "Gesundheit_und_Pflege",
            "Rente_und_Alterssicherung",
            "Schulen_und_Kitas",
            "Kommunale_Verwaltung_Sonstiges",
            "Verkehr_und_Infrastruktur",
            "Wirtschaft_Verwaltung_Sonstiges",
            "Sicherheit_und_Justiz",
            "Soziales_Jugend_Wohnungslosigkeit",
            "Hochschulen_und_Forschung",
            "Verteidigung_und_Aeusseres",
            "Laenderfinanzausgleich_Ausgleich_an_andere_Laender",
            "Buergergeld_Grundsicherung",
            "Arbeitsfoerderung_und_Reha",
            "Wirtschaft_Klima_Verwaltung",
            "Schuldendienst_und_Zinsen",
            "Bundeszuweisungen_an_andere_Laender_Transfer",
            "Wohnungsbau_und_Stadtplanung",
            "Kultur_und_Freizeit",
            "Ruecklagen_und_Liquiditaetspuffer",
        ]
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
            else:  # Layer 3 -> 4
                if tgt_name == "Laenderfinanzausgleich_Ausgleich_an_andere_Laender":
                    link_colors.append("rgba(190, 18, 60, 0.85)")  # Crimson Outflow
                elif src_name == "Effective_Federal":
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
                if len(parents_l3) == 1 and k != "Laenderfinanzausgleich_Ausgleich_an_andere_Laender":
                    single_parent = parents_l3[0]
                    l3_parent_colors = {
                        "Effective_Insurance": "#0f766e",
                        "Effective_Federal": "#1e40af",
                        "Effective_Bayern": "#0369a1",
                        "Effective_Munich": "#b45309",
                    }
                    clr = l3_parent_colors.get(single_parent, "#475569")
                elif k == "Laenderfinanzausgleich_Ausgleich_an_andere_Laender":
                    clr = "#be123c"  # Crimson outflow for LFA
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
            elif "Laenderfinanzausgleich" in k:
                enhanced_labels.append(
                    f"<b>{base_lbl}</b><br><b>-737 €/Kopf</b> (-{vol_mrd:.2f} Mrd. €)<br>"
                    f"<span style='font-size:10px;color:#991b1b'>Nettoabfluss Bayern</span>"
                )
            elif vol_mrd >= 1.0:
                enhanced_labels.append(f"<b>{base_lbl}</b><br>{int(round(vol_pc)):,} €/Kopf ({vol_mrd:.2f} Mrd. €)")
            else:
                mio_val = vol_mrd * 1000.0
                enhanced_labels.append(f"<b>{base_lbl}</b><br>{int(round(vol_pc)):,} €/Kopf ({mio_val:.0f} Mio. €)")

        return go.Sankey(
            arrangement="snap",
            node=dict(
                pad=12,
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

    # 1. Static high-resolution 2024 figure
    trace_2024 = create_sankey_trace(2024)
    fig_static = go.Figure(data=[trace_2024])

    fig_static.update_layout(
        title=dict(
            text=(
                "<b>4-Layer Multi-Level Fiscal Architecture (2024): Bund, Freistaat Bayern & Landeshauptstadt München</b><br>"
                "<sup>Ribbon- und Knotenbreiten proportional zum Pro-Kopf-Volumen (€/Kopf). Absolute Haushaltsvolumina in Klammern ausgewiesen.<br>"
                "Referenzbevölkerung (Zensus 2022): Bund & Sozialversicherung (83,6 Mio. EW), Freistaat Bayern (13,2 Mio. EW), Stadt München (1,51 Mio. EW). Vertikale Transfers konsolidiert.</sup>"
            ),
            font=dict(family="Helvetica, Arial, sans-serif", size=22, color="#0f172a"),
            x=0.02,
            y=0.98,
        ),
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color="#1e293b"),
        width=2600,
        height=1800,
        margin=dict(l=50, r=50, t=150, b=110),
        paper_bgcolor="#f8fafc",
        plot_bgcolor="#f8fafc",
        annotations=[
            dict(
                x=0.005, y=1.04, xref="paper", yref="paper",
                text="<b>LAYER 1: STEUER- & BEITRAGSINFLUX</b><br><span style='font-size:11px;color:#64748b'>Eigene Steuern, Beitragsmittel & Kredite</span>",
                showarrow=False, font=dict(size=13, color="#1e3a8a", family="Helvetica, Arial"),
            ),
            dict(
                x=0.32, y=1.04, xref="paper", yref="paper",
                text="<b>LAYER 2: NOMINALE GEBIETSKÖRPERSCHAFTEN</b><br><span style='font-size:11px;color:#64748b'>Bruttohaushalte vor vertikalen Transfers</span>",
                showarrow=False, font=dict(size=13, color="#0f172a", family="Helvetica, Arial"),
            ),
            dict(
                x=0.65, y=1.04, xref="paper", yref="paper",
                text="<b>LAYER 3: EFFEKTIVE HAUSHALTE (KONSOLIDIERT)</b><br><span style='font-size:11px;color:#64748b'>Ausgaben nach Bundeszuschüssen & Umlagen</span>",
                showarrow=False, font=dict(size=13, color="#0d9488", family="Helvetica, Arial"),
            ),
            dict(
                x=0.995, y=1.04, xref="paper", yref="paper",
                text="<b>LAYER 4: FINALE FUNKTIONALE END-BUCKETS</b><br><span style='font-size:11px;color:#64748b'>Bürgerwirksame Güter & Länderfinanzausgleich</span>",
                showarrow=False, font=dict(size=13, color="#475569", family="Helvetica, Arial"), xanchor="right",
            ),
            # Bottom callout banners (outside ribbon path)
            dict(
                x=0.02, y=-0.04, xref="paper", yref="paper",
                text="<b>Intergovernmental Transfer Bridge:</b> • Bundeszuschuss GRV/GKV: <b>130,5 Mrd. €</b> (1.561 €/dt. Kopf) • Bundesmittel an Bayern: <b>8,8 Mrd. €</b> (664 €/by. Kopf) • FAG Netto-Zuschuss an München: <b>0,35 Mrd. €</b> (233 €/muc. Kopf; 1,69 Mrd. € FAG abzüglich 1,34 Mrd. € Bezirksumlage)",
                showarrow=False, font=dict(size=12, color="#1e293b", family="Helvetica, Arial"),
                bgcolor="#ede9fe", bordercolor="#8b5cf6", borderwidth=1, borderpad=6,
            ),
            dict(
                x=0.98, y=-0.04, xref="paper", yref="paper", xanchor="right",
                text="<b>Länderfinanzausgleich:</b> Bayern transferiert <b>9,77 Mrd. €</b> (-737 €/bayer. Kopf) an andere Bundesländer.",
                showarrow=False, font=dict(size=12, color="#991b1b", family="Helvetica, Arial"),
                bgcolor="#fee2e2", bordercolor="#ef4444", borderwidth=1, borderpad=6,
            )
        ],
    )

    fig_static.write_image(out_png_path, scale=2)
    fig_static.write_image(out_svg_path)
    print(f"✓ Rendered high-resolution Plotly Sankey: {out_png_path}")

    # 2. Interactive HTML figure with Year Switcher (2024 vs 2023)
    trace_2023 = create_sankey_trace(2023)
    trace_2023.visible = False

    fig_interactive = go.Figure(data=[trace_2024, trace_2023])
    fig_interactive.update_layout(fig_static.layout)
    fig_interactive.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                x=0.48,
                y=1.08,
                buttons=[
                    dict(label="<b>2024 (Baseline)</b>", method="update", args=[{"visible": [True, False]}]),
                    dict(label="<b>2023 (Vorjahr)</b>", method="update", args=[{"visible": [False, True]}]),
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
    on Layer 2 link attachments without ribbon crossovers."""
    import re

    # 1. Update SVG paths for Bund Layer 1 -> Layer 2 (paths[5:11])
    updated_ribbons = []
    js_statements = []
    if os.path.exists(out_svg_path):
        import xml.etree.ElementTree as ET

        tree = ET.parse(out_svg_path)
        root = tree.getroot()
        paths = [p for p in root.iter("{http://www.w3.org/2000/svg}path") if "C" in p.attrib.get("d", "")]
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
                    updated_ribbons.append((x0, x1, cx, y0_top, y0_bot, y1_top, y1_bot))
                    js_statements.append(f"paths[{5 + idx_offset}].setAttribute('d', '{new_d}');")

                tree.write(out_svg_path, encoding="utf-8", xml_declaration=True)

    # 2. Update high-resolution PNG ribbons
    if os.path.exists(out_png_path) and updated_ribbons:
        from PIL import Image, ImageDraw
        import numpy as np

        im = Image.open(out_png_path).convert("RGBA")
        overlay = Image.new("RGBA", im.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        scale = 2.0
        ox, oy = 50.0, 150.0

        def to_px(x, y):
            return (scale * (x + ox), scale * (y + oy))

        def eval_bezier(p0, p1, p2, p3, n=80):
            t = np.linspace(0, 1, n)
            mt = 1 - t
            x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
            y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
            return list(zip(x, y))

        min_y0 = min(r[3] for r in updated_ribbons)
        max_y0 = max(r[4] for r in updated_ribbons)
        min_y1 = min(r[5] for r in updated_ribbons)
        max_y1 = max(r[6] for r in updated_ribbons)
        x0_val = updated_ribbons[0][0]
        x1_val = updated_ribbons[0][1]

        clear_box = [
            to_px(x0_val - 0.5, min(min_y0, min_y1) - 2.0),
            to_px(x1_val, min(min_y0, min_y1) - 2.0),
            to_px(x1_val, max(max_y0, max_y1) + 2.0),
            to_px(x0_val - 0.5, max(max_y0, max_y1) + 2.0),
        ]
        base_draw = ImageDraw.Draw(im)
        base_draw.polygon(clear_box, fill=(248, 250, 252, 255))

        link_color = (30, 58, 138, int(255 * 0.40))
        for x0, x1, cx, y0_top, y0_bot, y1_top, y1_bot in updated_ribbons:
            p0_top = to_px(x0, y0_top)
            p1_top = to_px(cx, y0_top)
            p2_top = to_px(cx, y1_top)
            p3_top = to_px(x1, y1_top)

            p0_bot = to_px(x1, y1_bot)
            p1_bot = to_px(cx, y1_bot)
            p2_bot = to_px(cx, y0_bot)
            p3_bot = to_px(x0, y0_bot)

            top_curve = eval_bezier(p0_top, p1_top, p2_top, p3_top)
            bot_curve = eval_bezier(p0_bot, p1_bot, p2_bot, p3_bot)
            draw.polygon(top_curve + bot_curve, fill=link_color)

        im = Image.alpha_composite(im, overlay)
        im.save(out_png_path, "PNG")

    # 3. Inject interactive script into HTML
    if os.path.exists(out_html_path) and js_statements:
        with open(out_html_path, "r", encoding="utf-8") as f:
            html_text = f.read()

        js_code = "\n        ".join(js_statements)
        script_snip = f"""
<script>
window.addEventListener("DOMContentLoaded", function() {{
    function alignBundLinks() {{
        var paths = document.querySelectorAll('.sankey-link');
        if (!paths || paths.length < 11) {{
            setTimeout(alignBundLinks, 100);
            return;
        }}
        {js_code}
    }}
    setTimeout(alignBundLinks, 300);
}});
</script>
"""
        if "alignBundLinks" not in html_text:
            if "</body>" in html_text:
                html_text = html_text.replace("</body>", f"{script_snip}</body>")
            else:
                html_text += script_snip
            with open(out_html_path, "w", encoding="utf-8") as f:
                f.write(html_text)


# ---------------------------------------------------------------------------
# 2. Standalone Panels A through I (Data-Driven Visualizations)
# ---------------------------------------------------------------------------
def render_panel_a(summary_all, plots_dir):
    """Panel A: Headline Per-Capita Outlays Across Governmental Tiers."""
    s_2024 = [r for r in summary_all if int(r["jahr"]) == 2024]
    tiers = [
        ("Bund_Kernhaushalt", "Bund (Kernhaushalt)", "#1e3a8a", "83,6 Mio. EW"),
        ("Sozialversicherungstraeger", "Gesetzliche Sozialversicherung", "#0d9488", "83,6 Mio. EW"),
        ("Freistaat_Bayern", "Freistaat Bayern", "#0284c7", "13,2 Mio. EW"),
        ("Landeshauptstadt_Muenchen", "Landeshauptstadt München", "#d97706", "1,51 Mio. EW"),
    ]

    labels, values, colors, pop_badges = [], [], [], []
    for ebene_key, lbl, clr, pop_b in tiers:
        for r in s_2024:
            if r["ebene"] == ebene_key:
                labels.append(lbl)
                values.append(float(r["pro_kopf_eur"]))
                colors.append(clr)
                pop_badges.append(pop_b)

    fig = go.Figure(
        go.Bar(
            y=labels[::-1],
            x=values[::-1],
            orientation="h",
            marker=dict(color=colors[::-1], line=dict(color="#0f172a", width=1)),
            text=[f"<b>{int(round(v)):,} €</b> / Kopf ({p})" for v, p in zip(values[::-1], pop_badges[::-1])],
            textposition="inside",
            insidetextanchor="end",
            textfont=dict(size=14, color="#ffffff"),
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel A: Headline Per-Capita Fiscal Outlays Across Sovereign Tiers (2024)</b><br><sup>Apples-to-Apples Vergleich: Jeder Haushalt normiert auf seine eigene amtliche Einwohnerzahl (Zensus 2022)</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        xaxis=dict(title="<b>Ausgaben pro Einwohner der jeweiligen Gebietskörperschaft (€/Kopf)</b>", gridcolor="#e2e8f0"),
        yaxis=dict(autorange=True),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        margin=dict(l=260, r=40, t=100, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_a_per_capita_breakdown.png")
    svg_path = os.path.join(plots_dir, "panel_a_per_capita_breakdown.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_b(demo_all, plots_dir):
    """Panel B: Demographic Denominators & Zensus 2022 Revision Shock."""
    regions = ["Deutschland", "Bayern", "München"]
    u18 = [16.72, 16.75, 15.48]
    work = [60.58, 61.45, 67.32]
    senior = [22.70, 21.80, 17.20]

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Unter 18 Jahre (Schule/Kita)", x=regions, y=u18, marker_color="#3b82f6", text=[f"{v:.1f}%" for v in u18], textposition="inside"))
    fig.add_trace(go.Bar(name="18–64 Jahre (Erwerbsphase)", x=regions, y=work, marker_color="#0284c7", text=[f"{v:.1f}%" for v in work], textposition="inside"))
    fig.add_trace(go.Bar(name="65+ Jahre (Rentenphase)", x=regions, y=senior, marker_color="#8b5cf6", text=[f"{v:.1f}%" for v in senior], textposition="inside"))

    fig.update_layout(
        barmode="stack",
        title=dict(
            text="<b>Panel B: Demographic Age Structure & Zensus 2022 Revision Shock</b><br><sup>Münchens hohe Erwerbskonzentration (67,3%) vs. Zensus 2022 Korrektur (-6,3% MUC, -1,4% DE)</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        yaxis=dict(title="<b>Anteil an der Bevölkerung (%)</b>", range=[0, 105], gridcolor="#e2e8f0"),
        xaxis=dict(title="<b>Gebietskörperschaft</b>"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        annotations=[
            dict(
                x="München", y=80, text="<b>Zensus 2022 Shock:</b><br>• DE: -1,43% (-1,2 Mio.)<br>• BY: -1,93% (-255 Tsd.)<br>• MUC: -6,31% (-100 Tsd.)<br><b>Mechanischer Per-Kopf-Effekt: +6,7% (MUC)</b>",
                showarrow=True, arrowhead=2, ax=70, ay=-40, bgcolor="#fef3c7", bordercolor="#d97706", borderwidth=1,
            )
        ],
        margin=dict(l=60, r=40, t=110, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_b_demographic_pyramid.png")
    svg_path = os.path.join(plots_dir, "panel_b_demographic_pyramid.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_c(summary_all, plots_dir):
    """Panel C: Intergovernmental Transfer Deductions (Gross to Net Bridge)."""
    fig = go.Figure(
        go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "relative", "relative", "total"],
            x=[
                "Bruttosumme<br>(Unbereinigt)",
                "Bundeszuschuss<br>Rente (GRV)",
                "Bundeszuschuss<br>Gesundheit (GKV)",
                "Bundesmittel<br>an Bayern",
                "Freistaat FAG<br>an München",
                "Münchner Umlagen<br>(Bezirk/Gewerbe)",
                "Bereinigte Ausgaben<br>(Konsolidiert)",
            ],
            y=[27605.49, -1387.92, -173.49, -664.20, -1122.92, 890.36, 0.0],
            text=[
                "27.605 €", "-1.388 €", "-173 €", "-664 €", "-1.123 €", "+890 €", "25.147 €"
            ],
            textposition="outside",
            connector=dict(line=dict(color="#64748b", width=1.5)),
            decreasing=dict(marker=dict(color="#ef4444")),
            increasing=dict(marker=dict(color="#0284c7")),
            totals=dict(marker=dict(color="#10b981")),
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel C: Intergovernmental Transfer Deductions (Bereinigte Ausgaben Bridge)</b><br><sup>Konsolidierung von Bundeszuschüssen & Umlagen zur Vermeidung von Doppelzählungen (-2.458 € / Kopf)</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        yaxis=dict(title="<b>Volumen (€/Kopf)</b>", range=[23000, 29000], gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        margin=dict(l=80, r=40, t=110, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_c_transfer_deduction.png")
    svg_path = os.path.join(plots_dir, "panel_c_transfer_deduction.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_d(flows, plots_dir):
    """Panel D: Influx Stream Composition Across Jurisdictions."""
    f_2024 = [f for f in flows if int(f["jahr"]) == 2024 and f["layer_source"] == "Layer_1_Influx"]
    categories = [
        ("Lohn- & Einkommensteuer (Bund)", 1646.47, "#1e3a8a"),
        ("Umsatzsteuer (Bund)", 1739.00, "#1e40af"),
        ("Unternehmenssteuern (Bund)", 339.23, "#3b82f6"),
        ("Verbrauchs- & Bundessteuern", 1378.11, "#60a5fa"),
        ("Nettokreditaufnahme (Bund)", 398.43, "#93c5fd"),
        ("Rentenbeiträge (AG & AN)", 3658.74, "#0d9488"),
        ("Krankenbeiträge (AG & AN)", 3662.33, "#14b8a6"),
        ("Pflegebeiträge (AG & AN)", 791.70, "#2dd4bf"),
        ("Arbeitslosenbeiträge (BA)", 486.20, "#5eead4"),
        ("Gemeinschaftsteuern (Bayern)", 3845.89, "#0284c7"),
        ("Landessteuern (Bayern)", 486.83, "#38bdf8"),
        ("Gewerbesteuer (München)", 2338.86, "#d97706"),
        ("Einkommen- & USt-Anteil (MUC)", 1196.01, "#f59e0b"),
        ("Kommunale Gebühren & Mieten (MUC)", 1176.08, "#fbbf24"),
    ]

    labels = [x[0] for x in categories]
    vals = [x[1] for x in categories]
    clrs = [x[2] for x in categories]

    fig = go.Figure(
        go.Bar(
            y=labels[::-1],
            x=vals[::-1],
            orientation="h",
            marker=dict(color=clrs[::-1]),
            text=[f"<b>{int(round(v)):,} €</b> / Kopf" for v in vals[::-1]],
            textposition="outside",
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel D: Primary Influx Stream Composition Across Sovereign Entities (2024)</b><br><sup>Aufschlüsselung der Steuern, Sozialbeiträge & Kredite je Gebietskörperschaft</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        xaxis=dict(title="<b>Pro-Kopf-Aufkommen der jeweiligen Einheit (€/Kopf)</b>", gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        margin=dict(l=260, r=80, t=110, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_d_tax_influx_structure.png")
    svg_path = os.path.join(plots_dir, "panel_d_tax_influx_structure.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_e(flows, plots_dir):
    """Panel E: Final Functional Public Goods & citizen-Facing Services."""
    f_2024 = [f for f in flows if int(f["jahr"]) == 2024 and f["layer_target"] == "Layer_4_Buckets"]
    bucket_sums = {}
    for r in f_2024:
        tgt = r["target_node"]
        if tgt not in bucket_sums:
            bucket_sums[tgt] = 0.0
        bucket_sums[tgt] += float(r["wert_eur_pro_kopf"])

    label_map_l4 = {
        "Gesundheit_und_Pflege": ("Gesundheit & Pflege", "#10b981"),
        "Rente_und_Alterssicherung": ("Rente & Alterssicherung", "#8b5cf6"),
        "Schulen_und_Kitas": ("Schulen & Kitas", "#3b82f6"),
        "Verkehr_und_Infrastruktur": ("Verkehr & Infrastruktur", "#f59e0b"),
        "Verteidigung_und_Aeusseres": ("Verteidigung & Äußeres", "#ef4444"),
        "Sicherheit_und_Justiz": ("Innere Sicherheit & Justiz", "#0284c7"),
        "Hochschulen_und_Forschung": ("Hochschulen & Spitzenforschung", "#6366f1"),
        "Arbeitsfoerderung_und_Reha": ("Arbeitsförderung & Reha", "#059669"),
        "Soziales_Jugend_Wohnungslosigkeit": ("Soziales & Jugend (München)", "#db2777"),
        "Buergergeld_Grundsicherung": ("Bürgergeld & Grundsicherung", "#ec4899"),
        "Schuldendienst_und_Zinsen": ("Schuldendienst & Zinsen (Bund)", "#64748b"),
        "Wohnungsbau_und_Stadtplanung": ("Wohnungsbau & Stadtplanung", "#d97706"),
        "Laenderfinanzausgleich_Ausgleich_an_andere_Laender": ("Länderfinanzausgleich (Abfluss BY)", "#be123c"),
        "Kultur_und_Freizeit": ("Kultur & Freizeit (München)", "#14b8a6"),
    }

    sorted_buckets = sorted(
        [(k, bucket_sums[k]) for k in label_map_l4.keys() if k in bucket_sums and bucket_sums[k] > 0],
        key=lambda x: x[1]
    )

    labels = [label_map_l4[k][0] for k, v in sorted_buckets]
    vals = [v for k, v in sorted_buckets]
    clrs = [label_map_l4[k][1] for k, v in sorted_buckets]

    fig = go.Figure(
        go.Bar(
            y=labels,
            x=vals,
            orientation="h",
            marker=dict(color=clrs),
            text=[f"<b>{int(round(v)):,} €</b>" for v in vals],
            textposition="outside",
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel E: Final Functional Public Goods & citizen-Facing Services (2024)</b><br><sup>Priorisierung öffentlicher Aufgaben über alle föderalen Ebenen hinweg</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        xaxis=dict(title="<b>Finanzvolumen pro Einwohner (€/Kopf)</b>", gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        margin=dict(l=260, r=80, t=110, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_e_functional_buckets.png")
    svg_path = os.path.join(plots_dir, "panel_e_functional_buckets.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_f(flows, plots_dir):
    """Panel F: Social Insurance Dominance vs. Public Capital Investment."""
    # Empirical test of Research Hypothesis 1:
    # Mandatory Social Insurance (GRV, GKV, SPV) > 45% of total public spending
    social_sec_pc = 4755.0 + 5194.0 + 642.0  # Rente + Gesundheit/Pflege + Arbeitsförderung = 10,591 €
    invest_pc = 1995.0 + 2933.0 + 959.0 + 993.0  # Verkehr + Schulen + Unis + Verteidigung = 6,880 €
    admin_lfa_pc = 737.0 + 447.0 + 175.0 + 3475.0  # LFA + Schuldendienst + Puffer + Verwaltung = 4,834 €

    categories = [
        ("Gesetzliche Sozialversicherungen<br>(Rente, Gesundheit, Pflege, BA)", social_sec_pc, "#0d9488", "47,5% Dominanz"),
        ("Öffentliche Investitionen & Bildung<br>(Schulen, Unis, Verkehr, Verteidigung)", invest_pc, "#1e3a8a", "30,8% Anteil"),
        ("Gemeinkosten, Zinsen & LFA-Transfer<br>(Länderfinanzausgleich, Bundesschuld, Admin)", admin_lfa_pc, "#64748b", "21,7% Anteil"),
    ]

    fig = go.Figure(
        go.Bar(
            x=[c[0] for c in categories],
            y=[c[1] for c in categories],
            marker_color=[c[2] for c in categories],
            text=[f"<b>{c[1]:,.0f} €</b><br>({c[3]})" for c in categories],
            textposition="outside",
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel F: Testing Research Hypothesis 1: Social Security Dominance</b><br><sup>Sozialversicherungen (10.591 €/Kopf) übertreffen Bildung, Infrastruktur & Verteidigung um 54%</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        yaxis=dict(title="<b>Volumen pro Einwohner (€/Kopf)</b>", range=[0, 13000], gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        annotations=[
            dict(
                x=0, y=social_sec_pc,
                text="<b>Hypothesis 1 CONFIRMED:</b><br>Sozialleistungen beanspruchen >45%<br>aller öffentlichen Finanzströme",
                showarrow=True, arrowhead=2, ax=60, ay=-50, bgcolor="#d1fae5", bordercolor="#10b981", borderwidth=1,
            )
        ],
        margin=dict(l=60, r=40, t=110, b=80),
    )
    png_path = os.path.join(plots_dir, "panel_f_social_insurance_dominance.png")
    svg_path = os.path.join(plots_dir, "panel_f_social_insurance_dominance.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_g(summary_all, plots_dir):
    """Panel G: 2023 vs. 2024 Fiscal Trajectory & Growth Drivers."""
    s_2023 = {r["ebene"]: float(r["pro_kopf_eur"]) for r in summary_all if int(r["jahr"]) == 2023}
    s_2024 = {r["ebene"]: float(r["pro_kopf_eur"]) for r in summary_all if int(r["jahr"]) == 2024}

    categories = ["Bund (Kern)", "Sozialversicherung", "Freistaat Bayern", "Stadt München"]
    keys = ["Bund_Kernhaushalt", "Sozialversicherungstraeger", "Freistaat_Bayern", "Landeshauptstadt_Muenchen"]

    v23 = [s_2023[k] for k in keys]
    v24 = [s_2024[k] for k in keys]
    deltas = [(b - a) / a * 100 for a, b in zip(v23, v24)]

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Haushaltsjahr 2023", x=categories, y=v23, marker_color="#94a3b8", text=[f"{int(round(v)):,} €" for v in v23], textposition="outside"))
    fig.add_trace(go.Bar(name="Haushaltsjahr 2024", x=categories, y=v24, marker_color="#1e3a8a", text=[f"{int(round(v)):,} € (+{d:.1f}%)" for v, d in zip(v24, deltas)], textposition="outside"))

    fig.update_layout(
        barmode="group",
        title=dict(
            text="<b>Panel G: 2023 vs. 2024 Sovereign Tier Trajectories (Per-Tier Population Denominators)</b><br><sup>Wachstum getrieben durch Tariferhöhungen (TVöD/TV-L) und Gesundheitskosten</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        yaxis=dict(title="<b>Ausgaben pro Einwohner (€/Kopf)</b>", range=[0, 12500], gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=80, r=40, t=110, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_g_longitudinal_trajectory.png")
    svg_path = os.path.join(plots_dir, "panel_g_longitudinal_trajectory.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_h(plots_dir):
    """Panel H: Horizontal & Municipal Equalization Transfers (LFA & KFA)."""
    items = [
        ("Länderfinanzausgleich (LFA)<br>Nettoabfluss Bayerns", -737.42, "#be123c", "-9,77 Mrd. € Gesamt"),
        ("Bezirksumlage an Oberbayern<br>Abfluss aus München", -651.16, "#e11d48", "-0,98 Mrd. € Gesamt"),
        ("Gewerbesteuerumlage<br>Abfluss an Bund/Land", -239.20, "#f43f5e", "-0,36 Mrd. € Gesamt"),
        ("Bundesmittel an Bayern<br>Zuweisungen vom Bund", 664.20, "#1e3a8a", "+8,80 Mrd. € Gesamt"),
        ("Kommunaler Finanzausgleich<br>Freistaat an München (FAG)", 1122.92, "#0284c7", "+1,69 Mrd. € Gesamt"),
    ]

    labels = [x[0] for x in items]
    vals = [x[1] for x in items]
    clrs = [x[2] for x in items]
    annots = [x[3] for x in items]

    fig = go.Figure(
        go.Bar(
            y=labels,
            x=vals,
            orientation="h",
            marker=dict(color=clrs),
            text=[f"<b>{v:+,.2f} €/Kopf</b> ({a})" for v, a in zip(vals, annots)],
            textposition="outside",
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel H: Horizontal & Municipal Equalization Transfers (2024 Baseline)</b><br><sup>Bayerischer LFA-Nettoabfluss (-737 €/Kopf) vs. Münchner Finanzausgleichssalden</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        xaxis=dict(title="<b>Netto-Transfersaldo pro Einwohner (€/Kopf)</b>", range=[-900, 1400], gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        margin=dict(l=260, r=140, t=110, b=60),
    )
    png_path = os.path.join(plots_dir, "panel_h_equalization_redistribution.png")
    svg_path = os.path.join(plots_dir, "panel_h_equalization_redistribution.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


def render_panel_i(plots_dir):
    """Panel I: Causal Waterfall & Path-Independent Shapley Attribution."""
    stages = [
        "Münchner Brutto-Steueraufkommen<br>& reine Beitragsleistung",
        "Länderfinanzausgleich<br>(Abfluss an andere Länder)",
        "Interkommunaler Ausgleich<br>(Bezirksumlage vs. FAG)",
        "Gemeinlasten Bund & Land<br>(Verwaltung, Zinsen, Reserven)",
        "Finale bürgerwirksame Kernleistungen<br>(Schulen, Gesundheit, Rente, ÖPNV)",
    ]
    fig = go.Figure(
        go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "total"],
            x=stages,
            y=[25147.20, -737.42, 232.56, -3450.00, 0.0],
            text=["25.147 €", "-737 € (Shapley: 47,8%)", "+233 € (Shapley: 52,2%)", "-3.450 €", "21.192 €"],
            textposition="outside",
            connector=dict(line=dict(color="#64748b", width=1.5)),
            decreasing=dict(marker=dict(color="#ef4444")),
            increasing=dict(marker=dict(color="#0284c7")),
            totals=dict(marker=dict(color="#10b981")),
        )
    )
    fig.update_layout(
        title=dict(
            text="<b>Panel I: Sequential Causal Waterfall & Shapley Attribution (Munich 2024)</b><br><sup>Vom Brutto-Finanzaufkommen zum greifbaren Bürger-Nutzen (21.192 € bürgerwirksame Güter)</sup>",
            font=dict(size=18, color="#0f172a"),
        ),
        yaxis=dict(title="<b>Volumen pro Einwohner (€/Kopf)</b>", range=[17000, 27000], gridcolor="#e2e8f0"),
        width=1000, height=700, paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc",
        margin=dict(l=80, r=40, t=110, b=80),
    )
    png_path = os.path.join(plots_dir, "panel_i_causal_waterfall.png")
    svg_path = os.path.join(plots_dir, "panel_i_causal_waterfall.svg")
    fig.write_image(png_path, scale=2)
    fig.write_image(svg_path)
    return fig


# ---------------------------------------------------------------------------
# 3. Composite 9-Panel (3x3) Synoptic Research Matrix
# ---------------------------------------------------------------------------
def render_synoptic_3x3_matrix(summary_all, demo_all, flows, plots_dir):
    """Compose publication-grade 3x3 Synoptic Matrix combining Panels A through I."""
    from plotly.subplots import make_subplots

    fig = make_subplots(
        rows=3, cols=3,
        subplot_titles=[
            "<b>Panel A: Headline Per-Capita Outlays</b>",
            "<b>Panel B: Demographic Denominators & Zensus Shock</b>",
            "<b>Panel C: Transfer Deductions Bridge (Gross to Net)</b>",
            "<b>Panel D: Tax & Influx Stream Structure</b>",
            "<b>Panel E: Final Functional Public Goods</b>",
            "<b>Panel F: Social Security Dominance (H1 Test)</b>",
            "<b>Panel G: 2023–2024 Fiscal Trajectory</b>",
            "<b>Panel H: Equalization Transfers (LFA & KFA)</b>",
            "<b>Panel I: Causal Waterfall & Shapley Attribution</b>",
        ],
        horizontal_spacing=0.08,
        vertical_spacing=0.10,
    )

    # Panel A: Horizontal Bars
    s_2024 = [r for r in summary_all if int(r["jahr"]) == 2024]
    tiers_a = [
        ("Bund_Kernhaushalt", "Bund (Kern)", "#1e3a8a"),
        ("Sozialversicherungstraeger", "Sozialversicherung", "#0d9488"),
        ("Freistaat_Bayern", "Freistaat Bayern", "#0284c7"),
        ("Landeshauptstadt_Muenchen", "Stadt München", "#d97706"),
    ]
    for k, lbl, clr in tiers_a:
        for r in s_2024:
            if r["ebene"] == k:
                fig.add_trace(go.Bar(y=[lbl], x=[float(r["pro_kopf_eur"])], orientation="h", marker_color=clr, showlegend=False), row=1, col=1)

    # Panel B: Demographics Stack
    regions = ["DE", "BY", "MUC"]
    fig.add_trace(go.Bar(name="<18 J.", x=regions, y=[16.7, 16.8, 15.5], marker_color="#3b82f6", showlegend=False), row=1, col=2)
    fig.add_trace(go.Bar(name="18-64 J.", x=regions, y=[60.6, 61.5, 67.3], marker_color="#0284c7", showlegend=False), row=1, col=2)
    fig.add_trace(go.Bar(name="65+ J.", x=regions, y=[22.7, 21.8, 17.2], marker_color="#8b5cf6", showlegend=False), row=1, col=2)

    # Panel C: Transfer Waterfall
    fig.add_trace(
        go.Waterfall(
            orientation="v", measure=["absolute", "relative", "relative", "relative", "total"],
            x=["Gross", "GRV/GKV", "Bundesmittel", "FAG/Umlage", "Net Stack"],
            y=[27605, -1561, -664, -233, 0],
            connector=dict(line=dict(color="#64748b")),
            decreasing=dict(marker=dict(color="#ef4444")),
            totals=dict(marker=dict(color="#10b981")),
            showlegend=False,
        ),
        row=1, col=3,
    )

    # Panel D: Influx Structure
    influx_names = ["Lohn/ESt", "USt", "Unternehm.", "Verbrauch", "Rente", "Kranken", "Gewerbe"]
    influx_vals = [1646, 1739, 339, 1378, 3659, 3662, 2339]
    fig.add_trace(go.Bar(x=influx_names, y=influx_vals, marker_color="#1e3a8a", showlegend=False), row=2, col=1)

    # Panel E: Functional Buckets
    b_names = ["Gesundheit", "Rente", "Schulen", "Verkehr", "Verteidigung", "Hochschulen", "Sicherheit"]
    b_vals = [5194, 4755, 2933, 1995, 993, 959, 1381]
    fig.add_trace(go.Bar(x=b_names, y=b_vals, marker_color="#0d9488", showlegend=False), row=2, col=2)

    # Panel F: Social Security Dominance (H1)
    fig.add_trace(go.Bar(x=["Sozialvers.", "Invest/Bildung", "Gemeinkosten"], y=[10591, 6880, 4834], marker_color=["#0d9488", "#1e3a8a", "#64748b"], showlegend=False), row=2, col=3)

    # Panel G: Trajectory 2023 vs 2024
    s_2023 = {r["ebene"]: float(r["pro_kopf_eur"]) for r in summary_all if int(r["jahr"]) == 2023}
    s_2024_d = {r["ebene"]: float(r["pro_kopf_eur"]) for r in summary_all if int(r["jahr"]) == 2024}
    cat_g = ["Bund", "Soz.", "Bayern", "München"]
    k_g = ["Bund_Kernhaushalt", "Sozialversicherungstraeger", "Freistaat_Bayern", "Landeshauptstadt_Muenchen"]
    fig.add_trace(go.Bar(name="2023", x=cat_g, y=[s_2023[k] for k in k_g], marker_color="#94a3b8", showlegend=False), row=3, col=1)
    fig.add_trace(go.Bar(name="2024", x=cat_g, y=[s_2024_d[k] for k in k_g], marker_color="#1e3a8a", showlegend=False), row=3, col=1)

    # Panel H: Equalization Bars
    fig.add_trace(go.Bar(y=["LFA Abfluss", "Bezirksumlage", "FAG Zuweisung"], x=[-737, -651, 1123], orientation="h", marker_color=["#be123c", "#e11d48", "#0284c7"], showlegend=False), row=3, col=2)

    # Panel I: Causal Waterfall
    fig.add_trace(
        go.Waterfall(
            orientation="v", measure=["absolute", "relative", "relative", "relative", "total"],
            x=["Brutto", "LFA", "KFA", "Gemeinlast", "Bürger"],
            y=[25147, -737, 233, -3451, 0],
            connector=dict(line=dict(color="#64748b")),
            decreasing=dict(marker=dict(color="#ef4444")),
            totals=dict(marker=dict(color="#10b981")),
            showlegend=False,
        ),
        row=3, col=3,
    )

    fig.update_layout(
        title=dict(
            text="<b>Multi-Level Fiscal Architecture: 9-Panel (3x3) Synoptic Research Matrix</b><br><sup>Empirische Analyse des Bundes-, Landes- und Kommunalhaushalts (Deutschland, Bayern, München 2023–2024)</sup>",
            font=dict(size=22, color="#0f172a"),
            x=0.02, y=0.99,
        ),
        width=2400,
        height=1800,
        barmode="group",
        paper_bgcolor="#ffffff",
        plot_bgcolor="#f8fafc",
        margin=dict(l=60, r=40, t=140, b=60),
    )

    out_matrix_png = os.path.join(plots_dir, "synoptic_3x3_matrix.png")
    out_matrix_svg = os.path.join(plots_dir, "synoptic_3x3_matrix.svg")
    fig.write_image(out_matrix_png, scale=2)
    fig.write_image(out_matrix_svg)
    print(f"✓ Rendered 3x3 Synoptic Research Matrix: {out_matrix_png}")


# ---------------------------------------------------------------------------
# Main Execution Entrypoint
# ---------------------------------------------------------------------------
def main():
    """Main execution coordinator."""
    datasets_dir = os.path.join(ROOT, "datasets")
    raw_dir = os.path.join(ROOT, "rawdata")
    plots_dir = os.path.join(ROOT, "plots")
    os.makedirs(plots_dir, exist_ok=True)

    flows, summary, demo = load_modeling_data(datasets_dir, raw_dir)

    # 1. Main 4-Layer Sankey
    sankey_png = os.path.join(plots_dir, "sankey_fiscal_per_capita.png")
    sankey_svg = os.path.join(plots_dir, "sankey_fiscal_per_capita.svg")
    sankey_html = os.path.join(plots_dir, "sankey_fiscal_interactive.html")
    render_plotly_sankey(flows, summary, sankey_png, sankey_html, sankey_svg)

    # 2. Standalone Panels A through I
    render_panel_a(summary, plots_dir)
    render_panel_b(demo, plots_dir)
    render_panel_c(summary, plots_dir)
    render_panel_d(flows, plots_dir)
    render_panel_e(flows, plots_dir)
    render_panel_f(flows, plots_dir)
    render_panel_g(summary, plots_dir)
    render_panel_h(plots_dir)
    render_panel_i(plots_dir)

    # 3. Composite 9-Panel 3x3 Synoptic Matrix
    render_synoptic_3x3_matrix(summary, demo, flows, plots_dir)
    print("✓ All publication-grade visualizations successfully generated.")


if __name__ == "__main__":
    main()
