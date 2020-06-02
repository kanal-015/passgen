from tkinter import *
import random,string

root=Tk()
root.geometry("400x400")
root.title("PASSWORD GENERATOR")

#intro text
title=StringVar()
label=Label(root,textvariable=title,fg="black",bg="skyblue",font=("Calibri",18,"bold")).pack()
title.set("Password Strength",)
def selection():
    selection=choice.get()

choice=IntVar()
R1=Radiobutton(root,text="POOR",variable=choice,value=1,command=selection,font=("Georgia",16)).pack(anchor=CENTER)
R2=Radiobutton(root,text="AVERAGE",variable=choice,value=2,command=selection,font=("Georgia",16)).pack(anchor=CENTER)
R2=Radiobutton(root,text="ADVANCED",variable=choice,value=3,command=selection,font=("Georgia",16)).pack(anchor=CENTER)
labelchoice=Label(root)
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("Password Length")
lentitle=Label(root,textvariable=lenlabel,font=(15)).pack()


val=IntVar()
spinlength=Spinbox(root,from_=8, to_=24,textvariable=val,width=13).pack()

def callback():
    lsum.config(text=passgen())

passgenButton=Button(root,text="Generate Password",bd=5,height=1,bg="HotPink4",font=("Segoe Print",17),command=callback,pady=3)
passgenButton.pack()
password=str(callback)

lsum=Label(root,text="")
lsum.pack(side=BOTTOM)

#logic
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits

symbols=""" '"!@~#$%^&*()_{}[];:.,<>?/\ """

advanced=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advanced,val.get()))

root.mainloop()
