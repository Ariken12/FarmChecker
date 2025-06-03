
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import FadeTransition, CardTransition, SwapTransition, \
    WipeTransition, SlideTransition, RiseInTransition, ShaderTransition, NoTransition

from Screens.MainScreen.MainScreen import MainScreen
from Screens.MenuScreen.MenuScreen import MenuScreen
from Screens.CheckGeographyScreen.CheckGeographyScreen import CheckGeographyScreen
from Screens.CheckAirSpeedScreen.CheckAirSpeedScreen import CheckAirSpeedScreen
from Screens.CheckLightingScreen.CheckLightingScreen import CheckLightingScreen
from Screens.CheckTemperatureScreen.CheckTemperatureScreen import CheckTemperatureScreen
from Screens.CheckManureScreen.CheckManureScreen import CheckManureScreen


class MainScreenManager(ScreenManager):
    def __init__(self, *args, core, **kwargs):
        super(MainScreenManager, self).__init__(*args, transition=SwapTransition(), **kwargs)
        self.add_widget(MainScreen(name='main'))
        self.add_widget(MenuScreen(name='menu'))
        self.add_widget(CheckGeographyScreen(core=core, name='checkgeography'))
        self.add_widget(CheckAirSpeedScreen(core=core, name='checkairspeed'))
        self.add_widget(CheckLightingScreen(core=core, name='checklighting'))
        self.add_widget(CheckTemperatureScreen(core=core, name='checktemperature'))
        self.add_widget(CheckManureScreen(core=core, name='checkmanure'))
        self.current = 'main'
