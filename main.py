from tkinter import *
import math 

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_title.config(text="Timer",fg=GREEN)
    canva.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if(reps % 2 == 1):
        timer_title.config(text="Work Session", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif(reps % 8 == 0):
        timer_title.config(text="Long Break",fg=RED)
        count_down(LONG_BREAK_MIN * 60)

    elif(reps % 2 ==0):
        timer_title.config(text="Short Break",fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps,timer
    count_min = math.floor(count/60)
    count_sec = count%60

    if(count_min == 0):
        count_min = "00"
    elif(count_min < 10):
        count_min = f"0{int(count_min)}"

    if(count_sec == 0):
        count_sec = "00"
    elif(count_sec < 10):
        count_sec = f"0{int(count_sec)}"

    if(count > 0):
        canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔️"
        
        tick.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


# Timer
timer_title = Label(bg=YELLOW,fg=GREEN, text="Timer", font=(FONT_NAME,40,"bold"))
timer_title.grid(row=0,column=1)

# Tick
tick = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,"normal"))
tick.grid(row=3,column=1)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(100,112,image=tomato_img)
timer_text = canva.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canva.grid(row=1,column=1)

# Buttons
start = Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

reset = Button(text="Reset",highlightthickness=0,command=reset)
reset.grid(row=2,column=2)






window.mainloop()