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
reps = 0
timer = None


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text='Timer')
    check_marks.config(text='')
    reps *= 0


def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    if reps % 8 == 0:
        label.config(text='Long Break', bg=GREEN, fg=YELLOW, highlightthickness=0)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        label.config(text='Short Break', bg=GREEN, fg=YELLOW, highlightthickness=0)
        countdown(short_break_sec)
    else:
        label.config(text='Work', bg=GREEN, fg=YELLOW, highlightthickness=0)
        countdown(work_sec)


def countdown(count):
    data_min = count // 60
    data_sec = count % 60
    if data_sec < 10:
        canvas.itemconfig(timer_text, text=f'{data_min}:0{data_sec}')
    else:
        canvas.itemconfig(timer_text, text=f'{data_min}:{data_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        start_timer()
        marks = ''
        work_session = reps // 2
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)


window = Tk()
window.title('pomodoro')
window.minsize(height=600, width=600)
window.config(bg=GREEN)

label = Label(text='Timer', bg=GREEN, fg=YELLOW)
label.pack()

canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white')
canvas.pack()

start_button = Button(text='Start', bg=GREEN, fg=YELLOW, highlightthickness=0, command=start_timer)
start_button.pack()

reset_button = Button(text='Reset', bg=GREEN, fg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.pack()
check_marks = Label(bg=GREEN, fg=YELLOW)
check_marks.pack()

window.mainloop()
