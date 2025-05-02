from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class AsthmaForm(FlaskForm):
    Age = FloatField('Age', validators=[DataRequired(), NumberRange(min=5, max=79)])
    Gender = FloatField('Gender', validators=[DataRequired(), NumberRange(min=0, max=1)])
    Ethnicity = FloatField('Ethnicity', validators=[DataRequired(), NumberRange(min=0, max=3)])
    EducationLevel = FloatField('EducationLevel', validators=[DataRequired(), NumberRange(min=0, max=3)])
    BMI = FloatField('BMI', validators=[DataRequired(), NumberRange(min=15.03, max=39.98)])
    Smoking = FloatField('Smoking', validators=[DataRequired(), NumberRange(min=0, max=1)])
    PhysicalActivity = FloatField('PhysicalActivity', validators=[DataRequired(), NumberRange(min=0.0017, max=9.9958)])
    DietQuality = FloatField('DietQuality', validators=[DataRequired(), NumberRange(min=0.003, max=9.9999)])
    SleepQuality = FloatField('SleepQuality', validators=[DataRequired(), NumberRange(min=4.001, max=9.996)])
    PollutionExposure = FloatField('PollutionExposure', validators=[DataRequired(), NumberRange(min=0.0010, max=9.999)])
    PollenExposure = FloatField('PollenExposure', validators=[DataRequired(), NumberRange(min=0.0006, max=9.999)])
    DustExposure = FloatField('DustExposure', validators=[DataRequired(), NumberRange(min=0.0024, max=9.999)])
    PetAllergy = FloatField('PetAllergy', validators=[DataRequired(), NumberRange(min=0, max=1)])
    FamilyHistoryAsthma = FloatField('FamilyHistoryAsthma', validators=[DataRequired(), NumberRange(min=0, max=1)])
    HistoryOfAllergies = FloatField('HistoryOfAllergies', validators=[DataRequired(), NumberRange(min=0, max=1)])
    Eczema = FloatField('Eczema', validators=[DataRequired(), NumberRange(min=0, max=1)])
    HayFever = FloatField('HayFever', validators=[DataRequired(), NumberRange(min=0, max=1)])
    GastroesophagealReflux = FloatField('GastroesophagealReflux', validators=[DataRequired(), NumberRange(min=0, max=1)])
    LungFunctionFEV1 = FloatField('LungFunctionFEV1', validators=[DataRequired(), NumberRange(min=1.0004, max=3.9997)])
    LungFunctionFVC = FloatField('LungFunctionFVC', validators=[DataRequired(), NumberRange(min=1.5000, max=5.9994)])
    Wheezing = FloatField('Wheezing', validators=[DataRequired(), NumberRange(min=0, max=1)])
    ShortnessOfBreath = FloatField('ShortnessOfBreath', validators=[DataRequired(), NumberRange(min=0, max=1)])
    ChestTightness = FloatField('ChestTightness', validators=[DataRequired(), NumberRange(min=0, max=1)])
    Coughing = FloatField('Coughing', validators=[DataRequired(), NumberRange(min=0, max=1)])
    NighttimeSymptoms = FloatField('NighttimeSymptoms', validators=[DataRequired(), NumberRange(min=0, max=1)])
    ExerciseInduced = FloatField('ExerciseInduced', validators=[DataRequired(), NumberRange(min=0, max=1)])

    submit = SubmitField('Predict Risk')
