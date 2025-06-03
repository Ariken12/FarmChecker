from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_check_geography(self):
        self.manager.current = 'checkgeography'

    def on_check_temperature(self):
        self.manager.current = 'checktemperature'

    def on_check_harmful_concentration(self):
        self.manager.current = 'checkharmfulconcentration'

    def on_check_lighting(self):
        self.manager.current='checklighting'
