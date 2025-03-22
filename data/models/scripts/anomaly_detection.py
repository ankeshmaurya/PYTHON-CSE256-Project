import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data_path="data/energy_data.csv"):
    df = pd.read_csv(data_path)
    model = IsolationForest(contamination=0.02)  # 2% anomalies
    df['Anomaly'] = model.fit_predict(df[['EnergyUsage']])
    df.to_csv("data/anomaly_detected.csv", index=False)
    print("🔹 Anomaly detection completed!")

if __name__ == "__main__":
    detect_anomalies()
    print("🔹 Anomalies detected and saved!")