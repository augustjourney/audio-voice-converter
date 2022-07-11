import uvicorn
from src.config import Config as config
if __name__ == '__main__':
    uvicorn.run("src.app:create_app", host=config.HOST, port=config.PORT, reload=True, access_log=False)