from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model from the pickle file
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input values from the form
    input_features = [
        float(request.form['Age']),
        float(request.form['Diabetes']),
        float(request.form['BloodPressureProblems']),
        float(request.form['AnyTransplants']),
        float(request.form['AnyChronicDiseases']),
        float(request.form['Height']),
        float(request.form['Weight']),
        float(request.form['KnownAllergies']),
        float(request.form['HistoryOfCancerInFamily']),
        float(request.form['NumberOfMajorSurgeries'])
    ]

    # Make a prediction using the loaded model
    predicted_premium = model.predict([input_features])[0]

    return render_template('index.html', prediction=f'Predicted Premium: {predicted_premium:.2f}')

if __name__ == '__main__':
    app.run(debug=True)
