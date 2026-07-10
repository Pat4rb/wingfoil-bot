import requests


def get_weather(lat, lon):

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&hourly="
        "temperature_2m,"
        "windspeed_10m,"
        "winddirection_10m,"
        "cloudcover,"
        "precipitation"
        "&forecast_days=2"
    )

    response = requests.get(url)

    return response.json()
