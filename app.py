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
    try:
        prediction = model.predict(df)[0]
        return {"prediction": float(prediction)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health():
    return {"status": "ok"}