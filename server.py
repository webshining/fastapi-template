import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router as api_router
from core.config import PORT, HOST
from core.handlers import shutdown_app_handler, start_app_handler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", shutdown_app_handler(app))
app.include_router(api_router, prefix="/api")

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, port=PORT, host=HOST)
