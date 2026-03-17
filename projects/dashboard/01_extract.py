"""
Étape 1 : Extract — Téléchargement des données Infrabel
Source : opendata.infrabel.be
Dataset : nationale-stiptheid-per-maand (Ponctualité nationale mensuelle)

Auteur  : Tahar Guenfoud
Date    : 2026-03-08
"""

import requests
import pandas as pd
import os

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────
API_URL = (
    "https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/"
    "nationale-stiptheid-per-maand/exports/csv"
    "?lang=fr&timezone=Europe%2FBrussels&use_labels=true&delimiter=%3B"
)

RAW_DIR  = os.path.join(os.path.dirname(__file__), "data", "raw")
OUT_FILE = os.path.join(RAW_DIR, "infrabel_ponctualite_mensuelle.csv")


def download_data(url: str, dest: str) -> None:
    """Télécharge le CSV depuis l'API Infrabel et le sauvegarde localement."""
    print(f"📡 Téléchargement depuis :\n   {url}\n")

    response = requests.get(url, timeout=60)
    response.raise_for_status()          # Lève une erreur si HTTP 4xx/5xx

    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(response.content)

    print(f"✅ Fichier sauvegardé : {dest}")
    print(f"   Taille : {len(response.content) / 1024:.1f} Ko\n")


def preview_data(filepath: str) -> pd.DataFrame:
    """Charge et affiche un aperçu du fichier téléchargé."""
    # Infrabel utilise le séparateur point-virgule
    df = pd.read_csv(filepath, sep=";", encoding="utf-8")

    print("─" * 60)
    print(f"📊 Aperçu des données ({df.shape[0]} lignes × {df.shape[1]} colonnes)")
    print("─" * 60)
    print("\n🔍 Colonnes disponibles :")
    for col in df.columns:
        print(f"   • {col}")
    print("\n🧾 Premières lignes :")
    print(df.head(5).to_string(index=False))
    print("\n📈 Types de données :")
    print(df.dtypes.to_string())
    print("\n🚨 Valeurs manquantes :")
    print(df.isnull().sum().to_string())

    return df


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  PROJET 3 — DASHBOARD SNCB/INFRABEL")
    print("  Étape 1 : Extraction des données")
    print("=" * 60 + "\n")

    # 1. Télécharger
    download_data(API_URL, OUT_FILE)

    # 2. Prévisualiser
    df = preview_data(OUT_FILE)

    print("\n✅ Extraction terminée. Prêt pour l'Étape Transform !")
