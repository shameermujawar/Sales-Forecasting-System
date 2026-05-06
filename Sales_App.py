#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import pickle

# Load model safely
try:
    model = pickle.load(open("sales_model.pkl", "rb"))
except:
    st.error("Model file not found! Please train model first.")
    st.stop()

st.title("📊 Sales Forecasting System")

st.write("Enter details to predict sales")

# User Inputs
date = st.date_input("Select Date")

product_ID = st.text_input("Enter Product ID (e.g., P101,P102,P103,P104,P105)")
store_ID = st.text_input("Enter Store ID (e.g., S1, S2, S3)")

# ❗ These should NOT be inputs if predicting Units_Sold
# (Units_Sold is target, Revenue depends on prediction),
# So we remove them OR keep optional display only

promotion = st.selectbox("Promotion", [0, 1])
holiday = st.selectbox("Holiday", [0, 1])

# Feature Engineering
year = date.year
month = date.month
day = date.day
dayofweek = date.weekday()

# Prediction
if st.button("Predict Sales"):

    input_df = pd.DataFrame({
        'Year': [year],
        'Month': [month],
        'Day': [day],
        'DayOfWeek': [dayofweek],
        'Promotion': [promotion],
        'Holiday': [holiday]
    })

    prediction = model.predict(input_df)

    st.success(f"📊 Predicted Units Sold: {int(prediction[0])}")


# In[ ]:




