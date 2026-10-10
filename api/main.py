from fastapi import FastAPI
from api import routers

app=FastAPI(title="Customer Churn Detector")

@app.get("/")
def root():
    return {"message": "Customer Churn Detector is running."}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(
    routers.router, 
    tags=["Customer Churn Predictor"])
