from fastapi import APIRouter, Request
from src.config import Config as config
from src.voice import VoiceConvering

router = APIRouter(
    prefix="helpers",
    tags=["helpers"],
    responses={404: {"description": "Not found"}},
)

@router.get('/', status_code=200)
def hello():
    return { "message":"Hi there!" }

@router.post('/convert-voice', status_code=200)
async def webhook(request:Request):
    data = await request.json()    
    container_name, object_name = data['container_name'], data['object_name']
    voice = VoiceConvering.convert_voice(container_name, object_name)
    print(voice)
    return { 'status': 'ok' }