# 1.60934

from tkinter import *


window=Tk()
window.title('my first GUI program')
window.minsize(width=300,height=180)
window.config(padx=10,pady=10)

def calculations():
    final=round(int(input_data.get())*1.60934)
    output_label.config(text=final)

my_label1=Label(text='is equal to',font=('arial',14,'bold'))
my_label1.grid(column=0,row=2)
# my_label1.config(padx=5,pady=5)

input_data=Entry(width=10)
input_data.grid(column=2 , row=0)
# input_data.config(column=1,row=1)

miles_label=Label(text='Miles',font=('arial',14,'bold'))
miles_label.grid(column=3,row=0)
# miles_label.config(padx=5,pady=5)

output_label=Label(text='0',font=('arial',14,'bold'))
output_label.grid(column=2,row=2)
# output_label.config(padx=5,pady=5)

km_label=Label(text='KM',font=('arial',14,'bold'))
km_label.grid(column=3,row=2)
# km_label.config(padx=5,pady=5)

new_button=Button(text='click me', command=calculations)
new_button.grid(column=2,row=3)
# new_button.config(padx=5,pady=5)


window.mainloop()



