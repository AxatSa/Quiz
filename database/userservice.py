from database.models import User, Question, UserAnswers, Leader
from datetime import datetime
from database import get_db


# Создаем регистрацию польоателя
def Register_user_db(name, phone):
    db = next(get_db())
    # проверка на наличие юзера
    checker = db.query(User).filter_by(phone=phone).first()

    if checker:
        return checker.id
    else:
        new_user = User(name=name, phone=phone)
    db.add(new_user)
    db.commit()

    return new_user.id


def set_user_answer_db(user_id, question_id, user_answer):
    db = next(get_db())

    exact_question = db.query(Question).filter_by(id=question_id).first()

    if exact_question:
        # Сравнить ответ Пользователя
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False

        new_user_answer = UserAnswers(user_id=user_id,
                                      question_id=question_id,
                                      user_answer=user_answer,
                                      correctness=correctness)

        db.add(new_user_answer)
        db.commit()

        return True if correctness else False
    return "Question not found"


# Увелечение баллов пользователя
def plus_point_user_db(user_id, correct_answers):
    db = next(get_db())

    checker = db.query(Leader).filter_by(user_id=user_id).first()

    if checker:
        checker.correct_answers += correct_answers

    else:
        new_leader_data = Leader(user_id=user_id, correct_answers=correct_answers)

        db.add(new_leader_data)
        db.commit()

        # получаем позицию в списке
        all_leaders = db.query(Leader.user_id).order_by(Leader.correct_answers.desc())

        return all_leaders.index((user_id,)) + 1


def get_all_users_db(name, phone):
    db = next(get_db())

    users = db.query(User).all()

    return users
