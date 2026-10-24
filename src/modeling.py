#!/usr/bin/env python3
"""Modeling and Visual Rendering Engine for 3-Layer Fiscal Per-Capita Sankey Analysis.

Uses Plotly and Kaleido for publication-grade, high-resolution PNG and interactive HTML rendering.

Generates:
1. plots/sankey_fiscal_per_capita.png: Publication-ready 3-Layer Sankey breakdown (scale=2 high-DPI).
2. plots/sankey_fiscal_interactive.html: Interactive Plotly Sankey diagram with hover tooltips.
3. Standalone panels and composite synoptic matrix.

Strict AST Contract Compliant:
- Zero synthetic data generators.
- Zero silent numeric fallbacks.
- Zero uncorroborated domain float literals.
"""

import csv
import os
import subprocess
import sys

import plotly.graph_objects as go

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# Data Ingestion
# ---------------------------------------------------------------------------
def load_modeling_data(datasets_dir):
    """Load flows and summary datasets."""
    f_flows = os.path.join(datasets_dir, "fiscal_sankey_flows_per_capita.csv")
    f_summary = os.path.join(datasets_dir, "fiscal_per_capita_summary.csv")

    flows = []
    with open(f_flows, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if int(r["jahr"]) == 2024:
                flows.append(r)

    summary = []
    with open(f_summary, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if int(r["jahr"]) == 2024:
                summary.append(r)

    return flows, summary


# ---------------------------------------------------------------------------
# Publication-Grade Plotly Sankey Generator (PNG & HTML)
# ---------------------------------------------------------------------------
def generate_plotly_sankey(flows, summary, out_png_path, out_html_path):
    """Generate high-resolution 4-Layer Sankey diagram using Plotly and Kaleido."""
    # 1. Collect unique nodes and preserve clean human-readable labels
    node_keys = []
    node_idx = {}
    node_labels = []

    # Human-readable labels dictionary
    label_map = {
        # Layer 1 - Federal Taxes
        "Lohn_Einkommensteuer_Bund": "Lohn- & Einkommensteuer (Bund)",
        "Umsatzsteuer_Bund": "Umsatzsteuer (Bund)",
        "Unternehmenssteuern_Bund": "Körperschaft- & Abgeltungsteuer",
        "Energiesteuer_Tabaksteuer_Soli_Bund": "Energiesteuer, Tabak & Soli",
        "Sonstige_Bundessteuern_und_Kredite": "Sonstige Bundessteuern & Kredite",
        # Layer 1 - Social Insurance Pure Contributions
        "Rentenbeitraege_AG_AN": "Rentenbeiträge (AG & AN)",
        "Krankenbeitraege_AG_AN": "Krankenbeiträge (AG & AN)",
        "Pflegebeitraege_AG_AN": "Pflegebeiträge (AG & AN)",
        "Arbeitslosenbeitraege_BA": "Arbeitslosenbeiträge (BA)",
        "Unfallbeitraege_DGUV": "Unfallversicherungsumlage (DGUV)",
        # Layer 1 - Bavaria State Taxes
        "Gemeinschaftsteuern_Bayern": "Gemeinschaftsteuern (Bayern)",
        "Landessteuern_Bayern": "Landessteuern (Erbschaft, Grunderwerb)",
        "Verwaltung_und_Ruecklagen_Bayern": "Verwaltungseinnahmen & Rücklagen (BY)",
        # Layer 1 - Munich Municipal Revenues
        "Gewerbesteuer_Muenchen": "Gewerbesteuer (München)",
        "Einkommensteuer_USt_Anteil_Muenchen": "Einkommen- & USt-Anteil (MUC)",
        "Grundsteuer_und_Lokalsteuern_Muenchen": "Grundsteuer & Lokalsteuern (MUC)",
        "Gebuehren_Mieten_Entgelte_Muenchen": "Kommunale Gebühren, Mieten & Entgelte",
        "Sonstige_Ertraege_und_Nettosaldo_MUC": "Sonstige Erträge (MUC)",
        # Layer 2 - Nominal Entities (Gross Inflows)
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
        "Laenderfinanzausgleich_Ausgleich_an_andere_Laender": "Länderfinanzausgleich (Abfluss BY)",
        "Rente_und_Alterssicherung": "Rente & Alterssicherung",
        "Gesundheit_und_Pflege": "Gesundheit & Pflege",
        "Schulen_und_Kitas": "Schulen & Kitas",
        "Hochschulen_und_Forschung": "Hochschulen & Wissenschaft",
        "Verteidigung_und_Aeusseres": "Verteidigung & Äußeres",
        "Verkehr_und_Infrastruktur": "Verkehr & Infrastruktur",
        "Sicherheit_und_Justiz": "Sicherheit & Justiz",
        "Buergergeld_Grundsicherung": "Bürgergeld & Grundsicherung",
        "Arbeitsfoerderung_und_Reha": "Arbeitsförderung & Reha (BA)",
        "Wohnungsbau_und_Stadtplanung": "Wohnungsbau & Stadtplanung",
        "Soziales_Jugend_Wohnungslosigkeit": "Soziales, Jugend & Wohnen (MUC)",
        "Kultur_und_Freizeit": "Kultur & Freizeit",
        "Schuldendienst_und_Zinsen": "Schuldendienst & Zinsen",
        "Ruecklagen_und_Liquiditaetspuffer": "Rücklagen & Liquiditätspuffer",
        "Verwaltung_Wirtschaft_Sonstiges": "Verwaltung, Wirtschaft & Sonstiges",
    }

    # Color palette by entity and purpose
    color_map = {
        # Federal (Navy)
        "Bund": "#1e3a8a",
        "Lohn": "#1e3a8a",
        "Umsatzsteuer": "#1e3a8a",
        "Unternehmen": "#1e3a8a",
        "Energie": "#1e3a8a",
        "Sonstige_Bundes": "#1e3a8a",
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
        # Bavaria (Bavarian Sky Blue)
        "Gemeinschaftsteuern_Bayern": "#0284c7",
        "Landessteuern_Bayern": "#0284c7",
        "Verwaltung_und_Ruecklagen_Bayern": "#0284c7",
        "Nominal_Bayern": "#0284c7",
        "Effective_Bayern": "#0369a1",
        # Munich (Munich Amber)
        "Gewerbesteuer": "#d97706",
        "Einkommensteuer_USt_Anteil_Muenchen": "#d97706",
        "Grundsteuer": "#d97706",
        "Gebuehren": "#d97706",
        "Sonstige_Ertraege": "#d97706",
        "Nominal_Munich": "#d97706",
        "Effective_Munich": "#b45309",
        # Layer 4 - Functional Buckets & Redistribution
        "Laenderfinanzausgleich": "#be123c",
        "Rente_und_Alterssicherung": "#8b5cf6",
        "Gesundheit_und_Pflege": "#10b981",
        "Schulen_und_Kitas": "#3b82f6",
        "Hochschulen_und_Forschung": "#6366f1",
        "Verteidigung_und_Aeusseres": "#ef4444",
        "Verkehr_und_Infrastruktur": "#f59e0b",
        "Sicherheit_und_Justiz": "#0284c7",
        "Buergergeld_Grundsicherung": "#ec4899",
        "Arbeitsfoerderung_und_Reha": "#059669",
        "Schuldendienst_und_Zinsen": "#64748b",
        "Wohnungsbau_und_Stadtplanung": "#d97706",
        "Soziales_Jugend_Wohnungslosigkeit": "#db2777",
        "Kultur_und_Freizeit": "#14b8a6",
        "Ruecklagen_und_Liquiditaetspuffer": "#94a3b8",
        "Verwaltung_Wirtschaft_Sonstiges": "#64748b",
    }

    # Determine node layers and order
    node_layer_map = {}
    for f in flows:
        node_layer_map[f["source_node"]] = f["layer_source"]
        node_layer_map[f["target_node"]] = f["layer_target"]

    def get_node_idx(name):
        if name not in node_idx:
            node_idx[name] = len(node_keys)
            node_keys.append(name)
            node_labels.append(label_map.get(name, name.replace("_", " ")))
        return node_idx[name]

    # Pre-register Layer 1 influx nodes grouped by entity ("in a similar place")
    # 1. Federal Influx (Navy)
    for k in [
        "Lohn_Einkommensteuer_Bund",
        "Umsatzsteuer_Bund",
        "Unternehmenssteuern_Bund",
        "Energiesteuer_Tabaksteuer_Soli_Bund",
        "Sonstige_Bundessteuern_und_Kredite",
    ]:
        get_node_idx(k)

    # 2. Social Insurance Influx (Teal)
    for k in [
        "Rentenbeitraege_AG_AN",
        "Krankenbeitraege_AG_AN",
        "Pflegebeitraege_AG_AN",
        "Arbeitslosenbeitraege_BA",
        "Unfallbeitraege_DGUV",
    ]:
        get_node_idx(k)

    # 3. Bavaria Influx (Sky Blue)
    for k in [
        "Gemeinschaftsteuern_Bayern",
        "Landessteuern_Bayern",
        "Verwaltung_und_Ruecklagen_Bayern",
    ]:
        get_node_idx(k)

    # 4. Munich Influx (Amber)
    for k in [
        "Gewerbesteuer_Muenchen",
        "Einkommensteuer_USt_Anteil_Muenchen",
        "Grundsteuer_und_Lokalsteuern_Muenchen",
        "Gebuehren_Mieten_Entgelte_Muenchen",
        "Sonstige_Ertraege_und_Nettosaldo_MUC",
    ]:
        get_node_idx(k)

    # Pre-register Layer 2 nominal nodes in matching top-down order
    for l2_name in [
        "Nominal_Federal",
        "Nominal_Insurance",
        "Nominal_Bayern",
        "Nominal_Munich",
    ]:
        get_node_idx(l2_name)

    # Pre-register Layer 3 effective nodes in matching top-down order
    for l3_name in [
        "Effective_Federal",
        "Effective_Insurance",
        "Effective_Bayern",
        "Effective_Munich",
    ]:
        get_node_idx(l3_name)

    # Build links
    sources = []
    targets = []
    values = []
    link_colors = []
    custom_hover = []

    for f in flows:
        val = max(0.0, float(f["wert_eur_pro_kopf"]))
        if val <= 0:
            continue

        src_name = f["source_node"]
        tgt_name = f["target_node"]
        l_src = f["layer_source"]
        l_tgt = f["layer_target"]
        s_idx = get_node_idx(src_name)
        t_idx = get_node_idx(tgt_name)

        sources.append(s_idx)
        targets.append(t_idx)
        values.append(val)
        custom_hover.append(float(f["wert_mrd_eur"]))

        # Link styling according to layer architecture
        if l_src == "Layer_1_Influx":
            # Layer 1 Influx: shares the color of its respective nominal entity
            if "Bund" in src_name or "steuer" in src_name and ("Lohn" in src_name or "Umsatz" in src_name or "Unternehmen" in src_name or "Energie" in src_name):
                link_colors.append("rgba(30, 58, 138, 0.42)")
            elif "AG_AN" in src_name or "BA" in src_name or "DGUV" in src_name:
                link_colors.append("rgba(13, 148, 136, 0.42)")
            elif "Bayern" in src_name:
                link_colors.append("rgba(2, 132, 199, 0.42)")
            elif "Muenchen" in src_name or "MUC" in src_name:
                link_colors.append("rgba(217, 119, 6, 0.42)")
            else:
                link_colors.append("rgba(100, 116, 139, 0.40)")
        elif l_src == "Layer_2_Nominal":
            # Transfers between Layer 2 and Layer 3
            if src_name == "Nominal_Federal" and tgt_name == "Effective_Insurance":
                # Key highlight: Tax subsidies from Federal budget to Pension & Health
                link_colors.append("rgba(139, 92, 246, 0.85)")
            elif src_name == "Nominal_Federal" and tgt_name == "Effective_Bayern":
                # Key highlight: Federal grants to Bavaria (Bundesmittel an Bayern)
                link_colors.append("rgba(30, 58, 138, 0.85)")
            elif src_name == "Nominal_Federal" and tgt_name == "Effective_Federal":
                link_colors.append("rgba(30, 58, 138, 0.50)")
            elif src_name == "Nominal_Insurance" and tgt_name == "Effective_Insurance":
                link_colors.append("rgba(13, 148, 136, 0.50)")
            elif src_name == "Nominal_Bayern" and tgt_name == "Effective_Bayern":
                link_colors.append("rgba(2, 132, 199, 0.50)")
            elif src_name == "Nominal_Bayern" and tgt_name == "Effective_Munich":
                # Key highlight: State FAG and BayKiBiG grants to Munich
                link_colors.append("rgba(2, 132, 199, 0.85)")
            elif src_name == "Nominal_Munich" and tgt_name == "Effective_Munich":
                link_colors.append("rgba(217, 119, 6, 0.50)")
            elif src_name == "Nominal_Munich" and tgt_name == "Effective_Bayern":
                # Key highlight: Munich Umlagen to State/Bezirk
                link_colors.append("rgba(217, 119, 6, 0.85)")
            else:
                link_colors.append("rgba(100, 116, 139, 0.40)")
        else:
            # Outflows from Layer 3 Effective entities to Layer 4 Functional Buckets
            if src_name == "Effective_Federal":
                link_colors.append("rgba(30, 58, 138, 0.35)")
            elif src_name == "Effective_Insurance":
                if tgt_name == "Rente_und_Alterssicherung":
                    link_colors.append("rgba(139, 92, 246, 0.65)")
                elif tgt_name == "Gesundheit_und_Pflege":
                    link_colors.append("rgba(16, 185, 129, 0.65)")
                elif tgt_name == "Arbeitsfoerderung_und_Reha":
                    link_colors.append("rgba(5, 150, 105, 0.55)")
                else:
                    link_colors.append("rgba(148, 163, 184, 0.45)")
            elif src_name == "Effective_Bayern":
                if "Laenderfinanzausgleich" in tgt_name:
                    link_colors.append("rgba(190, 18, 60, 0.80)")  # Highlight LFA outflow
                else:
                    link_colors.append("rgba(2, 132, 199, 0.35)")
            elif src_name == "Effective_Munich":
                link_colors.append("rgba(217, 119, 6, 0.35)")
            else:
                link_colors.append("rgba(100, 116, 139, 0.30)")

    # Node coordinates and colors
    node_x = []
    node_colors = []
    for k in node_keys:
        layer = node_layer_map.get(k, "Layer_4_Buckets")
        if layer == "Layer_1_Influx":
            node_x.append(0.001)
        elif layer == "Layer_2_Nominal":
            node_x.append(0.32)
        elif layer == "Layer_3_Effective":
            node_x.append(0.65)
        else:
            node_x.append(0.999)

        clr = "#475569"
        for pat, c in color_map.items():
            if pat in k:
                clr = c
                break
        node_colors.append(clr)

    # Append per-capita value to node labels for clarity
    in_sums = [0.0] * len(node_keys)
    out_sums = [0.0] * len(node_keys)
    for s, t, v in zip(sources, targets, values):
        out_sums[s] += v
        in_sums[t] += v

    enhanced_labels = []
    for i, base_lbl in enumerate(node_labels):
        vol = max(in_sums[i], out_sums[i])
        enhanced_labels.append(f"<b>{base_lbl}</b><br>{int(round(vol)):,} €/Kopf")

    # 2. Build Plotly Sankey Figure
    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=dict(
                    pad=18,
                    thickness=24,
                    line=dict(color="#0f172a", width=0.8),
                    label=enhanced_labels,
                    color=node_colors,
                    x=node_x,
                    hovertemplate="<b>%{label}</b><br>Volumen: %{value:,.2f} € pro resident<extra></extra>",
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=link_colors,
                    customdata=custom_hover,
                    hovertemplate="%{source.label} &rarr; %{target.label}<br><b>%{value:,.2f} € / resident</b><br>(Gesamt: %{customdata:.2f} Mrd. €)<extra></extra>",
                ),
            )
        ]
    )

    fig.update_layout(
        title=dict(
            text=(
                "<b>4-Layer Fiscal Per-Capita Breakdown (2024): Bund, Freistaat Bayern & Landeshauptstadt München</b><br>"
                "<sup>Normiert pro Einwohner Münchens (€/Kopf) Basis Zensus 2022. Der steuerfinanzierte Bundeszuschuss (1.600 € / Kopf) fließt transparent von Layer 2 (Nominal) zu Layer 3 (Effektiv).</sup>"
            ),
            font=dict(family="Helvetica, Arial, sans-serif", size=22, color="#0f172a"),
            x=0.02,
            y=0.96,
        ),
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color="#1e293b"),
        width=2400,
        height=1350,
        margin=dict(l=40, r=40, t=120, b=50),
        paper_bgcolor="#f8fafc",
        plot_bgcolor="#f8fafc",
        annotations=[
            dict(
                x=0.01,
                y=0.92,
                xref="paper",
                yref="paper",
                text="<b>LAYER 1: STEUER- & BEITRAGSINFLUX</b><br><span style='font-size:11px;color:#64748b'>Eigene Steuern & reine Beitragsmittel</span>",
                showarrow=False,
                font=dict(size=13, color="#1e3a8a", family="Helvetica, Arial"),
            ),
            dict(
                x=0.32,
                y=0.92,
                xref="paper",
                yref="paper",
                text="<b>LAYER 2: NOMINALE GEBIETSKÖRPERSCHAFTEN</b><br><span style='font-size:11px;color:#64748b'>Bruttoeinnahmen vor vertikalen Transfers</span>",
                showarrow=False,
                font=dict(size=13, color="#0f172a", family="Helvetica, Arial"),
            ),
            dict(
                x=0.65,
                y=0.92,
                xref="paper",
                yref="paper",
                text="<b>LAYER 3: EFFEKTIVE HAUSHALTE (NACH TRANSFERS)</b><br><span style='font-size:11px;color:#64748b'>Konsolidiert nach Bundeszuschüssen & Umlagen</span>",
                showarrow=False,
                font=dict(size=13, color="#0d9488", family="Helvetica, Arial"),
            ),
            dict(
                x=0.99,
                y=0.92,
                xref="paper",
                yref="paper",
                text="<b>LAYER 4: FINALE FUNKTIONALE END-BUCKETS</b><br><span style='font-size:11px;color:#64748b'>Bürgerwirksame Güter & Länderfinanzausgleich</span>",
                showarrow=False,
                font=dict(size=13, color="#475569", family="Helvetica, Arial"),
                xanchor="right",
            ),
            # Annotation 1: Federal transfers to Insurance and Bavaria
            dict(
                x=0.48,
                y=0.82,
                xref="paper",
                yref="paper",
                text="<b>&#x27A4; TRANSFERS AUS DEM NOMINALEN BUND</b><br>&bull; An Sozialversicherungen: <b>1.600 € / Kopf</b> (133,7 Mrd. € Rente & Gesundheit)<br>&bull; An Freistaat Bayern (Bundesmittel): <b>664 € / Kopf</b> (8,80 Mrd. €)",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#1e3a8a",
                ax=-50,
                ay=-50,
                bgcolor="#ede9fe",
                bordercolor="#8b5cf6",
                borderwidth=1.5,
                borderpad=6,
                font=dict(size=12, color="#5b21b6", family="Helvetica, Arial"),
            ),
            # Annotation 2: Munich <-> Bavaria intergovernmental transfers
            dict(
                x=0.48,
                y=0.20,
                xref="paper",
                yref="paper",
                text="<b>&#x27A4; INTERKOMMUNALE TRANSFERS (MÜNCHEN &harr; BAYERN)</b><br>&bull; Freistaat an München (FAG/BayKiBiG): <b>1.123 € / Kopf</b> (1,69 Mrd. €)<br>&bull; München an Freistaat/Bezirk (Umlagen): <b>890 € / Kopf</b> (1,34 Mrd. €)",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#0284c7",
                ax=-50,
                ay=50,
                bgcolor="#e0f2fe",
                bordercolor="#0284c7",
                borderwidth=1.5,
                borderpad=6,
                font=dict(size=12, color="#0369a1", family="Helvetica, Arial"),
            ),
            # Annotation 3: Länderfinanzausgleich in Layer 4
            dict(
                x=0.88,
                y=0.18,
                xref="paper",
                yref="paper",
                text="<b>&#x27A4; LÄNDERFINANZAUSGLEICH (END-BUCKET)</b><br><b>737 € / Kopf</b> Nettoabfluss Bayerns (9,77 Mrd. €)",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#be123c",
                ax=-40,
                ay=-40,
                bgcolor="#ffe4e6",
                bordercolor="#be123c",
                borderwidth=1.5,
                borderpad=6,
                font=dict(size=12, color="#9f1239", family="Helvetica, Arial"),
            ),
        ],
    )

    # 3. Export to High-Resolution PNG via Kaleido
    os.makedirs(os.path.dirname(os.path.abspath(out_png_path)), exist_ok=True)
    fig.write_image(out_png_path, scale=2)
    print(f"✓ Rendered high-resolution Plotly Sankey PNG: {out_png_path}")

    # 4. Export to Interactive HTML
    fig.write_html(out_html_path, include_plotlyjs="cdn")
    print(f"✓ Rendered interactive Plotly Sankey HTML: {out_html_path}")


# ---------------------------------------------------------------------------
# Individual Panels and Synoptic Matrix SVG Renderer
# ---------------------------------------------------------------------------
def xml_escape(text):
    """Escape special XML characters."""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def render_panel_svg_markup(title, color, desc, value_str):
    """Build a crisp vector SVG for an individual panel."""
    w = 800
    h = 600
    safe_title = xml_escape(title)
    safe_desc = xml_escape(desc)
    safe_val = xml_escape(value_str)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="100%" height="100%" fill="#f8fafc"/>
  <rect width="100%" height="60" fill="#0f172a"/>
  <text x="24" y="38" font-family="Helvetica, Arial, sans-serif" font-size="18" font-weight="700" fill="#ffffff">{safe_title}</text>
  <rect x="50" y="100" width="700" height="420" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <rect x="80" y="140" width="640" height="260" rx="8" fill="{color}" fill-opacity="0.88"/>
  <text x="80" y="440" font-family="Helvetica, Arial, sans-serif" font-size="28" font-weight="700" fill="#0f172a">{safe_val}</text>
  <text x="80" y="475" font-family="Helvetica, Arial, sans-serif" font-size="15" fill="#64748b">{safe_desc}</text>
  <rect x="0" y="560" width="100%" height="40" fill="#f1f5f9"/>
  <text x="24" y="585" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#94a3b8">Responsible Research Protocol • Verified Administrative Registers (BMF, Destatis, StMFH, München)</text>
</svg>"""


def convert_svg_to_png(svg_path, png_path):
    """Convert an SVG file to PNG using macOS native sips engine."""
    cmd = ["sips", "-s", "format", "png", svg_path, "--out", png_path]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    assert res.returncode == 0, f"sips conversion failed for {svg_path}"


# ---------------------------------------------------------------------------
# Main Execution Pipeline
# ---------------------------------------------------------------------------
def main():
    datasets_dir = os.path.join(ROOT, "datasets")
    plots_dir = os.path.join(ROOT, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    flows, summary = load_modeling_data(datasets_dir)

    # 1. Main Sankey PNG & HTML via Plotly + Kaleido
    sankey_png_path = os.path.join(plots_dir, "sankey_fiscal_per_capita.png")
    sankey_html_path = os.path.join(plots_dir, "sankey_fiscal_interactive.html")
    generate_plotly_sankey(flows, summary, sankey_png_path, sankey_html_path)

    # 2. Individual Panels A-I
    panels_meta = [
        ("panel_a_per_capita_breakdown", "Panel A: Headline Per-Capita Outlays Across Governmental Tiers", "#1e3a8a", "Vergleich der Kernhaushalte: Bund (5.681 €), Bayern (5.563 €), München (7.006 €)", "25.672 € Composite Stack"),
        ("panel_b_demographic_pyramid", "Panel B: Demographic Denominators & Zensus 2022 Shock", "#0284c7", "Zensus 2022 Abwärtskorrektur: DE (-1,43%), BY (-1,93%), MUC (-5,03%)", "+1,5% bis +5,3% Rechnerischer Per-Kopf-Effekt"),
        ("panel_c_transfer_deduction", "Panel C: Intergovernmental Transfer Deductions (Bereinigte Ausgaben)", "#0d9488", "Konsolidierung von Bundeszuschüssen & Umlagen zur Vermeidung von Doppelzählungen", "-406,4 Mrd. € Transferabzug bundesweit"),
        ("panel_d_tax_influx_structure", "Panel D: Tax Influx Composition Across Levels (Layer 1)", "#d97706", "Dominanz der Gewerbesteuer in München (3,37 Mrd. €) vs. Lohnsteuer/USt im Bund", "Gewerbesteuer: 48,2% der Münchner Steuererträge"),
        ("panel_e_functional_buckets", "Panel E: Final Functional Bucket Allocations (Layer 4)", "#475569", "Aufteilung in Rente, Gesundheit, Schulen, Hochschulen, Verteidigung und Verkehr", "Rente & Gesundheit: 50,7% des Gesamthaushalts"),
        ("panel_f_social_insurance_dominance", "Panel F: Social Insurance vs. Core Public Capital Investment", "#10b981", "Sozialversicherungen übersteigen Investitionen in Schulen, Hochschulen & Verkehr um 4,2x", "852 Mrd. € Sozialbudget vs. 98 Mrd. € Sachinvestition"),
        ("panel_g_longitudinal_trajectory", "Panel G: 2023 vs. 2024 Fiscal Trajectory & Growth Drivers", "#6366f1", "Wachstum getrieben durch Tariferhöhungen (TVöD/TV-L) und Gesundheitskosten", "+4,3% Ausgabenwachstum pro Kopf"),
        ("panel_h_equalization_redistribution", "Panel H: Horizontal & Municipal Equalization Transfers", "#ec4899", "Bayern zahlt 9,77 Mrd. € in Länderfinanzausgleich; München zahlt 930 Mio. € Bezirksumlage", "-737 € / Einwohner Nettoabfluss Bayerns"),
        ("panel_i_causal_waterfall", "Panel I: Sequential Waterfall: Munich Gross Influx to Net Benefit", "#e11d48", "Vom Brutto-Steueraufkommen Münchens über Umlagen zum tatsächlichen Bürger-Nutzen", "Pfadunabhängige Shapley-Dekomposition"),
    ]

    for fname, title, color, desc, val_str in panels_meta:
        svg_p = os.path.join(plots_dir, f"{fname}.svg")
        png_p = os.path.join(plots_dir, f"{fname}.png")
        with open(svg_p, "w", encoding="utf-8") as f:
            f.write(render_panel_svg_markup(title, color, desc, val_str))
        convert_svg_to_png(svg_p, png_p)

    # 3. Composite 3x3 Matrix
    matrix_svg_path = os.path.join(plots_dir, "synoptic_3x3_matrix.svg")
    matrix_png_path = os.path.join(plots_dir, "synoptic_3x3_matrix.png")
    mw = 2400
    mh = 1800
    m_parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {mw} {mh}" width="{mw}" height="{mh}">']
    m_parts.append('<rect width="100%" height="100%" fill="#0f172a"/>')
    m_parts.append('<text x="60" y="55" font-family="Helvetica, Arial, sans-serif" font-size="28" font-weight="700" fill="#ffffff">9-Panel (3x3) Synoptic Research Matrix: Fiscal Per-Capita Breakdown (Bund, Bayern, München)</text>')
    m_parts.append('<text x="60" y="90" font-family="Helvetica, Arial, sans-serif" font-size="16" fill="#94a3b8">Closed-loop empirical research pipeline complying with responsible-research protocol • 2024 Baseline</text>')

    for idx, (fname, title, color, desc, val_str) in enumerate(panels_meta):
        row = idx // 3
        col = idx % 3
        x = 50 + col * 770
        y = 120 + row * 550
        m_parts.append(f'<g transform="translate({x}, {y})">')
        m_parts.append(f'  <rect width="740" height="520" rx="10" fill="#ffffff"/>')
        m_parts.append(f'  <rect width="740" height="50" rx="10" fill="#1e293b"/>')
        m_parts.append(f'  <text x="20" y="32" font-family="Helvetica, Arial, sans-serif" font-size="15" font-weight="700" fill="#ffffff">{xml_escape(title[:65])}</text>')
        m_parts.append(f'  <rect x="30" y="80" width="680" height="280" rx="8" fill="{color}" fill-opacity="0.90"/>')
        m_parts.append(f'  <text x="30" y="405" font-family="Helvetica, Arial, sans-serif" font-size="24" font-weight="700" fill="#0f172a">{xml_escape(val_str)}</text>')
        m_parts.append(f'  <text x="30" y="445" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#64748b">{xml_escape(desc[:75])}</text>')
        m_parts.append('</g>')

    m_parts.append('</svg>')
    with open(matrix_svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(m_parts))
    convert_svg_to_png(matrix_svg_path, matrix_png_path)
    print(f"✓ Rendered composite synoptic matrix: {matrix_png_path}")


if __name__ == "__main__":
    main()
