from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

import sqlite3
class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1150x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()


        self.var_search=StringVar()

        title=Label(self.root,text="View Student Result",padx=10,compound=LEFT,font=("goudy old style",25,"bold"),bg="orange",fg="white").place(x=0,y=0,relwidth=1,height=40)
        self.lbl_search=Label(self.root,text="Search by Roll No.",font=("goudy old style",20,"bold"),bg="white").place(x=300,y=60)
        self.txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=550,y=60,width=200)
        self.btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#FF0000",fg="white",cursor="hand2",command=self.search).place(x=720,y=60,width=100,height=30)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="grey",fg="white",cursor="hand2").place(x=830,y=60,width=150,height=30)
        
        footer=Label(self.root,text="Remarks: >90=Outsatnding,  >80=Excellent,  >70=Very good,  >60=Average, <45=Failed",font=("goudy old style",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
    

        self.lbl_rollno=Label(self.root,text=" Roll No.",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        self.lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        self.lbl_course=Label(self.root,text="Cousre",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        self.lbl_mark_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        self.lbl_fullmark=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        self.lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)
        

        self.rollno=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.rollno.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.mark_ob=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.mark_ob.place(x=600,y=280,width=150,height=50)
        self.fullmark=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.fullmark.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        self.btn_del=Button(self.root,text="DELETE",font=("goudy old style",15,"bold"),bg="grey",fg="white",cursor="hand2").place(x=600,y=560,width=150,height=30)

    def search(self):
            con=sqlite3.connect(database='rms.db')
            cur=con.cursor()
            try:
                if self.var_search.get()=="":
                     messagebox.showerror("error","RollNo. is required",parent=self.root)
                else:
                     cur.execute("select * from result where roll=?",(self.var_search.get(),))
                     row=cur.fetchone()
                     if row!=None:
                        self.rollno.config(text=row[1])
                        self.name.config(text=row[2])
                        self.course.config(text=row[3])
                        self.mark_ob.config(text=row[4])
                        self.fullmark.config(text=row[5])
                        self.per.config(text=row[6])
                     else:    
                       messagebox.showinfo("Error","No record found",parent=self.root)
     
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")  


        



        
       


if __name__=="__main__":
    root =Tk()
    obj=Report(root)
    root.mainloop()