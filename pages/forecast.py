import datetime
import streamlit as st
import pandas as pd
from functions.get_data import get_query_data, execute_query
from functions.get_query import read_query
import altair as alt


st.subheader("Forecasting Ad Impressions")


day = st.number_input("Choose the number of days you wish to forecast for", min_value=7, max_value=60, value=7)

forecast_query = read_query(f"queries/forecast/forecast.sql").replace("{day_param}", str(day))

actual_data = read_query(f'queries/forecast/actual.sql')



button_clicked = st.button('Execute', key=1002)
if button_clicked:

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

    st.markdown(f"Here's a graph showing the actual and forecasted ad-impressions")
    st.altair_chart(chart, use_container_width=True)
       
st.markdown("---")
