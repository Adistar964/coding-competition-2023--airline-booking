from tkinter import *
import tkinter.font as font

def main():
    r = Tk()
    # r.state("zoomed")
    r.geometry("1000x700")
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
    month = StringVar()
    month.set("Jan")
    OptionMenu(f2,day,*days).grid(row=0,column=0)
    OptionMenu(f2,month,*months).grid(row=0,column=1)
    f2.pack(pady=10)
    Label(f, text="Return",font=font.Font(size=13)).pack()
    f3 = Frame(f)
    aday = StringVar()
    aday.set(1)
    amonth = StringVar()
    amonth.set("Jan")
    OptionMenu(f3,aday,*days).grid(row=0,column=0)
    OptionMenu(f3,amonth,*months).grid(row=0,column=1)
    f3.pack(pady=10)
    Label(f, text="Plane-class",font=font.Font(size=13)).pack()
    f4 = Frame(f)
    clas = StringVar()
    clas.set("Economy")
    classes = ["Economy","Premium Economy","Bussiness","First-class"]
    OptionMenu(f4,clas,*classes).pack()
    f4.pack(pady=10)
    f.pack(ipadx=200,ipady=350,pady=50)
    r.mainloop()

main()