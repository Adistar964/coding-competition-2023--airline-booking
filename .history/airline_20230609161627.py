from tkinter import *
import tkinter.font as font
from tkinter.scrolledtext import ScrolledText

def main(user,loc):
    r = Tk()
    r.resizable(0,0)
    r.geometry("1000x700")
    r.title("Airline Booking Portal")
    img = PhotoImage(file="bg.png")
    Label(r, image=img).place(x=0,y=0)
    text = ScrolledText()
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
    f1.pack()
    
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
    f2.pack(pady=10)
    
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
    f3.pack(pady=10)

    Label(f, text="class",font=font.Font(size=13)).pack()
    clas = StringVar()
    clas.set("Economy")
    classes = ["Economy","Premium Economy","Bussiness","First-class"]
    l=OptionMenu(f,clas,*classes)
    l["font"] = ("Arial",13)
    l.pack(pady=10)
    
    Label(f, text="Adults (12 and above)",font=font.Font(size=13)).pack()
    adults = IntVar()
    adults.set(1)
    classes = list(range(1,6))
    l=OptionMenu(f,adults,*classes)
    l["font"] = ("Arial",13)
    l.pack(pady=10)
    
    Label(f, text="Children (0-12)",font=font.Font(size=13)).pack()
    children = IntVar()
    children.set(1)
    classes = list(range(1,6))
    l=OptionMenu(f,children,*classes)
    l["font"] = ("Arial",13)
    l.pack(pady=10)
    
    Label(f, text="Airways",font=font.Font(size=13)).pack()
    airways = StringVar()
    airways.set("qatar airways")
    l = OptionMenu(f,airways,*["qatar airways","british airways","air India"])
    l["font"] = ("Arial",13)
    l.pack(pady=10)
    
    Label(f,text="Trip type:",font=("Arial",13)).pack(pady=10)
    trip_type = IntVar()
    Radiobutton(f, bg="white",font=("Arial",13),text="One-way",variable=trip_type,value=1).pack()
    Radiobutton(f, bg="white",font=("Arial",13),text="Round-way",variable=trip_type,value=2).pack()
    
    Button(f,text="Book Flights",font=("Helvetica",13),bg="green",fg="white").pack(pady=20)
    
    # f.pack(ipadx=200,ipady=350,pady=50)
    text.pack(ipadx=200,ipady=350,pady=50,padx=150)
    r.mainloop()

main("Ali","Doha")