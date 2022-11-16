def main():
    from PIL import Image
    from image import DrawImage
    image = DrawImage.from_file("water_slime.PNG", size=(40, 20))
    image.draw_image()
main()
