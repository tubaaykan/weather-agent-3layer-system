import requests

API_KEY = "82ee54b04d82d9fbb23ab967ed3b4674"
BASE_URL = "http://api.openweathermap.org/data/2.5"

def get_daily_weather(city: str):
    """Şehrin güncel hava durumunu getirir."""

    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr",       # Türkçe açıklama
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    print(f"🌤 WEATHER API [{city}] status={response.status_code}")

    if response.status_code == 404:
        raise ValueError(f"'{city}' şehri bulunamadı. Şehir adını kontrol edin.")

    if response.status_code == 401:
        raise ValueError("API anahtarı geçersiz.")

    if response.status_code != 200:
        raise ValueError(data.get("message", "API hatası oluştu."))

    return {
        "temp":        round(data["main"]["temp"]),
        "feels_like":  round(data["main"]["feels_like"]),
        "humidity":    data["main"]["humidity"],
        "description": data["weather"][0]["description"].capitalize(),
        "wind_speed":  data["wind"]["speed"],
    }
