from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open("best_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input values from the form and store them in a list
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

    # Prepare the input data as a numpy array
    input_data = np.array([input_features])

    # Make a prediction
    premium_price = model.predict(input_data)

    return render_template('result.html', premium_price=premium_price[0])

if __name__ == '__main__':
    app.run(debug=True)
