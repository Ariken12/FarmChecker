from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout

class DropDownApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Создаем выпадающий список
        self.dropdown = DropDown()

        # Добавляем элементы в выпадающий список
        for item in ['Элемент 1', 'Элемент 2', 'Элемент 3']:
            btn = Button(text=item, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        # Кнопка для отображения выпадающего списка
        mainbutton = Button(text='Выберите элемент', size_hint=(None, None), size=(200, 44))
        mainbutton.bind(on_release=self.dropdown.open)

        # Обновляем текст кнопки при выборе элемента
        self.dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        layout.add_widget(mainbutton)
        return layout

if __name__ == '__main__':
    DropDownApp().run()
