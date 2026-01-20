from inky.auto import auto
from PIL import Image, ImageDraw

def main():
    inky = auto()
    width, height = inky.resolution

    image = Image.new("P", (width, height), color=inky.WHITE)
    draw = ImageDraw.Draw(image)

    draw.text((10, 10), "Hello, world 👋", fill=inky.BLACK)
    draw.text((10, 40), "Inky Impression + Pi Zero", fill=inky.BLACK)

    inky.set_image(image)
    inky.show()

if __name__ == "__main__":
    main()
