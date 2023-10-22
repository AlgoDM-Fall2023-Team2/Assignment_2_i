import pandas as pd
import streamlit as st
import datetime
from functions.get_data import get_query_data, execute_query
from functions.get_query import read_query



# page headings
st.set_page_config(layout="wide", page_title="INFO7374: Algorithmic Marketing")
st.title("INFO7374: Assignment 2")
st.subheader("Group 1 (Team 2): Adit Bhosle, Sowmya Chatti, Vasundhara Sharma")


with open("home_page_content.html", mode="r",  encoding="utf8") as file:
    home_page_content = file.read()

st.markdown(home_page_content, unsafe_allow_html=True)


# ---------------------------------------------------------------
st.header("Generate Data")

st.write("To generate data for an interesting forecasting perspective and test for yourself, you can enter the date and number of days for which you want to generate data. With these inputs, a random volume of impressions is generated for each of the given number of days ahead of the input date. To make things more interesting, data is tweaked to showcase upward and downward trends on weekdays and weekends respectively.")

    
try:

    # Parameter for number of days of data to be generated  
    days_param = st.number_input("Enter number of Days", min_value=60, max_value=160, value=60)

    # Parameter for choosing the start date for data to be generated
    date_param = st.date_input("Select Start Date:", value=datetime.date(2022, 1, 1),
                                min_value=datetime.date(2022, 1, 1),
                                max_value=datetime.date(2022, 12, 31))
   
    
    # Clean any previous data in the table
    empty_table = read_query(f"queries/data/empty_table.sql")

    # Generate the data using the parameters
    generate_data = (read_query(f"queries/data/generate_data.sql").replace("{days_param}", str(days_param)).replace("{date_param}", date_param.strftime("%Y-%m-%d")))
    
    # Massage the data to create some seasonality
    massage_data = read_query(f"queries/data/massage_data.sql").replace("{date_param}", date_param.strftime("%Y-%m-%d"))
    
    # Fetch all the data
    fetch_all_data = read_query(f"queries/data/fetch_all_data.sql")

    button_clicked = st.button('Generate', key=1002)
   
    if button_clicked:
        
        st.session_state.date_param = date_param
        st.session_state.days_param = days_param
        
        execute_query(empty_table) # Empty table
        execute_query(generate_data) # Generate data
        execute_query(massage_data) # Massage the data

        df_1 = get_query_data(fetch_all_data) # Get all the data
        print(type(df_1))

        st.table(df_1)

        st.write("Here's a graph showing the data that has been generated:")
        st.line_chart(data=df_1, x="day", y="impression_count", color="#0000ff") # Line chart for impressions

    st.markdown("---")

except IndexError as ie:
    st.markdown(f">:red[Please select required number of options to generate a query. Error: {ie} :fearful:]",
                unsafe_allow_html=True)
except BaseException as e:
    st.markdown(f">{e}")
    

