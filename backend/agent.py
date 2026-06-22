from .weather_api import get_daily_weather

def process_request(text: str):

    if not text or not text.strip():
        return {"error": "Please enter a city name."}

    stop_words = ["weather", "hava", "durumu", "forecast"]
    city_words = [w for w in text.split() if w.lower() not in stop_words]
    city = " ".join(city_words).strip()

    if not city:
        return {"error": "Couldn't extract a city name."}

    try:
        weather = get_daily_weather(city)
        return {
            "city": city,
            "temp": weather.get("temp"),
            "feels_like": weather.get("feels_like"),
            "description": weather.get("description"),
            "humidity": weather.get("humidity"),
            "wind_speed": weather.get("wind_speed"),
        }
    except Exception as e:
        print("AGENT ERROR:", e)
        return {"error": str(e)}
    