# main.py
from fastapi import FastAPI

# alkalmazás példányosítása
app = FastAPI()

# endpoint definiálása
@app.get("/")
def read_root():
    return {"Üzenet": "Ez az első API végpontunk!"}