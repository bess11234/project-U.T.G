def main():
    from PIL import Image
    import climage
    output = climage.convert('1.png', is_unicode=True, width=80)
    print(output)
main()
