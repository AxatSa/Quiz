from .models import Leader, Question
from database import get_db


def get_leaders_db():
    db = next(get_db())
    leaders = db.query(Leader.user_id).order_by(Leader.correct_answers.desc())

    return leaders[:5]


def add_question_db(question_text, level, v1, v2, v3, v4):
    db = next(get_db())
    new_question = Question(question_text=question_text, level=level,
                            v1=v1, v2=v2, v3=v3, v4=v4)
    db.commit(new_question)
    db.add(new_question)
    return 'Question added'


def get_question_db():
    db = next(get_db())

    questions = db.query(Question).all()

    return questions[:20]

