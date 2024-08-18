import uvicorn
import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware


load_dotenv("../.env/all.env")
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get('/')
def home():
    return "Hello"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    print(os.getenv("HOST"))
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")))