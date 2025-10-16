# ecomenu-assistant

Assistant intelligent pour la gestion et l'analyse de menus écologiques. Ce projet utilise Streamlit pour l'interface utilisateur et l'API OpenAI pour les fonctionnalités d'IA.

## Structure du projet

```
ecomenu-assistant/
├── pyproject.toml          # Configuration du projet et dépendances
├── README.md              # Documentation principale
├── CLAUDE.md              # Ce fichier
├── .env                   # Variables d'environnement (à créer)
├── src/                   # Code source principal
├── tests/                 # Tests unitaires
├── data/                  # Données et fichiers de configuration
└── notebooks/             # Notebooks Jupyter pour l'analyse
```

## Technologies utilisées

- **Python 3.12+** - Langage principal
- **Streamlit 1.49+** - Interface web interactive
- **OpenAI API** - Intégration IA pour l'assistant
- **Pandas 2.3+** - Manipulation et analyse de données
- **Matplotlib/Seaborn/Plotly** - Visualisation de données
- **python-dotenv** - Gestion des variables d'environnement

### Outils de développement
- **Black** - Formatage automatique du code
- **isort** - Organisation des imports
- **pytest** - Tests unitaires
- **Jupyter** - Notebooks pour l'analyse

## Instructions de développement

### Installation
```bash
# Installer les dépendances principales
uv sync

# Ou avec pip
pip install -e .

# Pour le développement (inclut les outils de dev)
uv sync --group dev
```

### Configuration
1. Créer un fichier `.env` à la racine du projet :
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### Lancement de l'application
```bash
# Lancer l'application Streamlit
streamlit run src/app.py

# Ou si le point d'entrée est différent
streamlit run main.py
```

### Tests
```bash
# Lancer les tests
pytest

# Tests avec couverture
pytest --cov=src
```

### Formatage du code
```bash
# Formatter le code
black src/ tests/

# Organiser les imports
isort src/ tests/
```

## Conventions et standards

- **Style de code** : Utilisation de Black pour le formatage automatique
- **Imports** : Organisation avec isort
- **Nommage** : 
  - Variables et fonctions : `snake_case`
  - Classes : `PascalCase`
  - Constantes : `UPPER_CASE`
- **Docstrings** : Format Google/NumPy style
- **Type hints** : Utilisation recommandée pour les fonctions publiques

## Contexte spécifique

### Intégration OpenAI
- Utilise l'API OpenAI pour les fonctionnalités d'assistant
- Configuration via variables d'environnement
- Gestion des erreurs API importante

### Streamlit
- Interface utilisateur principale
- Session state pour la persistance des données
- Composants interactifs pour l'analyse de menus

### Données
- Focus sur les menus écologiques et durables
- Analyse de données nutritionnelles et environnementales
- Visualisations avec Matplotlib, Seaborn et Plotly

### Environnement de développement
- Python 3.12+ requis
- Utilisation d'uv pour la gestion des dépendances (recommandé)
- Support Jupyter pour l'analyse exploratoire