from fastapi import FastAPI
from inkyController import show_jjk, show_demon_slayer

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/jjk")
def show_jjk():
    show_jjk()
    return {"image": "Displaying Jujutsu Kaisen image"}

@app.get("/demon-slayer")
def show_demon_slayer():
    show_demon_slayer()
    return {"image": "Displaying Demon Slayer image"}