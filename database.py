# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Az adatbázis URL-je
# Azt mondja az SQLAlchemy-nek, hogy "egy 'habits.db' nevű SQLite adatbázist használj
# SQLite adatbázisként ebben a mappában".
SQLALCHEMY_DATABASE_URL = "sqlite:///./habits.db"

# 2. Az Engine
# Ez a központi objektum, amely kezeli az adatbázissal való kommunikációt.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # Ez a "connect_args" csak SQLite esetén szükséges.
    # Azt mondja, hogy engedélyezze, hogy több szál is használhassa ugyanazt a kapcsolatot.
    connect_args={"check_same_thread": False}
)

# 3. A Session
# Minden alkalommal, amikor beszélni akarunk az adatbázissal,
# egy "Session" objektumon keresztül tesszük ezt. Ez a SessionLocal egy gyár,
# amely új Session példányokat hoz létre.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Az alap osztály a modellekhez
# Később, amikor az adatbázis-táblákat Python osztályként leírjuk,
# ebből a 'Base'-ből fogunk származni.
Base = declarative_base()