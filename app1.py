# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:32:05 2023

@author: Appu
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st

# loading in the model to predict on the data
loaded_model = pickle.load(open('df.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Steel Plant Load Prediction',
                          
                          ['Introduction',
                           'Basic EDA',
                           'Steel Plant Load Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)


def steel_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Light Load'
    elif (prediction[0] == 1):
        return 'Medium Load'
    else:
        return 'Maximum Load'
    
def main():
    
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:pink;padding:13px">
    <h1 style ="color:black;text-align:center;font-family:Lucida Calligraphy; color:Brown; font-size: 22px;">Steel Plant Load Prediction With Artificial Intelligence</h1>
    </div>
    """  
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    Usage_kWh = st.number_input("Usage_kWh")
    Lagging_Reactive_Power_kVarh = st.number_input("Lagging_Reactive_Power_kVarh")
    Leading_Reactive_Power_kVarh = st.number_input("Leading_Reactive_Power_kVarh")
    CO2 = st.number_input("CO2")
    Lagging_Power_Factor = st.number_input("Lagging_Power_Factor")
    Leading_Power_Factor = st.number_input("Leading_Power_Factor")
    NSM = st.number_input("NSM")
    WeekStatus = st.number_input("WeekStatus")
    Day_of_week = st.number_input("Day_of_week")
    
    # code for Prediction
    load = ''
    # creating a button for Prediction
    
    if st.button('Steel industry load prediction[ PRESS BUTTON ]'):
        load = steel_prediction([Usage_kWh, Lagging_Reactive_Power_kVarh, Leading_Reactive_Power_kVarh, CO2, Lagging_Power_Factor, Leading_Power_Factor, NSM, WeekStatus, Day_of_week])
    st.success(load)

    
if __name__=='__main__':
    main()
    

# the font and background color, the padding and the text to be displayed
html_temp = """
<div style ="background-color:yellow;padding:13px">
<h1 style ="color:black;text-align:left;font-family:Lucida Calligraphy; color:Green; font-size: 18px;">Load Prediction of Steel Plant for the above data is above</h1>
</div>
"""  
# this line allows us to display the front end aspects we have 
# defined in the above code
st.markdown(html_temp, unsafe_allow_html = True)
    
