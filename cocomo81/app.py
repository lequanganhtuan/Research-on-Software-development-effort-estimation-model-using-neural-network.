import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load model
model = load_model('cocomo81_model.keras')


st.title("Dự đoán giá trị 'actual' từ các đặc trưng đầu vào")

# Input fields
rely = st.number_input('rely', value=1.0)
data = st.number_input('data', value=1.0)
cplx = st.number_input('cplx', value=1.0)
time = st.number_input('time', value=1.0)
stor = st.number_input('stor', value=1.0)
turn = st.number_input('turn', value=1.0)
acap = st.number_input('acap', value=1.0)
aexp = st.number_input('aexp', value=1.0)
lexp = st.number_input('lexp', value=1.0)
modp = st.number_input('modp', value=1.0)
tool = st.number_input('tool', value=1.0)
sced = st.number_input('sced', value=1.0)
loc  = st.number_input('loc', value=1.0)

# Prediction
if st.button('Dự đoán'):
    inputs = np.array([[rely, data, cplx, time, stor, turn,
                        acap, aexp, lexp, modp, tool, sced, loc]])
    prediction = model.predict(inputs)
    st.success(f"Dự đoán giá trị 'actual': {prediction[0][0]:.4f}")
