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

    f = Frame(r,bg="alice blue",highlightbackground="black",highlightthickness=3,padx=r.winfo_screenwidth()-1100)
    c.create_window((r.winfo_screenwidth()/2)-500,100,window=f,anchor="nw")

    Label(f, text="From",font=font.Font(size=13),padx=15).grid(row=0,column=0)
    Label(f, text="To",font=font.Font(size=13),padx=15).grid(row=0,column=1)
    Label(f, text="Departure",font=font.Font(size=13),padx=15).grid(row=0,column=2)
    Label(f, text="Arrival(optional)",font=font.Font(size=13),padx=15).grid(row=0,column=3)


    c.pack(fill=BOTH,expand=True)

    r.mainloop()


main("Abdullah")