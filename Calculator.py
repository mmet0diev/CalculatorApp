import tkinter as tk

root = tk.Tk()
root.title("Calculator")

# define the functions
def button_click(number):
    current = input.get()
    input.delete(0, tk.END)
    input.insert(0, str(current) + str(number))

def button_clear():
    input.delete(0, tk.END)

def button_add():
    first_number = input.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    input.delete(0, tk.END)

def button_subtract():
    first_number = input.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    input.delete(0, tk.END)

def button_multiply():
    first_number = input.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    input.delete(0, tk.END)

def button_divide():
    first_number = input.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    input.delete(0, tk.END)

def button_equal():
    second_number = input.get()
    input.delete(0, tk.END)

    if math == "addition":
        input.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        input.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        input.insert(0, f_num * int(second_number))
    elif math == "division":
        input.insert(0, f_num / int(second_number))

# initialize widgets
input = tk.Entry(root, width=35, borderwidth=5)
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
btn2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
btn_plus = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
btn_minus = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
btn_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
btn_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)
btn_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
btn_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# put the buttons on the screen
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)

btn_clear.grid(row=4, column=1, columnspan=2)
btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)
btn_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
