#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from PIL import Image
from xgboost import XGBRegressor
from sklearn import model_selection


# In[2]:


import pickle


# In[3]:


capstone_2 = pickle.load(open('capstone_2.pkl','rb'))


# In[4]:


def welcome():
    return 'welcome all'
  
# this is the main function in which we define our webpage 
def main():
    st.title("Second Hand Vehicles Price Prediction ")
    html_temp = """
    <div style= "backgroung-color:yellow;padding:13px">
    <h2 style= "color:black; text- align:center;"> 
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Brand_Name = st.number_input('Brand of the car',min_value=0, max_value=29)
    Year = st.number_input('Year', min_value=1998, max_value=2019)
    Kilometers_Driven = st.number_input('Kilometers_Driven', min_value=171, max_value=6500000)
    Fuel_Type = st.number_input('Fuel_Type', min_value=0, max_value=4)
    Transmission = st.number_input('Transmission', min_value=0, max_value=1)
    Owner_Type = st.number_input('Owner_Type', min_value=0, max_value=3)
    Mileage = st.number_input('Mileage', min_value=0.0, max_value=33.54)
    Engine = st.number_input('Engine', min_value=72.0, max_value=5998.0)
    Power = st.number_input('Power', min_value=34.2, max_value=560.0)
    Seats = st.number_input('Seats', min_value=0.0, max_value=10.0)
    result=pd.DataFrame([Brand_Name,Year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats])
    x=result.T
    if st.button("Predict"):
        result = capstone_2.predict(x)
    st.success('The Car Price is {}'.format(result))
        
if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:




