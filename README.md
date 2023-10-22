# Assignment 2 Part 1

<!-- **Welcome to Snowflake Powered ML Modelling**  -->



**Access the Streamlit application:** [Click here](https://team02-assignment02-part01.streamlit.app/)

**Access Codelabs document:** [Click here](https://codelabs-preview.appspot.com/?file_id=1_TlIprmugQnLkHQ8zF7xFMn84xxv-Di4Vctq-DFC7Kk#0)


This application, built for companies to assess advertising impressions, harnesses the power of Snowflake's ML-Powered Analysis. Through synthetic data generation, it enables users to simulate and test various scenarios. Leveraging Snowflake's advanced Forecasting feature, the application can project future ad impression volumes for a specified duration, aiding in strategic planning and resource allocation. Moreover, with its Anomaly Detection capability, it empowers businesses to identify unusual patterns or discrepancies in impression data, facilitating proactive decision-making and ensuring optimal advertising performance. By integrating these powerful ML capabilities, companies can gain valuable insights into their advertising strategies and make data-driven decisions to maximize the impact of their marketing efforts.

## Page 1: Generate Data 

To generate data for an interesting forecasting perspective and test for yourself, you can enter the date and number of days for which you want to generate data. With these inputs, a random volume of impressions is generated for each of the given number of days ahead of the input date. To make things more interesting, data is tweaked to showcase upward and downward trends on weekdays and weekends respectively.

## Page 2: Forecasting Ad Impressions  📈

Using the generated data, an ML model is trained to forecast the ad-impressions. You can input the number of days you wish to forecast the ad-impressions for, and the snowflake powered ML model comes up with predictions for each of the given days.

## Page 3: Anomaly Detection

Using the generated data, a new Snowflake-ML model is trained to detect an anomaly. This model is now ready to predict whether the volume of ad impressions on a given day is anticipated or is an anomaly.

