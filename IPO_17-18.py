from PIL import Image, ImageFilter

try:
    img = Image.open("C:/Users/alexb/OneDrive/Изображения/Saved Pictures/Wallpaper/1099445.png")
    img.show()
    img2 = img.filter(ImageFilter.FIND_EDGES)
    img2 = img.resize((100,100))
    img2.show()

    img2.save("edges.png")
    img.thumbnail((960, 640))
    #img.show()
    img1 = img.convert('L')
   # img1.show()
    img1.save("ipo18.png")
except IOError:
    pass
