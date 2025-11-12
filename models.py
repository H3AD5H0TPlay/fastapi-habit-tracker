# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text
from database import Base

# Alap "Habit" modell
# Meghatározza egy szokás alapvető tulajdonságait,
# amikor létrehozzuk vagy olvassuk.
class HabitBase(BaseModel):
    name: str
    description: str | None = None
    frequency: str
    
# SQLAlchemy modell
# Ez az osztály írja le a "habits" táblát az adatbázisban.
# a 'Base'-ből öröklődik, amit a database.py fájlban definiáltunk.
class Habit(Base):
    __tablename__ = "habits"                            # A tábla neve az adatbázisban
    
    # A tábla oszlopai:
    id = Column(Integer, primary_key=True, index=True)  # Elsődleges kulcs
    name = Column(String, index=True)                   # Szokás neve
    description = Column(Text, nullable=True)           # Szokás leírása
    frequency = Column(String)                          # Szokás gyakorisága