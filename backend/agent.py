from .weather_api import get_weather

def process_request(text: str):

    try:
        city = text.split()[0]
        weather = get_weather(city)

        return {
            "city": city,
            "temp": weather.get("temp"),
            "description": weather.get("description")
        }

    except Exception as e:
        print("🔥 AGENT ERROR:", e)
        return {
            "error": str(e)
        }