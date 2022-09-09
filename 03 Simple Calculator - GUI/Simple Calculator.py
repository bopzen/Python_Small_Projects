import tkinter as tk


def reset_entry():
    entry_screen.delete(0, tk.END)
    label_result['text'] = ''


def calculate():
    calculation_input = entry_screen.get()
    if '+' in calculation_input:
        tokens = calculation_input.split('+')
        left_side, right_side = tokens[0], tokens[1]
        try:
            result = float(left_side) + float(right_side)
            label_result['text'] = f'{result}'
        except:
            label_result['text'] = 'ERROR'
    elif '-' in calculation_input:
        tokens = calculation_input.split('-')
        left_side, right_side = tokens[0], tokens[1]
        try:
            result = float(left_side) - float(right_side)
            label_result['text'] = f'{result}'
        except:
            label_result['text'] = 'ERROR'
    elif '*' in calculation_input:
        tokens = calculation_input.split('*')
        left_side, right_side = tokens[0], tokens[1]
        try:
            result = float(left_side) * float(right_side)
            label_result['text'] = f'{result}'
        except:
            label_result['text'] = 'ERROR'
    elif '/' in calculation_input:
        tokens = calculation_input.split('/')
        left_side, right_side = tokens[0], tokens[1]
        try:
            result = float(left_side) / float(right_side)
            label_result['text'] = f'{result}'
        except:
            label_result['text'] = 'ERROR'


window = tk.Tk()
window.geometry('500x450')
window.title('Simple Calculator')
window.resizable(width=False, height=False)
window.iconbitmap(r'Simple Calculator.ico')

photo = tk.PhotoImage(file=r'Simple Calculator.png')
label_logo = tk.Label(image=photo)
label_logo.pack(padx=5, pady=10)

label_title = tk.Label(text='Simple Calculator', font=('Segoe UI',18))
label_title.pack(padx=5, pady=5)

entry_screen = tk.Entry(font=('Segoe UI',18), width=35, justify='right', bd=1)
entry_screen.pack(padx=5, pady=10, ipadx=10, ipady=10)

label_result_title = tk.Label(text='Result', font=('Segoe UI',12))
label_result_title.pack(padx=5, pady=10)

label_result = tk.Label(text='',font=('Segoe UI',18))
label_result.pack(padx=5, pady=10)

button_calculate = tk.Button(text='Calculate', width=20, height=2, bd=1, command=calculate)
button_calculate.pack(padx=5, pady=10)

button_reset = tk.Button(text='Reset', width=20, height=2, bd=1, command=reset_entry)
button_reset.pack(padx=5, pady=10)

window.mainloop()
