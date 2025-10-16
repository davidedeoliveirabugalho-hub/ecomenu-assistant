"""
Configuration de la navigation multipage Streamlit
"""
import streamlit as st


def create_navigation():
    """
    Crée la navigation entre les pages de l'application.
    """
    st.sidebar.title("🌱 EcoMenu Assistant")
    
    pages = {
        "🔍 Recherche de produits": "search",
        "📊 Analyse des données": "analysis",
        "📖 À propos": "about"
    }
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Navigation")
    
    # Sélection de page
    page = st.sidebar.radio(
        "Aller à :",
        options=list(pages.keys()),
        label_visibility="collapsed"
    )
    
    # Informations dans la sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### 💡 À propos
    
    EcoMenu Assistant vous aide à :
    - Rechercher des produits alimentaires
    - Comparer leurs impacts carbone
    - Obtenir des recommandations écologiques
    
    **Données** : AGRIBALYSE v3.2 (ADEME)
    """)
    
    return pages[page]


def show_page_header(title: str, subtitle: str = ""):
    """
    Affiche l'en-tête de page standardisé.
    
    Args:
        title: Titre de la page
        subtitle: Sous-titre optionnel
    """
    st.title(title)
    if subtitle:
        st.subheader(subtitle)
    st.markdown("---")