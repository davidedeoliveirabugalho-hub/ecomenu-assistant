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

### 🔍 Recherche de produits
- Base de données de 2451 produits alimentaires français
- Recherche par nom de produit
- Tri automatique par impact carbone
- Recommandations automatiques d'alternatives moins polluantes
- Codes couleur pour identifier rapidement les impacts (faible/moyen/élevé)

### 📊 Analyse des données
- Statistiques globales sur les impacts environnementaux
- Visualisations interactives Plotly par groupe d'aliments
- Distribution détaillée des impacts CO2
- Top 10 des produits champions (faible impact) et polluants (fort impact)
- Analyse par groupes et sous-groupes d'aliments

### 💬 Chat IA Intelligent
- Assistant conversationnel propulsé par OpenAI GPT-3.5
- Conseils personnalisés sur l'alimentation durable
- Explications pédagogiques de l'impact carbone
- Recommandations d'alternatives adaptées
- Questions suggérées pour démarrer
- Contexte enrichi avec les données AGRIBALYSE

### 🧭 Navigation intuitive
- Interface web responsive multi-pages
- Navigation claire via sidebar
- Expérience utilisateur fluide

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

### ✅ Complété (v1.0)
- [x] Chargement et traitement des données AGRIBALYSE
- [x] Module d'analyse statistique professionnelle
- [x] Visualisations interactives avec Plotly
- [x] Interface de recherche de produits
- [x] Recommandations automatiques basiques
- [x] Navigation multipage
- [x] **Intégration OpenAI GPT-3.5 pour chat intelligent**
- [x] Page d'analyse complète avec graphiques
- [x] Assistant conversationnel avec contexte des données

### 🚧 Prochaines améliorations (v2.0)
- [ ] Calculateur de recettes complètes avec plusieurs ingrédients
- [ ] Ajout données nutritionnelles (calories, macronutriments)
- [ ] Export des résultats (PDF, CSV)
- [ ] Amélioration esthétique des graphiques
- [ ] Tests automatisés (pytest)
- [ ] Mode sombre
- [ ] Filtres avancés (par saison, transport, DQR)

### 🌟 Vision future (v3.0)
- [ ] Déploiement en ligne (Streamlit Cloud)
- [ ] Suivi personnalisé de l'empreinte carbone
- [ ] Recommandations de menus hebdomadaires
- [ ] Intégration API nutritionnelles externes
- [ ] Mode hors ligne
- [ ] Support multilingue

## 💰 Considérations de coûts

L'application utilise l'API OpenAI GPT-3.5-turbo pour le chat intelligent. 

**Coûts estimés :**
- Développement/tests : ~$0.10-0.50
- Usage démo/portfolio : ~$1-2/mois
- Configuration recommandée : Limite de $5/mois pour sécurité

Les données AGRIBALYSE sont entièrement gratuites et open source.

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