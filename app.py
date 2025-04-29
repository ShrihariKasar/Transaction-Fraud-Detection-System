from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("fraud_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

# All features from the dataset
all_features = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

# Features used by the model (you can customize these if your model uses different ones)
used_features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'Amount']

@app.route('/')
def home():
    return render_template('index.html', features=all_features)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(request.form[f]) for f in all_features]
    input_df = pd.DataFrame([input_data], columns=all_features)

    model_input = input_df[used_features]  # select only used columns
    scaled = scaler.transform(model_input)
    prediction = model.predict(scaled)[0]

    result = "⚠️ Fraudulent Transaction Detected!" if prediction == 1 else "✅ Legitimate Transaction"
    return render_template('result.html', result=result)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return "No file uploaded!"

    df = pd.read_csv(file)
    if df.shape[1] != 30:
        return "CSV must have exactly 30 columns (Time, V1–V28, Amount)"

    model_input = df[used_features]  # only the 20 columns expected by model
    scaled = scaler.transform(model_input)
    predictions = model.predict(scaled)
    df['Prediction'] = ['Fraud' if p == 1 else 'Legit' for p in predictions]

    return df.to_html(classes="table table-bordered", index=False)

if __name__ == '__main__':
    app.run(debug=True)
