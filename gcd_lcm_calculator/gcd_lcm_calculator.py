import tkinter as tk
from tkinter import messagebox

# Function to calculate the GCD


def gcd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a

# Function to calculate GCD and LCM


def calculate():
    try:
        # Retrieve values entered by the user
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        # Calculate GCD
        result = gcd(num1, num2)
        # Calculate LCM
        lcm = (num1 * num2) // result
        # Display the result in a message box
        messagebox.showinfo("Result", f"The GCD of {num1} and {num2} is {result}\n"
                                      f"The LCM of {num1} and {num2} is {lcm}")
    except ValueError:
        # Handle invalid input
        messagebox.showerror(
            "Error", "Please enter valid integers for both numbers.")


# Create the main tkinter window
root = tk.Tk()
root.title("GCD and LCM Calculator")

# Create and place widgets
bold_font = ("Arial", 20, "bold")
title_label = tk.Label(root, text="GCD and LCM Calculator",
                       bg="white", fg="Green", font=bold_font)
title_label.pack()

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(padx=5, pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(padx=5, pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(padx=5, pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(padx=5, pady=5)

calculate_button = tk.Button(
    root, text="Calculate GCD And LCM", command=calculate)
calculate_button.pack(padx=5, pady=5)

# Run the tkinter event loop
root.mainloop()
