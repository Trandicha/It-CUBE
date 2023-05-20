import tkinter as tk

win=tk.Tk()
win.geometry('240x270')
win.resizable(0, 0)
win['bg']='#33ffe6'

def add_digit(digit):
    value=calc.get()+str(digit)
    calc.delete(0, 'end')
    calc.insert(0, value)

def add_operation(operation):
    value=calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
        calc.delete(0, 'end')
        calc.insert(0, value+operation)

def make_digit_button(digit):
    return tk.Button(win, text=digit, bd=10,font=('Arial',13), command=lambda : add_digit(digit))

def make_operation_button(operation):
    return tk.Button(win, text=operation,font=('Arial',13),fg='red', bd=10, command=lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(win, text=operation,font=('Arial',13),fg='red', bd=10, command=lambda : add_digit(operation))




calc=tk.Entry(win, font=('Arial', 15), width=15, justify=tk.RIGHT)
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
