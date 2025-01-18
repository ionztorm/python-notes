"""Pomodoro timer app."""

import tkinter as tk
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#7cb289"
YELLOW = "#f7f5dd"
FONT_NAME = "Berkeley Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_ICON = "✔"
timer = None
reps = 1

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer() -> None:
    """Reset current timer."""
    global reps
    if timer:
        window.after_cancel(timer)
        label_progress.config(text="")
        canvas.itemconfig(timer_text, text="00:00")
        label_timer.config(text="Timer")
        reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer() -> None:
    """Start the timer."""
    global reps
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        countdown(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN)
        tick_text = ""
        for _ in range(reps // 2):
            tick_text += CHECK_ICON
        label_progress.config(text=tick_text)
    else:
        countdown(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=PINK)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count) -> None:
    """Countdown from a value."""
    global timer

    def zero_concat(num: int) -> str:
        if 0 <= num < 10:
            return f"0{num}"
        return f"{num}"

    minutes = zero_concat(count // 60)
    seconds = zero_concat(count % 60)
    time = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Study timer")
window.config(padx=100, pady=50, bg=YELLOW)

# gui is event driven. Need to check for events every fraction of a second to react to user
# putting a loop elsewhere in the code stops us from reaching the main loop so the gui will
# never load. The window widget gives us the 'after' method which allows us to set a tim to wait
# and a function to execute after that period of time. We can then pass *args that will be passed
# to the function. If we want it to loop for any reason, we can put this inside a function.
# window.after(1000, func, args)

# canvas widget allows for layering shapes.
# width and height are in pixels
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# requires coordinates for the image to be placed, and the images as a PhotoImage object
tomato_image_file = Path("tomato.png")
tomato_image_object = tk.PhotoImage(file=tomato_image_file)
canvas.create_image(100, 112, image=tomato_image_object)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = tk.Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1,row=0)

button_start = tk.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_progress = tk.Label(bg=YELLOW, fg=GREEN)
label_progress.grid(column=1,row=3)


window.mainloop()

