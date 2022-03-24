from tkinter import Entry, Tk, Button, END


root = Tk()
root.title('Калькулятор')
root.configure(bg='pink')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

is_empty = 'is_empty'
number_length = 0
first_number = 'is_empty'
wait_second = False
calculated = False
second_number = 'is_empty'
operation = None


def button_click(symbol):
    global number_length
    global first_number
    global second_number
    global wait_second
    global calculated
    global operation

    if symbol == 'clear':
        e.delete(0, END)
        number_length = 0
        return

    if str(symbol) in '+-*/' and first_number != 'is_empty' and not wait_second:
        e.delete(0, END)
        wait_second = True

        operation = symbol
        number_length = 0
        return
    elif symbol == '+' and first_number != 'is_empty' and wait_second:
        e.delete(0, END)

        first_number = is_empty
        second_number = is_empty
        number_length = 0

        wait_second = False
        return
    elif (symbol == '+' or symbol == '=' or symbol == 'clear') and first_number == 'is_empty':
        e.delete(0, END)
        number_length = 0
        return
    elif symbol == '=' and first_number != 'is_empty' and second_number == 'is_empty':
        e.delete(0, END)

        first_number = 'is_empty'
        second_number = 'is_empty'

        number_length = 0
        return

    if symbol == '=' and first_number != 'is_empty' and second_number != 'is_empty':
        result = eval(f'{first_number} {operation} {second_number}')
        e.delete(0, END)

        e.insert(0, result)

        first_number = 'is_empty'
        second_number = 'is_empty'

        wait_second = False

        number_length = 0

        calculated = True
        return

    if calculated:
        e.delete(0, END)
        calculated = False

    e.insert(number_length, symbol)

    if not wait_second:
        first_number = int(e.get())
    else:
        second_number = int(e.get())

    number_length += 1


# define buttons

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_button_add = Button(root, text='+', padx=39, pady=20, command=lambda: button_click('+'))
button_button_subtraction = Button(root, text='-', padx=39, pady=20, command=lambda: button_click('-'))
button_button_multiplication = Button(root, text='*', padx=39, pady=20, command=lambda: button_click('*'))
button_button_division = Button(root, text='/', padx=39, pady=20, command=lambda: button_click('/'))

button_equal = Button(root, text='=', padx=91, pady=20, command=lambda: button_click('='))
button_clear = Button(root, text='Очистить', padx=76, pady=20, command=lambda: button_click('clear'))


# put the buttons on the screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=2)

button_button_add.grid(row=1, column=3)
button_button_subtraction.grid(row=2, column=3)
button_button_multiplication.grid(row=3, column=3)
button_button_division.grid(row=4, column=3)

button_clear.grid(row=4, column=0, columnspan=2)
button_equal.grid(row=5, column=0, columnspan=2)


root.mainloop()
