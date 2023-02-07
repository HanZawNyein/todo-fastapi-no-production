from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates

from models import Todo, TodoItem, TodoItems

router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")


@router.post('/todo', status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> dict:
    todo.id = len(todo_list)+1
    todo_list.append(todo)
    # return {"message":"Todo Added Successfully."}
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })


@router.get("/todo", response_model=TodoItems)
async def reterive_todo(request: Request) -> dict:
    # return {"todos": todo_list}
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })


@router.get('/todo/{todo_id}')
async def get_single_todo(request: Request, todo_id: int = Path(..., title="get to doo id")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse('todo.html', {
                "request": request,
                "todo": todo

            })
            # return {
            #     "todo": todo
            # }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID Doesn't exist."
    )


@router.put('/todo/{todo_id}')
async def update_single_todo(todo_item: TodoItem, todo_id: int = Path(..., title="get to doo id")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_item.item
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID Doesn't exist."
    )


@router.delete('/todo/{todo_id}')
async def delte_todo_task(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "todo list deleted successfully."}
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
