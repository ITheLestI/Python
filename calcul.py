import kivy
from kivy.app import App
from kivy.uix.button import Button

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy import Config
Config.set('graphics', 'multisamples', '0')

class DummyApp(App):
    def build(self):
        return Button(text="Hello World")

if __name__ == '__main__':
    DummyApp().run()
    