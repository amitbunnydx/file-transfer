import math
from logging import exception
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    from random import randint,shuffle,choice
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    print("Welcome to the PyPassword Generator!")

    password_list = []
    [password_list.append(choice(letters)) for _ in  range(randint(8,10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2,4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2,4))]
    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    if len(pass_input.get()) == 0:
        pass_input.insert(0,password)
# this will copy password to clipboard so we can copy and pest it
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save(web, email, passwords):
    json_data={
        web.get():
        {
        "email":email.get(),
        "password":passwords.get()
    }
    }
    if len(web.get()) ==0 or len(email.get()) ==0 or len(passwords.get()) == 0:
        print("warning")
        messagebox.showwarning("warning", "missing filed")
    else:
        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file)
                print(data)
        except:
            with open("data.json", "w") as data_file:
                json.dump(json_data, data_file, indent=4)
        else:
            data.update(json_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web.delete(0, "end")
            passwords.delete(0, "end")

#-----------------------------------SEARCH DATA-------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data=json.load(data_file)
#this section will catch exception and share the name of that exception
    # except Exception as e:
    #     messagebox.showinfo('warning', f'user required data not found or wrong data')
    #     print('type is:', e.__class__.__name__)
        # print_exc()
    except FileNotFoundError:
        messagebox.showinfo('warning', f'requested file is not available')
    # except UnboundLocalError:
    #     messagebox.showinfo('warning', f'data you enter is not available or no data entered')
    else:
        if website in data:
            # value=[value for key,value in data.items() if key==website]
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo('info', f'result\n Email: {email} \n Password: {password}')
        else:
            messagebox.showinfo(title="error",message=f'no details for {website} exist')

    # ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=30,pady=30)


canvas=Canvas(width=200, height=200,highlightthickness=0)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0 ,row=1)
Email_Username_label=Label(text="Email/Username:")
Email_Username_label.grid(column=0 ,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0 ,row=3)

website_input=Entry(width=35)
website_input.grid(column=1 ,row=1)
website_input.focus()
email_input=Entry(width=54)
email_input.grid(column=1 ,row=2,columnspan=2)
email_input.insert(0,"Godsplan@gmail.com")
pass_input=Entry(width=35)
pass_input.grid(column=1 ,row=3)



generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2 ,row=3)

add_button=Button(text="Add", width=46, command=lambda : save(website_input, email_input, pass_input))
add_button.grid(column=1 ,row=4,columnspan=2)

search_button=Button(text="search",width=15, command = find_password)
search_button.grid(column=2 ,row=1,)

window.mainloop()