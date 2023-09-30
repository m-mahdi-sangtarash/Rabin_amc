from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
import matplotlib.pyplot as plt


class Selection_screen(GridLayout):
    def __init__(self, **var_args):
        super(Selection_screen, self).__init__(**var_args)
        #Window.clearcolor = (1, 1, 1, 1)
        self.cols = 1
        self.add_widget(Image(source='Logo.png'))
        self.add_widget(Label(text="Welcome To Rabin", color=(0, 0, 0), font_size=40))
        self.add_widget(Button(text='Create new', background_color=(40, 0, 250, 1), size_hint=(0.2, 0.2), size=(350, 100), width=100))


class Main(GridLayout):
    def __init__(self, **var_args):
        super(Main, self).__init__(**var_args)
        self.cols = 2
        self.add_widget(TextInput(multiline=False))


class percent_month(GridLayout):
    def __init__(self, **var_args):
        super(percent_month, self).__init__(**var_args)
        self.cols = 1
        self.rows = 2
        self.add_widget(Button(text='hello'))


class RabinApp(App):
    def build(self):
        return Selection_screen


RabinApp().run()
