
from Screens.BaseScreen.BaseScreen import BaseScreen


class CheckManureScreen(BaseScreen):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, core=core, **kwargs)
        for animal in self.core.data['manure']:
            self.ids.animal_type.values.append(animal)

    @BaseScreen._output_result
    def on_check(self):
        self.not_ok = False
        self.result = 'Введенные данные:\n'
        animal = self._check_input(self.ids.animal_type.text, 'Тип животного')
        animal_count = self._check_input(self.ids.animal_count.text, 'Количество животных')
        manure_density = self._check_input(self.ids.manure_density.text, 'Плотность навоза')
        manure_area = self._check_input(self.ids.manure_area.text, 'Площадь навозохранилища')
        manure_depth = self._check_input(self.ids.manure_depth.text, 'Высота навозохранилища')
        limits = self.core.data['manure'][animal]
        self.result += '\nТабличные значения:\n'
        self.result += 'Нормы для этого животного:\n'
        self.result += f'Количество экскрементов в день: {limits["summ_of_manure"]}\n'
        self.result += f'Количество подстилки в день: {limits["summ_of_trash"]}\n'
        if self.not_ok:
            raise ValueError("Не все поля заполнены")
        self.not_ok = False
        self.result += '\nРассчеты:\n'
        custom_manure = int(animal_count) * (int(limits["summ_of_manure"])+int(limits["summ_of_trash"]))
        self.result += f'Количество экскрементов за 180 дней: {custom_manure}\n'
        calc_manure = int(manure_area) * int(manure_depth) * int(manure_density)
        self.result += f'Количество вмещаемых экскрементов на 180 дней: {calc_manure}\n'
        if custom_manure < calc_manure:
            self.result += '\nРезультат:\nОбьема навозохранилища достаточно'
            self.result += '\n'
        else:
            self.result += '\nРезультат:\nОбьема навозохранилища не достаточно'
            self.result += '\n'
            self.not_ok = True
       
