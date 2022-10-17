from json import load, dump
from tkinter import Button
from helpers import clean_screen, get_users_data, update_users_data, log_out
from PIL import Image, ImageTk
from canvas import *
import authentication
from account_page import show_account_details


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    global products_info
    frame.create_text(80, 30, text=f"Welcome, {authentication.current_user['username']}!", font=('Comic Sans MS', 12, 'bold'))

    account_btn = Button(
        root,
        text='Account',
        bg='dodger blue',
        fg='white',
        width=10,
        font=('Comic Sans MS', 10, 'bold'),
        borderwidth=0,
        command=display_account_info
    )
    frame.create_window(548, 30, window=account_btn)

    logout_btn = Button(
        root,
        text='Log Out',
        bg='brown1',
        fg='white',
        width=10,
        font=('Comic Sans MS', 10, 'bold'),
        borderwidth=0,
        command=log_out
    )
    frame.create_window(645, 30, window=logout_btn)

    with open("db/products_data.json", "r") as products_file:
        products_info = load(products_file)

    x, y = 120, 70

    for name, info in products_info.items():
        image = Image.open(info['image'])
        image = image.resize((130, 130))
        product_img = ImageTk.PhotoImage(image)
        images.append(product_img)
        frame.create_text(x, y, text=name, font=('Comic Sans MS', 10))
        frame.create_image(x, y + 80, image=product_img)
        if info['quantity'] > 0:
            color="green"
            text = f"In stock {info['quantity']}"
            buy_btn = Button(
                root,
                text='Buy',
                bg='green4',
                fg='white',
                width=5,
                font=('Comic Sans MS', 10, 'bold'),
                borderwidth=0,
                command=lambda name=name: buy_product(name)
            )
            frame.create_window(x, y + 190, window=buy_btn)
        else:
            color = "red"
            text = "Out of stock"
        frame.create_text(x, y + 160, text=text, fill=color, font=('Comic Sans MS', 10))

        x += 150
        if x > 600:
            x = 120
            y += 270


def display_account_info():
    show_account_details()


def buy_product(product):
    products_info[product]['quantity'] -= 1
    with open("db/products_data.json", "w") as products_file:
        dump(products_info, products_file)
    users_data = get_users_data()
    for line in users_data:
        if line['username'] == authentication.current_user['username']:
            line['products'].append(product)
            authentication.current_user['products'].append(product)
    update_users_data(users_data)

    display_products()


images = []