from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Define request schema
class HealthRequest(BaseModel):
    symptoms: str
    activity_level: str

# Load pre-trained model (replace 'model.pkl' with your actual model file)
try:
    model = joblib.load("model.pkl")  # Ensure you have trained and saved your model as 'model.pkl'
except FileNotFoundError:
    model = None

@app.get("/")
def read_root():
    return {"message": "Health Monitoring API is running."}

@app.post("/predict-health")
def predict_health(request: HealthRequest):
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded.")

    # Extract input data
    symptoms = request.symptoms.lower()
    activity_level = request.activity_level.lower()

    # Preprocess the input (this is a placeholder, adjust based on your model's requirements)
    try:
        input_data = np.array([len(symptoms), len(activity_level)]).reshape(1, -1)  # Example input transformation
        prediction = model.predict(input_data)
        result = {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing input: {str(e)}")

    return result

