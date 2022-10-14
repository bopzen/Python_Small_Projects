import tkinter as tk


def create_root():
    root = tk.Tk()
    root.geometry("700x600")
    root.resizable(False, False)
    root.title('Sneakers Shop')

    return root


def create_frame():
    frame = tk.Canvas(root, width=700, height=600, bg='white')
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
