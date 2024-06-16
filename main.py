from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class Imapp(App):
    def build(self):
        self.title = "Графический редактор"
        self.layout = BoxLayout()
        return self.layout



my = Imapp()
my.run()