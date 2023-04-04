
import os
from tkinter import*

from PIL import Image,ImageTk
from course import Course
from student import Student
from result import Result
from report import Report
from tkinter import messagebox
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1450x800+0+0")
        self.root.config(bg="white")


        imag=Image.open("PIC/logo1.png")
        image=imag.resize((60,60))
        self.logo_dash=ImageTk.PhotoImage(image)

        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",40,"bold"),bg="#0A0823",fg="white").place(x=0,y=0,relwidth=1,height=60)
        
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",20),bg="white")
        M_Frame.place(x=10,y=70,width=1430,height=90)

        btn1=Button(M_Frame,text="COURSE",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn2=Button(M_Frame,text="STUDENT",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn3=Button(M_Frame,text="RESULT",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn4=Button(M_Frame,text="VIEW STUDENT RESULT",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=250,height=40)
        btn5=Button(M_Frame,text="LOGOUT",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.logout).place(x=950,y=5,width=200,height=40)
        btn6=Button(M_Frame,text="EXIT",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.exit).place(x=1170,y=5,width=200,height=40)
        
        footer=Label(self.root,text="Student Result Management System\n Contact Us for any Technical issue:96xxxxxx0,96000542XX0,938827XXXX90",font=("goudy old style",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
    
       


        self.bg_image=Image.open("PIC/4.png")
        self.bg_image=self.bg_image.resize((920,350))
        self.bg_image=ImageTk.PhotoImage(self.bg_image)
        self.bg=Label(self.root,image=self.bg_image).place(x=450,y=180,width=920,height=550)
        
        self.lbl_course=Label(self.root,text="Total Course\n[0]",font=("goudy old style",15,"bold"),bd=10,relief=RIDGE,bg="#006A80").place(x=450,y=625,width=300,height=100)
        self.lbl_course=Label(self.root,text="Total Student\n[0]",font=("goudy old style",15,"bold"),bd=10,relief=RIDGE,bg="#FF0000").place(x=770,y=625,width=300,height=100)
        self.lbl_course=Label(self.root,text="Total Result\n[0]",font=("goudy old style",15,"bold"),bd=10,relief=RIDGE,bg="#004E38").place(x=1090,y=625,width=300,height=100)
        
        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Course(self.new_win)  

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Student(self.new_win)   

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Result(self.new_win) 
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Report(self.new_win) 
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really wants to logout?",parent=self.root)   
        if op==TRUE:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm","Do you really wants to Exit?",parent=self.root)   
        if op==TRUE:
            self.root.destroy()
            os.system("python login.py")
        

if __name__=="__main__":
    root =Tk()
    obj=RMS(root)
    root.mainloop()

