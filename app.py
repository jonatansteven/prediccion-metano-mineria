from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('modelo_final/modelo_metano.pkl')
scaler = joblib.load('modelo_final/scaler.pkl')
features = joblib.load('modelo_final/features.pkl')

@app.route('/')
def home(): return "<h1>API Predicción de Metano - Boyacá</h1><p>POST /predict</p>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    O2_min = float(data['O2_min']); O2_max = float(data['O2_max'])
    CO = float(data['CO']); H2S = float(data['H2S']); Temp = float(data['Temp'])
    O2_avg = (O2_min + O2_max) / 2
    X = scaler.transform([[O2_min, O2_max, O2_avg, CO, H2S, Temp]])
    pred = float(model.predict(X)[0])
    riesgo = "ALTO" if pred > 1.5 else "MODERADO" if pred > 1.0 else "BAJO"
    return jsonify({"prediccion_metano": round(pred,3), "nivel_riesgo": riesgo})
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)