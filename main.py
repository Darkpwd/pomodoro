import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PURPLE = "#7469B6"
RED = "#e7305b"
GREEN = "#7ABA78"
YELLOW = "#FFF2D7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60
    
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        my_label.config(text="Break", fg=PURPLE)
    else:
        countdown(work_sec)
        my_label.config(text="Work", fg=GREEN)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    my_canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_marks.config(text="")
    global reps 
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    my_canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#Label
my_label = tkinter.Label(text="Timer", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
my_label.grid(column=1, row=0)




#My canvas for displaying
my_canvas = tkinter.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
my_canvas.create_image(103, 112, image=tomato_img)
timer_text = my_canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
my_canvas.grid(column=1, row=1)








#Buttons
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()
