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


  #получение параметров
    def get_params(self, image):

        img = self.open(image)
        tmp= {'widht':img.width,'height':img.height,'filename':img.filename,'format':img.format,'mode':img.mode}
        return tmp

    def rotate(self, image, angle):
        img = self.open(image)
        img=img.rotate(angle)
        return img

    #наложение
    def paste(self, image1, image2, x1=0,y1=0,x2=20, y2=20):
        img = Image.open(image1)
        img2 = Image.open(image2)

        img=img.paste(img2, (x1,y1,x2,y2))
        return img


    #зеркальный поворот