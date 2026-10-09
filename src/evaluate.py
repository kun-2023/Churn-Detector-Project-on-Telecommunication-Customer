from src.inference import ChurnDetector
import pandas as pd
from src.config import (CLEAN_DATA_PATH, 
                        X_TRAIN_PATH, 
                        X_TEST_PATH, 
                        Y_TRAIN_PATH, 
                        Y_TEST_PATH,
                        METRICS_PATH,
                        FEATURE_IMPORTANCE_PATH,
                        CONFUSION_MATRIX_PATH,
                        FRONTEND_DATA_DIR)
from sklearn.metrics import (accuracy_score, 
                             recall_score, 
                             precision_score,
                             f1_score,
                             roc_auc_score,
                             confusion_matrix)

predictor=ChurnDetector()
cleaned_data=pd.read_csv(CLEAN_DATA_PATH)
X_train=pd.read_csv(X_TRAIN_PATH)
X_test=pd.read_csv(X_TEST_PATH)
y_train=pd.read_csv(Y_TRAIN_PATH).squeeze("columns")
y_test=pd.read_csv(Y_TEST_PATH).squeeze("columns")
test_results=predictor.predict(X_test)
y_test_pred=test_results["churn_predictions"]
y_test_proba=test_results["churn_probabilities"]
# metrics
accuracy_test_score=accuracy_score(y_test, y_test_pred)
recall_test_score=recall_score(y_test, y_test_pred)
precision_test_score=precision_score(y_test, y_test_pred)
f1_test_score=f1_score(y_test, y_test_pred)
roc_auc_test_score=roc_auc_score(y_test, y_test_proba)
df_test_metrics=pd.DataFrame({
    "test_scores":[accuracy_test_score, 
                   recall_test_score, 
                   precision_test_score,
                   f1_test_score, roc_auc_score]
}, index=["Accuracy", "Recall", "Precision", "F1_score", "ROC_AUC_SCORE"])

# feature importances
feature_names=predictor.model.named_steps["preprocessor"].get_feature_names_out()
importances=predictor.model.named_steps["model"].feature_importances_
feature_importance=pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})
feature_importance=feature_importance.sort_values("Importance", 
                                                  ascending=False
                                                  ).head(15).sort_values("Importance", ascending=True)

# confusion_matrix
cm_test=confusion_matrix(y_test,y_test_pred)
cm_df=pd.DataFrame(cm_test, 
                   index=["No_Churn", "Churn"], 
                   columns=["No_Churn", "Churn"])

# Save all three dfs
FRONTEND_DATA_DIR.mkdir(parents=True, exist_ok=True)
df_test_metrics.to_csv(METRICS_PATH, index=False)
feature_importance.to_csv(FEATURE_IMPORTANCE_PATH, index=False)
cm_df.to_csv(CONFUSION_MATRIX_PATH, index=True)