from tkinter import *
import tkinter.messagebox as msg
import tkinter.font as font
import random

r = Tk()
r.state("zoomed")
r.title("Airline Booking portal")

title_font = font.Font(size=20,slant="italic")

Label(r, text="Welcome User!", font=title_font,bg="Cadet blue").pack(pady=30)

f = Frame(highlightthickness=3,highlightbackground="blue")

Label(f,text="Flight selection",font=font.Font(size=20,underline=True),fg="red").pack(pady=20)
Label(f,text="----------------------------------------------------------------------------------------------------").pack(pady=4)
Label(f, text="Number of rooms:",font=font.Font(size=15)).pack(pady=2)
options = list(range(1,5))
n_rooms = StringVar()
n_rooms.set(1)
OptionMenu(f, n_rooms, *options).pack()
Label(f, text="Number of washrooms:",font=font.Font(size=15)).pack(pady=2)
options = list(range(1,3))
n_bathrooms = StringVar()
n_bathrooms.set(1)
OptionMenu(f, n_bathrooms, *options).pack()
Label(f, text="Wifi needed:",font=font.Font(size=15)).pack(pady=2)
options = ["yes","No"]
w_n = StringVar()
w_n.set("No")
OptionMenu(f, w_n, *options).pack()
Label(f, text="Type of beds:",font=font.Font(size=15)).pack(pady=2)
options = ["deluxe","twin","double-decked","single"]
b_n = StringVar()
b_n.set("deluxe")
OptionMenu(f, b_n, *options).pack()
Label(f, text="Type of AC:",font=font.Font(size=15)).pack(pady=2)
options = ["split","boxed"]
a_n = StringVar()
a_n.set("split")
OptionMenu(f, a_n, *options).pack()

Label(f,text="credit card Info:",font=font.Font(size=15)).pack(pady=2)

credit = Entry(f)
credit.pack()

def check():
    y = random.choice([True,False])
    number = random.randint(1,50)
    if y:
        msg.showinfo(title="successful!",message=f"Congrats! The room number {number} is booked under user's name")
    else:
        msg.showerror(title="no rooms found",message="We are sorry! we are currently out of rooms")

Button(f,text="check rooms",command=check, font=font.Font(size=12),fg="white",bg="black").pack(pady=10)

f.pack(ipadx=200,ipady=30)

def prev():
    t = Toplevel(r)
    t.title("History")
    t.geometry("400x400")
    Label(t, text="Your Bookings:",font=font.Font(size=18,underline=True)).pack()
    there = False
    if there:
        pass
    else:
        Label(t, text="All your previous bookings will appear here...",font=font.Font(size=12,slant="italic")).pack()
    t.mainloop()

Button(r, text="show bookings history",command=prev,font=font.Font(size=15)).pack(pady=10)

r.mainloop()