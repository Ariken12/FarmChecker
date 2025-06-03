from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MyPopup(Popup):
    def __init__(self, **kwargs):
        super(MyPopup, self).__init__(**kwargs)
        self.title = "Всплывающее окно"
        self.size_hint = (0.8, 0.4)  # Устанавливаем размер окна
        self.content = BoxLayout(orientation='vertical')
        
        self.content.add_widget(Label(text="Это всплывающее окно!"))
        
        close_button = Button(text="Закрыть", size_hint=(1, 0.2))
        close_button.bind(on_press=self.dismiss)  # Закрываем окно при нажатии
        self.content.add_widget(close_button)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        open_popup_button = Button(text="Открыть всплывающее окно", size_hint=(1, 0.2))
        open_popup_button.bind(on_press=self.open_popup)
        
        layout.add_widget(open_popup_button)
        return layout

    def open_popup(self, instance):
        popup = MyPopup()
        popup.open()  # Открываем всплывающее окно

if __name__ == '__main__':
    MyApp().run()
