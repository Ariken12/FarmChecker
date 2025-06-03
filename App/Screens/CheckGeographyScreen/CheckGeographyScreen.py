from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from Screens.KivyBase.ResultPopup import ResultPopup


class CheckGeographyScreen(Screen):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, **kwargs)
        self.core = core
        self.resultscreen = ResultPopup()
        self.ids.type_self.values = self.core.data['geography']['index'][0]
        self.ids.type_distance.values = self.core.data['geography']['index'][1]
        
    def on_check(self):
        if self.ids.distance.text == '' or self.ids.type_self.text == 'Выбрать' or self.ids.type_distance.text == 'Выбрать' \
        or self.ids.distance.text.isnumeric() == False:
            self.resultscreen.ids.result.text = 'Не все поля заполнены правильно'
            self.resultscreen.ids.result.color = 'orange'
            self.resultscreen.open()
            return
        lim = self.core.data['geography']['data'][self.ids.type_self.text][self.ids.type_distance.text]
        self.resultscreen.ids.result.text = f'''
Расстояние: {self.ids.distance.text}
Тип расстояния: от {self.ids.type_self.text} до {self.ids.type_distance.text}
Минимально разрешенное расстояние: {lim}
'''
        if int(self.ids.distance.text) > int(lim):
            self.resultscreen.ids.result.text += 'Расстояние в пределах допустимого'
            self.resultscreen.ids.result.color = 'green'
        else:
            self.resultscreen.ids.result.text += 'Расстояние не в пределах допустимого'
            self.resultscreen.ids.result.color = 'red'
        self.resultscreen.ids.result.text += '\n'
        self.resultscreen.open()

