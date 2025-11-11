from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Window.size = (500, 500)
Window.clearcolor = ("blue")

class MyApp(App):
  def build(self):
    layout = BoxLayout()
    layout.add_widget(Label(text="First Line\nHi Lol."))
    return layout
if __name__ == '__main__':
  MyApp().run()