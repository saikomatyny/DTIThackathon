from base64 import b64decode

from AI.main import correct_answer

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # List of allowed origins
    allow_credentials=True,  # Whether to allow cookies or authorization headers
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow all headers
)

@app.post("/")
async def create_files(request: Request):
    item = await request.json()


    result = correct_answer(item)

    return result