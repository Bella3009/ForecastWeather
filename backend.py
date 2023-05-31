import requests
API_Key = "3cb4d4b408331132fc3ca01b1f17ac69"

def get_data(place, fore_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    content = response.json()
    return content

if __name__ == "__main__":
    print(get_data(place="Ragusa"))
