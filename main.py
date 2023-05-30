import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days max 5 days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

temp_dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
temp_temp = [10, 11, 15]

figure = px.line(x=temp_dates, y=temp_temp, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)