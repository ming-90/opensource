from fastapi import FastAPI

class Getclass:
    def __init__(self, app, string):
        @app.get(f"/test{string}")
        def testapp():
            print(f"test {string}")
            return f"test {string}"

class Postclass:
    def __init__(self, app, string):
        @app.post(f"/test{string}")
        def testapp():
            print(f"test {string}")
            return f"test {string}"
