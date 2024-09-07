from tkinter import *
from tkinter import messagebox as msg
import tkinter.font as font
from tkinter.scrolledtext import ScrolledText as scroll
import pandas as pd
import random

df = pd.read_csv("test.csv",names=["name","airways","ticket_number","time","date","from","to"])

def main(user):
    r = Tk()

    r.geometry('1000x700')
    r.title('Airline ticketing portal')
    r.resizable(0,0)

    img = PhotoImage(file="bg.png")
    Label(r,image=img).place(x=0,y=0)

    text = scroll(r,highlightthickness=3,highlightbackground="blue")
    f = Frame(text, padx=160, bg="alice blue")
    text.window_create("1.0",window=f)

    Label(f, text="Welcome "+user, font=font.Font(size=20,slant="italic"), bg="cadet blue").pack(pady=12)

    f1 = Frame(f)
    Label(f1, text="From",font=font.Font(size=13,weight="bold")).grid(row=0,column=0)
    Label(f1, text="To",font=font.Font(size=13,weight="bold")).grid(row=0,column=1)
    fromm = Entry(f1, font=("Helvetica",12))
    fromm.grid(row=1,column=0)
    to = Entry(f1, font=("Helvetica",12))
    to.grid(row=1,column=1)
    f1.pack(pady=10)
    
    Label(f, text="Departure",font=font.Font(size=13,weight="bold")).pack()
    f2 = Frame(f)
    day = IntVar()
    day.set(1)
    opt = OptionMenu(f2, day, *list(range(1,32)))
    opt["font"] = ("Helvetica",13)
    opt.grid(row=0,column=0)
    month = StringVar()
    month.set("Jan")
    opt = OptionMenu(f2, month, *["Jan","Feb"])
    opt["font"] = ("Helvetica",13)
    opt.grid(row=0,column=1)
    f2.pack(pady=10)

    Label(f, text="Arrival(optional)",font=font.Font(size=13,weight="bold")).pack()
    f3 = Frame(f)
    aday = IntVar()
    aday.set(1)
    opt = OptionMenu(f3, aday, *list(range(1,32)))
    opt["font"] = ("Helvetica",13)
    opt.grid(row=0,column=0)
    amonth = StringVar()
    amonth.set("Jan")
    opt = OptionMenu(f3, amonth, *["Jan","Feb"])
    opt["font"] = ("Helvetica",13)
    opt.grid(row=0,column=1)
    f3.pack(pady=10)

    Label(f, text="Number of Adult passengers (12 and above)",font=font.Font(size=13,weight="bold")).pack()
    adults = IntVar()
    adults.set(1)
    opt = OptionMenu(f, adults, *list(range(1,7)))
    opt["font"] = ("Helvetica",13)
    opt.pack(pady=10)

    Label(f, text="Number of child passengers (0-11)",font=font.Font(size=13,weight="bold")).pack()
    children = IntVar()
    children.set(0)
    opt = OptionMenu(f, children, *list(range(0,7)))
    opt["font"] = ("Helvetica",13)
    opt.pack(pady=10)

    Label(f, text="Airlines",font=font.Font(size=13,weight="bold")).pack()
    airways = StringVar()
    airways.set("Qatar Airways")
    opt = OptionMenu(f, airways, *["Qatar Airways","British Airways"])
    opt["font"] = ("Helvetica",13)
    opt.pack(pady=10)

    Label(f, text="Class type",font=font.Font(size=13,weight="bold")).pack()
    classs = StringVar()
    classs.set("economy")
    opt = OptionMenu(f, classs, *["economy","premium economy"])
    opt["font"] = ("Helvetica",13)
    opt.pack(pady=10)

    Label(f, text="trip type",font=font.Font(size=13,weight="bold")).pack()
    trip_type = IntVar()
    trip_type.set(1)
    opt = Radiobutton(f, variable=trip_type, text="One-way(arrival date wont be considered)", value=1)
    opt["font"] = ("Helvetica",13)
    opt.pack()
    opt = Radiobutton(f, variable=trip_type, text="Round-way", value=2)
    opt["font"] = ("Helvetica",13)
    opt.pack()

    Label(f, text="").pack(pady=10)

    def confirm_book():
        p = adults.get() + children.get()*0.5
        n = 0
        if classs.get() == "economy":
            n = 150
        else:
            n=250
        tt = 1
        if trip_type == 2:
            tt = 1.7
        price = n*p*tt

        time = f"{random.randrange(1,23)}:{random.randrange(10,61)}"
        date = f"{day.get()} {month.get()}"
        
        t = Toplevel()
        Label(t, text=f"Your flight will be at {time} in {date}\nPlease enter your credit card number to confirm booking:\n", font=font.Font(weight="bold",size=16)).pack(pady=10,padx=20)
        Entry(t,font=font.Font(size=13)).pack(pady=5)
        def book():
            number = f"E{random.randrange(100000,999999)}"
            msg.showinfo(title="success",message=f"Your ticket has been successfully booked!\nYour ticket number: {number}")
            t.destroy()
            df.loc[int(len(df))] = [user,airways.get().replace(" ","_"),number,time.replace(":","_"),date.replace(" ","_"),fromm.get(),to.get()]
        
        Button(t, command=book,text="confirm booking",bg="yellow",font=font.Font(size=10)).pack(pady=10)
        t.mainloop()

    Button(f, text="Book",bg="green",fg="white",font=font.Font(size=13),command=confirm_book).pack(pady=5,ipadx=20)
    
    text.pack(padx=50,pady=(150,0))

    def show_bookings():
        t = Toplevel()

        t.geometry("700x500")

        Label(t, text="Your Bookings:",font=font.Font(size=17,weight="bold",underline=True)).pack(pady=15)

        if user in df["name"].values:
            for index,row in df.iterrows():
                if row["name"] == "Ali":
                    Label(t, bg="white",font=font.Font(size=12),text=f"ticket number {row['ticket_number']}:{row['airways'].replace('_',' ')} flight from {row['from']} to {row['to']} in {row['time'].replace('_',':')} in {row['date'].replace('_',' ')}").pack(pady=6,ipady=10)                    
        else:
            Label(t, text="All Your Bookings will be shown here .....",font=font.Font(size=13,slant="italic")).pack(pady=15)
                        
        
        t.mainloop()

    def cancel_bookings():
        t = Toplevel()
        t.geometry("500x500")
        Label(t,text="warning: only 95% amount will be refunded",font=font.Font(size=10,slant="italic")).pack(pady=10)
        Label(t, text="Enter your Ticket number:",font=font.Font(weight="bold",size=15)).pack(pady=5)
        tno = Entry(t, font=font.Font(size=13))
        tno.pack(pady=4)

        def cancel():
            for index,row in df.iterrows():
                if row["ticket_number"] == tno.get():
                    df.drop(index,inplace=True)
            msg.showinfo(title="booking cancelled", message=f"your booking with ticket number '{tno.get()}' is now cancelled")
            t.destroy()
        
        Button(t,text="cancel booking",bg="red",fg="white",command=cancel,font=font.Font(size=12)).pack(pady=5)

        t.mainloop()

    Button(r, text="Show bookings history", command=show_bookings,bg="light green",font=("Arial",13)).pack(pady=(40,10))
    Button(r, text="Cancel previous bookings", command=cancel_bookings,bg="light yellow",font=("Arial",13)).pack()
    Button(r, text="Sign out", command=show_bookings,bg="red",fg="white",font=("Arial",13)).pack(pady=5)

    
    r.mainloop()


main("Ali")

df.to_csv("test.csv")
