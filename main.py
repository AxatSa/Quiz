from api.test_api.test import test_router
from api.user_api.users import user_router
from fastapi import FastAPI
from database import Base, engine
# uvicorn Название файла:app --reload

app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(test_router)
app.include_router(user_router)















# get для получения запроса
# @app.get('/bebebe', tags=['Products'])
# async def all_products():
#     return {'Title': 'hp', 'price': '1241'}
#
#
# @app.get('/bibibi', tags=['Products'])
# async def bibibi():
#     return {'massage2': 'biba and boba bibibibi'}
#
#
# @app.post('/bibibi', tags=['my_products'])
# async def post(name: str, phone: int, email: str):
#     return {f'Name:{name}, Phone:{phone}, Email:{email}'}
#
#
# @app.put('/change_bibibi', tags=['my_products'])
# async def change_users(name: str, phone: int, email: str):
#     return {f'Name:{name}, Phone: {phone}, Email:{email}'}
