def main():
    from PIL import Image
    import climage
    for i in ["blood_potion.png", "broke_glasses.png", "mana_potion.png"]:
        output = climage.convert('item\\'+i, is_unicode=True, width=15)
        print(output)
main()