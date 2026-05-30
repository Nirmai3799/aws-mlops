from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("delivery_time_model.pkl")

@app.get("/")
def home():
    return {"message": "Delivery Time Prediction API"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"predicted_delivery_time": prediction}