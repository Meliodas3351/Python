from wand.image import Image
from wand.display import display


with Image(filename="D:/MouseWebSite/images/mouse_1.jpg") as img:
    # img.wave(amplitude=img.height / 50,       #волна
    #          wave_length=img.width / 80)
    # img.save(filename="fx-wave.jpg")

    img.vignette(sigma=20, x=50, y=25)     #виньетка
    img.save(filename="fx-vignette.jpg")

    # img.shade(gray=True,      #оттенок
    #           azimuth=286.0,
    #           elevation=45.0)
    # img.save(filename="effect-shade.jpg")

    # img.swirl(degree=-90)     #вихрь
    # img.save(filename='fx-swirl.jpg')

    # with Image(filename="fx-wave.jpg") as left_eye:   #стереограмма
    #     with Image(filename="fx-vignette.jpg") as right_eye:
    #         with Image.stereogram(left=left_eye,
    #                               right=right_eye) as img:
    #             img.save(filename="fx-stereogram.jpg")
    #             display(img)

    # img.transform_colorspace("gray")  #эскиз
    # img.sketch(0.5, 0.0, 98.0)
    # img.save(filename="fx-sketch.jpg")

    # img.charcoal(radius=1.5, sigma=0.5) #уголь
    # img.save(filename="fx-charcoal.jpg")

    display(img)

