from tkinter import *
import math

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


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text='Timer')
    check_mark.config(text="")

    reps *= 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(text='Long Break', fg=RED)
        count_down(long_sec)
    elif reps % 2 == 0:
        label.config(text='Short Break', fg=PINK)
        count_down(short_sec)
    else:
        label.config(text='Work', fg=YELLOW)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ----------t--------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=GREEN)

label = Label(text='Timer', bg=GREEN, fg=YELLOW, font=(FONT_NAME, '35', 'bold'))
label.grid(row=0, column=2)

start_button = Button(text="Start", font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=1)
reset_button = Button(text="Reset", font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

check_mark = Label(bg=GREEN, fg=YELLOW, font=(FONT_NAME, 15, 'normal'), highlightthickness=0)
check_mark.grid(row=3, column=2)

canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=2)

window.mainloop()
