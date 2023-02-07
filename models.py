from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class Item(BaseModel):
    item: str


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Work",
                    "status": "Completed"
                }
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Read the next"
            }
        }


class TodoItems(BaseModel):
    todos: List[Todo]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {'id': 1, "item": "Hello"},
                    {'id': 2, "item": "Item 2"},
                ]
            }
        }
