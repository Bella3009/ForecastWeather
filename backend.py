import requests
API_Key = "3cb4d4b408331132fc3ca01b1f17ac69"


def get_data(place, fore_days, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    content = response.json()

    # Filter the data
    data = content["list"]
    # The data is taken every 3 hours therefore 3/24 = 8
    points = 8 * fore_days
    filter_data = data[:points]
    if kind == "Temperature":
        filter_data = [dict["main"]["temp"] for dict in filter_data]
    if kind == "Sky":
        filter_data = [dict["weather"][0]["main"] for dict in filter_data]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="Ragusa", fore_days=2, kind="Temperature"))
