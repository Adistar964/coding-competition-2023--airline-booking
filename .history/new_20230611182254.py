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

    file = Image.open("bg.png")
    Img = file.resize((r.winfo_screenwidth(),r.winfo_screenheight()),Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(Img)

    c = Canvas(r)
    c.create_image(0,0,image=bg,anchor="nw")
    c.pack(fill=BOTH,expand=True)


main("Abdullah")