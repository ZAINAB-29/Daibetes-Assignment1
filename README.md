Diabetes Prediction API
A machine learning project that predicts diabetes using patient medical data, deployed with FastAPI.

Setup Instructions
Create virtual environment: python -m venv venv venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Run the API Server
python -m uvicorn app:app --reload

API Endpoints
GET / — Health check
POST /predict — Predict diabetes
Example Test Commands
Test 1 - Diabetic: Invoke-WebRequest -Uri "http://localhost:8000/predict" -Method POST -ContentType "application/json" -Body '{"age": 65, "urea": 7.5, "cr": 52.0, "hba1c": 11.2, "chol": 6.1, "tg": 2.8, "hdl": 0.9, "ldl": 3.5, "vldl": 1.2, "bmi": 32.5, "gender": "M"}'

Test 2 - Non Diabetic: Invoke-WebRequest -Uri "http://localhost:8000/predict" -Method POST -ContentType "application/json" -Body '{"age": 28, "urea": 4.2, "cr": 48.0, "hba1c": 5.1, "chol": 4.0, "tg": 1.2, "hdl": 1.8, "ldl": 2.1, "vldl": 0.6, "bmi": 22.0, "gender": "F"}'

Model Performance
Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	0.9439	0.9393	0.9439	0.9398
SVM	0.8482	0.7194	0.8482	0.7785
Decision Tree	0.9868	0.9868	0.9868	0.9867
Random Forest	0.9802	0.9804	0.9802	0.9793
KNN	0.9043	0.9160	0.9043	0.9093
Best Model
Decision Tree with F1-Score of 0.9867

Screenshots
See screenshots/ folder for API response examples.