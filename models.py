# models.py
from pydantic import BaseModel

# Alap "Habit" modell
# Meghatározza egy szokás alapvető tulajdonságait,
# amikor létrehozzuk vagy olvassuk.
class HabitBase(BaseModel):
    name: str
    description: str | None = None
    frequency: str