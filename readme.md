## Churn Detector Project on Telecommunication Customers
### Project Overview
1. The project is to making an pp that predict customer churn for a telecommunication company, so the firm would be able to identify potential churned customers
2. The app demostrates Visualization analysis of the customer data to showcase customers who are likely to churn and features that are most correlated to churn. It also display model metrics performances. Finally it will allow users to make churn predictions by entering information about customers
3. Tech Stack: Python, Scikit-learn, Xgboost, FastAPI, DVC, MLflow, Streamlit, AWS ECR, ECS, Pytest, Git/Github, GitHub Action
4. Automation pipelines: 1. MLflow + DVC training piple. It allows automatica model retraining by typing `dvc repro` in bash; 2. CI/CD pipeline. It allows reintegration and redeployment of the application by simplely typing `git push` in bash.

### How to run apps on your local machine
#### Option 1: Run with Docker (Recommended)
```bash
# Enter thos commands in bash
# 1. clone the repository
git clone https://github.com/kun-2023/Churn-Detector-Project-on-Telecommunication-Customer.git

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

# 7. Download models and data from DVC remote repository s3
dvc pull

# 8 build docker images and run apps with those images
# make sure you turn on Docker Desktop app before proceeding
docker compose up --build -d

# 9 enter http://localhost:8501 in google browser or any browser of your choices. And play with the app.

# 10 After it's finished, stop and remove docker images
docker compose down
```

#### option 2: Run Locally without Docker
```bash
# Enter those commands in bash
# 1 Clone the repo
git clone https://github.com/kun-2023/Churn-Detector-Project-on-Telecommunication-Customer.git

# 2 Navigate to the folder
cd churn_detector

# 3 Create virtul enviroment and activate it
python -m venv .churn_venv
source .churn_venv/Scripts/activate

# 4 Install libraries
pip install -r requirements.txt

# 5 copy enviroment variables
cp .env.example .env

# 6 download the data and the models from s3
dvc pull

# 7 Turn on FastAPI servers. 
# Documentation: http://127.0.0.1:8000/docs
uvicorn api.main:app --reload

# 8 Turn on Streamlit server
streamlit run streamlit/app.py
# open browser: http://localhost:8501
```


### How To retrain model (Assume You have finished the first 7 steps of option 1 or the first 6 steps of option 2)
```bash
# 1 Turn on mlflow services
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --artifacts-destination ./mlartifacts \
    --host 127.0.0.1 \
    --port 5000 \
    --workers 1

# go to MLflow ui by clicking http://127.0.0.1:5000

# 2 retrain the model with dvc
dvc repro

# 3 Go to MLflow UI (http://127.0.0.1:5000) to examine the metrics, params and model artifacts
```
`Thanks for Reading`