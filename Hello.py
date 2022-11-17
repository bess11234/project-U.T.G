def main():
    from PIL import Image
    import climage
    output = climage.convert('monster\\goblin.png', is_unicode=True, width=35)
    print(output)
main()