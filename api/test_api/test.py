from fastapi import APIRouter
from database.testservice import get_question_db, add_question_db
from database.userservice import set_user_answer_db

test_router = APIRouter(prefix='/test', tags=['Process Test'])


# Получаем все тесты(вопросы)


@test_router.post('/add-question')
async def add_question(question_text: str, level: str, v1: str, v2: str, v3: str, v4: str):
    result = add_question_db(question_text, level, v1, v2, v3, v4)
    if result:
        return {'status': 'success', 'massage': result}
    else:
        return 'Nevermore add question'


@test_router.get('/get-questions')
async def get_questions():
    questions_list = get_questions_db()
    if questions_list:
        return {'timer': 12, 'questions': questions_list}
    else:
        return 'Haven`t questions'


@test_router.post('/check-answer')
async def check_answer(user_id: int, question_id: int, user_answer: int):
    result = set_user_answer_db(user_id, question_id, user_answer)
    if result:
        return {'status': result}
    else:
        return "No Answers"
