from tkinter import *
from tkinter import messagebox
from random import random,randint,choice,shuffle
#----------------------------passwordGenerator--------------------------#

#Password Generator Project
def generate_pass():
    passwordEntry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letter + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)

    passwordEntry.insert(0,password)


#---------------------------logic---------------------------------------#
def saving():
    web= webEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    if len(email) and len(web) and len(password) > 1:

        isok = messagebox.askokcancel(title=" بۆ دڵنیایی", message="ئایا دڵنیای لە خەزن کردنی ئەم پاسۆردە؟")
        if isok:

            with open("password.txt","a") as kk:
                kk.write(f"\n {web} | {email} | {password}")
            webEntry.delete(0,END)
            passwordEntry.delete(0,END)
    else:
        messagebox.showinfo(title="nooo",message="نابێت بۆشاییەکان بەیاڵ بن")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # More padding for breathing room

# Logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website
labelWeb = Label(text="Website:")
labelWeb.grid(column=0, row=1, pady=5)
webEntry = Entry(width=35)
webEntry.focus()
webEntry.grid(row=1, column=1, columnspan=2, sticky="EW")

# Email/Username
labelEmail = Label(text="Email/Username:")
labelEmail.grid(column=0, row=2, pady=5)
emailEntry = Entry(width=35)
emailEntry.grid(row=2, column=1, columnspan=2, sticky="EW")
emailEntry.insert(0,"hama@gmail.com")

# Password
labelPassword = Label(text="Password:")
labelPassword.grid(column=0, row=3, pady=5)
passwordEntry = Entry(width=21)
passwordEntry.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password",command=generate_pass)
generate_password_button.grid(row=3, column=2, sticky="EW")

# Add Button (full width)
addButton = Button(text="Add", width=36,command=saving)
addButton.grid(column=1, row=4, columnspan=2, pady=10, sticky="EW")

# Configure columns to expand
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)

window.mainloop()
