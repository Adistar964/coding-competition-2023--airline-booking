from tkinter import *
import tkinter.font as font
from tkinter import messagebox as msg
from tkinter.scrolledtext import ScrolledText
import random
import pandas as pd


df = pd.read_csv("flights.csv")

def main(user,loc):
    r = Tk()
    r.resizable(0,0)
    r.geometry("1000x700")
    # r.state("zoomed")1
    r.title("Airline Booking Portal")
    img = PhotoImage(file="bg.png")
    Label(r, image=img).place(x=0,y=0)
    text = ScrolledText(cursor="arrow")
    f = Frame(text,padx=160,bg="white",highlightbackground="lightblue",highlightthickness=3)
    text.window_create("1.0",window=f)
    
    Label(f, text=f"Welcome {user}", bg="cadet blue", font=font.Font(size=20,slant="italic")).pack(pady=20)
    
    f1 = Frame(f)
    Label(f1, text="From",font=font.Font(size=13)).grid(row=0,column=0,padx=10)
    Label(f1, text="To",font=font.Font(size=13)).grid(row=0,column=1)
    fromm = Entry(f1, font=font.Font(size=13))
    fromm.insert(0,loc)
    fromm.grid(row=1,column=0,ipady=10)
    to = Entry(f1, font=font.Font(size=13))
    to.grid(ipady=10,row=1,column=1)
    f1.pack(pady=15)
    
    Label(f, text="Departure",font=font.Font(size=13)).pack()
    f2 = Frame(f)
    days = list(range(31))
    months = ["Jan","Feb","Mar","Apr","May","June","july"]
    day = StringVar()
    day.set(1)
    month = StringVar()
    month.set("Jan")
    l=OptionMenu(f2,day,*days)
    l["font"] = ("Arial",13)
    l.grid(row=0,column=0)
    l=OptionMenu(f2,month,*months)
    l["font"] = ("Arial",13)
    l.grid(row=0,column=1)
    f2.pack(pady=15)
    
    Label(f, text="Return",font=font.Font(size=13)).pack()
    f3 = Frame(f)
    aday = StringVar()
    aday.set(1)
    amonth = StringVar()
    amonth.set("Jan")
    l=OptionMenu(f3,aday,*days)
    l["font"] = ("Arial",13)
    l.grid(row=0,column=0)
    OptionMenu(f3,amonth,*months).grid(row=0,column=1)
    f3.pack(pady=15)

    Label(f, text="class",font=font.Font(size=13)).pack()
    clas = StringVar()
    clas.set("Economy")
    classes = ["Economy","Premium Economy","Bussiness","First class"]
    l=OptionMenu(f,clas,*classes)
    l["font"] = ("Arial",13)
    l.pack(pady=15)
    
    Label(f, text="Adults (12 and above)",font=font.Font(size=13)).pack()
    adults = IntVar()
    adults.set(1)
    classes = list(range(1,6))
    l=OptionMenu(f,adults,*classes)
    l["font"] = ("Arial",13)
    l.pack(pady=15)
    
    Label(f, text="Children (0-12)",font=font.Font(size=13)).pack()
    children = IntVar()
    children.set(0)
    classes = list(range(0,6))
    l=OptionMenu(f,children,*classes)
    l["font"] = ("Arial",13)
    l.pack(pady=15)
    
    Label(f, text="Airways",font=font.Font(size=13)).pack()
    airways = StringVar()
    airways.set("qatar airways")
    l = OptionMenu(f,airways,*["qatar airways","british airways","air India"])
    l["font"] = ("Arial",13)
    l.pack(pady=15)
    
    Label(f,text="Trip type:",font=("Arial",13)).pack(pady=15)
    trip_type = IntVar()
    Radiobutton(f, bg="white",font=("Arial",13),text="One-way(Return date wont be considered)",variable=trip_type,value=1).pack()
    Radiobutton(f, bg="white",font=("Arial",13),text="Round-way",variable=trip_type,value=2).pack()
    
    def confirm_book():
        t = Toplevel(r)
        n=0
        p=adults.get()+(children.get()*0.7)
        if clas == "Economy":
            n = 300
        if clas == "Premium Economy":
            n = 400
        if clas == "Bussiness":
            n = 500
        else:
            n=600
        ran = p*n
        if trip_type.get() == 2:
            ran = ran*1.8
        price = random.randrange(ran-500,ran)
        h = random.randrange(1,25)
        m = random.randrange(10,61)
        time = f"{h}:{m}"
        Label(t, font=("Arial",18),text="Your flight will  be at:"+time+" in "+day.get()+" "+month.get()+"\n your total cost is: $"+str(price)+"\n please confirm your credit card number:").pack()
        Entry(t,font=("Helvetica",13)).pack()
        def book():
            t.destroy()
            number = random.randint(1000000,9999999999)
            t="-"
            if trip_type == 1:
                t = "-"
            else:
                t=f"{time} at {aday.get()}/{amonth.get()}"
            df.loc[len(df)] = [user,number,f"{time} at {day.get()}/{month.get()}",t,fromm.get(),to.get()]
            msg.showinfo(title="Booked!",message=f"Your flight has been booked!\nflight-number:{number}\nflight time: {time} at {day.get()}/{month.get()}")
        Button(t, text="Book",bg="yellow",command=book).pack(pady=15)
        t.mainloop()

    Button(f,text="Book Flight",command=confirm_book,font=("Helvetica",13),bg="green",fg="white").pack(pady=20)
    
    # f.pack(ipadx=200,ipady=350,pady=50)
    text.pack(pady=50,padx=150)

    Button(r, text="Show Bookings",font=("Bahaus 93",13),bg="lightgreen").pack(pady=15)

    r.mainloop()

main("Ali","Doha")

df.to_csv("flights.csv")