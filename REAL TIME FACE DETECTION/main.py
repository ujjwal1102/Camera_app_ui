#from subprocess import call
#from unicodedata import name
import os
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


#from kivy.properties import ObjectProperty
#from kivy.config import Config


KV_DIR = f"d:\\python files\\KIVY AND KIVYMD\\REAL TIME FACE DETECTION\\files\\kv"

for kv_file in os.listdir(KV_DIR):
    
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())
        




KV ="""

#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import Screen1 files.baseclass.Screen_01.Screen1
#:import Screen2 files.baseclass.Screen_02.Screen2
#:import Screen3 files.baseclass.Screen_03.Screen3


ScreenManager:
    transition: WipeTransition()

    Screen1:
        name: "screen_1"

    Screen2:
        name: "screen_2"

    Screen3:
        name: "screen_3"

    
"""



class FaceDetectionApp(MDApp):

    

    def build(self):
        Window.size = (300,600)
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

        


if __name__ == '__main__':

    
    FaceDetectionApp().run()
