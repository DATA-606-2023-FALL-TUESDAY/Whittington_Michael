import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import LabelEncoder

# Load and preprocess data
df = pd.read_csv('neiss_2022.csv')

# Define feature columns and target column
X = df.drop(['CPSC_Case_Number','Other_Race', 'Body_Part','Diagnosis','Other_Diagnosis', 'Body_Part_2', 'Diagnosis_2', 'Other_Diagnosis_2', 'PSU', 'Stratum', 'Narrative_1','Treatment_Date','Product_2','Product_3','Weight','Disposition'], axis=1)

# Label encoder and encode the target column
le_body_part = LabelEncoder()
le_diagnosis = LabelEncoder()

y_body_part = le_body_part.fit_transform(df['Body_Part'])
y_diagnosis = le_diagnosis.fit_transform(df['Diagnosis'])

# Splitting the data for body part
X_train_body, X_test_body, y_train_body, y_test_body = train_test_split(X, y_body_part, test_size=0.2, random_state=42)

# Splitting the data for diagnosis
X_train_diag, X_test_diag, y_train_diag, y_test_diag = train_test_split(X, y_diagnosis, test_size=0.2, random_state=42)

# Training the XGBoost model for body part prediction
model_body_part = xgb.XGBClassifier(random_state=42, colsample_bytree=0.8, learning_rate=0.1, max_depth=9, n_estimators=100, subsample=0.9)
model_body_part.fit(X_train_body, y_train_body)

# Training the XGBoost model for diagnosis prediction
model_diagnosis = xgb.XGBClassifier(random_state=42, colsample_bytree=0.8, learning_rate=0.1, max_depth=9, n_estimators=100, subsample=0.9)
model_diagnosis.fit(X_train_diag, y_train_diag)

# Save the models
with open('xgboost_model_body_part.pkl', 'wb') as file:
    pickle.dump(model_body_part, file)

with open('xgboost_model_diagnosis.pkl', 'wb') as file:
    pickle.dump(model_diagnosis, file)

# Save the label encoders
with open('label_encoder_body_part.pkl', 'wb') as file:
    pickle.dump(le_body_part, file)

with open('label_encoder_diagnosis.pkl', 'wb') as file:
    pickle.dump(le_diagnosis, file)