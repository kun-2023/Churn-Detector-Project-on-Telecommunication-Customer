import pandas as pd
import joblib
from pathlib import Path

from api.settings import MODEL_PATH


def load_churn_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Risk model file not found at: {MODEL_PATH}"
        )
    model=joblib.load(MODEL_PATH)
    return model

def predict_churn(data: dict):
    model=load_churn_model()
    df=pd.DataFrame([data])
    prediction=int(model.predict(df)[0]) # prediction is int
    probability=float(model.predict_proba(df)[0,1])
    return prediction, probability