"""
Application principale EcoMenu Assistant
"""
import streamlit as st

# Configuration de la page (doit être la première commande Streamlit)
st.set_page_config(
    page_title="EcoMenu Assistant",
    page_icon="🌱",
    layout="wide"
)

# Imports
from navigation import create_navigation
from analysis_page import show_analysis_page


def show_search_page():
    """Page de recherche de produits (votre code existant)"""
    import sys
    from pathlib import Path
    
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from ecomenu_assistant.data.loader import load_agribalyse_data
    
    st.title("🔍 Recherche de produits")
    st.markdown("---")
    
    # Chargement des données
    if 'data' not in st.session_state:
        with st.spinner("Chargement des données AGRIBALYSE..."):
            st.session_state.data = load_agribalyse_data()
    
    data = st.session_state.data
    
    # Affichage des statistiques
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Produits alimentaires",
            value=f"{len(data):,}"
        )
    
    with col2:
        st.metric(
            label="Impact CO2 moyen",
            value=f"{data['Changement climatique'].mean():.1f} kg CO2"
        )
    
    with col3:
        st.metric(
            label="Groupes d'aliments",
            value=len(data['Groupe d\'aliment'].unique())
        )
    
    # Interface de recherche
    st.header("🔍 Rechercher un produit")
    
    produit_recherche = st.text_input(
        "Tapez le nom d'un produit",
        placeholder="Ex: pomme, bœuf, fromage..."
    )
    
    if produit_recherche:
        # Filtrer les données selon la recherche
        resultats = data[
            data['Nom du Produit en Français'].str.contains(
                produit_recherche, case=False, na=False
            )
        ].sort_values('Changement climatique')
        
        if len(resultats) > 0:
            st.write(f"Trouvé {len(resultats)} produit(s)")
            
            # Afficher les 10 premiers résultats
            for i, row in resultats.head(10).iterrows():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{row['Nom du Produit en Français']}**")
                    st.write(f"_{row['Groupe d\'aliment']}_")
                with col2:
                    impact = row['Changement climatique']
                    if impact < 2:
                        st.success(f"{impact:.2f} kg CO2")
                    elif impact < 6:
                        st.warning(f"{impact:.2f} kg CO2")
                    else:
                        st.error(f"{impact:.2f} kg CO2")
            
            # Recommandations automatiques
            if len(resultats) > 1:
                st.subheader("💡 Recommandation")
                
                produit_polluant = resultats.tail(1).iloc[0]
                produit_eco = resultats.head(1).iloc[0]
                
                if produit_polluant['Changement climatique'] > produit_eco['Changement climatique']:
                    economie = produit_polluant['Changement climatique'] - produit_eco['Changement climatique']
                    st.write(f"💚 Privilégiez **{produit_eco['Nom du Produit en Français']}** "
                            f"({produit_eco['Changement climatique']:.2f} kg CO2) "
                            f"plutôt que **{produit_polluant['Nom du Produit en Français']}** "
                            f"({produit_polluant['Changement climatique']:.2f} kg CO2)")
                    st.write(f"**Économie : {economie:.2f} kg CO2**")
        else:
            st.write("Aucun produit trouvé")
    
    # Section d'information
    with st.expander("ℹ️ À propos des données"):
        st.write("""
        Les données proviennent de la base **AGRIBALYSE 3.2** de l'ADEME, 
        qui fournit l'empreinte carbone de plus de 2400 produits alimentaires 
        selon la méthodologie d'Analyse de Cycle de Vie (ACV).
        
        - **Impact CO2** : Émissions de gaz à effet de serre en kg CO2 équivalent pour 1kg de produit
        - **Périmètre** : Du champ à l'assiette (production, transformation, transport, emballage)
        """)


def show_about_page():
    """Page À propos"""
    st.title("📖 À propos d'EcoMenu Assistant")
    st.markdown("---")
    
    st.markdown("""
    ## Mission
    
    EcoMenu Assistant vous aide à prendre des décisions alimentaires plus écologiques 
    en vous fournissant des informations claires sur l'impact carbone des produits.
    
    ## Données
    
    Toutes les données proviennent de **AGRIBALYSE v3.2**, la base de référence de l'ADEME 
    pour les impacts environnementaux des produits alimentaires français.
    
    ## Technologies
    
    - **Python** : Traitement des données
    - **Streamlit** : Interface web
    - **Plotly** : Visualisations interactives
    - **Pandas** : Analyse de données
    
    ## Contact
    
    Projet développé dans le cadre d'un portfolio data analyst.
    """)


def main():
    """Fonction principale de l'application"""
    # Créer la navigation et obtenir la page sélectionnée
    current_page = create_navigation()
    
    # Afficher la page correspondante
    if current_page == "search":
        show_search_page()
    elif current_page == "analysis":
        show_analysis_page()
    elif current_page == "about":
        show_about_page()


if __name__ == "__main__":
    main()