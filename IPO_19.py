from wand.image import Image
from wand.display import display


with Image(filename="D:/MouseWebSite/images/mouse_1.jpg") as img1:
    print('width =', img1.width)
    print('height =', img1.height)
    img = img1
    display(img)
    img.wave(amplitude=img.height / 50,
             wave_length=img.width / 80)
    img.save(filename="fx-wave.jpg")
    img = img1
    display(img)
    img.vignette(sigma=3, x=10, y=10)
    img.save(filename="fx-vignette.jpg")
    img = img1

    display(img)

