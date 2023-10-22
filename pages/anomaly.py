import datetime
import streamlit as st
import pandas as pd
from functions.get_data import get_query_data, execute_query, execute_model
from functions.get_query import read_query



st.subheader("Anamoly Detection")


try:

    ls_date = st.session_state.date_param + datetime.timedelta(days=st.session_state.days_param+1)

    end_date = ls_date + datetime.timedelta(days=60)

    impressions = st.number_input("Enter the number of impressions to be checked", min_value=None, max_value=None, value=7000)
    date_param = st.date_input("Select a Date:", value = ls_date,
                                    min_value=ls_date ,
                                    max_value= end_date)


    anomaly_model = read_query(f'queries/anomaly/anomaly_model.sql')
    anomaly_call = read_query(f'queries/anomaly/anomaly_call.sql').replace("{date_param}", date_param.strftime("%Y-%m-%d")).replace("{impression}", str(impressions))


    button_clicked = st.button('Execute',key=1004)
    if button_clicked:
        
        execute_model(anomaly_model)
        
        
        df_1 = get_query_data(anomaly_call)
        
        ans = df_1['is_anomaly'].loc[0]
        
        
        
        if ans == True:
            st.write("The impressions for the chosen date are an anomaly")
            
        else:
            st.write("For the chosen date the number of impressions are not an anomaly")   
    st.markdown("---")

except ValueError as e:
    st.error("Please dont leave any fields empty")