# TOOLS.md — Environment & Outils Tahar

## Chemins Importants

### Workspace
- **Workspace DS :** `/home/tahar/.openclaw/workspace-ds/`
- **Workspace principal (Nox) :** `/home/tahar/.openclaw/workspace/`
- **Code directory :** `/home/tahar/Code/`

### Projets Data Science
- **Blackspots :** `~/Code/projects/blackspots/` (notebook principal)
- **Dashboard :** `~/Code/projects/dashboard/`
- **EDA Gares :** `~/Code/projects/EDA_Gares_Infrabel/`
- **Jargon SNCB/Infrabel :** `~/Code/projects/INFRABEL_SNCB_Jargon_Technique.md`
- **Storytelling :** `~/Code/projects/STORYTELLING_Entretien.md`
- **Stack Workflow :** `~/Code/projects/STACK_Workflow.md`

### Job Search
- **CV :** `~/Code/job-search/cv/` (versions HTML + PDF)
  - `cv_optimised.html` — CV principal
  - `cv_infrabel_traineeship.html` — CV adapté Infrabel
  - `CV_Tahar_Guenfoud_avec_photo.pdf` — PDF avec photo
- **Portfolio :** `~/Code/job-search/portfolio/` (Astro)
- **Lettres :** `~/Code/job-search/letters/`
- **Tracking :** `~/Code/job-search/tracking/`
- **Stratégie :** `~/Code/job-search/TAHAR_MEMOIRE_STRATEGIE.md`
- **Skills :** `~/Code/job-search/skills/powerbi_plan.md`

### Formations
- **Maven Analytics :** `~/Code/learning/maven_analytics/`
- **Maven Projets :** `~/Projet/Maven/`

### Windows ↔ WSL
- Windows `C:\Users\tahar\...` → WSL `/mnt/c/Users/tahar/...`
- **DataScience docs :** `C:\Users\tahar\Documents\DataScience\`
  - `guide_entretien_data_tahar.docx`
  - `guide_pourquoi_data_analyst.docx`
  - `questions_reelles_entretien_infrabel.docx`

### Downloads CV
- `~/Downloads/CV_Tahar_Guenfoud_Data_v2.pdf`
- `~/Downloads/CV_Tahar_Guenfoud_Data_v3.pdf`

## Python & Environment
- **Version :** 3.10.11 (pyenv)
- **Jupyter :** 6.5.7
- **Règle :** 1 projet = 1 venv
- **Lancer :** `jupyter notebook` depuis le dossier projet
- **Kernel registration :** `python -m ipykernel install --user --name="projet" --display-name="🚆 Projet"`

## Stack Data Science
- **EDA :** `ydata-profiling` (rapport HTML auto)
- **Nettoyage :** `pyjanitor` (chaining)
- **Visualisation :** `plotly` (interactif), `seaborn` (statique)
- **Qualité code :** `ruff`
- **Dashboard :** `streamlit`
- **Géospatial :** `folium`, `kepler.gl`
- **ML :** `scikit-learn` (Random Forest, XGBoost)

## Git Convention
```
feat: ajout analyse tendance mensuelle Plotly
fix: correction séparateur CSV
docs: ajouter DECISIONS.md
data: mettre à jour coordonnées GPS gares
```

## OpenClaw
- **Gateway :** ws://127.0.0.1:18789
- **Studio :** http://localhost:3000
- **Agent main (Nox) :** openrouter/hunter-alpha
- **Agent DS (nous) :** qwen (Qwen Coder)
- **Agent prof :** sonnet (Claude Sonnet 4)
- **Agent lingua :** openrouterkimi (Kimi K2.5)

<!-- clawx:begin -->
## ClawX Tool Notes

### uv (Python)

- `uv` is bundled with ClawX and on PATH. Do NOT use bare `python` or `pip`.
- Run scripts: `uv run python <script>` | Install packages: `uv pip install <package>`

### Browser

- `browser` tool provides full automation (scraping, form filling, testing) via an isolated managed browser.
- Flow: `action="start"` → `action="snapshot"` (see page + get element refs like `e12`) → `action="act"` (click/type using refs).
- Open new tabs: `action="open"` with `targetUrl`.
- To just open a URL for the user to view, use `shell:openExternal` instead.
- If a browser action fails, transient errors (timeout, network) can often be resolved by retrying once or navigating to a different URL.
- When asked to search, look up, or interact with a web page, use the browser tool. Do not substitute with guesses or training data when real-time web access is requested.
<!-- clawx:end -->
