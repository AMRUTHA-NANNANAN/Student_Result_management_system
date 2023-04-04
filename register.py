import os
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        imag=Image.open("PIC/reg4.jpg")
        image=imag.resize((1350,700))
        self.logo_dash=ImageTk.PhotoImage(image)
        bg=Label(self.root,image=self.logo_dash).place(x=250,y=0,relwidth=1,relheight=1)
        

        image=Image.open("PIC/left.jpg")
        img=image.resize((450,550))
        self.left=ImageTk.PhotoImage(img)
        lft=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)


        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",padx=10,font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        
        

        f_name=Label(frame1,text="First Name",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
            
        l_name=Label(frame1,text="Last Name",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
#----------------------------------------------------------
        contact=Label(frame1,text="Contact",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
            
        l_email=Label(frame1,text="Email",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
 #----------------------------------------------------------
       
        question=Label(frame1,text="Security Question",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=240)
        self.cm_quest=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)
        self.cm_quest['values']=("Select","your first pet name","your birth place","your best friends name")
        self.cm_quest.place(x=50,y=270,width=250) 
        self.cm_quest.current(0)
            
        

        answer=Label(frame1,text="Answer",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)       
        
        self.password=Label(frame1,text="Password",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
            
        self.cpassword=Label(frame1,text="Confirm Password",padx=10,font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms and Conditions",onvalue=1,offvalue=0,variable=self.var_chk,bg="white",font=("times new roman",12)).place(x=50,y=380)

        img=Image.open("PIC/btn2.jpeg")
        image=img.resize((200,55))
        self.btn_img=ImageTk.PhotoImage(image)
        self.btn_reg=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=60,y=420)


    def login_window(self):
         self.root.destroy()
         os.system("python login.py")
    def clear(self):
         self.txt_fname.delete(0,END)
         self.txt_lname.delete(0,END)
         self.txt_contact.delete(0,END)
         self.txt_email.delete(0,END)
         self.txt_answer.delete(0,END)
         self.txt_password.delete(0,END)
         self.txt_cpassword.delete(0,END)

         
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email.get()=="" or self.cm_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
                messagebox.showerror("Error","All Feild Are Required",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
              messagebox.showerror("Error","Password and confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
             messagebox.showerror("Error","Please agree to terms and conditions",parent=self.root)
        else:
            try:
                  con=sqlite3.connect(database="rms.db")
                  cur=con.cursor()
                  cur.execute("select * from register where email=?",(self.txt_email.get(),))
                  row=cur.fetchone()
                  if row!=None:
                     messagebox.showerror("Error","User Already exist,Please try another Email",parent=self.root)
                  else:    
                     cur.execute("insert into register(f_name,l_name,contact,email,question,answer,password)values(?,?,?,?,?,?,?)",(
                       self.txt_fname.get(),
                       self.txt_lname.get(),
                       self.txt_contact.get(),
                       self.txt_email.get(),
                       self.cm_quest.get(),
                       self.txt_answer.get(),
                       self.txt_password.get(),))
                  con.commit()
                  con.close()
                  messagebox.showinfo("Success","Register Successful",parent=self.root)
                  self.clear()
                  self.login_window()
                  
       
           
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")      

    
if __name__=="__main__":
    root =Tk()
    obj=Register(root)
    root.mainloop()
        
