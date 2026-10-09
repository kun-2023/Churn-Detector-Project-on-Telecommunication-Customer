import pandas as pd
import numpy as np
from src.config import CLEAN_DATA_PATH, DATA_PATH


def preprocess():
    CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df=pd.read_csv(DATA_PATH)
    df["TotalCharges"]=pd.to_numeric(df.TotalCharges, errors="coerce")
    df["Churn_Label"]=df["Churn"].map({"Yes":1, "No":0})
    df.drop(columns=["customerID","Churn"], inplace=True)
    df.to_csv(CLEAN_DATA_PATH, index=False)

if __name__=="__main__":
    preprocess()
        
