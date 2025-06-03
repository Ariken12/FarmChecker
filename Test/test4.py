from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class MyApp(App):
    def build(self):


        # Добавляем много текста в Label
        text = "Это пример текста, который будет прокручиваться.\n" * 50  # Умножаем текст для увеличения объема
        label = Label(text=text, size_hint_y=None, halign='left', valign='top')
        label.bind(size=label.setter('text_size'))  # Позволяем Label изменять размер в зависимости от текста
        label.bind(texture_size=label.setter('size')) 
        layout = ScrollView(size_hint=(1, None), size=(400, 300))  # Устанавливаем размеры ScrollView
        # Добавляем Label в основной контейнер
        layout.add_widget(label)

        print(label.height)
        print(layout.height)

        return layout

if __name__ == '__main__':
    MyApp().run()
