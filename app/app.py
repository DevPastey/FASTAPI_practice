from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def user():
    return ({
        "name": "DevPastey"
    })
