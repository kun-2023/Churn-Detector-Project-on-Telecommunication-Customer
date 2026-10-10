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
    --port 5000 \
    --workers 1
```

#### Connect DVC to AWS s3
```bash
aws sts get-caller-identity
# if credentials ok then:
dvc remote add -d storage s3://churn-detector/dvc-cache
# confirm
dvc remote list
```

#### train pipeline 
```bash

dvc repro
# then manually register and promote the model
python -m register_promote register
python -m register_promote promote
```
#### to run app
```bash
dvc pull
```