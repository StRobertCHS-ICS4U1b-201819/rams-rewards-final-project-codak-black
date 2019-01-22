import kivy

kivy.require('1.10.1')

import kivy

kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# You can create your kv code in the Python file
Builder.load_string("""


<WelcomeLabel@Label>
   color: 1, 1, 1, 1
   font_size: 40

<CustButton@Button>:
   color: 0, 0, 0, 1
   font_size: 24
   size: 150, 100


<LogIn>:
   Widget:
      WelcomeLabel:
         text: "Welcome to the STR App"
         pos: 350, 400

      CustButton:
         text: "Login"
         pos: 50, 50

      CustButton:
         text: "Sign Up"
         pos: 520, 50
         on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "create_user"

<CreateUser>:

   Widget:
      WelcomeLabel:
         text: "Create Your Account"
         pos: 350, 400

      CustButton:
         text: "Go Back"
         pos: 50, 50
         on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "log_in"

""")


# Create a class for all screens in which you can include
# helpful methods specific to that screen
class LogIn(Screen):
    Window.clearcolor = (0.1333, 0.545, 0.1333, 1)


class CreateUser(Screen):
    pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(LogIn(name="log_in"))
screen_manager.add_widget(CreateUser(name="create_user"))


class HelpMeApp(App):

    def build(self):
        return screen_manager


sample_app = HelpMeApp()
sample_app.run()

