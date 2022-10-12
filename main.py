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
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# changing bg color and removing canvas thickness

canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer.grid(row=0, column=1)

# check mark label
check_mark = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

# Start button
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)



window.mainloop()
