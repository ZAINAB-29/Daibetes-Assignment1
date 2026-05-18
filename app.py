from fastapi import FastAPI
from pydantic import BaseModel, field_validator
import pandas as pd
import joblib

# Load model and columns
model = joblib.load('diabetes_model.pkl')
training_columns = joblib.load('training_columns.pkl')

app = FastAPI()

# Input schema
class PatientData(BaseModel):
    age: float
    urea: float
    cr: float
    hba1c: float
    chol: float
    tg: float
    hdl: float
    ldl: float
    vldl: float
    bmi: float
    gender: str

    @field_validator('gender')
    def validate_gender(cls, v):
        if v not in ('M', 'F'):
            raise ValueError("Gender must be 'M' or 'F'")
        return v

# Health check endpoint
@app.get("/")
def health():
    return {"status": "API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: PatientData):
    # Convert input to dataframe
    input_dict = {
        'AGE': data.age,
        'Urea': data.urea,
        'Cr': data.cr,
        'HbA1c': data.hba1c,
        'Chol': data.chol,
        'TG': data.tg,
        'HDL': data.hdl,
        'LDL': data.ldl,
        'VLDL': data.vldl,
        'BMI': data.bmi,
        'Gender_F': data.gender == 'F',
        'Gender_M': data.gender == 'M'
    }
    input_df = pd.DataFrame([input_dict])
    input_df = input_df[training_columns]

    # Make prediction
    prediction = model.predict(input_df)[0]

    result = {
        'N': 'Not Diabetic',
        'P': 'Pre-Diabetic',
        'Y': 'Diabetic'
    }

    return {
        "prediction": prediction,
        "result": result.get(prediction, prediction)
    }