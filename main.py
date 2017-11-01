from time import strftime

from kivy.app import App
from kivy.clock import Clock


class ClockApp(App):
    pass

    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b] %H [/b]:%M:%S')
    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

if __name__ == '__main__':
    from kivy.core.text import LabelBase
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex

    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    ClockApp().run()
