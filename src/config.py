from pathlib import Path

# folder
ROOT_FOLDER=Path(__file__).resolve().parents[1]
MODEL_FOLDER=ROOT_FOLDER/"outputs/models"
SPLITDATA_FOLDER=ROOT_FOLDER/"outputs/split_data"
# data & model
DATA_PATH=ROOT_FOLDER/"data/data.csv"
CLEAN_DATA_FOLDER=ROOT_FOLDER/"outputs/clean_data"
CLEAN_DATA_PATH=CLEAN_DATA_FOLDER/"clean_data.csv"
MODEL_PATH=MODEL_FOLDER/"churn_model.pkl"
X_TRAIN_PATH=SPLITDATA_FOLDER/"X_train.csv"
Y_TRAIN_PATH=SPLITDATA_FOLDER/"y_train.csv"
X_TEST_PATH=SPLITDATA_FOLDER/"X_test.csv"
Y_TEST_PATH=SPLITDATA_FOLDER/"y_test.csv"

# Variables
NUM_COLS=['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']
CAT_COLS=['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
RANDOM_SEED=42
TARGET_VARIABLE="Churn_Label"

# Model Parameter
N_ESTIMATORS=100
MAX_DEPTH=5
LEARNING_RATE=0.05
MIN_CHILD_WEIGHT=2
SUBSAMPLE=1.0
SCALE_POS_WEIGHT=2.768561872909699
OBJECTIVE="binary:logistic"
EVAL_METRIC="logloss"
RANDOM_STATE=42

# metrics
FRONTEND_DATA_DIR=ROOT_FOLDER/"outputs/frontend_data"
METRICS_PATH=FRONTEND_DATA_DIR/"metrics.csv"
FEATURE_IMPORTANCE_PATH=FRONTEND_DATA_DIR/"feature_importance.csv"
CONFUSION_MATRIX_PATH=FRONTEND_DATA_DIR/"confusion_matrix.csv"
# mlflow
TRACKING_URI="http://127.0.0.1:5000"
EXPERIMENT_NAME="churn_detector"
CANDIDATE_ALIAS="candidate"
CHAMPION_ALIAS="champion"
RUN_NAME="xgb_classifier"
REGISTERED_MODEL_NAME="optimized_xgb_churn_detector"
ARTIFACT_URI=(ROOT_FOLDER/"mlartifacts").as_uri()



