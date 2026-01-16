from pathlib import Path
from inky.auto import auto
from PIL import Image

EXAMPLE_ROOT = Path(__file__).resolve().parent.parent
inky = auto(ask_user=True, verbose=True)

def show_image(resized_image):
    print("Displaying image on Inky...")
    print(resized_image)
    try:
        inky.set_image(resized_image, saturation=0.5)
    except TypeError:
        inky.set_image(resized_image)

def draw_jjk_image():
    image = Image.open(EXAMPLE_ROOT / "images" / "jjk.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)

def draw_demon_slayer_image():
    image = Image.open(EXAMPLE_ROOT / "images" / "demonSlayer.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)