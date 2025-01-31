from fastapi import FastAPI
from src.api import router as main_api
import uvicorn

fastapi_app = FastAPI()

fastapi_app.include_router(main_api)

if __name__ == "__main__":
    uvicorn.run("app:fastapi_app", reload=True, host="0.0.0.0")
