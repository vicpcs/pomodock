from pathlib import Path
from inky.auto import auto
from PIL import Image

base_dir = Path(__file__).resolve().parent
inky = auto(ask_user=True, verbose=True)

def show_image(resized_image):
    try:
        inky.set_image(resized_image, saturation=0.5)
    except TypeError:
        inky.set_image(resized_image)

def draw_jjk_image():
    image = Image.open(base_dir / "images" / "jjk.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)

def draw_demon_slayer_image():
    image = Image.open(base_dir / "images" / "demonSlayer.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)