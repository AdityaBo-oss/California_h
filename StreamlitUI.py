import streamlit as st
import joblib
import numpy 
st.title('California House Price Prediction')
obj=joblib.load(r'C:\Users\PC World\Documents\project File\california_h.joblib')
model=obj['model']
cols=obj['columns']
st.write('For the Housing Prediction click this button ')
le=[]
for i in cols:
    v=st.number_input(f'Put the value of {i} in this ')
    le.append(v)

ans=model.predict([le])
if st.button('Click for the required Prediction'):
    st.success(f'The prediction is:{ans}')
