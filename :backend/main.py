from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FinTech Bank API v0.1")

# Müşteri Modeli (Hocanın istediği KYC bilgileri) [cite: 46, 48]
class Customer(BaseModel):
    full_name: str
    identity_no: str # Kimlik numarası

@app.get("/")
def home():
    return {"message": "Banka Backend Sistemi Aktif!"}

@app.post("/customers/") # Müşteri oluşturma ucu [cite: 47]
def create_customer(c: Customer):
    # 1. hafta için veriyi almak ve onaylamak yeterli [cite: 181]
    return {"status": "Müşteri Başarıyla Kaydedildi", "data": c}