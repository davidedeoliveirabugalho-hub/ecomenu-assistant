"""
Interface Streamlit pour EcoMenu Assistant
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Ajouter le dossier parent au path pour importer nos modules
sys.path.append(str(Path(__file__).parent.parent.parent))

from ecomenu_assistant.data.loader import load_agribalyse_data


def main():
    st.set_page_config(page_title="EcoMenu Assistant", page_icon="🌱", layout="wide")

    st.title("🌱 EcoMenu Assistant")
    st.subheader("Votre assistant alimentaire éco-responsable")
    
    # Description du projet
    st.markdown("""
    ### 🍃 Découvrez l'impact environnemental de vos aliments
    
    EcoMenu Assistant vous aide à faire des choix alimentaires plus durables en vous fournissant 
    l'empreinte carbone de plus de 2400 produits alimentaires basée sur les données officielles 
    **AGRIBALYSE 3.2** de l'ADEME.
    
    **Fonctionnalités :**
    - 🔍 Recherchez l'impact CO2 de vos aliments préférés
    - 📊 Comparez les alternatives plus écologiques
    - 💡 Recevez des recommandations personnalisées
    - 📈 Visualisez les données environnementales
    
    ---
    """)

    # Chargement des données
    if "data" not in st.session_state:
        with st.spinner("Chargement des données AGRIBALYSE..."):
            st.session_state.data = load_agribalyse_data()

    data = st.session_state.data

    # Affichage des statistiques
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Produits alimentaires", value=f"{len(data):,}")

    with col2:
        st.metric(
            label="Impact CO2 moyen",
            value=f"{data['Changement climatique'].mean():.1f} kg CO2",
        )

    with col3:
        st.metric(
            label="Groupes d'aliments", value=len(data["Groupe d'aliment"].unique())
        )

        # Interface de recherche
    st.header("🔍 Rechercher un produit")

    produit_recherche = st.text_input(
        "Tapez le nom d'un produit", placeholder="Ex: pomme, bœuf, fromage..."
    )

    if produit_recherche:
        # Filtrer les données selon la recherche
        resultats = data[
            data["Nom du Produit en Français"].str.contains(
                produit_recherche, case=False, na=False
            )
        ].sort_values("Changement climatique")

        if len(resultats) > 0:
            st.write(f"Trouvé {len(resultats)} produit(s)")

            # Afficher les 10 premiers résultats
            for i, row in resultats.head(10).iterrows():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{row['Nom du Produit en Français']}**")
                    st.write(f"_{row['Groupe d\'aliment']}_")
                with col2:
                    impact = row["Changement climatique"]
                    if impact < 2:
                        st.success(f"{impact:.2f} kg CO2")
                    elif impact < 6:
                        st.warning(f"{impact:.2f} kg CO2")
                    else:
                        st.error(f"{impact:.2f} kg CO2")
        else:
            st.write("Aucun produit trouvé")

        # Recommandations automatiques
        if len(resultats) > 1:
            st.subheader("💡 Recommandation")

            # Prendre le produit le plus polluant de la recherche
            produit_polluant = resultats.tail(1).iloc[0]
            # Prendre le moins polluant
            produit_eco = resultats.head(1).iloc[0]

            if (
                produit_polluant["Changement climatique"]
                > produit_eco["Changement climatique"]
            ):
                economie = (
                    produit_polluant["Changement climatique"]
                    - produit_eco["Changement climatique"]
                )
                st.write(
                    f"💚 Privilégiez **{produit_eco['Nom du Produit en Français']}** "
                    f"({produit_eco['Changement climatique']:.2f} kg CO2) "
                    f"plutôt que **{produit_polluant['Nom du Produit en Français']}** "
                    f"({produit_polluant['Changement climatique']:.2f} kg CO2)"
                )
                st.write(f"**Économie : {economie:.2f} kg CO2**")

    # Section d'information
    with st.expander("ℹ️ À propos des données"):
        st.write(
            """
        Les données proviennent de la base **AGRIBALYSE 3.2** de l'ADEME, 
        qui fournit l'empreinte carbone de plus de 2400 produits alimentaires 
        selon la méthodologie d'Analyse de Cycle de Vie (ACV).
        
        - **Impact CO2** : Émissions de gaz à effet de serre en kg CO2 équivalent pour 1kg de produit
        - **Périmètre** : Du champ à l'assiette (production, transformation, transport, emballage)
        """
        )


if __name__ == "__main__":
    main()
