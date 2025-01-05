import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.title("Py | Calculator")
root.geometry("300x400")

# Make the window non-resizable
root.resizable(False, False)

# Entry widget to display the result with larger font size
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font=("Helvetica", 24), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Configure style for theme
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Helvetica", 16), width=10, height=4)

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:
            # Replace custom symbols with Python operators
            expression = current_text.replace("÷", "/").replace("×", "*")
            result = eval(expression)

            # Check if the result is a whole number
            if result.is_integer():
                result = int(result)

            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "%":
        # Convert the current number to a decimal by dividing it by 100
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == "( - )":
        # Convert the current number to its negative
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + clicked_button_text)


# Button layout
buttons = [
    ("C", 1, 0), ("( - )", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

# Create buttons and add them to the grid
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

# Configure row and column weights so that they expand proportionally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Keyboard control
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))
root.bind("</>", lambda event: handle_button_click("÷"))
root.bind("<*>", lambda event: handle_button_click("×"))
root.bind("<minus>", lambda event: handle_button_click("-"))
root.bind("<+>", lambda event: handle_button_click("+"))
root.bind("<.>", lambda event: handle_button_click("."))
root.bind("<%>", lambda event: handle_button_click("%"))
root.bind("<underscore>", lambda event: handle_button_click("( - )"))
root.bind("<0>", lambda event: handle_button_click("0"))
root.bind("<Key-1>", lambda event: handle_button_click("1"))
root.bind("<Key-2>", lambda event: handle_button_click("2"))
root.bind("<Key-3>", lambda event: handle_button_click("3"))
root.bind("<Key-4>", lambda event: handle_button_click("4"))
root.bind("<Key-5>", lambda event: handle_button_click("5"))
root.bind("<Key-6>", lambda event: handle_button_click("6"))
root.bind("<Key-7>", lambda event: handle_button_click("7"))
root.bind("<Key-8>", lambda event: handle_button_click("8"))
root.bind("<Key-9>", lambda event: handle_button_click("9"))



root.mainloop()
