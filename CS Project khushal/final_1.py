from sqlite3.dbapi2 import Cursor
from tkinter import *
import mysql.connector as sqlcon
mycon=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
if mycon.is_connected():
    print("successfully connected to mysql database")

import tkinter.messagebox as MessageBox

def insert():
    StudentID=e_StudentID.get()
    Rollno=e_Rollno.get()
    StudentClass=e_StudentClass.get()

    if(StudentID=="" or Rollno=="" or StudentID==""):
        MessageBox.showinfo("Insert details , All fields are required")
    else:
       con=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
       Cursor = con.cursor()
       Cursor.execute("Insert into student values('"+StudentID+"','"+Rollno+"','"+StudentClass+"')")
       Cursor.execute("commit")

       e_StudentID.delete(0, 'end')
       e_Rollno.delete(0, 'end')
       e_StudentClass.delete(0, 'end')
       show()
       MessageBox.showinfo("Insert Status"," Inserted successfully ")
       con.close()

def delete():
    if(e_StudentID.get()==""):
        MessageBox.showinfo("Delete Status","Student is compalsary for delete")
    else:
       con=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
       Cursor = con.cursor()
       Cursor.execute("delete from student where ID='"+e_StudentID.get()+"'")
       Cursor.execute("commit")

       e_StudentID.delete(0, 'end')
       e_Rollno.delete(0, 'end')
       e_StudentClass.delete(0, 'end')
       show()
       MessageBox.showinfo("Delete Status"," Deleted successfully ")
       con.close()

def update():
    StudentID=e_StudentID.get()
    Rollno =e_Rollno.get()
    StudentClass=e_StudentClass.get()

    if(StudentID=="" or Rollno=="" or StudentID==""):
        MessageBox.showinfo("Update details , All fields are required")
    else:
       con=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
       Cursor = con.cursor()
       Cursor.execute("Update student set name='"+StudentID+"',Rollno='"+Rollno+"' ,StudentClass='"+StudentClass+"'")
       Cursor.execute("commit")

       e_StudentID.delete(0, 'end')
       e_Rollno.delete(0, 'end')    
       e_StudentClass.delete(0, 'end')
       show()
       MessageBox.showinfo("Update Status"," Updated successfully ")
       con.close()

def get():
   if(e_StudentID.get()==""):
        MessageBox.showinfo("Fetch Status","Student ID is compalsary for delete")
   else:
       con=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
       Cursor = con.cursor()
       Cursor.execute("Select * from xi where ID='"+e_StudentID.get()+"'")
       rows = Cursor.fetchall()

       for row in rows:
           e_Rollno.insert(0, row[1])
           e_StudentClass.insert(0, row[2])

       con.close() 

def show():
    con=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
    Cursor = con.cursor()
    Cursor.execute("Select * from xi")
    rows = Cursor.fetchall()
    list.delete(0, list.size()) 

    for row in rows:
        insertData = str(row[0])+'       '+str(row[1])
        list.insert(list.size()+1 , insertData)

    con.close() 


root =Tk()
root.geometry("600x500")
root.title('Student database management')
root.bg="yellow"

StudentID = Label(root,text='Enter student ID',font=('bold',10))
StudentID.place(x=20 , y=30)

Rollno = Label(root,text='Enter student Roll no.',font=('bold',10))
Rollno.place(x=20 , y=60)

StudentClass = Label(root,text='Enter student Class',font=('bold',10))
StudentClass.place(x=20 , y=90)

e_StudentID = Entry()
e_StudentID.place(x=150 , y=30)

e_Rollno = Entry()
e_Rollno.place(x=150 , y=60)

e_StudentClass = Entry()
e_StudentClass.place(x=150 , y=90)

insert = Button(root, text="Insert", font=("italic", 10), bg="cyan" ,fg="black" , command=insert)
insert.place(x=20 , y=140) 

delete = Button(root, text="Delete", font=("italic", 10), bg="cyan" ,fg="black" , command=delete)
delete.place(x=70 , y=140) 


update = Button(root, text="Update", font=("italic", 10), bg="cyan" ,fg="black" , command=update)
update.place(x=130 , y=140) 

get = Button(root, text="Get", font=("italic", 10), bg="cyan" ,fg="black" , command=get)
get.place(x=190 , y=140) 

list = Listbox(root)
list.place(x=290 , y=30)
show()

'''''
entry ke liye
e= Entry()
e.pack()
root.iconbitmap('C:\\Users\\24sai\\OneDrive\\Desktop\\201818')


def click1():
    thislabel = Label(root, text="Choose the student name")
    thislabel.pack()

#isme create karo
thislabel1= Label(root, text="student management system")
thisbutton= Button(root,text="get started" , padx=30, pady=30, command=click1
,bg="red" , fg="white" , borderwidth=2)

thisbutton.pack()
'''''



root.mainloop()
