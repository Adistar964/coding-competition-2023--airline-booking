from tkinter import *


def main():
    r = Tk()
    r.state("zoomed")
    # r.geometry("800x450")
    r.title("Airline Booking Portal")
    img = PhotoImage(file="bg.png")
    Label(r, image=img).pack()
    Label(r, text="Welcome User", bg="cadet blue", font=("Bahaus 93",20)).pack()

    r.mainloop()

main()