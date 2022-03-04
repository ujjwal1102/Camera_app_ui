

from kivymd.uix.screen import MDScreen

from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard,MDCardSwipe
from kivy.properties import StringProperty


class Screen3(MDScreen):
    #Builder.load_file('D:\\python files\\KIVY AND KIVYMD\\REAL TIME FACE DETECTION\\files\\Screen_03.kv')
    
    
    def d_down(self):

        items_d=['Settings','About us.']
        menu_item = [
                {   "text": f"{i}",
                    "viewclass":"OneLineListItem",
                    "height": dp(35),
                    "on_release":lambda x=f"{i}" :self.dropdown_menu(x),
                }
                for i in items_d ] 
        self.dropdown = MDDropdownMenu(
                                caller = self.ids.toolbar,
                                items= menu_item,
                                width_mult=2
                                )
    
    def dropdown_menu(self,x):
        self.dropdown.dismiss()
        if (x == 'Settings'):
            print(x)
        elif (x =='About us.'):
            print(x)

    def add_image_layout(self):

        for i in range(1,6):
            self.ids.md_list_of_images.add_widget(adding_images(text = f'Image {i}'))


    def add_videos_layout(self):
        
        for i in range(1,6):
            self.ids.md_list_of_videos.add_widget(adding_videos(text = f'Video {i}'))


    
class adding_images(MDCardSwipe):
    text = StringProperty()
    
class adding_videos(MDCardSwipe):
    text = StringProperty()


