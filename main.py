import tkinter as tk
from tkinter import *


def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def delete_digit():
    value = calc.get()
    if value != "0":
        value = "0"
    calc.delete(0, tk.END)
    calc.insert(0, value)


def get_result():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), command=lambda: add_operation(operation))


def result_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), command=lambda: add_digit(operation))


def delete_button():
    return tk.Button(text='C', bd=5, font=('Arial', 15), command=lambda: delete_digit())


def get_result_button():
    return tk.Button(text='=', bd=5, font=('Arial', 15), command=get_result)


root = Tk()

root['bg'] = '#dfdfdf'
root.title("Calculator")
root.geometry(f'250x300')
root.resizable(width=False, height=False)

calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

get_result_button().grid(row=4, column=2, stick='wens', padx=5, pady=5)

delete_button().grid(row=4, column=1, stick='wens', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)

root.mainloop()
