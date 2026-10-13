from fastapi.testclient import TestClient
from api.main import app

client=TestClient(app)

def test_root():
    response=client.get("/")

    assert response.status_code==200
    assert response.json()=={
        "message": "Customer Churn Detector is running."
    }

def test_health():
    response=client.get("/health")

    assert response.status_code==200
    assert response.json()=={"status": "ok"}

def test_predict(monkeypatch):
    monkeypatch.setattr(
        "api.routers.predict_churn",
        lambda data: (1, 0.75)
    )

    payload={
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.0,
        "TotalCharges": 840.0

    }

    response=client.post("/predict", json=payload)

    assert response.status_code==200
    assert response.json()["churn_prediction"]==1
    assert response.json()["churn_probability"]=="75.0%"

def test_invalid_prediction():
    response=client.post("/predict", json={})
    assert response.status_code==422
