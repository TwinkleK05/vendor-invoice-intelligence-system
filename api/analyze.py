import joblib
import pandas as pd
from pathlib import Path

# -------------------------------------------------------
# Model Paths
# -------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

FREIGHT_MODEL_PATH = BASE_DIR / "models" / "predict_freight_model.pkl"
FLAG_MODEL_PATH = BASE_DIR / "models" / "predict_flag_invoice.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
# -------------------------------------------------------
# Load Models (Only Once)
# -------------------------------------------------------

freight_model = joblib.load(FREIGHT_MODEL_PATH)
flag_model = joblib.load(FLAG_MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# -------------------------------------------------------
# Analyze Invoice
# -------------------------------------------------------

def analyze_invoice(request):

    # ===============================================
    # Step 1
    # Freight Prediction
    # ===============================================

    freight_input = pd.DataFrame(
        {
            "Dollars": [request.invoice_dollars]
        }
    )

    predicted_freight = float(
        freight_model.predict(freight_input)[0]
    )

    # ===============================================
    # Step 2
    # Build Classification Features
    # ===============================================

    classification_input = pd.DataFrame(
        {
            "invoice_quantity": [
                request.invoice_quantity
            ],

            "invoice_dollars": [
                request.invoice_dollars
            ],

            "Freight": [
                predicted_freight
            ],

            "total_item_quantity": [
                request.total_item_quantity
            ],

            "total_item_dollars": [
                request.total_item_dollars
            ]
        }
    )

    # ===============================================
    # Step 3
    # Scale Features
    # ===============================================

    scaled_input = scaler.transform(
        classification_input
    )

    # ===============================================
    # Step 4
    # Predict Risk
    # ===============================================

    invoice_flag = int(
        flag_model.predict(scaled_input)[0]
    )

    # ===============================================
    # Step 5
    # Business Logic
    # ===============================================

    risk_status = (
        "Flagged"
        if invoice_flag == 1
        else "Low Risk"
    )

    freight_ratio = round(
        (predicted_freight / request.invoice_dollars)
        * 100,
        2
    )

    # ===============================================
    # Return
    # ===============================================

    return {
        "predicted_freight": round(
            predicted_freight,
            2
        ),

        "invoice_flag": invoice_flag,

        "risk_status": risk_status,

        "freight_ratio": freight_ratio
    }