import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
from sklearn.impute import SimpleImputer
from config import (NUM_COLS, CAT_COLS, RANDOM_SEED, TARGET_VARIABLE,
                    N_ESTIMATORS, MAX_DEPTH, LEARNING_RATE, MIN_CHILD_WEIGHT,
                    SUBSAMPLE, SCALE_POS_WEIGHT, OBJECTIVE,EVAL_METRIC,
                    MODEL_FOLDER, TRACKING_URI, EXPERIMENT_NAME, RUN_NAME,
                    CLEAN_DATA_PATH)
from sklearn.metrics import (accuracy_score, 
                             recall_score, 
                             precision_score,
                             f1_score, roc_auc_score
                              )
import joblib
import random
import mlflow


def train():
    df=pd.read_csv(CLEAN_DATA_PATH)
    random.seed(RANDOM_SEED)
    # MLFLOW SET UP
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)
    with mlflow.start_run(run_name=RUN_NAME):
        X=df[NUM_COLS+CAT_COLS]
        y=df[TARGET_VARIABLE]
        X_train, X_test, y_train, y_test=train_test_split(
            X,y, test_size=0.2,
            random_state=RANDOM_SEED,
            stratify=y
        )
        num_pipeline=Pipeline([
            ("imputer", SimpleImputer(strategy="median"))
        ])
        cat_pipeline=Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ])


        preprocessor=ColumnTransformer([
            ("num", num_pipeline, NUM_COLS),
            ("cat", cat_pipeline, CAT_COLS)
        ])
        params={
            "n_estimators": N_ESTIMATORS,
            "max_depth": MAX_DEPTH,
            "learning_rate": LEARNING_RATE,
            "min_child_weight": MIN_CHILD_WEIGHT,
            "subsample": SUBSAMPLE,
            "scale_pos_weight": SCALE_POS_WEIGHT,
            "objective": OBJECTIVE,
            "eval_metrics": EVAL_METRIC,
            "random_state": RANDOM_SEED,

        }
        model_pipeline=Pipeline([
            ("prepprocessor", preprocessor),
            ("model", XGBClassifier(
                params=params
            ))
        ])
        # logging params
        mlflow.log_params(params)
        # train and log models
        model_pipeline.fit(X_train, y_train)
        mlflow.sklearn.log_model(
            sk_model=model_pipeline,
            name="churn_model"
        )
        # log metrics
        y_test_pred=model_pipeline.predict(X_test)
        y_test_proba=model_pipeline.predict_proba(X_test)[:,1]
        accuracy_test_score=accuracy_score(y_test, y_test_pred)
        recall_test_score=recall_score(y_test, y_test_pred)
        precision_test_score=precision_score(y_test, y_test_pred)
        f1_test_score=f1_score(y_test, y_test_pred)
        roc_auc_test_score=roc_auc_score(y_test, y_test_proba)
        mlflow.log_metrics({
            "test_accuracy": accuracy_test_score,
            "test_recall": recall_test_score,
            "test_precision": precision_test_score,
            "test_f1": f1_test_score,
            "test_roc_auc": roc_auc_test_score
        })
        joblib.dump(model_pipeline, MODEL_FOLDER/"churn_model.pkl")

if __name__=="__main__":
    train()