# main.py
from fastapi import FastAPI, Depends
from database import engine, Base, SessionLocal
from models import HabitBase
from sqlalchemy.orm import Session

import models

# --- ADATBÁZIS LÉTREHOZÁSA ---
# Ez a sor az, ami ténylegesen megcsinálja a varázslatot.
# Megmondja az SQLAlchemy-nek, hogy hozza létre az összes táblát
# (amit a 'Base'-ből örökölt osztályok definiálnak, pl. a mi 'Habit' modellünk)
# az 'engine'-ben meghatározott adatbázisban.
Base.metadata.create_all(bind=engine)


# alkalmazás példányosítása
app = FastAPI()

# --- DEPENDENCY ---
# Ez a függvény biztosít egy adatbázis munkamenetet minden kéréshez.
def get_db():
    db = SessionLocal()     # 1. Hozzon létre egy új sessiont
    try:
        yield db            # 2. Adja oda a sessiont a végpontnak, amely kéri
    finally:
        db.close()          # 3. Zárja be a sessiont a kérés befejezése után

# régi "hello world" végpont
@app.get("/")
def read_root():
    return {"Üzenet": "Ez az első API végpontunk!"}


# új végpont szokás létrehozásához
@app.post("/habits/")
def create_habit(habit: HabitBase, db: Session = Depends(get_db)):
    
    # 1. LÉPÉS: Hozzuk létre az adatbázis-modellt a kapott API-adatból
    db_habit = models.Habit(
        name=habit.name,
        description=habit.description,
        frequency=habit.frequency
    )
    
    # 2. LÉPÉS: Adjuk hozzá az új objektumot a munkamenethez
    db.add(db_habit)
    
    # 3. LÉPÉS: Véglegesítsük a változást az adatbázisban (Mentés!)
    db.commit()
    
    # 4. LÉPÉS: Frissítsük az objektumot (hogy megkapja pl. az adatbázis-generált ID-t)
    db.refresh(db_habit)
    
    # 5. LÉPÉS: Adjuk vissza az újonnan létrehozott objektumot
    return db_habit