from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_button_press(self):
        self.manager.current = 'menu'