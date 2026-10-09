from src.config import (MODEL_PATH, NUM_COLS, 
                        CAT_COLS, TARGET_VARIABLE,
                        CLEAN_DATA_PATH)
import joblib
import pandas as pd

class ChurnDetector:
    def __init__(self, model_path=MODEL_PATH):
        self.model=joblib.load(model_path)

    def predict(self, df: pd.DataFrame):
        X=df[NUM_COLS+CAT_COLS]
        predictions=self.model.predict(X)
        probabilities=self.model.predict_proba(X)[:,1]
        results=df.copy()
        results["churn_predictions"]=predictions
        results["churn_probabilities"]=probabilities
        return results

if __name__=="__main__":
    predictor=ChurnDetector()
    df=pd.read_csv(CLEAN_DATA_PATH)
    data=df.head()
    results=predictor.predict(data)
    print(results)
