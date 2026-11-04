import streamlit as st
import joblib
import pandas as pd

model = joblib.load('soh_model.pkl')
st.set_page_config(page_title='EV Battery Health Prediction', page_icon='🔋')
st.title('EV Battery Health Prediction')
st.write('Predict Battery State of Health using charging cycles.')

cycles = st.number_input('Enter Charging Cycles:', min_value=0, max_value=5000, value=850, step=1)

if st.button('Predict Battery Health'):
    input_data = pd.DataFrame({'Charging_Cycles': [cycles]})
    prediction = float(model.predict(input_data)[0])
    prediction = max(0.0, min(100.0, prediction))
    st.subheader('Predicted Battery Health')
    st.success(f'{prediction:.2f}%')
    if prediction >= 80:
        status = 'Good'
    elif prediction >= 70:
        status = 'Moderate'
    else:
        status = 'Poor'
    st.write(f'Battery Health Status: {status}')
    st.progress(int(prediction))
