from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    global entry_password
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website : {
        "email": email,
        "password": password
    }
}


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!", title="ALERT!")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                # to open first : json.dump(new_data, data_file, indent=4) also mode="w"
                data = json.load(data_file)

        except FileNotFoundError:
            print("File doesn't, so we are creating one, we got you covered!")
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            print("else")
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

def find_password():
    global entry_website
    asked_website = entry_website.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            asked_password = data[asked_website]["password"]


    except FileNotFoundError:
        messagebox.showinfo(message="Data file does not exist", title="ALERT!")

    except KeyError:
        messagebox.showinfo(message="Website not found in Database!", title="ALERT!")

    else:
        #get data of required website
        #put the asked password in password entry
        global entry_password
        entry_password.focus()
        entry_password.insert(0, asked_password)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



#Canvas Column
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels:
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

#Entries:
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "saiabhi3690@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)


#Buttons:
generate_button = Button(width=11, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add = Button(width=36, text="Add", command=save)
add.grid(row=4, column=1, columnspan=2)

search_button = Button(width=11, text="Search", command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()

