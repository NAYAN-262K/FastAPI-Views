from fastapi import FastAPI
from src.routers import router as sampleRouter
from src.database import get_db

app = FastAPI()

app.include_router(sampleRouter)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
