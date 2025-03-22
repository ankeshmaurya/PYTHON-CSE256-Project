import pandas as pd

def estimate_bill(energy_usage, tariff_rate=0.12):
    return round(energy_usage * tariff_rate, 2)

def process_billing(data_path="data/anomaly_detected.csv"):
    df = pd.read_csv(data_path)
    df['EstimatedBill'] = df['EnergyUsage'].apply(estimate_bill)
    df.to_csv("data/billing_data.csv", index=False)
    print("🔹 Billing data updated!")

if __name__ == "__main__":
    process_billing()
