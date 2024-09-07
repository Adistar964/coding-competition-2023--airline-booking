from tkinter import *
from tkinter import messagebox as msg
import tkinter.font as Font
import pandas as pd
import random
import pickle
from PIL import ImageTk,Image

def main(user):
    r = Tk()
    r.state("zoomed")

    file = Image.open("bg2.png")
    Img = file.resize((r.winfo_screenwidth(),r.winfo_screenheight()),Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(Img)

    c = Canvas(r)
    c.create_image(0,0,image=bg,anchor="nw")

    f = Frame(r,pady=100,bg="cyan",padx=160)
    c.create_window(r.winfo_screenwidth()/2,r.winfo_screenheight()/2,window=f,anchor="nw")

    Button(f,text="Hello").pack()

    c.pack(fill=BOTH,expand=True)

    r.mainloop()


main("Abdullah")