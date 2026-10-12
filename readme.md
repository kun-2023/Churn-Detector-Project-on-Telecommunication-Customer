## Churn Detector Project on Telecommunication Customers


#### How to run apps on your local machine
```bash
# 1. clone the repository
git clone <repository-url>

# 2. Navigate to folder
cd churn_detector

# 3. create .churn_venv
python -m venv .churn_venv

# 4. activate the environment
source .churn_venv/Scripts/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. clone .env file
cp .env.example .env

# 7. Download models and data from DVC remote
dvc pull

# 8. Start the FastAPI application
uvicorn api.main:app --reload
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