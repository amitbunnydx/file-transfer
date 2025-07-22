import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Complicated= '✔'
reps=0
timer=''
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    Timer_label.config(text='Timer', fg=GREEN)
    yes_label.config(text='')
    canvas.itemconfig(timer_text,text='00:00')
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*10
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        Timer_label.config(text='LONG BREAK',fg=RED)
        count_down(long_break_sec)
    elif reps %2 ==0:
        Timer_label.config(text='BREAK',fg=PINK)
        count_down(short_break_sec)
    else:
        Timer_label.config(text='WORK',fg=GREEN)
        count_down(work_sec)

    # while reps!=0:
    #     if reps in [1,3,5,7]:
    #         print(reps)
    #         # count_down(work_sec)
    #         reps+=1
    #     elif reps in [2,4,6] :
    #         print(reps)
    #         # count_down(short_break_sec)
    #         reps += 1
    #     else:
    #         # count_down(long_break_sec)
    #         print(reps)
    #         reps=0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print(count)
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        # print(f"math formula {math.floor(reps/2)}")
        # print(f"reps {reps}")
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+= '✔'
        yes_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

Timer_label=Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,'bold'))
Timer_label.grid(column=2 ,row=1)

canvas=Canvas(width=210, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(103,112,image=tomato_img)
timer_text=canvas.create_text(103,140,text='00:00',fill='white',font=(FONT_NAME,30,'bold'))
canvas.grid(column=2 ,row=2)

start_button=Button(text='Start',bg=YELLOW,command=start_timer)
start_button.grid(column=1 ,row=3)

reset_button=Button(text='Reset',bg=YELLOW,command=reset_timer)
reset_button.grid(column=3 ,row=3)

yes_label=Label(fg=GREEN,bg=YELLOW)
yes_label.grid(column=2 ,row=4)





window.mainloop()