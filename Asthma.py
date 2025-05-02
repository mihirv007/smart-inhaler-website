import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
import joblib  # for saving the model

# Load dataset
dataset = pd.read_csv("/Users/mihirverma/Astham/asthma_disease_data.csv")

print(list(dataset))

#sensor detection features
'Smoking', 'PhysicalActivity','PollutionExposure', 'PollenExposure', 'DustExposure', 'Wheezing', 'ShortnessOfBreath', 'ChestTightness', 'Coughing'

# Features and target
X = dataset.drop(['Diagnosis', 'DoctorInCharge','PatientID'], axis=1)  # Exclude target and irrelevant columns
y = dataset['Diagnosis']  # Binary or multi-class labels


# Display min and max for each column
'''print("\n=== Minimum Values ===")
print(dataset.min(numeric_only=True))

print("\n=== Maximum Values ===")
print(dataset.max(numeric_only=True))'''

# Encode categorical variables
X_encoded = pd.get_dummies(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.3, stratify=y, random_state=42
)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

# Display results
print("=== Evaluation Metrics ===")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))

# Save the trained model
#joblib.dump(model, "asthma_model.pkl")
print("\nModel saved as 'asthma_rf_model.pkl'")

'''
=== Minimum Values ===
PatientID                 5034.000000
Age                          5.000000
Gender                       0.000000
Ethnicity                    0.000000
EducationLevel               0.000000
BMI                         15.031803
Smoking                      0.000000
PhysicalActivity             0.001740
DietQuality                  0.003031
SleepQuality                 4.001437
PollutionExposure            0.001022
PollenExposure               0.000659
DustExposure                 0.002434
PetAllergy                   0.000000
FamilyHistoryAsthma          0.000000
HistoryOfAllergies           0.000000
Eczema                       0.000000
HayFever                     0.000000
GastroesophagealReflux       0.000000
LungFunctionFEV1             1.000459
LungFunctionFVC              1.500045
Wheezing                     0.000000
ShortnessOfBreath            0.000000
ChestTightness               0.000000
Coughing                     0.000000
NighttimeSymptoms            0.000000
ExerciseInduced              0.000000
Diagnosis                    0.000000
dtype: float64

=== Maximum Values ===
PatientID                 7425.000000
Age                         79.000000
Gender                       1.000000
Ethnicity                    3.000000
EducationLevel               3.000000
BMI                         39.985611
Smoking                      1.000000
PhysicalActivity             9.995809
DietQuality                  9.999904
SleepQuality                 9.996235
PollutionExposure            9.998964
PollenExposure               9.999555
DustExposure                 9.999708
PetAllergy                   1.000000
FamilyHistoryAsthma          1.000000
HistoryOfAllergies           1.000000
Eczema                       1.000000
HayFever                     1.000000
GastroesophagealReflux       1.000000
LungFunctionFEV1             3.999719
LungFunctionFVC              5.999421
Wheezing                     1.000000
ShortnessOfBreath            1.000000
ChestTightness               1.000000
Coughing                     1.000000
NighttimeSymptoms            1.000000
ExerciseInduced              1.000000
Diagnosis                    1.000000
'''
