from pathlib import Path
import streamlit as st
import pandas as pd

ROOT_FOLDER=Path(__file__).resolve().parents[1]

def show_overview():
    st.title("Telecommunication Customers Churn Detector")
    st.subheader("Project Overview")
    st.write(
        """
        This project is an end-to-end binary Churn Detection for 
        telecommunication customers. The model is trained 
        with Xgboost algorithm. The app prediction page 
        predicts whether or not a customer is about to churn 
        or unsubscribe the servie offered by the company given 
        informatioins such as gender, paterner, dependents, 
        tenures and so on. The result includes prediction and 
        probability. The prediction is either 1 or 0, representing 
        either churn or not churn respectively. Probability shows 
        confidence percentage of how likely the prediction is. This 
        technology could be adpated into fraud transaction detector,
        or even multiclass classification tasks.""")

    st.subheader("Tech Stacks")
    st.write("""
    Python, Pandas, MLflow, DVC, Git/GitHub, FastAPI,Docker, 
    Streamlit, AWS ECR, ECS, GitHub Actions, CI/CD pipeline, Pytest.
""")