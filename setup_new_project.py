#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
STACK_PACKAGES = [
    "pandas",
    "ydata-profiling",  # EDA Automatique
    "pyjanitor",        # Nettoyage facile
    "ruff",             # Code quality
    "streamlit",        # Dashboard
    "matplotlib",       # Viz de base
    "seaborn",          # Viz statistique
    "scikit-learn",     # ML Classique
    "ipykernel",        # Pour Jupyter/VSCode
    "plotly",           # Graphiques interactifs
    "nbformat>=4.2.0",  # Requis par Plotly pour l'affichage Jupyter
]

DIRECTORIES = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models",
    "reports",
]

GITIGNORE_CONTENT = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebooks
.ipynb_checkpoints

# Data (Never commit data!)
data/
*.csv
*.xlsx
*.parquet
*.json
*.sqlite
*.db

# OS
.DS_Store
Thumbs.db

# Reports
reports/*.html
"""

README_CONTENT = """
# {project_name}

Projet généré automatiquement avec la **Stack Data Science Pro**.

## 🛠️ Stack Technique

| Outil | Usage |
|---|---|
| **Pandas + PyJanitor** | Nettoyage de données efficace |
| **YData Profiling** | EDA Automatique (voir `reports/`) |
| **Scikit-Learn** | Modélisation ML |
| **Streamlit** | Dashboard Interactif |
| **Ruff** | Qualité du code (Linter/Formatter) |

## 🚀 Démarrage Rapide

1. Activer l'environnement :
   ```bash
   source .venv/bin/activate
   ```

2. Nettoyer le code :
   ```bash
   ruff check . --fix
   ruff format .
   ```

3. Lancer le dashboard (si existant) :
   ```bash
   streamlit run src/app.py
   ```
"""

# -----------------------------------------------------------------------------
# Script Logic
# -----------------------------------------------------------------------------

def create_structure(project_name):
    print(f"🚀 Création du projet : {project_name}")
    
    if os.path.exists(project_name):
        print(f"⚠️  Le dossier '{project_name}' existe déjà. Arrêt.")
        sys.exit(1)
    
    os.makedirs(project_name)
    os.chdir(project_name)

    # Création des dossiers
    for directory in DIRECTORIES:
        os.makedirs(directory, exist_ok=True)
        # Add .gitkeep to ensure empty dirs are tracked if needed (optional)
        with open(os.path.join(directory, ".gitkeep"), "w") as f:
            pass

    print("✅ Structure de dossiers créée (Cookiecutter style)")

def create_files(project_name):
    # .gitignore
    with open(".gitignore", "w") as f:
        f.write(GITIGNORE_CONTENT.strip())
    
    # README.md
    with open("README.md", "w") as f:
        f.write(README_CONTENT.format(project_name=project_name).strip())
    
    # requirements.txt
    with open("requirements.txt", "w") as f:
        f.write("\n".join(STACK_PACKAGES))

    print("✅ Fichiers de configuration créés (.gitignore, README, requirements.txt)")

def setup_environment():
    print("🐍 Création de l'environnement virtuel (.venv)...")
    try:
        subprocess.check_call([sys.executable, "-m", "venv", ".venv"])
    except subprocess.CalledProcessError:
        print("❌ Erreur lors de la création du venv.")
        return

    print("📦 Installation de la Stack Data Science (ça peut prendre une minute)...")
    
    # Determine pip path inside venv
    if os.name == "nt":  # Windows
        pip_path = os.path.join(".venv", "Scripts", "pip")
    else:  # Linux/Mac
        pip_path = os.path.join(".venv", "bin", "pip")

    try:
        subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
        subprocess.check_call([pip_path, "install"] + STACK_PACKAGES)
        print("✅ Stack installée avec succès !")
    except subprocess.CalledProcessError:
        print("❌ Erreur lors de l'installation des paquets.")

def init_git():
    try:
        subprocess.check_call(["git", "init"])
        print("Example: git add . && git commit -m 'Initial commit'")
        print("✅ Git initialisé")
    except FileNotFoundError:
        print("⚠️  Git n'est pas installé. On saute cette étape.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python setup_new_project.py <Nom_du_Projet>")
        sys.exit(1)
    
    project_name = sys.argv[1]
    
    create_structure(project_name)
    create_files(project_name)
    setup_environment()
    init_git()

    print("\n✨ Tout est prêt ! Pour commencer :")
    print(f"cd {project_name}")
    print("source .venv/bin/activate")
    print("code .  # Si tu utilises VSCode")

if __name__ == "__main__":
    main()
