import uvicorn
from fastapi import FastAPI
from settings import settings
from web.api.operations import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run('main:app', port=settings.server_port, host=settings.server_host, reload=True)
