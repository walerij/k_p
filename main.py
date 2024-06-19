from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from  img_ import  ImageManage


class Imapp(App):
    def build(self):
        self.manage = ImageManage()
        self.title = "Графический редактор"
        self.layout = BoxLayout()
        return self.layout

    def rotate_pressed(self, *args):
        image = self.manage.rotate(self.layout.imageview, 90)
        self.layout.imageview= image

    def rotate_window_pressed(self, *args):
        content = Button(text='Close me!')
        popup = Popup(title='Test popup',
                      content=content,
                      size_hint=(None, None), size=(400, 400),auto_dismiss=False)
        content.bind(on_press=popup.dismiss)

        popup.open()



my = Imapp()
my.run()