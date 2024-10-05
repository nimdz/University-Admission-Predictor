from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('admission_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Convert the input data to a pandas DataFrame
    input_data = pd.DataFrame({
        'GRE Score': [data['gre_score']],
        'TOEFL Score': [data['toefl_score']],
        'University Rating': [data['university_rating']],
        'SOP': [data['sop_strength']],
        'LOR ': [data['lor_strength']],
        'CGPA': [data['cgpa']],
        'Research': [data['research']]
    })

    input_data_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data_scaled)

    prediction = int(prediction[0])

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
