# Admission Predictor

A simple web application that predicts the likelihood of university admission based on various factors such as GRE score, TOEFL score, CGPA, and more. The form takes input from the user, submits the data to a prediction API, and displays whether the user is likely to be admitted or not.

## Features

- User-friendly form to input key academic details:
  - GRE score (0-320)
  - TOEFL score (0-120)
  - University Rating (1-5)
  - SOP Strength (1-5)
  - LOR Strength (1-5)
  - CGPA (0-10)
  - Research Experience (1 for Yes, 0 for No)
- Provides feedback on whether the user is likely to be admitted based on the input data.
- Clean, modern UI with helpful input guidelines.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Backend**: Python (Flask framework)
- **Machine Learning**: TensorFlow, Scikit-learn for model training and prediction
- **Data Handling**: NumPy, Pandas
- **Model Storage**: Joblib for saving and loading machine learning models

## How to Use

1. Clone the repository.
2. Run the Flask app (`app.py`) on your local machine.
3. Open the `index.html` file in your browser.
4. Fill in your academic details and click on the "Predict" button.
5. View the prediction result.

## API

The application sends a POST request with the form data in JSON format to an endpoint `/predict` and expects a JSON response containing the prediction (`1` for likely admitted, `0` for not admitted).

