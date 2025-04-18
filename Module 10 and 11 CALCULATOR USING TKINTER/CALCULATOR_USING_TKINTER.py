import tkinter as tk

# Function to update the display when a button is pressed
def update_display(value):
    current_text = display_var.get()
    if current_text == "0" or current_text == "Error":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression and show the result
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")
root.resizable(0, 0)

# Variable to store the display text
display_var = tk.StringVar()
display_var.set("0")

# Display label
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="white", anchor="e", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4, sticky="we")

# Button layout: text, row, column
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    action = lambda x=text: update_display(x) if x != "=" else calculate_result()
    tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20, command=action).grid(row=row, column=col)

# Clear button spans three columns
tk.Button(root, text="C", font=("Arial", 18), padx=20, pady=20, command=clear_display).grid(row=5, column=0, columnspan=4, sticky="we")

# Start the GUI event loop
root.mainloop()
