import pandas as pd
import numpy as np
from src.config import CLEAN_DATA_PATH,DATA_FOLDER


def preprocess():
    df=pd.read_csv(DATA_FOLDER)
    df["TotalCharges"]=pd.to_numeric(df.TotalCharges, errors="coerce")
    df["Churn_Label"]=df["Churn"].map({"Yes":1, "No":0})
    df.drop(["customerID","Churn"], inplace=True)
    df.to_csv(CLEAN_DATA_PATH)

if __name__=="__main__":
    preprocess()
        
