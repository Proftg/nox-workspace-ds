# 📊 Projet 3 : Dashboard Qualité de Service (SNCB/Infrabel)

## 🎯 Objectif
Créer un tableau de bord interactif (Streamlit ou PowerBI) qui permet à un manager de visualiser la **ponctualité** et la **fiabilité** du réseau ferroviaire belge.

## 📅 Feuille de Route (Plan de Bataille)

### Étape 1 : Préparation des Données (ETL)
- [ ] **Extract** : Télécharger les données mensuelles de ponctualité sur OpenData Infrabel.
- [ ] **Transform** :
  - Nettoyer les dates (format datetime).
  - Gérer les valeurs manquantes.
  - Créer une colonne "Retard_Minutes" (car les données brutes sont souvent en secondes).
  - Créer une colonne "Statut" : À l'heure (<6min), Retard léger (6-15min), Retard grave (>15min), Annulé.
- [ ] **Load** : Sauvegarder en CSV propre ou SQLite local.

### Étape 2 : Analyse Exploratoire (EDA)
- [ ] Calculer le **Taux de Ponctualité Global** (Trains à l'heure / Total trains).
- [ ] Identifier les **Lignes les plus problématiques** (Top 5 des pires lignes).
- [ ] Analyser la **Tendance Temporelle** (Est-ce que ça empire en hiver ?).

### Étape 3 : Création des KPIs Métier (Le "Jargon" Infrabel)
- [ ] **Punctuality** : % de trains arrivés avec < 6 min de retard.
- [ ] **Reliability** : % de trains non annulés.
- [ ] **Minutes Perdues** : Somme totale des minutes de retard (impact économique).

### Étape 4 : Visualisation & Dashboard
- [ ] **KPI Cards** en haut : Gros chiffres (Ponctualité Mois M, Variation vs M-1).
- [ ] **Graphique de Tendance** (Line Chart) : Ponctualité sur 12 mois.
- [ ] **Top Flop** (Bar Chart) : Les 5 gares/lignes avec le plus de retards.
- [ ] **Heatmap** : Jours/Heures les plus critiques (ex: Lundi matin 8h).

### Étape 5 : Storytelling (Pour l'entretien)
- [ ] Préparer 3 "insights" clés à raconter. (Ex: "J'ai découvert que les retards du mardi matin sont corrélés à...")
- [ ] Expliquer tes choix de design ("J'ai mis les KPIs en haut pour que le manager voie l'essentiel en 3 secondes").

## 📁 Répertoire de Travail
`/home/tahar/Code/projects/dashboard/`

## 🛠️ Stack Technique Conseillée
- **Python** (Pandas pour le traitement)
- **Streamlit** (Pour l'interface web rapide et pro)
- **Plotly** (Pour les graphiques interactifs)
