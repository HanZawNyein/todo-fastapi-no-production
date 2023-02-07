from fastapi import APIRouter

router = APIRouter()

@router.get('/hello')
async def hello()->dict:
    return {"message":"Hello"}