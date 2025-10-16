"""
Page d'analyse des données AGRIBALYSE
"""
import streamlit as st
import sys
from pathlib import Path

# Ajouter le chemin pour les imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from ecomenu_assistant.data.loader import load_agribalyse_data
from ecomenu_assistant.data.analyzer import (
    get_global_stats,
    analyze_by_group,
    get_extreme_products
)
from ecomenu_assistant.visualization.charts import (
    create_group_impact_chart,
    create_distribution_histogram,
    create_extreme_products_chart
)


def show_analysis_page():
    """Affiche la page d'analyse des données"""
    st.title("📊 Analyse des données AGRIBALYSE")
    st.markdown("---")
    
    # Chargement des données
    if 'data' not in st.session_state:
        with st.spinner("Chargement des données..."):
            st.session_state.data = load_agribalyse_data()
    
    data = st.session_state.data
    
    # Section 1 : Statistiques globales
    st.header("📈 Statistiques globales")
    
    stats = get_global_stats(data)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Moyenne", f"{stats['moyenne']} kg CO2")
    
    with col2:
        st.metric("Médiane", f"{stats['mediane']} kg CO2")
    
    with col3:
        st.metric("Minimum", f"{stats['min']} kg CO2")
    
    with col4:
        st.metric("Maximum", f"{stats['max']} kg CO2")
    
    st.markdown("---")
    
    # Section 2 : Distribution
    st.header("📊 Distribution des impacts")
    
    fig_distribution = create_distribution_histogram(data)
    st.plotly_chart(fig_distribution, use_container_width=True)
    
    st.markdown("---")
    
    # Section 3 : Analyse par groupe
    st.header("🍽️ Impact par groupe d'aliments")
    
    group_stats = analyze_by_group(data)
    fig_groups = create_group_impact_chart(group_stats)
    st.plotly_chart(fig_groups, use_container_width=True)
    
    # Afficher le tableau des statistiques
    with st.expander("📋 Voir le tableau détaillé"):
        st.dataframe(group_stats, use_container_width=True)
    
    st.markdown("---")
    
    # Section 4 : Produits extrêmes
    st.header("🏆 Produits champions et polluants")
    
    extremes = get_extreme_products(data, n=10)
    fig_extremes = create_extreme_products_chart(
        extremes['champions'],
        extremes['polluants']
    )
    st.plotly_chart(fig_extremes, use_container_width=True)
    
    # Tableaux des produits extrêmes
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💚 Top 10 Champions")
        st.dataframe(
            extremes['champions'].reset_index(drop=True),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.subheader("🔴 Top 10 Polluants")
        st.dataframe(
            extremes['polluants'].reset_index(drop=True),
            use_container_width=True,
            hide_index=True
        )