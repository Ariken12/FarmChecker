from Core.Core import Core

from kivy.app import App
from Screens.MainScreenManager import MainScreenManager
from kivy.logger import Logger, LOG_LEVELS


class MyApp(App):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, **kwargs)
        self.core = core
        print("App initialized")

    def build(self):
        print("Building the app")
        return MainScreenManager(core=self.core)

    def on_start(self):
        print("App is starting")

    def on_pause(self):
        print("App is paused")
        return True  # Return True to indicate that the app can be paused

    def on_resume(self):
        print("App is resumed")

    def on_stop(self):
        print("App is stopping")

def main():
    Logger.setLevel(LOG_LEVELS['debug'])
    core = Core()
    MyApp(core=core).run()

if __name__ == '__main__':
    main()
