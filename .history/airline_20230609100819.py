from tkinter import *


def main():
    r = Tk()
    # r.state("zoomed")
    r.geometry("1000x600")
    r.title("Airline Booking Portal")
    img = PhotoImage(file="bg.png")
    Label(r, image=img).place(x=0,y=0)
    f = Frame(bg="white")
    Label(f, text="Welcome User", bg="cadet blue", font=("Bahaus 93",20)).pack(pady=6)
    f.pack(ipadx=200,ipady=200,pady=80)
    r.mainloop()

main()