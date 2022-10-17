from json import loads, dump
from buying_page import display_products
from canvas import *
from helpers import clean_screen, get_users_data, navigate_back_to_home_page
from PIL import Image, ImageTk


def render_entry():
    global sneaker_img
    frame.create_text(350, 80, text="Welcome to Sneakers Shop", font=('Comic Sans MS', 30, 'bold'))

    register_btn = tk.Button(
        root,
        text="Register",
        bg="green3",
        fg='white',
        font=('Comic Sans MS', 12, 'bold'),
        borderwidth=0,
        width=16,
        height=2,
        command=register
    )

    login_btn = tk.Button(
        root,
        text="Login",
        bg="dodger blue",
        fg='white',
        font=('Comic Sans MS', 12, 'bold'),
        borderwidth=0,
        width=16,
        height=2,
        command=login
    )

    quit_btn = tk.Button(
        root,
        text="Quit",
        bg="brown1",
        fg='white',
        font=('Comic Sans MS', 12, 'bold'),
        borderwidth=0,
        width=16,
        height=2,
        command=program_quit
    )

    sneaker_image = Image.open("sneakers.ico")
    sneaker_image = sneaker_image.resize((150, 150))
    sneaker_img = ImageTk.PhotoImage(sneaker_image)
    frame.create_image(350, 155, image=sneaker_img)

    frame.create_window(350, 250, window=register_btn)
    frame.create_window(350, 330, window=login_btn)
    frame.create_window(350, 410, window=quit_btn)


def login():
    clean_screen()

    frame.create_text(350, 80, text="Login Form", font=('Comic Sans MS', 30, 'bold'))

    frame.create_text(190, 160, text="Username", anchor='w', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(190, 200, text="Password", anchor='w', font=('Comic Sans MS', 12, 'bold'))

    frame.create_window(400, 160, window=username_box)
    username_box.focus_set()
    frame.create_window(400, 200, window=password_box)

    logging_btn = tk.Button(
        root,
        text="Login",
        bg="dodger blue",
        fg='white',
        font=('Comic Sans MS', 12, 'bold'),
        borderwidth=0,
        width=16,
        height=2,
        command=logging
    )

    frame.create_window(350, 410, window=logging_btn)

    login_back_btn = tk.Button(
        root,
        text="Back",
        bg="brown1",
        fg='white',
        font=('Comic Sans MS', 12, 'bold'),
        borderwidth=0,
        width=16,
        height=2,
        command=navigate_back_to_home_page
    )

    frame.create_window(350, 490, window=login_back_btn)


def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(
            350,
            300,
            text="Invalid username or password!",
            fill="red",
            tag='error'
            )


def check_login():
    global current_user
    users_data = get_users_data()
    for record in users_data:
        if record['username'] == username_box.get() and record['password'] == password_box.get():
            current_user = record
            return True

    return False


def register():
    clean_screen()

    frame.create_text(350, 80, text="Registration Form", font=('Comic Sans MS', 30, 'bold'))

    frame.create_text(190, 160, text="First Name", anchor='w', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(190, 200, text="Last Name", anchor='w', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(190, 240, text="Username", anchor='w', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(190, 280, text="Password", anchor='w', font=('Comic Sans MS', 12, 'bold'))

    frame.create_window(400, 160, window=first_name_box)
    first_name_box.focus_set()
    frame.create_window(400, 200, window=last_name_box)
    frame.create_window(400, 240, window=username_box)
    frame.create_window(400, 280, window=password_box)

    registration_btn = tk.Button(
        root,
        text="Register",
        bg="green3",
        fg='white',
        font=('Comic Sans MS', 12),
        borderwidth=0,
        width=16,
        height=2,
        command=registration
    )

    frame.create_window(350, 410, window=registration_btn)

    registration_back_btn = tk.Button(
        root,
        text="Back",
        bg="brown1",
        fg='white',
        font=('Comic Sans MS', 12, 'bold'),
        borderwidth=0,
        width=16,
        height=2,
        command=navigate_back_to_home_page
    )

    frame.create_window(350, 490, window=registration_back_btn)


def registration():
    global current_user
    new_credentials = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
        "products": []
    }
    if check_registration(new_credentials):
        current_user = new_credentials
        with open("db/user_information.json", "a") as users_file:
            dump(new_credentials, users_file)
            users_file.write('\n')
        display_products()


def check_registration(credentials):
    if credentials['first_name'].strip() == "" \
            or credentials['last_name'].strip() == "" \
            or credentials['username'].strip() == "" \
            or credentials['password'].strip() == "":
        frame.create_text(
            350,
            300,
            text="Please fill out all fields",
            fill="red",
            tag='error'
        )
        return False
    frame.delete('error')
    users_data = get_users_data()
    for record in users_data:
        if record['username'] == credentials['username']:
            frame.create_text(
                350,
                300,
                text="Username already exists!",
                fill="red",
                tag='error'
            )
            return False
    frame.delete('error')
    return True


def program_quit():
    root.destroy()


current_user = {}
first_name_box = tk.Entry(root, font=('Comic Sans MS', 12), bd=0, borderwidth=1, relief='solid')
last_name_box = tk.Entry(root, font=('Comic Sans MS', 12),bd=0, borderwidth=1, relief='solid')
username_box = tk.Entry(root, font=('Comic Sans MS', 12), bd=0, borderwidth=1, relief='solid')
password_box = tk.Entry(root, font=('Comic Sans MS', 12), bd=0, show="*", borderwidth=1, relief='solid')
