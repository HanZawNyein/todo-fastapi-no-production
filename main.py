from fastapi import FastAPI
from router import todo_router

app = FastAPI()

app.include_router(todo_router)