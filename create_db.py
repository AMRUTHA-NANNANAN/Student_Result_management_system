import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY ,name text,duration text,charges text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY ,name text,email text,gender text,course text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY ,roll text,name text,course text,mark_ob text,fullmark text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS register(eid INTEGER PRIMARY KEY ,f_name text,l_name text,contact text,email text,question text,answer text,password text)")
    con.commit()
     
    cur.execute("CREATE TABLE IF NOT EXISTS login(lid INTEGER PRIMARY KEY ,email text,password text)")
    con.commit() 
    
create_db()