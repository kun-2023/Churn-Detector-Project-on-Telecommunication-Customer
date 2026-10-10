from pydantic import BaseModel, Field


class ChurnDetectorRequest(BaseModel):
   gender: str = Field(...,examples=["Female"]) 
   SeniorCitizen: int = Field(..., examples=[0])
   Partner: str = Field(..., examples=["Yes"])
   Dependents: str = Field(..., examples=["No"])    
   tenure: int = Field(..., examples=[1])
   PhoneService: str = Field(..., examples=["No"])    
   MultipleLines: str = Field(..., examples=["No phone service"])    
   InternetService: str = Field(..., examples=["DSL"])    
   OnlineSecurity: str = Field(..., examples=["No"])    
   OnlineBackup: str = Field(..., examples=["Yes"])    
   DeviceProtection: str = Field(..., examples=["No"])    
   TechSupport: str = Field(..., examples=["No"])    
   StreamingTV: str = Field(..., examples=["No"])    
   StreamingMovies: str = Field(..., examples=["No"])    
   Contract: str = Field(..., examples=["Month-to-month"])    
   PaperlessBilling: str = Field(..., examples=["Yes"])    
   PaymentMethod: str = Field(..., examples=["Electronic check"])    
   MonthlyCharges: float = Field(..., examples=[29.85])
   TotalCharges: float = Field(..., examples=[29.85])