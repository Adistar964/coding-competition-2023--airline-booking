from tkinter import *
import tkinter.font as font

def main():
    r = Tk()
    # r.state("zoomed")
    r.geometry("1000x600")
    r.title("Airline Booking Portal")
    img = PhotoImage(file="bg.png")
    Label(r, image=img).place(x=0,y=0)
    f = Frame(bg="white",highlightbackground="lightblue",highlightthickness=3)
    Label(f, text="Welcome User", bg="cadet blue", font=font.Font(size=20,slant="italic")).pack(pady=20)
    Label(f, text="Departure:",font=font.Font(size=13)).pack(anchor="w")
    dep = Entry(f, font=font.Font(size=10))
    dep.pack()
    f.pack(ipadx=200,ipady=200,pady=80)
    r.mainloop()

main()