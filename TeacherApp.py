from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    pass


class TeacherApp(BoxLayout):

    # Connects the value in the TextInput widget to these
    # fields
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_number_text_input = ObjectProperty()
    grade_text_input = ObjectProperty()
    student_list_text_input = ObjectProperty()

    def submit_student(self):

        # Get the student name from the TextInputs
        student_name = "Name: " + self.first_name_text_input.text + " " + self.last_name_text_input.text + \
                       "     Student Number: " + self.student_number_text_input.text + "     Grade: " + self.grade_text_input.text + "     Points: " + self.reward_points_text_input.text

        # Add the student to the ListView
        self.student_list.adapter.data.extend([student_name])

        # Reset the ListView
        self.student_list._trigger_reset_populate()

    def delete_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:

            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Reset the ListView
            self.student_list._trigger_reset_populate()

    def replace_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:

            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Get the student name from the TextInputs
            student_name = "Name: " + self.first_name_text_input.text + " " + self.last_name_text_input.text + \
                           "     Student Number: " + self.student_number_text_input.text + "     Grade: " + self.grade_text_input.text + "     Points: " + self.reward_points_text_input.text

            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])

            # Reset the ListView
            self.student_list._trigger_reset_populate()

    def update_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:

            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Get the student name from the TextInputs
            student_name = "Name: " + self.first_name_text_input.text + " " + self.last_name_text_input.text + \
                           "     Student Number: " + self.student_number_text_input.text + "     Grade: " + self.grade_text_input.text + "     Points: " + self.reward_points_text_input.text

            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])

            # Reset the ListView
            self.student_list._trigger_reset_populate()

class TeacherAppApp(App):
    def build(self):
        return TeacherApp()


dbApp = TeacherAppApp()

dbApp.run()
