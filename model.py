import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('admission_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_admission(features):
    # Scale the features using the scaler
    features_scaled = scaler.transform(features)
    
    # Make a prediction
    prediction = model.predict(features_scaled)
    
    # Return the predicted chance of admission
    return prediction[0]
