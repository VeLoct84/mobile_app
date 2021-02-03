from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design_interface.kv')


class LoginScreen(Screen):
    def login(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_menu'


class SignupSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class MainMenu(Screen):
    def create_job(self, num):
        job = []
        job.append(num)
        print(job)
        # TODO


class RootWidget(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
