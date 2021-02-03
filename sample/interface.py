from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design_interface.kv')


class MenuScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
