from time import strftime

from kivy.app import App
from kivy.clock import Clock


class ClockApp(App):
    sw_started = False
    sw_seconds = 0

    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        self.root.ids.time.text = strftime('[b] %H [/b]:%M:%S')
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = (
            '%02d:%02d.[size=40]%02d[/size]' % (int(minutes), int(seconds), int(seconds * 100 % 100)))

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0


if __name__ == '__main__':
    from kivy.core.text import LabelBase
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex

    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    ClockApp().run()
