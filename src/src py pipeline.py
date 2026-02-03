# src/cleaning.py (Pipeline)

import pandas as pd
import numpy as np

def clean_airbnb(df):
    """
    Nettoyage et feature engineering du dataset NYC Airbnb 2019.
    
    Étapes incluses :
    - Renommage des colonnes
    - Suppression des colonnes inutiles
    - Correction des types
    - Gestion des valeurs manquantes
    - Nettoyage des outliers
    - Feature engineering
    - Conversion des colonnes catégorielles
    """

    # ---------------------------
    # 1. Renommer les colonnes
    # ---------------------------
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # ---------------------------
    # 2. Supprimer colonnes inutiles
    # ---------------------------
    cols_to_drop = ["name", "host_name"]
    df = df.drop(columns=cols_to_drop)

    # ---------------------------
    # 3. Correction des types
    # ---------------------------
    df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")

    # ---------------------------
    # 4. Gestion des NaN
    # ---------------------------
    # reviews_per_month : remplacer NaN par 0
    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
    
    # last_review : conserver NaT, information métier
    df["has_reviews"] = np.where(df["number_of_reviews"] > 0, 1, 0)

    # ---------------------------
    # 5. Nettoyage des outliers
    # ---------------------------
    # Price : 100 <= price <= 2000
    df = df[(df["price"] >= 100) & (df["price"] <= 2000)]
    
    # minimum_nights : 1 <= minimum_nights <= 365
    df = df[(df["minimum_nights"] >= 1) & (df["minimum_nights"] <= 365)]

    # ---------------------------
    # 6. Feature engineering
    # ---------------------------
    # Nombre d'annonces par host
    host_listing_counts = df.groupby("host_id")["id"].count().reset_index()
    host_listing_counts.rename(columns={"id": "host_total_listings"}, inplace=True)
    df = df.merge(host_listing_counts, on="host_id", how="left")
    
    # Hôte professionnel (>1 annonce)
    df["host_is_professional"] = np.where(df["host_total_listings"] > 1, 1, 0)

    # Prix moyen par quartier
    avg_price_neighbourhood = df.groupby("neighbourhood_group")["price"].mean().reset_index()
    avg_price_neighbourhood.rename(columns={"price": "avg_price_neighbourhood"}, inplace=True)
    df = df.merge(avg_price_neighbourhood, on="neighbourhood_group", how="left")

    # Disponibilité en %
    df["availability_pct"] = (df["availability_365"] / 365) * 100

    # Normalisation reviews_per_month
    df["reviews_per_month_scaled"] = df["reviews_per_month"] / df["reviews_per_month"].max()

    # One-hot encoding pour room_type
    df = pd.get_dummies(df, columns=["room_type"], prefix="room")

    # ---------------------------
    # 7. Conversion des colonnes catégorielles
    # ---------------------------
    df["neighbourhood_group"] = df["neighbourhood_group"].astype("category")
    df["neighbourhood"] = df["neighbourhood"].astype("category")

    # ---------------------------
    # 8. Reset index
    # ---------------------------
    df = df.reset_index(drop=True)

    return df


# ---------------------------
# Exemple d'utilisation
# ---------------------------
if __name__ == "__main__":
    # Charger le CSV brut
    df_raw = pd.read_csv("../data/raw/AB_NYC_2019.csv")
    
    # Nettoyer
    df_clean = clean_airbnb(df_raw)
    
    # Export CSV
    df_clean.to_csv("../data/cleaned/AB_NYC_2019_cleaned.csv", index=False)
    print("Dataset nettoyé et exporté !")
