from tkinter import *


window=Tk()
window.title('my first GUI program')
window.minsize(width=500,height=380)
window.config(padx=100,pady=100)

my_label=Label(text='i am label',font=('arial',24,'bold'))
my_label.grid(column=0,row=0)
my_label.config(pady=50,padx=50)

def button_command():
    # my_label['text']=button['text']
    my_label.config(text=button['text'])
    print('button is clicked')

def get_input():
    print(input_data.get())
    my_label.config(text=input_data.get())


button=Button(text='click me',command=get_input)
button.grid(column=1, row=1)


input_data=Entry(width=10)
input_data.grid(column=4 , row=3)


new_button=Button(text='click me', command=button_command)
new_button.grid(column=3,row=0)


window.mainloop()