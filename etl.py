import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")
    df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

    df["duration_min"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60

    df = df.dropna(subset=["trip_id", "zone", "duration_min", "distance_km", "battery_start"])
    df = df[df["duration_min"] > 0]
    df = df[df["distance_km"] >= 0]

    return df

def compute_kpis(df: pd.DataFrame) -> dict:
    return {
        "nb_trajets": int(df["trip_id"].nunique()),
        "distance_moyenne_km": round(df["distance_km"].mean(), 2),
        "duree_moyenne_min": round(df["duration_min"].mean(), 2),
        "batterie_moyenne_depart": round(df["battery_start"].mean(), 2),
        "top_zone": df["zone"].value_counts().idxmax()
    }

def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["anomaly_long_trip"] = df["duration_min"] > 60
    df["anomaly_short_trip"] = df["duration_min"] < 2
    df["anomaly_low_battery"] = df["battery_start"] < 15
    return df

def main():
    path = "data/trottinettes.csv"

    df_raw = load_data(path)
    df_clean = clean_data(df_raw)

    print("=== KPI ===")
    kpis = compute_kpis(df_clean)
    for k, v in kpis.items():
        print(f"{k}: {v}")

    df_anom = detect_anomalies(df_clean)
    anomalies = df_anom[df_anom[["anomaly_long_trip", "anomaly_short_trip", "anomaly_low_battery"]].any(axis=1)]

    print("\n=== Anomalies (extrait) ===")
    cols = ["trip_id", "zone", "duration_min", "distance_km", "battery_start",
            "anomaly_long_trip", "anomaly_short_trip", "anomaly_low_battery"]
    print(anomalies[cols].head(10))

if __name__ == "__main__":
    main()
