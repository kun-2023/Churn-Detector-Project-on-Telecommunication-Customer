## Churn Detector Project on Telecommunication Customers


#### navigate to the folder and create environment
```bash
cd churn_detector
# create .churn_venv
python -m venv .churn_venv
# activate the environment
source .churn_venv/Scripts/activate
```
#### Turn on MLflower server before re-training models
```bash
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --artifacts-destination ./mlartifacts \
    --host 127.0.0.1 \
    --port 5000
```