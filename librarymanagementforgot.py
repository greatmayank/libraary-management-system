from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors

def forget():
    nm=name.get()
    em=email.get()
    con=contact.get()
    conn=pymysql.connect(host='localhost',user='root',password='Mayank@123',db='book_library')
    a=conn.cursor()
    a.execute("select * from registration where name='"+nm+"' and email='"+em+"' and contact='"+con+"'")
    results=a.fetchall()
    count=a.rowcount
    print(results)
    print(count)
    if(count>0):
        for row in results:
            name.set(row[0])
            email.set(row[1])
            contact.set(row[2])
            messagebox.showinfo("password",row[1])
    else:
        print("no record found")
        messagebox.showinfo("message","wrong details")
    
win=Tk()
win.title("book library management")
win.config(bg="gray")

lb1=Label(win,text="BOOK  LIBRARY  MANAGEMENT",font=('arial',50,'bold'),bd=10,bg="white",width=45,relief="raised",justify='right')
lb1.grid(row=0,columnspan=6)

frame2=Frame(win,width=800,height=400,bg="yellow",highlightbackground="black",highlightthickness=5,bd=10,pady=20,padx=20,relief="raised")

lb2=Label(win,text="Forget Password",width=35,font=('arial',20,'bold'),bg="white",justify=CENTER)
lb2.place(x=500,y=150)

lb3=Label(win,text="Username",font=('arial',15,'bold'),width=10,bg="white",justify=LEFT)
lb3.place(x=520,y=230)
name=StringVar()
tb3=Entry(win,textvariable=name,bg="white",width=35)
tb3.place(x=900,y=230)

lb5=Label(win,text="Email-id",width=10,font=('arial',15,'bold'),bg="white",justify=LEFT)
lb5.place(x=520,y=280)
email=StringVar()
tb5=Entry(win,textvariable=email,bg="white",width=35)
tb5.place(x=900,y=280)

lb6=Label(win,text="Contact No.",width=10,font=('arial',15,'bold'),bg="white",justify=LEFT)
lb6.place(x=520,y=330)
contact=StringVar()
tb6=Entry(win,textvariable=contact,bg="white",width=35)
tb6.place(x=900,y=330)

btn=Button(win,text="Forget",command=forget,width=20,bg="white",font=('arial',20,'bold'),justify=CENTER)
btn.place(x=650,y=430)

frame2.place(x=400,y=125)



