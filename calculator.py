import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Create input fields for numbers
        self.num1_label = tk.Label(root, text="Number 1:")
        self.num1_label.grid(row=0, column=0)
        self.num1_entry = tk.Entry(root, width=20)
        self.num1_entry.grid(row=0, column=1)

        self.num2_label = tk.Label(root, text="Number 2:")
        self.num2_label.grid(row=1, column=0)
        self.num2_entry = tk.Entry(root, width=20)
        self.num2_entry.grid(row=1, column=1)

        # Create dropdown menu for operation choice
        self.operation_label = tk.Label(root, text="Operation:")
        self.operation_label.grid(row=2, column=0)
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")  # default operation
        self.operation_menu = tk.OptionMenu(root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=2, column=1)

        # Create button to perform calculation
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        # Create label to display result
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=4, column=0)
        self.result_entry = tk.Entry(root, width=20)
        self.result_entry.grid(row=4, column=1)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero!"

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Error: Invalid input!")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
