
import tkinter as tk

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operator = operator_entry.get()
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")

num1_label = tk.Label(root, text="Enter first number:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

num2_label = tk.Label(root, text="Enter second number:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

operator_label = tk.Label(root, text="Enter operator:")
operator_label.pack()
operator_entry = tk.Entry(root)
operator_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
