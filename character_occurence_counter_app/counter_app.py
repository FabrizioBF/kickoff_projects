import tkinter as tk


def count_occurrences():
    # Get user input from the entry widget
    user_input = entry.get()
    # Initialize an empty dictionary to store the count of occurrences for each character
    char_count = {}
    # Iterate through each character in the user_input string
    for char in user_input:
        # Check if the character is already in the dictionary, if not, default to 0
        current_count = char_count.get(char, 0)
        # Increment the count for the current character
        char_count[char] = current_count + 1
    # Display the result in the label
    result_label.config(text=str(char_count))


# Create the main window
root = tk.Tk()
root.title("Character Occurrence Counter")

# Create and place widgets
label = tk.Label(root, text="Enter a message:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

count_button = tk.Button(root, text="Count Occurrences",
                         command=count_occurrences)
count_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
