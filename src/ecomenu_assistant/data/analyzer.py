"""
Module d'analyse statistique des données AGRIBALYSE
"""
import pandas as pd
from typing import Dict, Tuple


def analyze_by_group(data: pd.DataFrame) -> pd.DataFrame:
    """
    Analyse les impacts CO2 par groupe d'aliments.
    
    Args:
        data: DataFrame AGRIBALYSE
        
    Returns:
        DataFrame avec statistiques par groupe
    """
    result = data.groupby("Groupe d'aliment")["Changement climatique"].agg([
        'count', 'mean', 'min', 'max'
    ]).sort_values('mean', ascending=False)
    
    result.columns = ['Nombre', 'Moyenne', 'Min', 'Max']
    return result


def analyze_by_subgroup(data: pd.DataFrame) -> pd.DataFrame:
    """
    Analyse les impacts CO2 par groupe et sous-groupe d'aliments.
    
    Args:
        data: DataFrame AGRIBALYSE
        
    Returns:
        DataFrame avec statistiques par groupe et sous-groupe
    """
    result = data.groupby([
        "Groupe d'aliment", 
        "Sous-groupe d'aliment"
    ])["Changement climatique"].agg([
        'count', 'mean', 'min', 'max'
    ]).sort_values('mean', ascending=False).reset_index()
    
    result.columns = ['Groupe', 'Sous-groupe', 'Nombre', 'Moyenne', 'Min', 'Max']
    return result


def get_extreme_products(data: pd.DataFrame, n: int = 10) -> Dict[str, pd.DataFrame]:
    """
    Identifie les produits avec les impacts les plus élevés/faibles.
    
    Args:
        data: DataFrame AGRIBALYSE
        n: Nombre de produits à retourner
        
    Returns:
        Dict avec 'polluants' et 'champions'
    """
    polluants = data.nlargest(n, 'Changement climatique')[
        ['Nom du Produit en Français', 'Changement climatique']
    ]
    
    champions = data.nsmallest(n, 'Changement climatique')[
        ['Nom du Produit en Français', 'Changement climatique']
    ]
    
    return {
        'polluants': polluants,
        'champions': champions
    }


def get_global_stats(data: pd.DataFrame) -> Dict[str, float]:
    """
    Calcule les statistiques globales des impacts CO2.
    
    Args:
        data: DataFrame AGRIBALYSE
        
    Returns:
        Dict avec les statistiques clés
    """
    impacts = data['Changement climatique']
    
    return {
        'moyenne': round(impacts.mean(), 2),
        'mediane': round(impacts.median(), 2),
        'ecart_type': round(impacts.std(), 2),
        'min': round(impacts.min(), 2),
        'max': round(impacts.max(), 2),
        'q25': round(impacts.quantile(0.25), 2),
        'q75': round(impacts.quantile(0.75), 2)
    }


# Test des fonctions si exécuté directement
if __name__ == "__main__":
    from loader import load_agribalyse_data
    
    print("Chargement des données...")
    data = load_agribalyse_data()
    
    print("\n=== Statistiques globales ===")
    print(get_global_stats(data))
    
    print("\n=== Analyse par groupe ===")
    print(analyze_by_group(data))
    
    print("\n=== Produits extrêmes ===")
    extremes = get_extreme_products(data, n=5)
    print("Champions:", extremes['champions'])
    print("Polluants:", extremes['polluants'])