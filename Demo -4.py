
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

Window.size = (250, 450)

class ChatBot(MDApp):

    def change_screen(self, name):
     screen_manager.current = name

    def build(self):
        global screen_manager 
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))

        return screen_manager
    





