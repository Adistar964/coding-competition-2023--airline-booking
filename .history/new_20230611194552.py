from tkinter import *
from tkinter import messagebox as msg
import tkinter.font as font
import pandas as pd
import random
import pickle
from PIL import ImageTk,Image

def main(user):
    r = Tk()
    r.state("zoomed")

    file = Image.open("bg3.jpg")
    Img = file.resize((r.winfo_screenwidth(),r.winfo_screenheight()),Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(Img)

    c = Canvas(r)
    c.create_image(0,0,image=bg,anchor="nw")

    f = Frame(r,pady=20,bg="alice blue",highlightbackground="black",highlightthickness=3,padx=r.winfo_screenwidth()-1100)
    c.create_window((r.winfo_screenwidth()/2)-1000,100,window=f,anchor="nw")

    Label(f,bg="alice blue", text="From",font=font.Font(size=13),padx=15).grid(row=0,column=0)
    Label(f,bg="alice blue", text="To",font=font.Font(size=13),padx=15).grid(row=0,column=1)
    Label(f,bg="alice blue", text="Departure",font=font.Font(size=13),padx=15).grid(row=0,column=2)
    Label(f,bg="alice blue", text="Arrival(optional)",font=font.Font(size=13),padx=15).grid(row=0,column=3)
    Label(f,bg="alice blue", text="Airways",font=font.Font(size=13),padx=15).grid(row=0,column=4)

    fromm = Entry(f, font=font.Font(size=15))
    fromm.grid(row=1,column=0,pady=15)
    to = Entry(f, font=font.Font(size=15))
    to.grid(row=1,column=1,pady=15)

    f1 = Frame(f)
    day = IntVar()
    day.set(1)
    month = StringVar()
    month.set("Jan")
    l = OptionMenu(f1,day,*list(range(1,32)))
    l["font"] = ("Arial",12)
    l.grid(row=0,column=0)
    l = OptionMenu(f1,month,*["Jan","Feb"])
    l["font"] = ("Arial",12)
    l.grid(row=0,column=1)
    f1.grid(row=1,column=2,padx=20)

    f1 = Frame(f)
    aday = IntVar()
    aday.set(1)
    amonth = StringVar()
    amonth.set("Jan")
    l = OptionMenu(f1,aday,*list(range(1,32)))
    l["font"] = ("Arial",12)
    l.grid(row=0,column=0)
    l = OptionMenu(f1,amonth,*["Jan","Feb"])
    l["font"] = ("Arial",12)
    l.grid(row=0,column=1)
    f1.grid(row=1,column=3,padx=20)

    airways = StringVar()
    airways.set("Qatar Airways")
    l = OptionMenu(f, airways,*["Qatar Airways","British Airways"])
    l["font"] = ("Arial",12)
    l.grid(row=1,column=4)

    Label(f,bg="alice blue", text="Adults(12)",font=font.Font(size=13),padx=15,pady=10).grid(row=2,column=0)
    Label(f,bg="alice blue", text="Children(0-12)",font=font.Font(size=13),padx=15,pady=20).grid(row=2,column=1)
    Label(f,bg="alice blue", text="Cabin Class",font=font.Font(size=13),padx=15,pady=20).grid(row=2,column=2)
    Label(f,bg="alice blue", text="Trip Type",font=font.Font(size=13),padx=15,pady=20).grid(row=2,column=3)

    adults = IntVar()
    adults.set(1)
    l = OptionMenu(f, adults,*list(range(1,7)))
    l["font"] = ("Arial",12)
    l.grid(row=3,column=0)

    children = IntVar()
    children.set(0)
    l = OptionMenu(f, children,*list(range(0,7)))
    l["font"] = ("Arial",12)
    l.grid(row=3,column=1)

    classs = StringVar()
    classs.set("economy")
    l = OptionMenu(f, classs,*["economy","premium economy"])
    l["font"] = ("Arial",12)
    l.grid(row=3,column=2)

    # Button(f, text="Show Flight",bg="green",fg="white",font=font.Font(size=13),padx=15).grid(row=4,column=4)

    c.pack(fill=BOTH,expand=True)

    r.mainloop()


main("Abdullah")