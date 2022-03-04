
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
#from kivy.properties import ObjectProperty
#from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.camera import Camera
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock
import cv2
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDFillRoundFlatButton
#from camera_and_video import *
from kivymd.toast.kivytoast.kivytoast import toast 
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton


class Screen2(MDScreen):
    #Builder.load_file('D:\\python files\\KIVY AND KIVYMD\\REAL TIME FACE DETECTION\\files\\Screen_02.kv') 
    #def __init__(self, **kw):
    #    super().__init__(**kw)

    
    def capture(self):

        self.img1 = Image(size = (300,600))
        self.capt = cv2.VideoCapture(0)


        if not self.capt.isOpened():
            raise Exception("Could Not open Camera")


        self.ids.for_widgets.add_widget(self.img1)
        Clock.schedule_interval(self.update,1.0/33.0)

    def update(self,dt):
        
        ret,self.frame = self.capt.read()
        buf1 = cv2.flip(self.frame,0)
        buf = buf1.tostring()
        texture1 = Texture.create(size = (self.frame.shape[1],self.frame.shape[0]), colorfmt = 'bgr')
        texture1.blit_buffer(buf, colorfmt = 'bgr', bufferfmt = 'ubyte')
        self.img1.texture = texture1

    def capture_button(self):
        
        cv2.imwrite('This_image.png',self.frame)
        
    def show_toast(self):
        toast('Saved',duration=0.5)


    def  color(self,instance):
        
        instance.md_bg_color = get_color_from_hex('#888888')
        

class MyToggleButton(MDRectangleFlatButton,MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light
        


        
