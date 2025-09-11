"""
Chargeur de données AGRIBALYSE
"""

import pandas as pd
from pathlib import Path
from typing import Optional


def load_agribalyse_data(file_path: Optional[str] = None) -> pd.DataFrame:
    """
    Charge et nettoie les données AGRIBALYSE

    Args:
        file_path: Chemin vers le fichier CSV. Si None, utilise le chemin par défaut.

    Returns:
        DataFrame pandas avec les données nettoyées
    """
    if file_path is None:
        # Chemin par défaut vers le fichier
        project_root = Path(__file__).parent.parent.parent.parent
        file_path = project_root / "data" / "raw" / "Agribalyse_Synthese.csv"

    # Charger le CSV
    print(f"Chargement des données depuis: {file_path}")
    df = pd.read_csv(file_path)

    # Afficher les infos de base
    print(f"Données chargées: {len(df)} lignes, {len(df.columns)} colonnes")

    # Nettoyer les données (garder seulement les lignes utiles)
    df_clean = df.dropna(subset=["Nom du Produit en Français"]).copy()
    print(f"Après nettoyage: {len(df_clean)} lignes utiles")

    # Sélectionner les colonnes importantes
    colonnes_importantes = [
        "Nom du Produit en Français",
        "Groupe d'aliment",
        "Sous-groupe d'aliment",
        "Changement climatique",
        "DQR",
        "code saison",
        "code avion",
    ]

    # Vérifier que les colonnes existent
    colonnes_existantes = [
        col for col in colonnes_importantes if col in df_clean.columns
    ]
    colonnes_manquantes = [
        col for col in colonnes_importantes if col not in df_clean.columns
    ]

    if colonnes_manquantes:
        print(f"Attention: colonnes manquantes: {colonnes_manquantes}")

    df_final = df_clean[colonnes_existantes].copy()

    print(f"Colonnes sélectionnées: {len(colonnes_existantes)}")
    return df_final


if __name__ == "__main__":
    try:
        data = load_agribalyse_data()
        print("\nAperçu des données:")
        print(data.head())
        print(f"\nTypes de données:")
        print(data.dtypes)
    except Exception as e:
        print(f"Erreur: {e}")
