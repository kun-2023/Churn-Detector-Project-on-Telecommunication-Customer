import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()


API_BASE_URL=os.getenv("API_BASE_URL", 
                       "http://127.0.0.1:8000",
                       "http://api:8000")

PREDICT_URL=f"{API_BASE_URL}/predict"

def churn_predict_ui(
        SeniorCitizen, 
        tenure,
        MonthlyCharges, 
        TotalCharges,
        gender, 
        Partner, 
        Dependents, 
        PhoneService, 
        MultipleLines, 
        InternetService, 
        OnlineSecurity, 
        OnlineBackup, 
        DeviceProtection, 
        TechSupport, 
        StreamingTV, 
        StreamingMovies, 
        Contract, 
        PaperlessBilling, 
        PaymentMethod
):
    payload={
        "SeniorCitizen": SeniorCitizen, 
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges, 
        "TotalCharges": TotalCharges,
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

    response=requests.post(
        PREDICT_URL,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    result=response.json()
    return result[0], result[1]

st.title("Live Prediction")
st.markdown("Use the interfce to test Churn prediction model through FastAPI")
with st.Row():
    # st.
    with st.Column():
        SeniorCitizen= st.Dropdown([0,1],label="Senior Citizen"), 
        tenure= st.Number(),
        MonthlyCharges= st.slider(min_value=0.00, max_value=150.00, value=10), 
        TotalCharges= st.slider(min_value=0, max_value=9000),
        gender= st.Dropdown(["Male", "Female"]), 
        Partner=st.Dropdown(["Yes", "No"]) , 
        Dependents= st.Dropdown(["No", "Yes"]), 
        PhoneService= st.Dropdown(["Yes", "No"]), 
        MultipleLines= st.Dropdown(["Yes", "No"]), 
        InternetService= st.Downdrop(["Fiber optic", "DSL", "No"]), 
        OnlineSecurity= st.Downdrop(["No", "Yes", "No internet service"]), 
        OnlineBackup= st.Dropdown(["No", "Yes", "No internet service"]), 
        DeviceProtection= st.Dropdown(["No", "Yes", "No internet service"]), 
        TechSupport= st.Dropdown(["No", "Yes", "No internet service"]), 
        StreamingTV= st.Dropdown(["No", "Yes", "No internet service"]), 
        StreamingMovies= st.Dropdown(["No", "Yes", "No internet service"]), 
        Contract= st.Dropdown(["Month-to-month", "Two year", "One year"]), 
        PaperlessBilling= st.Dropdown(["No", "Yes"]), 
        PaymentMethod= st.Dropdown(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

        churn_button=st.Button("Predict Churn")
    with st.Column():
        churn_output=st.TextBox(label="Churn Prediction Result")
churn_button.click(
    fn=PREDICT_URL,
    inputs=[
                SeniorCitizen, 
                tenure,
                MonthlyCharges, 
                TotalCharges,
                gender, 
                Partner, 
                Dependents, 
                PhoneService, 
                MultipleLines, 
                InternetService, 
                OnlineSecurity, 
                OnlineBackup, 
                DeviceProtection, 
                TechSupport, 
                StreamingTV, 
                StreamingMovies, 
                Contract, 
                PaperlessBilling, 
                PaymentMethod
    ],
    outputs=churn_output
)

if __name__=="__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

