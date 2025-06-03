from kivy.uix.screenmanager import Screen

from Screens.KivyBase.ResultPopup import ResultPopup


class CheckTemperatureScreen(Screen):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, **kwargs)
        self.core = core

    def on_check(self):
        pass

