
from Screens.BaseScreen.BaseScreen import BaseScreen

class CheckLightingScreen(BaseScreen):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, core=core, **kwargs)
        for room_type in self.core.data['lighting']['standard']:
            self.ids.room_type.values.append(room_type)
        for artificial_type in self.core.data['lighting']['artificial_coeff']:
            self.ids.artificial_type.values.append(artificial_type)

    @BaseScreen._output_result
    def on_check(self):
        self.not_ok = False
        self.result = 'Введенные данные:\n'
        room_type = self._check_input(self.ids.room_type.text, 'Тип помещения') 
        room_area = self._check_input(self.ids.room_area.text, 'Площадь помещения')
        natural_size = self._check_input(self.ids.natural_size.text, 'Площадь окон')
        artificial_type = self._check_input(self.ids.artificial_type.text, 'Тип искусственного освещения')
        artificial_power = self._check_input(self.ids.artificial_power.text, 'Мощность искусственного освещения')
        artificial_count = self._check_input(self.ids.artificial_count.text, 'Количество искусственного освещения')
        if self.not_ok:
            raise ValueError('Wrong input')
        self.not_ok = False
        limits = self.core.data['lighting']['standard'][room_type]
        self.result += '\nТабличные значения:\n'
        self.result += 'Нормы для таких помещений:\n'
        self.result += f'Относительная площадь световых проемов: {limits["S"]} %\n'
        self.result += f'Освещенность при газоразрядных лампах: {limits["E1"]} лк\n'
        self.result += f'Освещенность при лампах накаливания: {limits["E2"]} лк\n'
        room_type = str(room_type)
        room_area = float(room_area)
        natural_size = float(natural_size)
        artificial_type = str(artificial_type)
        artificial_power = float(artificial_power)
        artificial_count = float(artificial_count)
        recommends = ''
        s_custom = round(natural_size / room_area * 100, 2)
        self.result += '\nРассчеты:\n'
        self.result += f'ОПСП: {s_custom} %\n'
        if s_custom < limits['S']:
            recommends += 'Необходимо добавить источники естественного света\n'
            self.not_ok = True
        lim_k1 = limits['E2'] if artificial_type == 'Люменесцентные лампы' else limits['E1']
        watt_type = '<100' if artificial_power < 100 else '>100'
        coeff = self.core.data['lighting']['artificial_coeff'][artificial_type][watt_type]
        k_custom = round((artificial_power * artificial_count) / room_area * coeff, 2)
        self.result += f'Искуственная освещенность: {k_custom} лк'
        if k_custom < lim_k1:
            self.not_ok = True
            difference = int((lim_k1 - k_custom) * room_area / coeff / artificial_power)
            recommends += f'Необходимо добавить {difference} лампочек по {artificial_power} Вт \n'
        self.result += '\n'
        if self.not_ok:
            self.result += recommends
        else:
            self.result += '\nПроверка освещения прошла'