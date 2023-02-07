from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    item:str

class Todo(BaseModel):
    id:int
    item:str

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "item":{
                    "item":"Work",
                    "status":"Completed"
                }
            }
        }

class TodoItem(BaseModel):
    item:str

    class Config:
        schema_extra = {
            "example":{
                "title":"Read the next"
            }
        }
class TodoItems(BaseModel):
    todos:List[Todo]

    class Config:
        schema_extra = {
            "example":{
                "todos":[
                    {'id':1, "item":"Hello"},
                    {'id':2, "item":"Item 2"},
                ]
            }
        }