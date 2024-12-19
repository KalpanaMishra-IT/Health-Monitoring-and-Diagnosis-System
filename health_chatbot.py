from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize app
app = FastAPI()

# Define request schema
class HealthRequest(BaseModel):
    symptoms: str
    activity_level: str

class ChatbotRequest(BaseModel):
    message: str

# Load pre-trained model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Error: 'model.pkl' not found. Ensure the file exists in the correct directory.")
    model = None

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Health Monitoring API is running."}

# Health prediction endpoint
@app.post("/predict-health")
def predict_health(request: HealthRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Cannot process request.")
    
    symptoms = request.symptoms.lower()
    activity_level = request.activity_level.lower()

    # Example input preprocessing
    input_data = np.array([[len(symptoms), len(activity_level)]])
    prediction = model.predict(input_data)
    return {"prediction": prediction[0]}

# Chatbot endpoint
@app.post("/chatbot")
def chatbot_interaction(request: ChatbotRequest):
    user_message = request.message.lower()
    
    if "symptom" in user_message:
        response = "Can you describe your symptoms in detail?"
    elif "activity" in user_message:
        response = "How would you rate your activity level: low, medium, or high?"
    elif "predict" in user_message:
        response = "Please provide your symptoms and activity level to get a prediction."
    else:
        response = "I am here to help you with your health. Please tell me your symptoms or activity level."
    
    return {"response": response}
