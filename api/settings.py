import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR=Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR/".env")

API_TITLE=os.getenv(
    "API_TITLE",
    "Customer Churn Detector"
)

MODEL_PATH=Path(
os.getenv(
    "MODEL_PATH",
    "outputs/models/churn_model.pkl"
)
)

if not MODEL_PATH.is_absolute():
    MODEL_PATH=BASE_DIR/MODEL_PATH