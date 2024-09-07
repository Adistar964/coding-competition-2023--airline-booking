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
    Label(f, text="From",font=font.Font(size=13)).pack()
    fromm = Entry(f, font=font.Font(size=13))
    fromm.pack(ipady=10)
    Label(f, text="To",font=font.Font(size=13)).pack()
    to = Entry(f, font=font.Font(size=13))
    to.pack(ipady=10)
    Label(f, text="Departure",font=font.Font(size=13)).pack()
    f2 = Frame(f)
    days = list(range(31))
    months = ["Jan","Feb","Mar","Apr","May","June","july"]
    day = StringVar()
    day.set(1)
    day = StringVar()
    day.set("Jan")
    OptionMenu(f2,day,*days).grid(row=0,column=0)
    OptionMenu(f2,month,*months).grid(row=0,column=1)
    f2.pack(pady=10)
    f.pack(ipadx=200,ipady=200,pady=80)
    r.mainloop()

main()