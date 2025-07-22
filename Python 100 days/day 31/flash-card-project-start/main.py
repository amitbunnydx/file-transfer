import random
import time
from tkinter import *
from tkinter import messagebox

import pandas
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME='Ariel'
chosen_word={}
french_data={}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except:
    original_data = pandas.read_csv('data/french_words.csv')
    french_data = original_data.to_dict(orient="records")
else:
    french_data = data.to_dict(orient="records")

print(french_data)


def next_card():
    global chosen_word,flip_timer
    window.after_cancel(flip_timer)
    chosen_word=random.choice(french_data)
    print(chosen_word)
    canvas.itemconfigure(french_text,text='French',fill='black')
    canvas.itemconfigure(english_text,text=chosen_word['French'],fill='black')
    canvas.itemconfigure(card_background,image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfigure(french_text,text='English',fill='white')
    canvas.itemconfigure(english_text,text=chosen_word['English'],fill='white')
    canvas.itemconfigure(card_background,image=card_back_img)

def remove():
    french_data.remove(chosen_word)
    print(french_data)
    csv_file=pandas.DataFrame(french_data)
    csv_file.to_csv('data/words_to_learn.csv',index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400,263,image=card_front_img)

card_back_img=PhotoImage(file="images/card_back.png")

french_text=canvas.create_text(400,150,text='',font=(FONT_NAME,40,'bold'),)
english_text=canvas.create_text(400,263,text='',font=(FONT_NAME,60,'bold'))

canvas.grid(column=0 ,row=0,columnspan=2)


yes_image = PhotoImage(file="images/right.png")
no_image = PhotoImage(file="images/wrong.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=remove)
yes_button.grid(row=1,column=1)
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(row=1,column=0)
next_card()


window.mainloop()