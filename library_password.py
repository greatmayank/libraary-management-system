from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors

def register():
    nm=name.get()
    pas=password.get()
    npas=Npassword.get()
    cpas=Cpassword.get()
    if(cpas==npas):
        try:
            conn=pymysql.connect(host='localhost',user='root',password='Mayank@123',db='book_library')
            a=conn.cursor()
            a.execute("update registration set password='"+npas+"' where name='"+nm+"' and password='"+pas+"'")
            conn.commit()
            print('save')
            messagebox.showinfo("message","password is changed successfully")
        except:
            conn.rollback()
            print('not update')
        conn.close()    
    else:
         messagebox.showerror("message","New password and confirm password are not same please check")
       

    
win=Tk()
win.title("book library management")
win.config(bg="gray")

lb1=Label(win,text="BOOK  LIBRARY  MANAGEMENT",font=('arial',50,'bold'),bd=10,bg="white",width=45,relief="raised",justify='right')
lb1.grid(row=0,columnspan=6)

frame2=Frame(win,width=800,height=450,bg="yellow",highlightbackground="black",highlightthickness=5,bd=10,pady=20,padx=20,relief="raised")

lb2=Label(win,text="Change Password",width=35,font=('arial',20,'bold'),bg="white",justify=CENTER)
lb2.place(x=500,y=150)

lb3=Label(win,text="Username",font=('arial',15,'bold'),width=15,bg="white",justify=LEFT)
lb3.place(x=520,y=230)
name=StringVar()
tb3=Entry(win,textvariable=name,bg="white",width=35)
tb3.place(x=900,y=230)

lb4=Label(win,text="old Password",width=15,font=('arial',15,'bold'),bg="white",justify=LEFT)
lb4.place(x=520,y=280)
password=StringVar()
tb4=Entry(win,textvariable=password,bg="white",width=35)
tb4.place(x=900,y=280)

lb5=Label(win,text="New Password",width=15,font=('arial',15,'bold'),bg="white",justify=LEFT)
lb5.place(x=520,y=330)
Npassword=StringVar()
tb5=Entry(win,textvariable=Npassword,bg="white",width=35)
tb5.place(x=900,y=330)

lb6=Label(win,text="Confirm Password",width=15,font=('arial',15,'bold'),bg="white",justify=LEFT)
lb6.place(x=520,y=380)
Cpassword=StringVar()
tb6=Entry(win,textvariable=Cpassword,bg="white",width=35)
tb6.place(x=900,y=380)

btn=Button(win,text="Change",command=register,width=20,bg="white",font=('arial',20,'bold'),justify=CENTER)
btn.place(x=650,y=430)

frame2.place(x=400,y=125)



