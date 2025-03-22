from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    df = pd.read_csv("data/anomaly_detected.csv").tail(100)  # Fetch latest 100 records
    return jsonify(df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
