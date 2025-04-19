from fastapi import APIRouter, HTTPException, status

from typing import List

from app.models import Question
from app.dependencies import db_dep, current_user_dep
from app.schemas.question import *


router = APIRouter(prefix="/question", tags=["question"])


@router.get('/', response_model=List[QuestionResponse])
async def get_questions(db: db_dep):
    return db.query(Question).all()


@router.get('/{id}', response_model=QuestionResponse)
async def get_question(id: int, db: db_dep):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    return question


@router.post('/', response_model=QuestionResponse)
async def create_question(db: db_dep,
                          question: QuestionCreate,
                          current_user: current_user_dep):
    db_question = Question(
        **question.model_dump(),
        owner_id=current_user.id
    )

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


@router.put('/{id}', response_model=QuestionResponse)
async def update_question(id: int,
                          db: db_dep,
                          question: QuestionUpdate):
    db_question = db.query(Question).filter(Question.id == id).first()
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    db_question.title = question.title if question.title else db_question.title
    db_question.description = question.description if question.description else db_question.description
    db_question.topic_id = question.topic_id

    db.add(question)
    db.commit()
    db.refresh(db_question)

    return db_question


@router.delete('/delete/{id}', response_model=QuestionResponse)
async def delete_question(id: int, db: db_dep):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

    db.delete(question)
    db.commit()
    return question