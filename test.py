from tkinter import *
from tkinter import messagebox as msg
import tkinter.font as font
import pandas as pd
from PIL import Image,ImageTk
import random

df = pd.read_csv("test.csv",names=["name","airlines","ticket_number","time","date","from","to"])

def main(user):
    r=Tk()

    r.state("zoomed")
    r.resizable(0,0)

    c = Canvas(r)
    file = Image.open("bg3.jpg")
    img = file.resize((r.winfo_screenwidth(),r.winfo_screenheight()),Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img,master=r)
    c.create_image(0,0, image=img,anchor="nw")

    f = Frame(highlightthickness=3,highlightbackground="black",bg="deep sky blue",padx=15,pady=15)

    c.create_window(r.winfo_screenwidth()/2,300,window=f)

    Label(f, text="From",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=0,row=0)
    Label(f, text="To",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=1,row=0)
    Label(f, text="Departure",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=2,row=0)
    Label(f, text="Return (optional)",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=3,row=0)
    Label(f, text="Airlines",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=4,row=0)

    fromm = Entry(f,font=font.Font(size=15))
    fromm.grid(column=0,row=1)
    to=Entry(f,font=font.Font(size=15))
    to.grid(column=1,row=1)

    f1 = Frame(f)
    day = IntVar()
    day.set(1)
    month = StringVar()
    month.set("Jan")
    l = OptionMenu(f1, day, *list(range(1,32)))
    l["font"] = ("Arial",13)
    l.grid(row=0,column=0)
    OptionMenu(f1, month, *["Jan","Feb"]).grid(row=0,column=1)
    f1.grid(row=1,column=2)

    f1 = Frame(f)
    aday = IntVar()
    aday.set(1)
    amonth = StringVar()
    amonth.set("Jan")
    l = OptionMenu(f1, aday, *list(range(1,32)))
    l["font"] = ("Arial",13)
    l.grid(row=0,column=0)
    l=OptionMenu(f1, amonth, *["Jan","Feb"])
    l["font"] = ("Arial",13)
    l.grid(row=0,column=1)
    f1.grid(row=1,column=3)

    airlines = StringVar()
    airlines.set("Qatar Airways")
    l=OptionMenu(f, airlines, *["Qatar Airways","British Airways"])
    l["font"] = ("Arial",13)
    l.grid(row=1,column=4)

    Label(f, text="Adults",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=0,row=2)
    Label(f, text="Children (0-12)",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=1,row=2)
    Label(f, text="Cabin Class",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=2,row=2)
    Label(f, text="Trip Type",padx=15,pady=5,font=font.Font(size=13,weight="bold"),bg="deep sky blue").grid(column=3,row=2)

    adults = IntVar()
    adults.set(1)
    l=OptionMenu(f, adults, *list(range(1,7)))
    l["font"] = ("Arial",13)
    l.grid(row=3,column=0)

    children = IntVar()
    children.set(0)
    l = OptionMenu(f, children, *list(range(0,7)))
    l["font"] = ("Arial",13)
    l.grid(row=3,column=1)

    classs = StringVar()
    classs.set("economy")
    l=OptionMenu(f, classs, *["economy","premium economy","bussiness","first"])
    l["font"] = ("Arial",13)
    l.grid(row=3,column=2)

    trip_type = StringVar()
    trip_type.set("one-way")
    l=OptionMenu(f, trip_type, *["one-way","round-trip"])
    l["font"] = ("Arial",13)
    l.grid(row=3,column=3)
    
    def conf():
        p = adults.get() + children.get()/2
        n=0
        t = 1
        #############
        if trip_type.get() == "round=trip":
            t = 1.7
        price = random.randrange(p*t-100,p*t)
        time = f"{random.randrange(1,12)}:{random.randrange(10,61)} am"
        date = f"{day.get()} {month.get()}"

        top = Toplevel()

        Label(top, font=font.Font(size=16,weight="bold"),padx=10,pady=10,text=f"{airlines.get()} flight found at {time} in {date}\n your total fare would be '${price}'\ enter your credit card number to finish booking\n").pack(pady=10)
        Entry(top,font=font.Font(size=14)).pack(pady=7)

        def book():
            number = f"E{random.randrange(10000,999999)}"
            email = "Ali@gmail.com"
            msg.showinfo(title="Booked!",message=f"Your Flight has been booked!\nticket-number:{number}\nticket has been sent to {email}")
            df.loc[int(len(df))] = [user,airlines.get().replace(" ","_"),number,time.replace(":","_"),date.replace(" ","_"),fromm.get(),to.get()]

        Button(top,command=book,font=font.Font(size=13),bg="green",fg="white",text="finish booking").pack(pady=5)

        top.mainloop()

    Button(f, command=conf,text="Check Available Flight",bg="green",fg="white",padx=15,pady=5,font=font.Font(size=13,weight="bold")).grid(column=4,row=3)

    def show():
        top = Toplevel()
        
        Label(top, text="My Bookings:",font=font.Font(size=18,weight="bold",underline=True)).pack(pady=15)

        if user in df["name"].values:
            pass
        else:
            Label(top, padx=10,text="Your bookings will appear here...",font=font.Font(size=13,slant="italic"))

        top.mainloop()

    b = Button(command=show,text="Show my flights",bg="purple",fg="white",padx=15,pady=5,font=font.Font(size=13,weight="bold"))
    c.create_window(600,450,window=b)

    b = Button(command=conf,text="Cancel my flight",bg="red",fg="white",padx=15,pady=5,font=font.Font(size=13,weight="bold"))
    c.create_window(800,450,window=b)

    def logout():
        r.destroy()
        login()

    b = Button(command=logout,text="Sign out",bg="grey",fg="white",padx=15,pady=5,font=font.Font(size=13,weight="bold"))
    c.create_window(1000,450,window=b)
    
    c.pack(fill=BOTH,expand=True)

    r.mainloop()
d={}

def register():
    a = Tk()
    rbimg = ImageTk.PhotoImage(file='bg_register.png')
    rbgr = Canvas(width=1000,height=629)
    rbgr.create_image(0,0,anchor='nw',image=rbimg)
    rbgr.create_text(500,60,text='Register',font=('Calibri',50))
    rbgr.create_text(500,140,text='Create your username:',font=('Calibri',10))
    runame = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    rbgr.create_window(500,170,window=runame)

    rbgr.create_text(500,220,text='Create your password:',font=('Calibri',10))
    rpass = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    rbgr.create_window(500,250,window=rpass)

    rbgr.create_text(500,300,text='Enter your passport number:',font=('Calibri',10))
    rp_no = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    rbgr.create_window(500,330,window=rp_no)

    rbgr.create_text(500,380,text='Enter your Email:',font=('Calibri',10))
    email = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    rbgr.create_window(500,410,window=email)

    rbgr.create_text(500,460,text='Enter your city:',font=('Calibri',10))
    city = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    rbgr.create_window(500,490,window=city)

    def reg():
        d[runame.get()] = {'password':rpass.get(),
                           'passport number':rp_no.get(),
                           'email address':email.get(),
                           'city':city.get()
            }
        msg.showinfo(title='success',message='account with username \''+runame.get()+'\' has been registered successfully')
        a.destroy()
        login()


    rbtn = Button(a,text='Register',padx=30,pady=15,command=reg,bg='yellow')
    rbgr.create_window(500,560,window=rbtn)

    def gotolog():
        a.destroy()
        login()

    rlbtn = Button(a,text='Sign In Instead',padx=25,pady=10,command=gotolog,bg='green',fg='white')
    rbgr.create_window(640,560,window=rlbtn)


    rbgr.pack(fill='both',expand='True')
    a.mainloop()
def login():
    a = Tk()
    lbimg = ImageTk.PhotoImage(file='bg_login.png')
    lbgr = Canvas(width=800,height=600)
    lbgr.create_image(0,0,anchor='nw',image=lbimg)
    lbgr.create_text(400,60,text='Sign In',font=('Calibri',60))
    lbgr.create_text(400,170,text='Enter your username:',font=('Calibri',15))
    luname = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    lbgr.create_window(400,200,window=luname)

    lbgr.create_text(400,270,text='Enter your password:',font=('Calibri',15))
    lpass = Entry(borderwidth=1,width=30,font=('Calibri',21),fg='grey')
    lbgr.create_window(400,300,window=lpass)

    def reg():
        if luname.get() in d:
            if d[luname.get()]['password'] == lpass.get():
                msg.showinfo(title="You are logged in!",message="You are logged in!")
                name = luname.get()
                a.destroy()
                main(name)
                
            else:
                msg.showerror(title='success',message='Username or password is incorrect')
        else:
                msg.showerror(title='success',message='Username or password is incorrect')

    lbtn = Button(a,text='SignIn',padx=30,pady=15,command=reg,bg='green',fg='white')
    lbgr.create_window(400,370,window=lbtn)

    def gotoreg():
        a.destroy()
        register()

    rlbtn = Button(a,text='Don\'t have an account',padx=25,pady=10,command=gotoreg,bg='yellow')
    lbgr.create_window(400,440,window=rlbtn)


    lbgr.pack(fill='both',expand='True')
    a.mainloop()


login()
