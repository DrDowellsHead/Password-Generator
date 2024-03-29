import random
import string
import tkinter as tk


def pass_gen(*args):

    # Condition for examination length of password
    if length_entry.get() == '':
        password_label['text'] = 'Error. Please, entry length of password.'
        return None

    # Variable in which entry length of password
    length = int(length_entry.get())

    # Get meaning from tkinter.Checkbutton()
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    digits = digits_var.get()
    special_symb = special_chars_var.get()

    # Variable in which store random means from string library
    char = ''

    # If variable == True that generating random char, digit or special symbol from string library
    if uppercase:
        char += string.ascii_uppercase
    if lowercase:
        char += string.ascii_lowercase
    if digits:
        char += string.digits
    if special_symb:
        char += string.punctuation
    # If nothing choice that will be print 'error'
    if not char:
        password_label['text'] = 'Error: Please enable at least one character type.'

    # Final random symbols from char in a given length
    password = ''.join(random.choice(char) for _ in range(length))
    # Print password in tkinter window
    password_label.config(text=password)


#function for copy password`s text
def copy_function():
    root.clipboard_clear() #clear clipboard
    root.clipboard_append(password_label['text']) #add text to clipboard


# Creating tkinter window
root = tk.Tk()
root.title('Password Generation')

# Place the window in the center of the monitor
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (600 // 2)

root.geometry(f'{600}x{600}+{x}+{y}')

# Creating text above input field
length_of_password = tk.Label(root, text='Length of Password', font='TimesNewRoman 30')
length_of_password.pack()

# Print documentation of program
documentation_of_program = tk.Label(root, text='''This program is generating random password.
User can entry symbols upper registry, lower registry, digits or special symbols.
Also user can entry length of password.''')
documentation_of_program.pack()

# Creating an input field
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for upper character types
uppercase_var = tk.IntVar()
use_uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var, onvalue=1, offvalue=0)
use_uppercase_checkbox.pack()

# Checkboxes for lower character types
lowercase_var = tk.IntVar()
use_lowercase_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var, onvalue=1, offvalue=0)
use_lowercase_checkbox.pack()

# Checkboxes for digits
digits_var = tk.IntVar()
use_digits_checkbox = tk.Checkbutton(root, text="Include digits", variable=digits_var, onvalue=1, offvalue=0)
use_digits_checkbox.pack()

# Checkboxes for special chars
special_chars_var = tk.IntVar()
use_special_chars_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var, onvalue=1, offvalue=0)
use_special_chars_checkbox.pack()

# Creating button for generation password
generate_button = tk.Button(root, text="Generation Password", command=pass_gen)
generate_button.pack()

# Creating field for print password
password_label = tk.Label(root, text="", font='TimesNewRoman 20')
password_label.pack()

# Creating button for copy password`s text
copy_button = tk.Button(root, text='Copy Password', command=copy_function)
copy_button.pack()

# Program execution cycle
root.mainloop()
