from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window


class Selection_screen(GridLayout):
    def __init__(self, **kwargs):
        super(Selection_screen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Welcome To Rabin", font_size=40))
        self.button = Button(text='Create new', background_color=(40, 0, 250, 1), size_hint=(0.2, 0.2), size=(350, 100),
                             width=100)
        self.add_widget(self.button)


class MyApp(App):
    def build(self):
        return Selection_screen


MyApp().run()
