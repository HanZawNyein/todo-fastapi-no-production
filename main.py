from fastapi import FastAPI
from router import todo_router
app = FastAPI()

app.include_router(
    router=todo_router
)