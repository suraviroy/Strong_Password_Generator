from tkinter import *
import random 
from random import randint
import time
from plyer import notification

root=Tk()
root.title('Password Generator')
root.config(bg='blue')
root.geometry("600x450")
#my_password= chr(randint(33,126))

def new_rand():
    pw_entry.delete(0,END)
    pw_id=(my_entry.get())
    pw_key=(my_entryy.get())
    characters = pw_id+pw_key
    num1 = len(pw_id)
    num2 = len(pw_key)
    password_length = num1+num2



    password = ""   

    for index in range(password_length):
        password = password + random.choice(characters)

    pw_entry.insert(0,password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    notification.notify(
        #title = "Password Generator",
        message = "Copied to clipboard",
        timeout=5
    )

lf=LabelFrame( root, text="Enter User Id",font=("Times",14,"bold"))
lf.pack(pady=10)
lff=LabelFrame( root, text="Enter Key",font=("Times",14,"bold"))
lff.pack(pady=20)
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack (pady=20, padx=20)
pw_entry = Entry(root, text=' ' , font=("Helvetica",24))
pw_entry.pack(pady=20)
my_frame = Frame(root)
my_frame.pack(pady=0)


my_entryy = Entry(lff, font=("Helvetica", 24))
my_entryy.pack (pady=20, padx=20)
pw_entryy = Entry(root, text=' ' , font=("Helvetica",24))



my_button=Button (my_frame, text="Generate Strong passoward",font=("Times",16,"bold"),highlightthickness=5,highlightcolor="black",command=new_rand)
my_button.grid(row=0,column=0,padx=0)

clip_button=Button(my_frame,text="Copy to Clipboard",font=("Times",16,"bold"),highlightthickness=5,highlightcolor='black',command=clipper)
clip_button.grid(row=0,column=2,padx=0)
root.mainloop()
