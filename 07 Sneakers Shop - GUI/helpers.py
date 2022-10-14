from canvas import *
from json import *
import buying_page
import authentication


def clean_screen():
    frame.delete("all")


def get_users_data():
    users_data = []
    with open("db/user_information.json", "r") as users_file:
        for line in users_file:
            users_data.append(loads(line))
    return users_data


def update_users_data(users_data):
    with open("db/user_information.json", "w") as users_file:
        for line in users_data:
            dump(line, users_file)
            users_file.write('\n')


def navigate_back_to_buying_page():
    buying_page.display_products()


def navigate_back_to_home_page():
    clean_screen()
    authentication.first_name_box.delete(0, "end")
    authentication.last_name_box.delete(0, "end")
    authentication.username_box.delete(0, "end")
    authentication.password_box.delete(0, "end")
    authentication.render_entry()


def log_out():
    clean_screen()
    authentication.current_user = []
    authentication.first_name_box.delete(0, "end")
    authentication.last_name_box.delete(0, "end")
    authentication.username_box.delete(0, "end")
    authentication.password_box.delete(0, "end")
    authentication.render_entry()

