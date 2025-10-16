"""
Page de chat avec assistant IA
"""
import streamlit as st
import sys
from pathlib import Path

# Ajouter le chemin pour les imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from ecomenu_assistant.data.loader import load_agribalyse_data
from ecomenu_assistant.llm.openai_client import EcoMenuAssistant


def show_chat_page():
    """Affiche la page de chat avec l'assistant IA"""
    st.title("💬 Assistant IA Éco-Responsable")
    st.markdown("---")
    
    st.markdown("""
    Posez vos questions sur l'alimentation durable et l'impact carbone des aliments.
    L'assistant utilise les données AGRIBALYSE pour vous donner des conseils personnalisés.
    """)
    
    # Initialisation de l'assistant et des données
    if 'chat_assistant' not in st.session_state:
        st.session_state.chat_assistant = EcoMenuAssistant()
    
    if 'data' not in st.session_state:
        with st.spinner("Chargement des données..."):
            st.session_state.data = load_agribalyse_data()
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Bouton pour réinitialiser la conversation
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🔄 Nouvelle conversation"):
            st.session_state.chat_assistant.reset_conversation()
            st.session_state.messages = []
            st.rerun()
    
    # Afficher l'historique des messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Exemples de questions suggérées
    if len(st.session_state.messages) == 0:
        st.subheader("💡 Questions suggérées :")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🥩 Alternatives à la viande rouge ?"):
                prompt = "Quelles sont les meilleures alternatives à la viande rouge pour réduire mon impact carbone ?"
                process_user_input(prompt)
                st.rerun()
            
            if st.button("🧀 Impact des produits laitiers ?"):
                prompt = "Quel est l'impact environnemental des produits laitiers et comment le réduire ?"
                process_user_input(prompt)
                st.rerun()
        
        with col2:
            if st.button("🥗 Menu bas carbone ?"):
                prompt = "Propose-moi un menu d'une journée avec un faible impact carbone"
                process_user_input(prompt)
                st.rerun()
            
            if st.button("🌱 Conseils alimentation durable ?"):
                prompt = "Donne-moi 5 conseils pratiques pour une alimentation plus durable"
                process_user_input(prompt)
                st.rerun()
    
    # Input utilisateur
    if user_input := st.chat_input("Posez votre question..."):
        process_user_input(user_input)
        st.rerun()


def process_user_input(user_input: str):
    """
    Traite l'input utilisateur et génère une réponse.
    
    Args:
        user_input: Message de l'utilisateur
    """
    # Ajouter le message utilisateur
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Vérifier si l'utilisateur mentionne un produit spécifique
    # et ajouter le contexte si nécessaire
    product_context = ""
    
    # Mots-clés pour détecter une demande sur un produit spécifique
    product_keywords = ["bœuf", "agneau", "porc", "poulet", "fromage", "lait", 
                       "tomate", "pomme", "pain", "riz", "pâtes"]
    
    for keyword in product_keywords:
        if keyword.lower() in user_input.lower():
            product_context = st.session_state.chat_assistant.get_product_info(
                keyword, 
                st.session_state.data
            )
            break
    
    # Générer la réponse de l'assistant
    with st.spinner("L'assistant réfléchit..."):
        response = st.session_state.chat_assistant.chat(
            user_input,
            product_context
        )
    
    # Ajouter la réponse de l'assistant
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })