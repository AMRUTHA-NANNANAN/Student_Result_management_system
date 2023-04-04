from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class Course:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1150x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()


        title=Label(self.root,text="Course Details",padx=10,compound=LEFT,font=("goudy old style",25,"bold"),bg="#0A0823",fg="white").place(x=0,y=0,relwidth=1,height=40)
        
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charge=StringVar()
        
        self.lbl_course=Label(self.root,text=" Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        self.lbl_Duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)
        self.lbl_charge=Label(self.root,text="Charge",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        self.txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_course.place(x=150,y=60)
        self.txt_Duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=120)
        self.txt_charge=Entry(self.root,textvariable=self.var_charge,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=180)


        self.btn1=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#FF0000",fg="white",cursor="hand2",command=self.add).place(x=20,y=420,width=150,height=40)
        self.btn2=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#006A80",fg="white",cursor="hand2",command=self.update).place(x=200,y=420,width=150,height=40)
        self.btn3=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#00008B",fg="white",cursor="hand2",command=self.delete).place(x=380,y=420,width=150,height=40)
        self.btn4=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#004E38",fg="white",cursor="hand2",command=self.clear).place(x=560,y=420,width=150,height=40)



        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=520,y=60,width=590,height=320)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)


        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charge"),xscrollcommand=scrollx.set,yscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Course Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charge",text="Charges")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charge",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

        
#===============================================================#
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_charge.set("")
        self.var_duration.set("")
        self.txt_course.config(state=NORMAL)
        
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","please select the course from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("delete","delete successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            


    def get_data(self,ev):
        self.txt_course.config(state='readonly')
        self.txt_course
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charge.set(row[3])

       


    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","course name already present",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges)values(?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charge.get()
                    ))  
                    con.commit()
                    messagebox.showinfo("Course added successfully",parent=self.root)  
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=? where name=?",(
                        
                        
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.var_course.get()
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
         cur.execute("select * from course")
         rows=cur.fetchall()
         self.CourseTable.delete(*self.CourseTable.get_children())
         for row in rows:
             self.CourseTable.insert('',END,values=row)
                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

     
                    


if __name__=="__main__":
    root =Tk()
    obj=Course(root)
    root.mainloop()