import os

import uvicorn
from dotenv import load_dotenv
load_dotenv("../.env/all.env")

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.api import router


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")))
