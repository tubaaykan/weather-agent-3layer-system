import requests

API_KEY = "82ee54b04d82d9fbb23ab967ed3b4674"

def get_weather(city: str):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    print("🔥 WEATHER API RESPONSE:", data)

    # 🚨 SAFE CHECK (EN ÖNEMLİ KISIM)
    if response.status_code != 200:
        return {
            "temp": None,
            "description": data.get("message", "API error")
        }

    # ✔ sadece başarılı response'ta buraya gelir
    return {
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }