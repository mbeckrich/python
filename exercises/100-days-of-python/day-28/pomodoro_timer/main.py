import tkinter as tk
from tkinter import Canvas, PhotoImage
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"  # fg
YELLOW = "#f7f5dd"  # bg
FONT_NAME = "Mononoki Nerd Font Mono"
CHECK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer reset


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# Timer mechanism


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += CHECK
        checkmark.config(text=marks)


# Countdown mechanism


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()


# UI setup

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# background image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day-28/pomodoro_timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(column=1, row=1)


# labels
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 32), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmark = tk.Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

# buttons
button_start = tk.Button(
    text="Start", highlightthickness=0, command=start_timer
)
button_start.grid(column=0, row=2)

button_reset = tk.Button(text="Reset", command=reset, highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()
