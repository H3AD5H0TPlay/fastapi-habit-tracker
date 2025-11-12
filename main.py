# main.py
from fastapi import FastAPI
from models import HabitBase

# alkalmazás példányosítása
app = FastAPI()


# régi "hello world" végpont
@app.get("/")
def read_root():
    return {"Üzenet": "Ez az első API végpontunk!"}

# új végpont szokás létrehozásához
@app.post("/habits/")
def create_habit(habit: HabitBase):
    return habit