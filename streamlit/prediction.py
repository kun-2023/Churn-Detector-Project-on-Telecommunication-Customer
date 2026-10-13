import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()


API_BASE_URL=os.getenv("API_BASE_URL",
                       "http://api:8000")

PREDICT_URL=f"{API_BASE_URL.rstrip('/')}/predict"

def churn_predict_uri(payload):
    response=requests.post(
        PREDICT_URL,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    
    return response.json()

def show_prediction():
    st.title("Live Prediction")
    st.markdown("Use the interfce to test Churn prediction model through FastAPI")
   
    with st.form("churn_form"):
        col1, col2, col3=st.columns(3, gap="large")

        with col1:
            SeniorCitizen= st.selectbox("Senior Citizen", ["No","Yes"]) 
            tenure= st.number_input("Tenure", min_value=0, max_value=100, value=12)
            MonthlyCharges= st.number_input(
                "Monthly Charges", min_value=0.00, max_value=150.00, 
                value=70.00, step=0.01,format="%.2f") 
            TotalCharges= st.number_input(
                "Total Charges", min_value=0.0, max_value=9000.00,
                value=500.0, step=0.01, format="%.2f")
            gender= st.selectbox("Gender", ["Male", "Female"]) 
            Partner=st.selectbox("Partner", ["Yes", "No"])  
            Dependents= st.selectbox("Dependents" ,["No", "Yes"])
        with col2:
            PhoneService= st.selectbox("Phone Service" ,["Yes", "No"]) 
            MultipleLines= st.selectbox("Multiple Lines" ,["Yes", "No", "No phone service"]) 
            InternetService= st.selectbox("Internet Service",["Fiber optic", "DSL", "No"]) 
            OnlineSecurity= st.selectbox("Online Security", 
                                         ["No", "Yes", "No internet service"]) 
            OnlineBackup= st.selectbox("Online Backup",
                                       ["No", "Yes", "No internet service"]) 
            DeviceProtection= st.selectbox("Device Protection",
                                           ["No", "Yes", "No internet service"]) 
        with col3: 
            TechSupport= st.selectbox("Tech Support",
                                      ["No", "Yes", "No internet service"]) 
            StreamingTV= st.selectbox("Streaming TV",
                                      ["No", "Yes", "No internet service"]) 
            StreamingMovies= st.selectbox("Streaming Movies",["No", "Yes", "No internet service"]) 
            Contract= st.selectbox("Contract",["Month-to-month", "Two year", "One year"]) 
            PaperlessBilling= st.selectbox("Paperless Billing",["No", "Yes"]) 
            PaymentMethod= st.selectbox("Payment Method",["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

        left, center, right=st.columns([2,1,2])
        with center:
            churn_button=st.form_submit_button("Predict Churn",
                                               type="primary",
                                               use_container_width=True)
        
    if churn_button:

        payload={
                "SeniorCitizen": 1 if SeniorCitizen=="Yes" else 0, 
                "tenure": tenure,
                "MonthlyCharges": round(MonthlyCharges, 2),
                "TotalCharges": round(TotalCharges,2),
                "gender": gender, 
                "Partner": Partner, 
                "Dependents": Dependents, 
                "PhoneService": PhoneService, 
                "MultipleLines": MultipleLines, 
                "InternetService": InternetService, 
                "OnlineSecurity": OnlineSecurity, 
                "OnlineBackup": OnlineBackup, 
                "DeviceProtection": DeviceProtection, 
                "TechSupport": TechSupport, 
                "StreamingTV": StreamingTV, 
                "StreamingMovies": StreamingMovies, 
                "Contract": Contract, 
                "PaperlessBilling": PaperlessBilling, 
                "PaymentMethod": PaymentMethod
            }
        try:
            with st.spinner("Processing...", show_time=True):
                result=churn_predict_uri(payload)
                
            prediction=result["churn_prediction"]
            probability=result["churn_probability"]
            st.subheader("Prediction Result")
            if prediction==1:
                st.warning("Prediction: Churn")
            else:
                st.success("Prediction: Not Churn")
            st.metric("Probability of churn", probability)
            
        except requests.RequestException as e:
            st.error(f"Prediction failed: {e}")

        