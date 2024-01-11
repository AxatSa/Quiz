from fastapi import APIRouter
from database.testservice import get_question_db, add_question_db
from database.userservice import set_user_answer_db, Register_user_db, plus_point_user_db, get_all_users_db

user_router = APIRouter(prefix='/user', tags=['Users'])


# Регистрация пользователей
@user_router.post('/register')
async def register(name: str, phone: int):
    register = Register_user_db(name, phone)


@user_router.get('/leaders')
async def get_leaders(user_id: int, question_id: int, user_answer: str):
    get_leaders = set_user_answer_db(user_id, question_id, user_answer)


@user_router.post('/done')
async def done(user_id: int, correct_answers: int):
    done = plus_point_user_db(user_id, correct_answers)


@user_router.get('/all_users')
async def get_all_users():
    return get_all_users_db
