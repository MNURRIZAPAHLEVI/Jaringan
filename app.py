from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

with open("svm_bayes12.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def root():
    return {"status": "ML API running"}

@app.post("/predict")
def predict(data: dict):
    X = np.array([[ 
        data["age"],
        data["hemoglobin"],
        data["white_cell_count"],
        data["blood_glucose_pressure"],
        data["creatin_serum"],
        data["rasio_urea_creatinin"]
    ]])
    pred = int(model.predict(X)[0])
    prob = model.predict_proba(X)[0]

    return {
        "prediction": pred,
        "probabilities": {
            "Healthy": float(prob[0]),
            "Moderate": float(prob[1]),
            "High": float(prob[2])
        }
    }
