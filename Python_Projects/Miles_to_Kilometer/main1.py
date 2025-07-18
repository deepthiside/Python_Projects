# import tkinter
# from tkinter import mainloop
#
# window = tkinter.Tk()
# window.title("My Window")
# window.minsize(width=500,height=500)
#
# my_lable = tkinter.Label(text="Hey There how are you?",font=("Arial",24,"bold"))
# my_lable.pack()
#
#
#
#
#
#
#
# window.mainloop()
#
# import tkinter as tk
#
# # Function to be called when the button is clicked
# def show_text():
#     user_input = entry.get()
#     result_label.config(text=f"You typed: {user_input}")
#
# # Create the main window
# root = tk.Tk()
# root.title("Tkinter Input Example")
# root.geometry("300x200")
#
# # Create a label
# label = tk.Label(root, text="Enter something:")
# label.pack(pady=5)
#
# # Create an entry (text input)
# entry = tk.Entry(root, width=30)
# entry.pack(pady=5)
#
# # Create a button
# button = tk.Button(root, text="Submit", command=show_text)
# button.pack(pady=5)
#
# # Create a label to display the result
# result_label = tk.Label(root, text="")
# result_label.pack(pady=10)
#
# # Start the GUI event loop
# root.mainloop()
import tkinter as tk
from tkinter import ttk

# Conversion function
def convert():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 4)
        result_label.config(text=f"{km} Kilometers")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Clear function
def clear():
    miles_input.delete(0, tk.END)
    result_label.config(text="")

# Create main window
window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.geometry("400x250")
window.config(padx=20, pady=20, bg="#f5f5f5")

# Title
title = tk.Label(window, text="Miles to Kilometers", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=10)

# Input field
miles_input = ttk.Entry(window, font=("Helvetica", 14), width=15)
miles_input.pack(pady=10)
miles_input.focus()

# Convert button
convert_btn = ttk.Button(window, text="Convert", command=convert)
convert_btn.pack(pady=5)

# Result label
result_label = tk.Label(window, text="", font=("Helvetica", 16), bg="#f5f5f5", fg="#007acc")
result_label.pack(pady=10)

# Clear button
clear_btn = ttk.Button(window, text="Clear", command=clear)
clear_btn.pack()

# Run the app
window.mainloop()
