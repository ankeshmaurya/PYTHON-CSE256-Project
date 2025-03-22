import pandas as pd
import numpy as np

def generate_data(samples=1000):
    np.random.seed(42)
    time_stamps = pd.date_range("2024-01-01", periods=samples, freq='H')
    temperature = np.random.randint(15, 35, size=samples)
    humidity = np.random.randint(30, 80, size=samples)
    energy_usage = np.random.randint(100, 1000, size=samples) + temperature * 2 - humidity * 1.5
    
    df = pd.DataFrame({'Timestamp': time_stamps, 'Temperature': temperature, 
                       'Humidity': humidity, 'EnergyUsage': energy_usage})
    df.to_csv("data/energy_data.csv", index=False)
    return df

if __name__ == "__main__":
    generate_data()
    print("🔹 Energy data generated successfully!")
