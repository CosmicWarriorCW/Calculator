import tkinter as tk
from tkinter import ttk
import math

def on_button_click(text):
    if text == '=':
        calculate()
    elif text == 'AC':
        clear_all()
    elif text == 'DEL':
        delete()

    else:
        add_to_expression(text)

def add_to_expression(text):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(text))

def get_operation(operator):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + operator)

def add_function(func):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + func + '(')

def clear_all():
    display.delete(0, tk.END)

def delete():
    current = display.get()
    new_string = current[:-1]
    clear_all()
    display.insert(0, new_string)

def calculate():
    entire_string = display.get()
    try:
        entire_string = entire_string.replace('sin','math.sin')
        entire_string = entire_string.replace('cos', 'math.cos')
        entire_string = entire_string.replace('tan', 'math.tan')
        entire_string = entire_string.replace('log', 'math.log')
        entire_string = entire_string.replace('exp', 'math.exp')

        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=70)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=10,sticky='nsew')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

button_texts = [
    '7', '8', '9', 'log','(','+',
    '4', '5', '6', 'sin',')','*',
    '1', '2', '3', 'cos','/','-',
    '0', 'AC', 'DEL', 'tan','exp','='
]

row_val = 1
col_val = 0

# Configure the style for rounded buttons
style = ttk.Style()
style.configure('TButton', padding=(20, 20), relief='flat')

for button_text in button_texts:
    button = ttk.Button(root, text=button_text, padding=(20, 20), command=lambda text=button_text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    root.grid_rowconfigure(row_val, weight=1)
    root.grid_columnconfigure(col_val, weight=1)


    button.grid(sticky="nsew")
    col_val += 1
    if col_val > 5:
        col_val = 0
        row_val += 1

root.mainloop()
