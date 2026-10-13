import numpy as np
from api import services

def test_predict_churn(monkeypatch):
    class FakeModel:

        def predict(self, X):
            return [1]

        def predict_proba(self, X):
            return np.array([[0.2, 0.8]])

    monkeypatch.setattr(
        services,
        "load_churn_model",
        lambda: FakeModel()
    )

    prediction, probability=services.predict_churn(
        {"tenure": 12, "MonthlyCharges": 70.0}
    )

    assert prediction==1
    assert probability==0.8