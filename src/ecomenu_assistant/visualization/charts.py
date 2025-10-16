"""
Module de visualisation avec Plotly
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Optional


def create_group_impact_chart(data: pd.DataFrame) -> go.Figure:
    """
    Crée un graphique en barres des impacts moyens par groupe d'aliments.

    Args:
        data: DataFrame des statistiques par groupe (résultat de analyze_by_group)

    Returns:
        Figure Plotly
    """
    fig = px.bar(
        data.reset_index(),
        x="Moyenne",
        y="Groupe d'aliment",
        orientation="h",
        title="Impact carbone moyen par groupe d'aliments",
        labels={"Moyenne": "Impact CO2 moyen (kg)", "Groupe d'aliment": "Groupe"},
        color="Moyenne",
        color_continuous_scale="Reds",
    )

    fig.update_layout(
        height=500, showlegend=False, yaxis={"categoryorder": "total ascending"}
    )

    return fig


def create_distribution_histogram(data: pd.DataFrame) -> go.Figure:
    """
    Crée un histogramme de la distribution des impacts CO2.

    Args:
        data: DataFrame AGRIBALYSE complet

    Returns:
        Figure Plotly
    """
    fig = px.histogram(
        data,
        x="Changement climatique",
        nbins=50,
        title="Distribution des impacts carbone",
        labels={
            "Changement climatique": "Impact CO2 (kg)",
            "count": "Nombre de produits",
        },
        color_discrete_sequence=["#2ecc71"],
    )

    # Ajouter une ligne verticale pour la moyenne
    moyenne = data["Changement climatique"].mean()
    fig.add_vline(
        x=moyenne,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Moyenne: {moyenne:.2f} kg",
        annotation_position="top",
    )

    fig.update_layout(height=400)

    return fig


def create_extreme_products_chart(
    champions: pd.DataFrame, polluants: pd.DataFrame
) -> go.Figure:
    """
    Crée un graphique comparant les produits champions et polluants.

    Args:
        champions: DataFrame des produits les moins polluants
        polluants: DataFrame des produits les plus polluants

    Returns:
        Figure Plotly
    """
    # Préparer les données
    champions_plot = champions.head(10).copy()
    champions_plot["Type"] = "Champion"

    polluants_plot = polluants.head(10).copy()
    polluants_plot["Type"] = "Polluant"

    combined = pd.concat([champions_plot, polluants_plot])

    fig = px.bar(
        combined,
        x="Changement climatique",
        y="Nom du Produit en Français",
        color="Type",
        orientation="h",
        title="Top 10 des produits champions vs polluants",
        labels={
            "Changement climatique": "Impact CO2 (kg)",
            "Nom du Produit en Français": "Produit",
        },
        color_discrete_map={"Champion": "#2ecc71", "Polluant": "#e74c3c"},
    )

    fig.update_layout(height=600, yaxis={"categoryorder": "total ascending"})

    return fig


def create_subgroup_sunburst(data: pd.DataFrame) -> go.Figure:
    """
    Crée un graphique sunburst (hierarchique) des groupes et sous-groupes.

    Args:
        data: DataFrame AGRIBALYSE complet

    Returns:
        Figure Plotly
    """
    # Agrégation par groupe et sous-groupe
    agg_data = (
        data.groupby(["Groupe d'aliment", "Sous-groupe d'aliment"])
        .agg({"Changement climatique": "mean"})
        .reset_index()
    )

    fig = px.sunburst(
        agg_data,
        path=["Groupe d'aliment", "Sous-groupe d'aliment"],
        values="Changement climatique",
        title="Répartition hiérarchique des impacts par groupe et sous-groupe",
        color="Changement climatique",
        color_continuous_scale="RdYlGn_r",
    )

    fig.update_layout(height=600)

    return fig


# Test des fonctions si exécuté directement
if __name__ == "__main__":
    import sys
    from pathlib import Path

    # Ajouter le chemin pour les imports
    sys.path.append(str(Path(__file__).parent.parent.parent))

    from ecomenu_assistant.data.loader import load_agribalyse_data
    from ecomenu_assistant.data.analyzer import analyze_by_group, get_extreme_products

    print("Chargement des données...")
    data = load_agribalyse_data()

    print("Création des graphiques...")

    # Test graphique par groupe
    group_stats = analyze_by_group(data)
    fig1 = create_group_impact_chart(group_stats)
    fig1.write_html("graph_groupes.html")

    # Test histogramme
    fig2 = create_distribution_histogram(data)
    fig2.write_html("graph_distribution.html")

    # Test produits extrêmes
    extremes = get_extreme_products(data)
    fig3 = create_extreme_products_chart(extremes["champions"], extremes["polluants"])
    fig3.write_html("graph_extremes.html")

    print("✅ Graphiques sauvegardés avec succès !")
    print("   - graph_groupes.html")
    print("   - graph_distribution.html")
    print("   - graph_extremes.html")
