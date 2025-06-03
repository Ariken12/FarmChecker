import math as m

from Screens.BaseScreen.BaseScreen import BaseScreen

TRANSLATOR = {
    'cold': 'холодный',
    'warm': 'теплый',
    'hot': 'жаркий'
}

class CheckAirSpeedScreen(BaseScreen):
    def __init__(self, *args, core, **kwargs):
        super().__init__(*args, core=core, **kwargs)
        #self.resultscreen.ids.result.size_hint_y = 10
        #self.resultscreen.ids.screen.size = (self.resultscreen.ids.screen.width, 1000 )
        for room_type in self.core.data['air_conditioning']['CO2_types']:
            self.ids.room_type_gas.values.append(room_type)
        for room_type in self.core.data['air_conditioning']['room_types']:
            self.ids.room_type.values.append(room_type)
        for animal_category in self.core.data['air_conditioning']['animal_category']:
            self.ids.animal_category.values.append(animal_category)
        for animal in self.core.data['air_conditioning']['animals']:
            self.ids.animal_type.values.append(animal)
        for city in self.core.data['air_conditioning']['cities']:
            self.ids.city.values.append(city)
        for coeff in range(-250, 251):
            self.core.data['air_conditioning']['coeff'][round(coeff/10, 1)] = m.fabs(coeff / 50)
        
    @BaseScreen._output_result
    def on_check(self):
        self.not_ok = False
        self.result = 'Введенные данные:\n'
        city = self._check_input(self.ids.city.text, 'Город')
        room_type_gas = self._check_input(self.ids.room_type_gas.text, 'Тип помещения')
        room_type = self._check_input(self.ids.room_type.text, 'Тип помещения')
        animal_category = self._check_input(self.ids.animal_category.text, 'Категория животных')
        animal_type = self._check_input(self.ids.animal_type.text, 'Тип животного')
        animal_count = float(self._check_input(self.ids.animal_count.text, 'Количество животных'))
        gas_level = float(self._check_input(self.ids.gas_level.text, 'Уровень газа'))
        water_level = float(self._check_input(self.ids.water_level.text, 'Уровень воды'))
        if self.not_ok:
            raise ValueError('Wrong input')
        temperature_limits = self.core.data['air_conditioning']['cities'][city]['temperature']
        humidity_limits = self.core.data['air_conditioning']['cities'][city]['humidity']
        self.result += '\n'
        self.result += 'Табличные значения:\n'
        self.result += 'Нормы для этого города:\n'
        self.result += 'Температура:\n'
        self.result += f'Наиболее холодного месяца: {temperature_limits["cold"]} °C\n'
        self.result += f'Наиболее жаркого месяца: {temperature_limits["hot"]} °C\n'
        self.result += f'В марте: {temperature_limits["warm"]} °C\n'
        self.result += 'Влажность:\n'
        self.result += f'Наиболее холодного месяца: {humidity_limits["cold"]} %\n'
        self.result += f'Наиболее жаркого месяца: {humidity_limits["hot"]} %\n'
        self.result += f'В марте: {humidity_limits["warm"]} %\n'
        objectCO2_limits = self.core.data['air_conditioning']['CO2_types'][room_type_gas]
        self.result += 'Нормы для таких помещений:\n'
        self.result += f'Уровень углекислого газа: {objectCO2_limits["CO2"]} °C\n'
        objectRoomlimits = self.core.data['air_conditioning']['room_types'][room_type]
        self.result += f'Уровень максимальной влажности: {objectRoomlimits["humidity_max"]} %\n'
        self.result += f'Уровень минимальной влажности: {objectRoomlimits["humidity_min"]} °C\n'
        animal_category = self.core.data['air_conditioning']['animal_category'][animal_category]
        self.result += 'Нормы для этого животного:\n'
        self.result += f'Надбавочный коэффициент на уровень выделяемого углекислого газа в зависимости от температуры: \n{animal_category["K-CO2"]}\n'
        self.result += f'Надбавочный коэффициент на уровень выделяемой влажности в зависимости от температуры: \n{animal_category["K-H2O"]}\n'
        animal_type = self.core.data['air_conditioning']['animals'][animal_type]
        self.result += 'Нормы для этого животного:\n'
        self.result += 'Выделения на одно животное(для птиц на 1 кг живой массы):\n'
        self.result += f'Уровень углекислого газа: {animal_type["CO2"]} °C\n'
        self.result += f'Уровень влажности: {animal_type["H2O"]} %\n'
        self.result += '\n'
        self.result += 'Результаты вычислений:\n'
        recommends = ''
        temperature = objectRoomlimits['temperature']
        temp_category = int(temperature // 5) * 5
        coeff_co2 = animal_category['K-H2O'][temp_category]
        coeff_h2o = animal_category['K-CO2'][temp_category]
        A = animal_count * coeff_co2 * animal_type['CO2']
        lco2 = A / m.fabs(objectCO2_limits['CO2'] - 0.3)
        self.result += f'Необходимый уровень проветривания углекислого газа: {round(lco2, 2)}\n'
        if lco2 > gas_level:
            self.not_ok = True
            recommends += f'Необходимо увеличить уровень проветривания углекислого газа на {round(lco2 - gas_level, 2)}\n'
        D = animal_count * coeff_h2o * animal_type['H2O']
        for season in ('cold', 'warm', 'hot'):
            Dmax = self.density_from_temperature(temperature)
            Dmax1 = self.density_from_temperature(temperature_limits[season])
            sigma = objectRoomlimits['temperature']
            sigma1 = humidity_limits[season]
            d = Dmax * sigma / 100
            d1 = Dmax1 * sigma1 / 100
            lh20 = D / abs(d-d1)
            self.result += f'Необходимый уровень проветривания влажности в {TRANSLATOR[season]} сезон: {round(lh20, 2)}\n'
            if lh20 > water_level:
                self.not_ok = True
                recommends += f'Необходимо увеличить уровень проветривания влажности в {TRANSLATOR[season]} сезон на {round(lh20 - water_level, 2)}\n'
        if self.not_ok:
            self.result += '\n'
            self.result += recommends

    def density_from_temperature(self, temperature):
        return self.core.data['air_conditioning']['coeff'][round(temperature, 1)]