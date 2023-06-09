import streamlit as st
import plotly.express as px
from backend import get_data as gt

# Setting up the front-end
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days max 5 days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    # Show the graph or picture graph only if there is a place written by user
    if place:
        data = gt(place, days)
        dates = [dict["dt_txt"] for dict in data]

        if option == "Temperature":
            # Retrive the temperature data and then create the graph
            temp = [dict["main"]["temp"] / 10 for dict in data]

            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            # Setting the picture to show according to the data retrieved
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky = [dict["weather"][0]["main"] for dict in data]
            image_path = [images[condition] for condition in sky]

            st.image(image_path, width=115)
except KeyError:
    st.warning("The place chosen is written incorrectly.")