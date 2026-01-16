from fastapi import FastAPI
from inkyController import draw_jjk_image, draw_demon_slayer_image, draw_mha_image

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/jjk")
def show_jjk():
    draw_jjk_image()
    return {"image": "Displaying Jujutsu Kaisen image"}

@app.get("/demon-slayer")
def show_demon_slayer():
    draw_demon_slayer_image()
    return {"image": "Displaying Demon Slayer image"}

@app.get("/mha")
def show_mha():
    draw_mha_image()
    return {"image": "Displaying My Hero Academia image"}