from PIL import Image

class ImageManage():
    def __init__(self):
        pass

    # открытие файла изображения
    def open(self, image):
        img= Image.open(image)
        return img
    # показ файла изображения
    def show(self, image):
        img=self.open(image)
        img.show()

    #сохранение файла изображения
    def save (self, image, filename):
        img = self.open(image)
        img.save(filename)