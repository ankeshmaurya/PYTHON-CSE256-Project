import streamlit as st
import pandas as pd
from data.generate_data import generate_data
from scripts.anomaly_detection import detect_anomalies
from scripts.billing import process_billing
from notifications.alerts import check_anomalies

def run_pipeline():
    print("🚀 Running NeuroGrid AI System...")
    generate_data()
    detect_anomalies()
    process_billing()
    check_anomalies()
    print("✅ System execution completed!")

if __name__ == "__main__":
    run_pipeline()
