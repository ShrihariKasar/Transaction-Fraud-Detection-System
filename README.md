# Transaction Fraud Detection System

This project is a **Transaction Fraud Detection System** that uses a machine learning model to classify whether a financial transaction is fraudulent or legitimate. It is built using **Python (Flask)** and includes a trained model and scaler for accurate predictions.

---

## 📁 Project Structure

```
Transaction Fraud Detection System/
├── app.py                         # Flask application
├── fraud_detection_model.pkl      # Trained ML model (Pickle file)
├── scaler.pkl                     # Feature scaler used in training
├── sample_test_transactions.csv   # Sample data for testing
└── templates/
    ├── index.html                 # Main input form
    └── result.html                # Result display page
```

---

## 🚀 Features

- Upload transaction data or manually enter it
- Predict fraud using a trained machine learning model
- Scaled inputs using a pre-trained scaler
- Clean and responsive web interface

---

## 🛠️ Installation

1. Clone the repository or download the ZIP.

2. Navigate to the project directory:
   ```bash
   cd "Transaction Fraud Detection System"
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> **Note:** If `requirements.txt` is not present, install Flask manually:
```bash
pip install flask
```

---

## 🧠 How It Works

- The backend loads the trained model and scaler.
- The user submits transaction features via the form.
- The app preprocesses the input using the scaler.
- The model predicts if the transaction is **Fraudulent** or **Legitimate**.
- The result is displayed to the user.

---

## 💡 Usage

1. Start the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Enter transaction details and get predictions instantly.

---

## 📊 Sample Data

Use the provided `sample_test_transactions.csv` to simulate multiple predictions or test model accuracy manually.

---

## 👨‍💻 Authors

- **Shrihari Kasar**
- **Utkarsha Kakulte**
- **Rohit Khadangle**

---

## 📃 License

This project is open source and free to use for educational purposes.
```