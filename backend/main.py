from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .agent import process_request

app = FastAPI()

# CORS — tarayıcının isteği bloklamasını engeller
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # geliştirme için; prod'da domain yaz
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    text: str

@app.post("/weather")
def weather(req: Request):
    return process_request(req.text)
