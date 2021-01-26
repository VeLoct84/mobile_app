from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file('design.kv')


# main app page with login, signup, forgot password button
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pwd):
        with open("users.json") as file:
            users = json.load(file)

        # function to match user and password in database
        if uname in users and users[uname]["password"] == pwd:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password!"


# unknown
class RootWidget(ScreenManager):
    pass


# signup page and save data to users.json file
class SignUpScreen(Screen):
    def add_user(self, uname, pwd):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {"username": uname,
                        "password": pwd,
                        "created": datetime.now().strftime("%Y/%m/%d %H-%M-%S")
                        }
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"

    # jump to main page
    def go_to_login(self):
        self.manager.current = "login_screen"


# successfull page with main app button
class SignUpScreenSuccess(Screen):
    # jump to main page
    def go_to_login(self):
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    # jump to main page after logout
    def logout(self):
        self.manager.transition.direction = "left"
        self.manager.current = "login_screen"

    # funtion to collect feeling input and generate result
    def get_quotes(self, feel):
        feel = feel.lower()
        available_feeling = glob.glob("quote/*txt")

        available_feeling = [Path(filename).stem for filename in
                             available_feeling]

        # TODO the result doesn't show in app!
        if feel in available_feeling:
            with open(f"quote/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.result.txt = random.choice(quotes)
        else:
            self.ids.result.txt = "Try another feeling"


# start the program
class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
