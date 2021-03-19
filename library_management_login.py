from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors

def register():
    nm=name.get()
    pas=password.get()
    conn=pymysql.connect(host='localhost',user='root',password='Mayank@123',db='book_library')
    a=conn.cursor()
    a.execute("select * from registration where name='"+nm+"' and password='"+pas+"'")
    results=a.fetchall()
    count=a.rowcount
    print(results)
    print(count)
    if(count>0):
        print("record is found")
        wel=Tk()
        wel.config(bg="lime")
        win.title("login")
        win.geometry("400x400")
        lb1=Label(wel,text="welcome user",font=("gigi",20,"bold"),width=20,bd=10,relief="raised")
        lb1.grid(row=0,padx=40,pady=40)
                  
    else:
         print("no record found")
         messagebox.showerror("message","wrong details please check")
       

    
win=Tk()
win.title("book library management")
win.config(bg="gray")

lb1=Label(win,text="BOOK  LIBRARY  MANAGEMENT",font=('arial',50,'bold'),bd=10,bg="white",width=45,relief="raised",justify='right')
lb1.grid(row=0,columnspan=6)

frame2=Frame(win,width=800,height=300,bg="yellow",highlightbackground="black",highlightthickness=5,bd=10,pady=20,padx=20,relief="raised")

lb2=Label(win,text="Login/SignUp",width=35,font=('arial',20,'bold'),bg="white",justify=CENTER)
lb2.place(x=500,y=150)

lb3=Label(win,text="Username",font=('arial',15,'bold'),width=10,bg="white",justify=LEFT)
lb3.place(x=520,y=230)
name=StringVar()
tb3=Entry(win,textvariable=name,bg="white",width=35)
tb3.place(x=900,y=230)

lb4=Label(win,text="Password",width=10,font=('arial',15,'bold'),bg="white",justify=LEFT)
lb4.place(x=520,y=280)
password=StringVar()
tb4=Entry(win,textvariable=password,bg="white",width=35)
tb4.place(x=900,y=280)

btn=Button(win,text="Login",command=register,width=20,bg="white",font=('arial',20,'bold'),justify=CENTER)
btn.place(x=650,y=330)

frame2.place(x=400,y=125)



