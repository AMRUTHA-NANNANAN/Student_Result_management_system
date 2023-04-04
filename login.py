from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#0000A5")
        

       
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

       
        

        title=Label(login_frame,text="LOGIN HERE",padx=10,font=("times new roman",20,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        email=Label(login_frame,text="EMAIL ADDRESS",padx=10,font=("times new roman",15,"bold"),bg="white",fg="#08A3D2").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        
        pwd=Label(login_frame,text="PASSWORD",padx=10,font=("times new roman",15,"bold"),bg="white",fg="#08A3D2").place(x=250,y=250)
        self.txt_pwd=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pwd.place(x=250,y=300,width=350,height=35)
        

        self.btn_reg=Button(login_frame,text="Register new Account",font=("times new roman",12),cursor="hand2",command=self.register_win).place(x=250,y=350)
        self.btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),bg="#800857",fg="white",cursor="hand2",command=self.login1).place(x=250,y=400,width=180,height=40)
     
    def register_win(self):
        self.root.destroy()
        os.system("python register.py")

    def login1(self):
            if self.txt_email.get()=="" or self.txt_pwd.get()=="":
                 messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
            else:
                try:
                  con=sqlite3.connect(database="rms.db")
                  cur=con.cursor()
                  cur.execute("select * from register where email=? and password=?",(self.txt_email.get(),self.txt_pwd.get()))
                  row=cur.fetchone()
                  if row==None:
                     messagebox.showerror("Error","Invalid username or password",parent=self.root)
                     
                  else:    
                     
                     messagebox.showinfo("Success","Welcome",parent=self.root)
                     self.root.destroy()
                     os.system("python dashboard.py")
                     
                except Exception as ex:
                 messagebox.showerror("Error",f"Error due to {str(ex)}")      
  
                      
         

       


        
        


if __name__=="__main__":
    root =Tk()
    obj=Login(root)
    root.mainloop()