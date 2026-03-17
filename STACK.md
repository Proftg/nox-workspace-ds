# ⚡ La Stack Data Science "Pro" de Tahar

Ce document définit le **workflow standard** pour tout nouveau projet Data Science.
L'objectif : coder moins, livrer plus vite, impressionner par la qualité.

---

## 🚀 Le Workflow en 5 Étapes

| Étape | Tâche | Outil "Secret" | Pourquoi ? |
|:---:|---|---|---|
| **0** | **Initialisation** | `setup_new_project.py` | Crée dossiers (`data/`, `notebooks/`), git, venv et installe la stack en 1 clic. |
| **1** | **Nettoyage** | **`pyjanitor`** | Nettoie les noms de colonnes et les valeurs vides en une ligne lisible. |
| **2** | **EDA (Exploration)** | **`ydata-profiling`** | Génère un rapport HTML complet (distributions, corrélations) sans écrire de code. |
| **3** | **Qualité Code** | **`ruff`** | Formate et corrige ton code (imports, style PEP8) instantanément. |
| **4** | **Qualité Data** | **`great_expectations`** | (Avancé) Vérifie que tes données respectent les règles (ex: pas de prix négatif). |
| **5** | **Dashboard** | **`streamlit`** | Transforme ton analyse en Web App interactive pour le portfolio. |

---

## 🛠️ Détail des Outils & Commandes

### 1. Initialisation
Ne crée jamais tes dossiers à la main. Lance le script d'automatisation :
```bash
python3 ~/.openclaw/workspace-ds/setup_new_project.py "Nom_du_Projet"
```

### 2. EDA Automatique (`ydata-profiling`)
Au lieu de faire 50 `df.describe()` et `df.plot()`, fais ceci dès le début :
```python
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/raw/mon_fichier.csv")
profile = ProfileReport(df, title="Rapport EDA")
profile.to_file("notebooks/rapport_eda.html")
```
👉 *Ouvre ensuite `notebooks/rapport_eda.html` dans ton navigateur.*

### 3. Nettoyage Propre (`pyjanitor`)
Au lieu de pandas classique (lourd), utilise le chaining :
```python
import janitor  # Active les méthodes magiques sur pandas

df_clean = (
    df
    .clean_names()              # "Nom Client" -> "nom_client"
    .remove_empty()             # Vire les lignes/cols vides
    .rename_column("a", "b")    # Renommage simple
    .drop_constant_columns()    # Vire les colonnes qui ont partout la même valeur
)
```

### 4. Code Impeccable (`ruff`)
Avant de commit sur GitHub, lance ça à la racine du projet :
```bash
ruff check . --fix  # Corrige les erreurs
ruff format .       # Reformate tout le code (comme Black)
```

### 5. Visualisation — Quand utiliser quoi ?

| Outil | Type | Quand l'utiliser |
|---|---|---|
| `matplotlib` / `plt` | Statique | Analyse rapide pour toi, debug |
| `seaborn` / `sns` | Statique | Graphiques stat propres, rapports PDF |
| `plotly` | **Interactif** | Dashboard client, présentation, portfolio |

**La règle :**
```
Analyse rapide pour toi     → seaborn / matplotlib
Rapport / Dashboard client  → plotly
```

**Pourquoi Plotly pour un dashboard manager ?**
- Hover → voir le chiffre exact en survolant
- Zoom → explorer une période
- Filtres visuels → sans régénérer le graphique

> 💡 **Formulation entretien :** *"J'ai choisi Plotly plutôt que Seaborn car mon dashboard est destiné à des managers non-techniques. L'interactivité permet d'explorer les données sans avoir à régénérer des graphiques."*

### 6. Visualisation Géospatial (`kepler.gl`)
Si tu as des données GPS (trains, trajets) :
```python
from keplergl import KeplerGl
map = KeplerGl(height=600)
map.add_data(data=df, name="Trains")
map.save_to_html(file_name="map.html")
```

---

## ⚠️ Règle d'Or : Toujours Configurer le `.venv` AVANT de Coder

> **Principe :** chaque projet = son propre environnement isolé.
> Sans ça → conflits de versions, bugs inexplicables, "ça marche chez moi mais pas ailleurs".

---

### 🆕 Démarrer un Nouveau Projet — Procédure Complète

```bash
# 1. Créer le dossier et se placer dedans
mkdir mon_projet && cd mon_projet

# 2. Créer l'environnement virtuel
python -m venv .venv

# 3. L'activer
source .venv/bin/activate        # Linux / Mac
# .venv\Scripts\activate         # Windows

# 4. Installer les packages nécessaires
pip install streamlit pandas plotly jupyter ipykernel

# 5. Sauvegarder les dépendances (important pour GitHub)
pip freeze > requirements.txt

# 6. Enregistrer comme kernel Jupyter
python -m ipykernel install --user --name="mon-projet" --display-name="🚆 Mon Projet"

# 7. Ajouter .venv au .gitignore
echo ".venv/" >> .gitignore
```

**Dans Jupyter :** Menu **Kernel** → **Change Kernel** → choisir `🚆 Mon Projet`

---

### 🔄 Reprendre un Projet Existant

```bash
cd mon_projet
source .venv/bin/activate        # toujours activer en premier !
```

> 💡 **Comment savoir si le venv est actif ?**
> Le nom du venv apparaît au début de la ligne dans le terminal : `(.venv) ➜`

---

### 📦 Installer les packages d'un projet cloné depuis GitHub

```bash
git clone https://github.com/...
cd le-projet
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # installe exactement les mêmes versions
```

---

### ❌ Ce qu'il ne faut JAMAIS faire

| ❌ Mauvaise pratique | ✅ Bonne pratique |
|---|---|
| `sudo pip install pandas` | `pip install pandas` dans le venv |
| Partager le dossier `.venv` sur GitHub | Mettre `.venv/` dans `.gitignore` |
| Un seul venv pour tous les projets | Un venv par projet |
| Oublier `pip freeze > requirements.txt` | Le faire avant chaque commit important |

---

> 💬 **Formulation entretien :**
> *"J'isole chaque projet dans un environnement virtuel pour garantir la reproductibilité. N'importe qui peut cloner le repo, faire `pip install -r requirements.txt` et obtenir exactement le même résultat."*

---

## 📝 Checklist Avant de Clôturer un Projet
- [ ] Le code est formaté avec `ruff`.
- [ ] Un rapport `ydata-profiling` a été généré pour prouver l'analyse.
- [ ] Le dossier `data/` est exclu du git (`.gitignore`).
- [ ] Il y a un `README.md` clair qui explique comment lancer le projet.
