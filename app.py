import streamlit as st
pip install joblib
from joblib import load
import pandas as pd

# Load your pre-trained model
model = load(r"C:\Users\aazar\OneDrive\Desktop\Data Science projects\xg_boost_classifier.joblib")

# Function to predict COVID-19 likelihood
def predict(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        return "Yes"
    else:
        return "No"

def main():
    st.title("COVID-19 Prediction")
    st.write('Enter the following information to predict COVID-19:')
    
    # Define symptoms with default values
    symptoms = {
        'Breathing Problem': False,
        'Fever': False,
        'Dry Cough': False,
        'Sore Throat': False,
        'Asthma': False,
        'Chronic Lung Disease': False,
        'Headache': False,
        'Heart Disease': False,
        'Diabetes': False,
        'Hypertension': False,
        'Fatigue': False,
        'Abroad Travel': False,
        'Contact with COVID Patient': False,
        'Attended Large Gathering': False,
        'Visited Public Exposed Places': False,
        'Family Working in Public Exposed Places': False,
        'Wearing Masks': False,
        'Sanitization from Market': False
    }
    
    # Display symptom checkboxes
    for symptom in symptoms:
        symptoms[symptom] = st.checkbox(symptom)

    # Collect user input into a dictionary
    input_data = {
        'breathingproblem': symptoms['Breathing Problem'],
        'fever': symptoms['Fever'],
        'drycough': symptoms['Dry Cough'],
        'sorethroat': symptoms['Sore Throat'],
        'asthma': symptoms['Asthma'],
        'chroniclungdisease': symptoms['Chronic Lung Disease'],
        'headache': symptoms['Headache'],
        'heartdisease': symptoms['Heart Disease'],
        'diabetes': symptoms['Diabetes'],
        'hypertension': symptoms['Hypertension'],
        'fatigue': symptoms['Fatigue'],
        'abroadtravel': symptoms['Abroad Travel'],
        'contactwithcovidpatient': symptoms['Contact with COVID Patient'],
        'attendedlargegathering': symptoms['Attended Large Gathering'],
        'visitedpublicexposedplaces': symptoms['Visited Public Exposed Places'],
        'familyworkinginpublicexposedplaces': symptoms['Family Working in Public Exposed Places'],
        'wearingmasks': symptoms['Wearing Masks'],
        'sanitizationfrommarket': symptoms['Sanitization from Market']
    }
    
    # Predict button
    if st.button("Predict"):
        prediction = predict(input_data)
        st.write(f'COVID-19 Prediction: {prediction}')

    # Clear All button
    if st.button('Clear All'):
        # Clear all checkboxes
        for symptom in symptoms:
            symptoms[symptom] = False

if __name__ == "__main__":
    main()

