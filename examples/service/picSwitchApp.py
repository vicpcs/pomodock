from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/jjk")
def show_jjk():
    return {"image": "Displaying Jujutsu Kaisen image"}

@app.get("/demon-slayer")
def show_demon_slayer():
    return {"image": "Displaying Demon Slayer image"}