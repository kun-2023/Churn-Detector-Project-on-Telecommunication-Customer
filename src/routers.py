from fastapi import APIRouter
from api.schemas import ChurnDetectorRequest
from api.services import predict_churn

router=APIRouter()

@router.post("/predict")
def churn_status(request: ChurnDetectorRequest):
    result=predict_churn(request.model_dump())
    return {"churn_prediction": result}