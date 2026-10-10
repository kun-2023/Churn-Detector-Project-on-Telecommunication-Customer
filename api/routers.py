from fastapi import APIRouter
from api.schemas import ChurnDetectorRequest
from api.services import predict_churn

router=APIRouter()

@router.post("/predict")
def churn_status(request: ChurnDetectorRequest):
    prediction, probability=predict_churn(request.model_dump())
    return {"churn_prediction": prediction, 
            "churn_probability": f"{round(probability*100,2)}%"}