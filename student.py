from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1150x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()


        title=Label(self.root,text="Student Details",padx=10,compound=LEFT,font=("goudy old style",25,"bold"),bg="#0A0823",fg="white").place(x=0,y=0,relwidth=1,height=40)
        
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_course=StringVar()
        
        self.lbl_rollno=Label(self.root,text=" Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        self.lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)
        self.lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        self.lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=250)
        self.lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=300)


        self.course_list=[]
        self.fetch_course()

        self.txt_rollno=Entry(self.root,textvariable=self.var_rollno,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_rollno.place(x=150,y=60)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=120)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=180)        
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Female","Male","Other"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=250,width=200,height=30)
        self.txt_gender.current(0)

        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=150,y=300,width=200,height=30)
        self.txt_course.set("Select")



        
        self.btn1=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#FF0000",fg="white",cursor="hand2",command=self.add).place(x=20,y=420,width=150,height=40)
        self.btn2=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#006A80",fg="white",cursor="hand2",command=self.update).place(x=200,y=420,width=150,height=40)
        self.btn3=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.delete).place(x=380,y=420,width=150,height=40)
        self.btn4=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#004E38",fg="white",cursor="hand2",command=self.clear).place(x=560,y=420,width=150,height=40)
  

#==========================================================================================#
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=520,y=60,width=590,height=320)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)


        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","course"),xscrollcommand=scrollx.set,yscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll",text="Roll No")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        

        
#===============================================================#
    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.txt_gender.config(state=NORMAL)
     
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Rollno should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","please select the Rollno from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("delete","delete successfully",parent=self.root)
                        self.clear()



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            


    def get_data(self,ev):
                
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])

       


    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll No. name should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","Roll No. already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,course)values(?,?,?,?,?)",(
                        self.var_rollno.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_course.get()
                    ))  
                    con.commit()
                    messagebox.showinfo(" added successfully",parent=self.root)  
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","rollno should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","Select roll from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,course=? where roll=?",(
                        
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_course.get(),
                        self.var_rollno.get()
                    ))  
                    con.commit()
                    messagebox.showinfo("Course update successfully",parent=self.root)  
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")             


    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:  
         cur.execute("select * from student")
         rows=cur.fetchall()
         self.CourseTable.delete(*self.CourseTable.get_children())
         for row in rows:
             self.CourseTable.insert('',END,values=row)
                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def fetch_course(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to {str(ex)}")         
            
     
                    


if __name__=="__main__":
    root =Tk()
    obj=Student(root)
    root.mainloop()