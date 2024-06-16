from PIL import Image

# открытие изображения
img = Image.open("leto.jpg")
img=img.rotate(90)

img.show()
