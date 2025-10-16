# 🌱 EcoMenu Assistant

Assistant alimentaire éco-responsable pour évaluer et réduire l'impact carbone de votre alimentation.

![Python](https://img.shields.io/badge/python-3.12-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.49-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Description

EcoMenu Assistant est une application web interactive qui permet de :
- 🔍 Rechercher des produits alimentaires et comparer leurs impacts carbone
- 📊 Visualiser des analyses statistiques sur plus de 2400 produits
- 💡 Obtenir des recommandations pour des alternatives plus écologiques
- 📈 Explorer les données AGRIBALYSE de l'ADEME

## ✨ Fonctionnalités

### Recherche de produits
- Base de données de 2451 produits alimentaires français
- Recherche par nom de produit
- Tri par impact carbone
- Recommandations automatiques d'alternatives moins polluantes

### Analyse des données
- Statistiques globales sur les impacts environnementaux
- Visualisations interactives par groupe d'aliments
- Distribution des impacts CO2
- Top 10 des produits champions et polluants

### Navigation intuitive
- Interface web responsive
- Navigation multipage
- Graphiques interactifs Plotly

## 🚀 Installation

### Prérequis
- Python 3.12+
- [UV](https://github.com/astral-sh/uv) (gestionnaire de dépendances)

### Installation locale
```bash
# Cloner le repository
git clone https://github.com/davidedeoliveirabugalho-hub/ecomenu-assistant.git
cd ecomenu-assistant

# Installer les dépendances avec UV
uv sync

# Lancer l'application
uv run streamlit run src/ecomenu_assistant/ui/app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

## 📊 Source des données

Les données proviennent de **AGRIBALYSE v3.2**, la base de référence de l'ADEME pour les impacts environnementaux des produits agricoles et alimentaires français.

- **Nombre de produits** : 2451 produits alimentaires
- **Méthodologie** : Analyse de Cycle de Vie (ACV)
- **Périmètre** : Du champ à l'assiette
- **Indicateur principal** : Changement climatique (kg CO2 eq.)

[📖 Documentation AGRIBALYSE](https://doc.agribalyse.fr/)

## 🛠️ Technologies utilisées

- **Python 3.12** - Langage de programmation
- **Streamlit** - Framework d'interface web
- **Pandas** - Manipulation et analyse de données
- **Plotly** - Visualisations interactives
- **UV** - Gestion des dépendances Python
- **Git/GitHub** - Versioning et collaboration

## 📁 Structure du projet
```
ecomenu-assistant/
├── src/
│   └── ecomenu_assistant/
│       ├── data/              # Modules de traitement des données
│       │   ├── loader.py      # Chargement données AGRIBALYSE
│       │   └── analyzer.py    # Analyses statistiques
│       ├── visualization/     # Graphiques et visualisations
│       │   └── charts.py      # Fonctions Plotly
│       ├── ui/                # Interface Streamlit
│       │   ├── app.py         # Application principale
│       │   ├── navigation.py  # Navigation multipage
│       │   └── analysis_page.py # Page d'analyse
│       └── utils/             # Utilitaires
├── data/                      # Données
│   ├── raw/                   # Données brutes AGRIBALYSE
│   └── processed/             # Données traitées
├── notebooks/                 # Notebooks d'exploration
├── tests/                     # Tests unitaires
└── docs/                      # Documentation
```

## 🎯 Roadmap

- [x] Chargement et traitement des données AGRIBALYSE
- [x] Interface de recherche de produits
- [x] Recommandations automatiques
- [x] Analyses statistiques et visualisations
- [x] Navigation multipage
- [ ] Intégration LLM (OpenAI) pour recommandations intelligentes
- [ ] Calculateur de recettes complètes
- [ ] Ajout données nutritionnelles (calories)
- [ ] Export des résultats
- [ ] Tests automatisés
- [ ] Déploiement en ligne

## 👨‍💻 Auteur

**David Bugalho**
- Portfolio de projets data analyst
- [GitHub](https://github.com/davidedeoliveirabugalho-hub)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

- [ADEME](https://www.ademe.fr/) pour la base de données AGRIBALYSE
- [Streamlit](https://streamlit.io/) pour le framework d'interface
- [Plotly](https://plotly.com/) pour les visualisations interactives

---

💚 *Fait avec passion pour un avenir plus durable*