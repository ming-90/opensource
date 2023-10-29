import os
from fastapi import FastAPI, Request, UploadFile
import uvicorn


from tesatapp import Getclass, Postclass

app = FastAPI()

###################
# APIs
###################

# Healthchec
@app.get("/healthcheck")
def healthcheck() -> bool:
    """Server health check."""
    return True

Getclass(app, "123")
Postclass(app, "321")
Postclass(app, "asdf")

class mingradio:
    def __init__(self):
        print("start")

    # if __name__ == 'main':
    def launch(self):
        print("start")
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",
            port=8886
        )
