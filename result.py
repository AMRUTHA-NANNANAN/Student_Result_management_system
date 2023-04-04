from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
class Result:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1150x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        imag=Image.open("PIC/Result2.jpg")
        image=imag.resize((500,350))
        self.logo_dash=ImageTk.PhotoImage(image)
        self.lbl_bg=Label(self.root,image=self.logo_dash).place(x=600,y=100)



        title=Label(self.root,text="Add Student Result",padx=10,compound=LEFT,font=("goudy old style",25,"bold"),bg="orange",fg="white").place(x=0,y=0,relwidth=1,height=40)
        self.var_rolln=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_mark_ob=StringVar()
        self.var_fullmark=StringVar()
        self.var_per=StringVar()
        self.var_res=StringVar()
        
        self.roll_list=[]
        self.fetch_roll()


        self.lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        self.lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)
        self.lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        self.lbl_mark_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=250)
        self.lbl_fullmark=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=320)
        


        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_rolln,values=self.roll_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=250,y=60,width=250)
        self.txt_student.set("Select")
        self.btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#FF0000",fg="white",cursor="hand2",command=self.search).place(x=530,y=60,width=150,height=30)


        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly')
        self.txt_name.place(x=250,y=120,width=300)
        self.txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow",state="readonly")
        self.txt_course.place(x=250,y=180,width=300)
        self.txt_mark_ob=Entry(self.root,textvariable=self.var_mark_ob,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_mark_ob.place(x=250,y=250,width=300)
        self.txt_fullmark=Entry(self.root,textvariable=self.var_fullmark,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_fullmark.place(x=250,y=320,width=300)
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++
        self.btnsub=Button(self.root,text="Submit",font=("goudy old style",15,"bold"),bg="light grey",fg="black",cursor="hand2",command=self.add).place(x=100,y=420,width=150,height=40)
        self.btnclr=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="light grey",fg="black",cursor="hand2").place(x=300,y=420,width=150,height=40)
       
       
#+++++++++++++++++++++++++++++++++++++++++==================================================#
    def fetch_roll(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to {str(ex)}")          



    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_rolln.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:    
             messagebox.showinfo("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")      

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","please search student record!",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_rolln.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","Result already present",parent=self.root)
                else:
                    per=(int(self.var_mark_ob.get())*100)/int(self.var_fullmark.get())
                    cur.execute("insert into result(roll,name,course,mark_ob,fullmark,per)values(?,?,?,?,?,?)",(
                        self.var_rolln.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_mark_ob.get(),
                        self.var_fullmark.get(),
                        str(per)
                    )) 
                    con.commit()
                    messagebox.showinfo("Result added successfully",parent=self.root)  
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")                             

    
if __name__=="__main__":
    root =Tk()
    obj=Result(root)
    root.mainloop()