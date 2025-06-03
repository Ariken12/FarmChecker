from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Создаем выпадающий список
        dropdown = DropDown()

        # Добавляем элементы в выпадающий список
        for index in range(5):
            btn = Button(text=f'Item {index}', size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # Создаем кнопку, которая будет открывать выпадающий список
        mainbutton = Button(text='Select an item', size_hint=(None, None), size=(200, 44))
        mainbutton.bind(on_release=dropdown.open)

        # Обработчик выбора элемента
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        # Добавляем кнопку в layout
        layout.add_widget(mainbutton)

        # Устанавливаем позицию выпадающего списка
        dropdown.bind(on_dismiss=lambda instance: mainbutton.state = 'normal')

        return layout

if __name__ == '__main__':
    MyApp().run()
