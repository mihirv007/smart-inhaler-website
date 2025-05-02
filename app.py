from flask import Flask, render_template, request
import joblib
import pandas as pd
from forms import AsthmaForm

app = Flask(__name__)
app.secret_key =  '9a28370ca232cb2ae21adc0069a149a227363aa8e4c8853be311aa96b64de66e'

# Load trained model
model = joblib.load("asthma_model.pkl")

# Feature names in order
expected_features = [
    'Age', 'Gender', 'Ethnicity', 'EducationLevel', 'BMI', 'Smoking',
    'PhysicalActivity', 'DietQuality', 'SleepQuality', 'PollutionExposure',
    'PollenExposure', 'DustExposure', 'PetAllergy', 'FamilyHistoryAsthma',
    'HistoryOfAllergies', 'Eczema', 'HayFever', 'GastroesophagealReflux',
    'LungFunctionFEV1', 'LungFunctionFVC', 'Wheezing', 'ShortnessOfBreath',
    'ChestTightness', 'Coughing', 'NighttimeSymptoms', 'ExerciseInduced'
]
@app.route('/')
def index():
    return render_template('dashboard.html', form=AsthmaForm())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    form = AsthmaForm()
    prediction = None

    if form.validate_on_submit():
        # Collecting form data
        input_data = [getattr(form, feature).data for feature in expected_features]
        df = pd.DataFrame([input_data], columns=expected_features)
        
        # Make prediction
        prediction = model.predict(df)[0]

    return render_template('dashboard.html', form=form, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5006)
