from fastapi import FastAPI
import uvicorn
from view.users.view_users import router_users
from view.app.view_app import router_app
from view.quiz import view_quiz, view_quiz_generate_oge

app = FastAPI()

app.include_router(router_app)
app.include_router(router_users)
app.include_router(view_quiz.router_quiz)
app.include_router(view_quiz_generate_oge.router_quiz_oge_generate)


if __name__ == '__main__':
    uvicorn.run(app)