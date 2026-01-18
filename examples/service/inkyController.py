from pathlib import Path
from inky.auto import auto
from PIL import Image

EXAMPLE_DIR_ROOT = Path(__file__).resolve().parent.parent
inky = auto(ask_user=True, verbose=True)

def show_image(resized_image):
    print("Displaying image on Inky...")
    print(resized_image)
    try:
        inky.set_image(resized_image, saturation=0.5)
    except TypeError:
        inky.set_image(resized_image)
    inky.show()

def draw_image(image_path):
    image = Image.open(image_path)
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)

def draw_jjk_image():
    image = Image.open(EXAMPLE_DIR_ROOT / "images" / "jjk.png")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)

def draw_demon_slayer_image():
    image = Image.open(EXAMPLE_DIR_ROOT / "images" / "demonSlayer.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)

def draw_mha_image():
    image = Image.open(EXAMPLE_DIR_ROOT / "images" / "mha.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)

def draw_fire_force_image():
    image = Image.open(EXAMPLE_DIR_ROOT / "images" / "fireForce.jpg")
    resized_image = image.resize(inky.resolution)
    show_image(resized_image)