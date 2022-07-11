from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.config import Config as config
from src.router import router

def create_app():
    app = FastAPI()  
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in config.ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ) 
    app.include_router(router)
    print('Started')
    return app