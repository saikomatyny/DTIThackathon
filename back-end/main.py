from base64 import b64decode

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

    with open('userFile.pdf', 'wb') as fw:
        fw.write(b64decode(item["userFile"]))

    with open('templateFile.pdf', 'wb') as fw:
        fw.write(b64decode(item["templateFile"]))