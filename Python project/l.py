from mutagen.mp3 import MPEGFrame
from pygame import error
from mpplayermain import *
from tkinter import *
from tkinter import messagebox
import mpplayer
import pyodbc
class Login:
    def __init__(self):
        self.conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-QKA9C3N;"
        "Database=Users;"
        "Trusted_Connection=yes;"
        )
        self.rootl=Tk()
        self.rootl.geometry("400x450")
        self.rootl.title("Login")
        l = PhotoImage(file="E:\Python project\login.png")
        Label(self.rootl,image=l).pack()
        self.fr = Frame(self.rootl)
        self.fr.pack()
        l1=Label(self.fr,text="Enter Username :")
        self.t1=Text(self.fr,height=1,width=50,fg="purple")
        l2=Label(self.fr,text="Enter Password :")
        self.t2=Entry(self.fr,width=65,fg="purple" ,show ="*")
        b1=Button(self.rootl,text="Login",command=self.login)
        b2=Button(self.rootl,text="make a new Account",command=self.newacc)
        b6=Button(self.rootl,text="Coutinue Without Logging in ",command=self.run)
        l1.grid(row=0,column=1,padx=10,pady=10)
        self.t1.grid(row=0,column=2,padx=10,pady=10)
        l2.grid(row=1,column=1,padx=10,pady=10)
        self.t2.grid(row=1,column=2,padx=10,pady=10)
        b1.pack(pady=10)
        b2.pack(pady=10)
        b6.pack(pady=10)

        self.rootl.mainloop()
    def login(self):
        username = self.t1.get("1.0","end-1c")
        password = self.t2.get()
        #password = Entry(self.rootl, show="*")
        if password == "" or username == "":
            messagebox.showerror("hii ","Please enter a valid username or password")
            print(self.t1.get("1.0","end-1c"))
        else:
            try:
                cursor = self.conn.cursor()
                username = self.t1.get("1.0","end-1c")
                password = self.t2.get()
                query= "SELECT * from Users where U_email = ? and U_pass = ?"
                cursor.execute(query,[(username),(password)])
                results = cursor.fetchall()
                if results :
                    for i in results:
                        self.rootl.destroy()
                        MPPlayer()
                        #messagebox.showinfo("Welcome to Music player","logged in ")
                        break
                else:
                        messagebox.showerror("Error ","Please enter a correct username or password")
            except Exception as e:
                print(e)
    def timep(self):
        contactnumber=self.t4.get("1.0","end-1c")
        if len(contactnumber)!=10:
            messagebox.showerror("Welcome to Music player "," please enter a valid mobile number and proper details")
        else:
            try:
                cursor = self.conn.cursor()
                name =self.t3.get("1.0","end-1c")
                cn = self.t4.get("1.0","end-1c")
                email = self.t5.get("1.0","end-1c")
                password = self.t6.get("1.0","end-1c")
                query = "INSERT INTO Users values (?,?,?,?)"
                cursor.execute(query,[email,name,cn,password])
                self.conn.commit()
                messagebox.showinfo("Welcome to Music player "," Account Created hurray :) ")
            except Exception as e:
                print(e)
            finally:
                self.conn.close()
    def newacc(self):
        self.rootl.destroy()
        self.rootn=Tk()
        self.rootn.geometry("400x550")
        self.rootn.title("New Registration")
        
        regis = PhotoImage(file="E:\Python project\mem.png")
        Label(self.rootn,image=regis).pack()
        self.f = Frame(self.rootn)
        self.f.pack()
        self.l3=Label(self.f,text="Enter Your name : ")
        self.t3=Text(self.f,height=1,width=17)
        self.l4=Label(self.f,text="Enter Your Contact number :")
        self.t4=Text(self.f,height=1,width=17) 
        self.l5=Label(self.f,text="Enter Your Email Address :")
        self.t5=Text(self.f,height=1,width=17)
        self.l6=Label(self.f,text="Enter new password :")
        self.t6=Text(self.f,height=1,width=17)
        b3=Button(self.rootn,text="Submit",command=self.timep)
        b4=Button(self.rootn,text="Back",command=self.back_l)
        self.l3.grid(row=0,column=1,padx=10,pady=10)
        self.t3.grid(row=0,column=2,padx=10,pady=10)
        self.l4.grid(row=1,column=1,padx=10,pady=10)
        self.t4.grid(row=1,column=2,padx=10,pady=10)
        self.l5.grid(row=2,column=1,padx=10,pady=10)
        self.t5.grid(row=2,column=2,padx=10,pady=10)
        self.l6.grid(row=3,column=1,padx=10,pady=10)
        self.t6.grid(row=3,column=2,padx=10,pady=10)
        b3.pack(pady=15)
        b4.pack(pady=10)
        self.rootn.mainloop()
    def back_l(self):
        self.rootn.destroy()
        self.__init__()
    def run(self):
        self.rootl.destroy()
        mpplayer.Player()
Login()
