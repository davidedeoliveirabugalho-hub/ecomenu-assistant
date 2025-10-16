"""
Client OpenAI pour recommandations intelligentes
"""
import os
from openai import OpenAI
from typing import List, Dict
import pandas as pd
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class EcoMenuAssistant:
    """Assistant conversationnel pour recommandations alimentaires écologiques"""
    
    def __init__(self):
        """Initialise le client OpenAI"""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY non trouvée dans les variables d'environnement")
        
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"
        self.conversation_history = []
    
    def create_system_prompt(self, data_context: str = "") -> str:
        """
        Crée le prompt système avec contexte des données.
        
        Args:
            data_context: Contexte sur les données disponibles
            
        Returns:
            Prompt système
        """
        return f"""Tu es un assistant expert en alimentation durable et impact environnemental.
        
Tu aides les utilisateurs à faire des choix alimentaires plus écologiques en te basant sur la base de données AGRIBALYSE de l'ADEME.

Tes rôles :
- Expliquer l'impact carbone des aliments de façon pédagogique
- Proposer des alternatives moins polluantes
- Donner des conseils pratiques pour réduire l'empreinte carbone alimentaire
- Être encourageant et positif

Contexte des données disponibles :
{data_context}

Règles :
- Réponds de façon concise et claire
- Utilise des émojis pour rendre les réponses plus engageantes
- Donne des chiffres précis quand c'est pertinent
- Propose toujours des alternatives concrètes"""
    
    def get_product_info(self, product_name: str, data: pd.DataFrame) -> str:
        """
        Récupère les informations d'un produit pour alimenter le contexte.
        
        Args:
            product_name: Nom du produit recherché
            data: DataFrame AGRIBALYSE
            
        Returns:
            Informations formatées sur le produit
        """
        results = data[
            data['Nom du Produit en Français'].str.contains(
                product_name, case=False, na=False
            )
        ].head(5)
        
        if len(results) == 0:
            return f"Aucun produit trouvé pour '{product_name}'"
        
        info = f"Produits trouvés pour '{product_name}':\n"
        for _, row in results.iterrows():
            info += f"- {row['Nom du Produit en Français']}: {row['Changement climatique']:.2f} kg CO2\n"
        
        return info
    
    def chat(self, user_message: str, product_context: str = "") -> str:
        """
        Envoie un message au chat et récupère la réponse.
        
        Args:
            user_message: Message de l'utilisateur
            product_context: Contexte additionnel sur les produits
            
        Returns:
            Réponse de l'assistant
        """
        # Ajouter le contexte produit si fourni
        if product_context:
            system_prompt = self.create_system_prompt(product_context)
        else:
            system_prompt = self.create_system_prompt()
        
        # Construire les messages
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(self.conversation_history)
        messages.append({"role": "user", "content": user_message})
        
        # Appel API OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_message = response.choices[0].message.content
        
        # Sauvegarder l'historique
        self.conversation_history.append({"role": "user", "content": user_message})
        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def reset_conversation(self):
        """Réinitialise l'historique de conversation"""
        self.conversation_history = []


# Test si exécuté directement
if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from ecomenu_assistant.data.loader import load_agribalyse_data
    
    print("🌱 Test du client OpenAI")
    print("Chargement des données...")
    data = load_agribalyse_data()
    
    assistant = EcoMenuAssistant()
    
    # Test 1 : Question simple
    print("\n--- Test 1 : Question générale ---")
    response = assistant.chat("Pourquoi la viande rouge a-t-elle un impact carbone élevé ?")
    print(response)
    
    # Test 2 : Avec contexte produit
    print("\n--- Test 2 : Question avec contexte ---")
    context = assistant.get_product_info("bœuf", data)
    response = assistant.chat("Quelles alternatives au bœuf me recommandes-tu ?", context)
    print(response)
    
    print("\n✅ Tests terminés")