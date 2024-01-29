from tkinter import *
import time

app = Tk()
app.title("Clock")
app.geometry("500x200")
app.resizable(False, False)
canvas = Canvas(app, width=500, height=300, bg="skyblue")
canvas.pack(fill=BOTH, expand=1)

clock = Label(app, bg="skyblue", fg="white", font=("Arial", 80, "bold"), justify=CENTER)
canvas.create_window(250, 100, window=clock, anchor=CENTER)


def clock_func():
    now = time.strftime("%H:%M:%S")
    clock.config(text=now)
    clock.after(1000, clock_func)


clock_func()
app.mainloop()
