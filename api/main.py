from fastapi import FastAPI, HTTPException, Query, Path
from scripts.regsetup import description
from sqlalchemy import Session
from typing import List, Optional
from database import SessionLocal
import query_helpers as helpers
import schemas

api_description = '''Bienvenue dans l'API MovieLens'''

# --- Initialisation de l'application FastAPI ---
app = FastAPI(
    title='MovieLens API',
    description= api_description,
    version='0.1'
)


# --- Dépendance pour la session de base de données ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoint pour tester la santé de l'API
@app.get(
    '/',
    summary="Vérification de la santé de l'API",
    description="Vérifie que l'API fonctionne correctement",
    response_description="Statut de l'API",
    operation_id="health_check_movies_api",
    tags=["monitoring"]
)

async def root():
    return {"message": "API MovieLens opérationnelle"}

