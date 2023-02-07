from fastapi import APIRouter,Path,HTTPException, status

from models import Todo,TodoItem,TodoItems

router = APIRouter()

todo_list=[]

@router.post('/todo',status_code=201)
async def add_todo(todo:Todo)->dict:
    todo_list.append(todo)
    return {"message":"Todo Added Successfully."}

@router.get("/todo",response_model=TodoItems)
async def reterive_todo()-> dict:
    return {"todos":todo_list}

@router.get('/todo/{todo_id}')
async def get_single_todo(todo_id:int = Path(...,title="get to doo id"))->dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo":todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID Doesn't exist."
    )

@router.put('/todo/{todo_id}')
async def update_single_todo(todo_item:TodoItem, todo_id:int = Path(...,title="get to doo id"))->dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_item.item
            return{
                "todo":todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID Doesn't exist."
    )

@router.delete('/todo/{todo_id}')
async def delte_todo_task(todo_id:int)->dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message":"todo list deleted successfully."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID Doesn't exist."
    )

@router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }
