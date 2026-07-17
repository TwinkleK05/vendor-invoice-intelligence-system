from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from pathlib import Path

from api.schemas import (
    FreightPredictionRequest,
    FreightPredictionResponse,
    AnalyzeRequest,
    AnalyzeResponse,
)

from api.analyze import analyze_invoice
# =====================================================
# APP
# =====================================================

app = FastAPI(
    title="Invoice Intelligence API",
    version="2.0"
)

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# LOAD FREIGHT MODEL
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR /
    "models" /
    "predict_freight_model.pkl"
)

freight_model = joblib.load(MODEL_PATH)

# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {
        "application": "Invoice Intelligence API",
        "status": "Running"
    }

# =====================================================
# EXISTING FREIGHT PREDICTION
# =====================================================

@app.post(
    "/predict",
    response_model=FreightPredictionResponse
)
def predict(request: FreightPredictionRequest):

    df = pd.DataFrame(
        {
            "Dollars": [
                request.Dollars
            ]
        }
    )

    prediction = float(
        freight_model.predict(df)[0]
    )

    return {
        "predicted_freight": round(
            prediction,
            2
        )
    }

# =====================================================
# NEW ANALYZE ENDPOINT
# =====================================================

@app.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(request: AnalyzeRequest):

    result = analyze_invoice(request)

    return result