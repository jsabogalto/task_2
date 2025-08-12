from fastapi import FastAPI
from routes import posts

app = FastAPI(title="task2")

app.include_router(posts.router)