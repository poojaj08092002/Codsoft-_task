from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector
def insertdata ():
    taskno1=tno.get()
    taskname1=tna.get()
    if(taskno1=="" or taskname1==""):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="list")
        cur = con.cursor()
        qry="insert into task(taskno,taskname)values(%s,%s);"
        cur.execute(qry,(taskno1,taskname1))
        cur.execute("commit")
        tno.delete(0, 'end')
        tna.delete(0, 'end')
        MessageBox.showinfo("insert status", "inserted successfully")
        con.close()
def deletedata():
    taskno1 = tno.get()
    if taskno1=="":
        MessageBox.showinfo("delete status","id field is required")
    else:
        con = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="list")
        cur = con.cursor()
        qry="delete from task where taskno=%s;"
        cur.execute(qry,(taskno1,))
        cur.execute("commit")
        tno.delete(0,'end')
        tna.delete(0,'end')
        MessageBox.showinfo("delete status", "deleted successfully")
        con.close()
def displaydata():
    con = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="list")
    cur = con.cursor()
    qry = "select * from task;"
    cur.execute(qry)
    rows=cur.fetchall()
    for row in rows:
        insertdata=str(row[0])+'     '+row[1]
        list.insert(list.size()+1,insertdata)
        print("-----------------------------")
    tno.delete(0, 'end')
    tna.delete(0, 'end')
    con.close()
task=Tk()
task.title("To Do List")
task.geometry("700x500")
title=Label(task,text="TO DO LIST",font=("bold",24))
title.place(x=140,y=10)
taskno1=Label(task,text="Enter your task number",font=("bold",10))
taskno1.place(x=80,y=70)
taskname1=Label(task,text="Enter your task name",font=("bold",10))
taskname1.place(x=80,y=120)
tno=Entry(bd=5)
tno.place(x=240,y=70)
tna=Entry(bd=5)
tna.place(x=240,y=110)
bt=Button(task,text="Add Task",font=("bold",10),bd=10,command=insertdata)
bt.place(x=70,y=170)
bt=Button(task,text="Delete Task",font=("bold",10),bd=10,command=deletedata)
bt.place(x=180,y=170)
bt=Button(task,text="Display Task",font=("bold",10),bd=10,command=displaydata)
bt.place(x=300,y=170)
list=Listbox(task,bd=10)
list.place(x=490,y=60)

task.mainloop()