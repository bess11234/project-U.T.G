def main():
    from PIL import Image
    from image import DrawImage
    tmp = "water_slime.png"
    image = DrawImage.from_file(tmp, size=(40, 20))
    image.draw_image()
main()
