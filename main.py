from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.animation import Animation
class MyApp(App):
  def build(self):
    layout = FloatLayout()

    bg = Image(
      source="my-gradient.png",
      allow_stretch = True,
      keep_ratio = False,
      size_hint=(1,1),
      pos_hint={'x':0,'y':0}
    )

    ayn = Image(source="Al-Ayn-logo.png",
                size_hint=(.5, .5),
                pos_hint={'center_x':0.5, 'top':1})

    layout.add_widget(bg)
    layout.add_widget(ayn)
    layout.add_widget(Label(text="First Line\nHi Lol."))
    return layout
if __name__ == '__main__':
  MyApp().run()