from fastapi import FastAPI, Request

from app.routers.auth import router as auth_router
from app.routers.question import router as question_router
from app.dependencies import db_dep
from app.models import User


app = FastAPI()

app.include_router(auth_router)
app.include_router(question_router)


@app.get('/get')
async def get(db: db_dep):
    return db.query(User).all()