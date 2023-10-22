import datetime
import streamlit as st
import pandas as pd
from functions.get_data import get_query_data, execute_query, execute_model
from functions.get_query import read_query
import altair as alt


st.subheader("Forecasting Ad Impressions")

st.write("Using the generated data, an ML model is trained to forecast the ad-impressions. You can input the number of days you wish to forecast the ad-impressions for, and the snowflake powered ML model comes up with predictions for each of the given days.")

day = st.number_input("Enter the number of days you wish to forecast for", min_value=7, max_value=None, value=7)

forecast_query = read_query(f"queries/forecast/forecast.sql").replace("{day_param}", str(day))

actual_data = read_query(f'queries/forecast/actual.sql')

forecast_model = read_query(f'queries/forecast/forecast_model.sql')

button_clicked = st.button('Execute', key=1003)
if button_clicked:
    
    execute_model(forecast_model)

    df_1 = get_query_data(forecast_query)
    df_2 = get_query_data(actual_data)
    
    df_3 = pd.DataFrame(columns=['Days','Impression_counts'])
    df_3['Days'] = pd.concat([df_1['ts'],df_2['day']],axis=0,ignore_index=True)
    df_3['Impression_counts'] = pd.concat([df_1['forecast'],df_2['impression_count']],axis=0,ignore_index=True)
    
    df_3 = df_3.sort_values('Days')

    # Creating color coding column
    df_3['Legend'] = ['Actual' if i < len(df_3)-day else 'Forecast' for i in range(len(df_3))]

    
    # Creating a color-coded line chart
    chart = alt.Chart(df_3).mark_line().encode(
        x='Days',
        y='Impression_counts',
        color=alt.Color('Legend', scale=alt.Scale(domain=['Actual', 'Forecast'], range=['grey', 'orange']))
    ).properties(width=600, height=400)

    st.markdown(f"Here's a graph showing the actual ad-impressions that the model has been trained for and forecasted ad-impressions")
    st.altair_chart(chart, use_container_width=True)
       
st.markdown("---")
