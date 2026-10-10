import pandas as pd
import joblib
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parents[1]

MODELS_DIR=BASE_DIR/"outputs/models"
CHURN_MODEL_PATH=MODELS_DIR/"churn_model.pkl"

def load_churn_model():
    if not CHURN_MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Risk model file not found at: {CHURN_MODEL_PATH}"
        )
    model=joblib.load(CHURN_MODEL_PATH)
    return model

def predict_churn(data: dict):
    model=load_churn_model()
    df=pd.DataFrame([data])
    prediction=int(model.predict(df)[0]) # prediction is int
    probability=float(model.predict_proba(df)[0,1])
    return prediction, probability