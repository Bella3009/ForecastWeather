import streamlit as st
import plotly.express as px
from backend import get_data as gt

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days max 5 days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    data = gt(place, days)
    dates = [dict["dt_txt"] for dict in data]

    if option == "Temperature":
        temp = [dict["main"]["temp"] for dict in data]
        # Create graph
        figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if option == "Sky":
        filter_data = [dict["weather"][0]["main"] for dict in data]
