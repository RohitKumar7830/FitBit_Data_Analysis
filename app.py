import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# App title
st.title('Total Steps Predictor')

# Add sliders for the input variables
total_distance = st.slider('Total Distance', 0.0, 20.0, 5.0)
very_active_distance = st.slider('Very Active Distance', 0.0, 10.0, 2.0)
moderately_active_distance = st.slider('Moderately Active Distance', 0.0, 10.0, 2.0)
light_active_distance = st.slider('Light Active Distance', 0.0, 10.0, 2.0)
sedentary_minutes = st.slider('Sedentary Minutes', 0, 1500, 500)
lightly_active_minutes = st.slider('Lightly Active Minutes', 0, 1000, 200)
fairly_active_minutes = st.slider('Fairly Active Minutes', 0, 500, 50)
very_active_minutes = st.slider('Very Active Minutes', 0, 500, 100)

# Store the input values in an array (shape it like the model input)
input_data = np.array([[total_distance, very_active_distance, moderately_active_distance, light_active_distance,
                        sedentary_minutes, lightly_active_minutes, fairly_active_minutes, very_active_minutes]])

# Make prediction using the loaded model
predicted_steps = model.predict(input_data)

# Display the prediction result
st.subheader(f'Predicted Total Steps: {int(predicted_steps[0])}')
