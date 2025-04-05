from app.db import Base

from datetime import datetime, date, timezone
from typing import Optional, List

from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import String, DateTime, Date, Boolean, Integer, ForeignKey


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(32), unique=True)
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthdate: Mapped[Optional[date]] = mapped_column(Date)
    joined_at: Mapped[datetime] =  mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[Optional[str]] = mapped_column(String(1000), default='Not Information')
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    score: Mapped[int] = mapped_column(Integer, default=0)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="owned_games")
    questions: Mapped[List["Question"]] = relationship(back_populates="game")


class GameQuestion(Base):
    __tablename__ = "game_questions"

    id: Mapped[int] = mapped_column(primary_key=True)

    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    questions_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))

    question: Mapped["Question"] = relationship(back_populates="games")
    game: Mapped["Game"] = relationship(back_populates="questions")


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String, default='Not Information')
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    option_ids: Mapped[List["Option"]] = relationship(back_populates="questions")
    games: Mapped[List["GameQuestion"]] = relationship(back_populates="question")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))


class Participation(Base):
    __tablename__ = "participations"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    gained_score: Mapped[int] = mapped_column(Integer, default=0)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))


class Option(Base):
    __tablename__ = "options"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
    title: Mapped[str] = mapped_column(String, unique=True)
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    question= relationship("Question", back_populates="option_ids")
    submissions: Mapped[List["Submission"]] = relationship(back_populates="option")


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
    option_id: Mapped[int] = mapped_column(Integer, ForeignKey("options.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="submissions")
    option: Mapped["Option"] = relationship("Option", back_populates="submissions")
    question: Mapped["Question"] = relationship("Question", back_populates="submissions")
