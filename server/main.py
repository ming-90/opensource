import os
from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
import uvicorn

from createApis import Getclass, Postclass
from htmlparser import insert_text

app = FastAPI()

###################
# APIs
###################

# Healthchec
@app.get("/healthcheck")
def healthcheck() -> bool:
    """Server health check."""
    return True

def funcTest():
    print("func test")
    linkedFunc()

def linkedFunc():
    print("linked func")

Getclass(app, "123")
Postclass(app, "321", funcTest)
Postclass(app, "asdf", funcTest)

class Mingradio:
    def __init__(self):
        self.htmlString = ""

    def test(self, string, id):
        self.htmlString = "<html> <p id='tt'></p> </html>"
        insert_text(self.htmlString, 'tt', 'aabbcc')


    @app.get("/", response_class=HTMLResponse)
    async def read_users():
        return '''
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        '''

    # if __name__ == 'main':
    def launch(self):
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",
            port=8886
        )
