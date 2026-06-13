# FastAPI framework’ünü import ediyoruz (web server oluşturmak için)
from fastapi import FastAPI

# Pydantic: gelen veriyi doğrulamak (input model) için kullanılır
from pydantic import BaseModel

# Kendi yazdığımız logic dosyasından fonksiyon import ediyoruz
# hava durumu işlemi
from .agent import process_request


# FastAPI uygulamasını oluşturuyoruz
app = FastAPI()


# Frontend’den gelecek veri yapısını tanımlıyoruz
# Yani kullanıcıdan "text" adlı bir string bekliyoruz
class Request(BaseModel):
    text: str


# POST endpoint oluşturuyoruz
# Frontend buraya istek atıyor: /weather
@app.post("/weather")
def weather(req: Request):

    # Frontend’den gelen text’i alıyoruz (örnek: "Tübingen weather")
    # req.text → JSON içindeki "text" alanı
    return process_request(req.text)