import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Color Changer")

# Define a bold font style
bold_font = ("Arial", 12, "bold")

# Create a label to provide instructions
color_label = tk.Label(
    root,
    text="Click a color button to change the form color",
    bg='white',
    font=bold_font
)
color_label.pack(pady=40)

# Create a frame to contain color buttons
color_frame = tk.Frame(root, padx=10, pady=10)
color_frame.pack()

# Define a list of colors and their labels
colors = [
    ("Red", "red"),
    ("Green", "green"),
    ("Blue", "blue"),
    ("Yellow", "yellow"),
    ("Pink", "pink"),
    ("Brown", "brown"),
    ("Orange", "orange"),
]

# Create buttons dynamically
for color_name, color_value in colors:
    tk.Button(
        color_frame,
        text=color_name,
        bg=color_value,
        padx=5,
        pady=5,
        command=lambda c=color_value: root.config(bg=c),
        font=bold_font
    ).pack(side="left")

# Start the Tkinter event loop
root.mainloop()
