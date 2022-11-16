def main():
    from PIL import Image
    from image import DrawImage
    import climage
    tmp = "1.png"
    image = DrawImage.from_file(tmp, size=(40, 20))
    image.draw_image()
    
    output = climage.convert('1.png', is_unicode=True, width=80)
    print(output)
main()
