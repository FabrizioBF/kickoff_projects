# Import libraries
from tkinter import *
from datetime import date

# Initialized window
root = Tk()
root.geometry('280x300')
root.resizable(0, 0)
root.title('Age Calculator')

# Variables
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

# Defining the function for calculating age


def ageCalc():
    global statement
    try:
        statement.destroy()
    except NameError:
        pass

    today = date.today()
    try:
        birthDate = date(int(yearValue.get()), int(
            monthValue.get()), int(dayValue.get()))
        age = today.year - birthDate.year
        if today.month < birthDate.month or (today.month == birthDate.month and today.day < birthDate.day):
            age -= 1

        statement = Label(root, text=f"{nameValue.get()}'s age is {age}.")
    except ValueError:
        statement = Label(root, text="Invalid date entered.")

    statement.grid(row=6, column=1, pady=15)


# Creating input labels and entries
Label(text="Name: ").grid(row=1, column=0)
Entry(root, textvariable=nameValue).grid(row=1, column=1, padx=10, pady=10)

Label(text="Year: ").grid(row=2, column=0)
Entry(root, textvariable=yearValue).grid(row=2, column=1, padx=10, pady=10)

Label(text="Month: ").grid(row=3, column=0)
Entry(root, textvariable=monthValue).grid(row=3, column=1, padx=10, pady=10)

Label(text="Day: ").grid(row=4, column=0)
Entry(root, textvariable=dayValue).grid(row=4, column=1, padx=10, pady=10)

# Create a button for calculating age
Button(text="Calculate age", command=ageCalc).grid(row=5, column=1)

# Infinite loop to run program
root.mainloop()
