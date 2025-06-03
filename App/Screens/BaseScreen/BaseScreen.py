from kivy.uix.screenmanager import Screen

from Screens.KivyBase.ResultPopup import ResultPopup


class BaseScreen(Screen):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, **kwargs)
        self.core = core
        self.resultscreen = ResultPopup()
        self.result = ''
        self.not_ok = False

    def _check_input(self, text, descr=''):
        if text in ('', 'Выбрать', 'Ввести'):
            self.not_ok = True
            self.result += f'Поле {descr} заполнено неправильно\n'
            return
        else:
            self.result += f'{descr}: {text}\n'
            return text

    @staticmethod
    def _output_result(func):
        def wrapper(self):
            try:
                func(self)
                self.resultscreen.ids.result.text = self.result
            except Exception as e:
                self.resultscreen.ids.result.text += 'Произошла ошибка'
                self.resultscreen.ids.result.text += f'{type(e)}: {e}\n'
                self.not_ok = True
            finally:
                self.resultscreen.ids.result.color = 'green' if not self.not_ok else 'red'
                self.resultscreen.ids.result.bind(texture_size=self.resultscreen.ids.result.setter('size'))
                self.resultscreen.open()
        return wrapper