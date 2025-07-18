from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters)for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers)for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols +  password_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    import json
    from tkinter import messagebox

    # Assuming new_data is defined somewhere like this:
    # new_data = {
    #     website: {
    #         "email": email,
    #         "password": password
    #     }
    # }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure that you filled every detail.")
    else:
        try:
            # Try to open and load existing data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If file doesn't exist, start with empty data
            data = {}
        except json.JSONDecodeError:
            # If file is empty or not valid JSON
            messagebox.showerror(title="Error", message="Data file is corrupted.")
            data = {}
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Unexpected error occurred: {e}")
            data = {}
        finally:
            # Update the data dictionary regardless of what happened
            data.update(new_data)

            try:
                # Save updated data to file
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Could not save data: {e}")
            else:
                # Clear the form fields only if saving was successful
                website_entry.delete(0, END)
                password_entry.delete(0, END)
def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is corrupted.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for '{website}' exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)

canvas = Canvas(height=250, width=250)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125,125, image=logo_img)
canvas.grid(row=0,column=1)

#lables
website_lable = Label(text="website:")
website_lable.grid(row= 1,column=0)

email_lable = Label(text="email/Username:")
email_lable.grid(row= 2,column=0)

password_lable = Label(text="password:")
password_lable.grid(row= 3,column=0)

#entries
website_entry = Entry(width=35)
website_entry.grid(row= 1, column=1)
search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2)
email_entry = Entry(width=35)
email_entry.grid(row= 2,column=1)
email_entry.insert(0,"dc@gmail.com")
password_entry = Entry(width=21, )
password_entry.grid(row= 3,column=1)

#buttons
generate_password_button = Button(text= "Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text= "Add", width=36,command= save)
add_button.grid(row= 4, column=1, columnspan=2)





window.mainloop()