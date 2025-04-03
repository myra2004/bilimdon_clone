from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, relationship
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(DateTime)
    joined_at = Column(DateTime)
    is_active = Column(Boolean)
    is_staff = Column(Boolean)
    is_superuser = Column(Boolean)

    games= relationship("Game", back_populates="owner")
    participations = relationship("Participation", back_populates="user_id")
    submissions = relationship("Submission", back_populates="user_id")


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", backref="games")
    title = Column(String)
    description = Column(String)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    topic = relationship("Topic", backref="games")
    score = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    owner = Column(String)
    title = Column(String)
    description = Column(String)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    topic = relationship("Topic", back_populates='questions')
    options_id = Column(Integer, ForeignKey("options.id"))
    options = relationship("Option", back_populates="questions")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class GameQuestion(Base):
    __tablename__ = "game_questions"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="questions")
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="questions")


class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True)
    question_id= Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="options")
    title = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="submissions")
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="submissions")
    option_id = Column(Integer, ForeignKey("options.id"))
    options = relationship("Option", back_populates="submissions")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Participation(Base):
    __tablename__ = "participations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="participations")
    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="participations")
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    gained_score = Column(Integer)
    registered_at = Column(DateTime)