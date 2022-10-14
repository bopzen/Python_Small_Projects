import authentication
from helpers import *


def show_account_details():
    clean_screen()

    frame.create_text(350, 100, text="Account information", font=('Comic Sans MS', 20, 'bold'))

    frame.create_text(340, 160, text="First Name", anchor='e', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(360, 160, text=authentication.current_user["first_name"], anchor='w', font=('Comic Sans MS', 12))

    frame.create_text(340, 200, text="Last Name", anchor='e', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(360, 200, text=authentication.current_user["last_name"], anchor='w', font=('Comic Sans MS', 12))

    frame.create_text(340, 240, text="Username", anchor='e', font=('Comic Sans MS', 12, 'bold'))
    frame.create_text(360, 240, text=authentication.current_user["username"], anchor='w', font=('Comic Sans MS', 12))

    frame.create_text(350, 300, text="Ordered products", font=('Comic Sans MS', 16, 'bold'))
    y = 330
    if authentication.current_user['products']:
        for product in authentication.current_user['products']:
            frame.create_text(350, y, text=product, font=('Comic Sans MS', 12))
            y += 20
    else:
        frame.create_text(350, y, text="No ordered products", font=('Comic Sans MS', 12))

    acc_info_back_btn = tk.Button(
        root,
        text="Back",
        bg="brown1",
        fg='white',
        font=('Comic Sans MS', 12),
        borderwidth=0,
        width=10,
        height=1,
        command=navigate_back_to_buying_page
    )

    frame.create_window(350, 550, window=acc_info_back_btn)






