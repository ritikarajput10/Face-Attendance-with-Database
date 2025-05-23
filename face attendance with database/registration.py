

from tkinter import *
import sqlite3

import tkinter as tk
from tkinter import messagebox as ms

from PIL import Image , ImageTk     


root = Tk()
root.geometry('700x600')
root.title("Registration Form")



image2 =Image.open('m.jpg')
image2 =image2.resize((700,700), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

Name=StringVar()
LastName=StringVar()
Address = StringVar()
status1=StringVar()
Mobile= StringVar()

def database():
   
   name = Name.get()
   lastname = LastName.get()
   address = Address.get()
   status = status1.get()
   mobileno = Mobile.get()
   conn = sqlite3.connect('face.db')
   
   
   # validation
   if (name.isdigit() or (name == "")):
       ms.showinfo("Message", "please enter valid name")
   elif (lastname.isdigit() or (lastname == "")):
       ms.showinfo("Message", "please enter valid lastname")
   
   elif (address == ""):
       ms.showinfo("Message", "Please Enter valid Address")
   elif (status == ""):
       ms.showinfo("Message", "Please Enter valid Status")
   elif((len(str(mobileno)))<10 or len(str((mobileno)))>10):
       ms.showinfo("Message", "Please Enter 10 digit mobile number")
   
   
   
   
   
   else:
       with conn:
          cursor=conn.cursor()
      # cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
       cursor.execute('INSERT INTO User (Name,Lastname,Address,Status,Mobileno) VALUES(?,?,?,?,?)',(name,lastname,address,status,mobileno))
       conn.commit()
       ms.showinfo('Success','User Registered Successfully.........')
       root.destroy()

def display():
    
##### tkinter window ######
    
    print("Display.....")
    from subprocess import call
    call(["python", "display.py"])   
             
label_0 = Label(root, text="Registration Form",width=25,font=("bold", 22),fg="#FF8040",bg="black")
label_0.place(x=150,y=50)




label_1 = Label(root, text="Name",width=25,font=("bold", 10))
label_1.place(x=150,y=130)

entry_1 = Entry(root,textvar=Name,width=25,font=("bold", 10))
entry_1.place(x=380,y=130)

label_2 = Label(root, text="Last Name",width=25,font=("bold", 10))
label_2.place(x=150,y=180)

entry_2 = Entry(root,textvar=LastName,width=25,font=("bold", 10))
entry_2.place(x=380,y=180)

label_3 = Label(root, text="Address",width=25,font=("bold", 10))
label_3.place(x=150,y=230)

entry_3 = Entry(root,textvar=Address,width=25,font=("bold", 10))
entry_3.place(x=380,y=230)

label_4 = Label(root, text="Status",width=25,font=("bold", 10))
label_4.place(x=150,y=280)

entry_3 = Entry(root,textvar=status1,width=25,font=("bold", 10))
entry_3.place(x=380,y=280)

label_5 = Label(root, text="Mobile No",width=25,font=("bold", 10))
label_5.place(x=150,y=330)

entry_5 = Entry(root,textvar=Mobile,width=25,font=("bold", 10))
entry_5.place(x=380,y=330)

Button(root, text='Submit',width=25,bg='red',fg='white',command=database).place(x=150,y=380)

Button(root, text='Display',width=25,bg='red',fg='white',command=display).place(x=375,y=380)

root.mainloop()



