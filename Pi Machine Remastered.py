from tkinter import *
from tkinter import messagebox
import pyperclip



root = Tk() 

root.iconbitmap("favicon.ico")
root.title("Pi Machine Remastered")
root.geometry("300x350")
root.configure(bg="#202020")
root.resizable(False, False)



def clear():
    girinti1.delete(0,END)
    girinti2.delete(0,END)
    wequal.config(state=NORMAL)
    wequal.delete(0,END)
    wequal.config(state=DISABLED)



def copyier():
    pyperclip.copy(str(wequal.get()))



def pi():
    pyperclip.copy("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067")
    messagebox.showinfo("First 100 Digits","3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067 (copied to the clipboard)")



def add():
    while True:
        try:
            wequal.config(state=NORMAL)
            equal=float(girinti1.get())+float(girinti2.get())
            wequal.delete(0,END)
            wequal.insert(0,equal)
            wequal.config(state=DISABLED)
            break

        except:
            wequal.config(state=NORMAL)
            wequal.delete(0,END)
            wequal.insert(0,"Please Only Put Number(s)/Numeral(s)!")
            wequal.config(state=DISABLED)
            break
   


def subtract():
    while True:
        try:
            wequal.config(state=NORMAL)
            equal=float(girinti1.get())-float(girinti2.get())
            wequal.delete(0,END)
            wequal.insert(0,equal)
            wequal.config(state=DISABLED)
            break

        except:
            wequal.config(state=NORMAL)
            wequal.delete(0,END)
            wequal.insert(0,"Please Only Put Number(s)/Numeral(s)!")
            wequal.config(state=DISABLED)
            break

    

def multiply():
    while True:
        try:
            wequal.config(state=NORMAL)
            equal=float(girinti1.get())*float(girinti2.get())
            wequal.delete(0,END)
            wequal.insert(0,equal)
            wequal.config(state=DISABLED)
            break

        except:
            wequal.config(state=NORMAL)
            wequal.delete(0,END)
            wequal.insert(0,"Please Only Put Number(s)/Numeral(s)!")
            wequal.config(state=DISABLED)
            break



def divide():
    while True:
        try:
            wequal.config(state=NORMAL)
            equal=float(girinti1.get())/float(girinti2.get())
            wequal.delete(0,END)
            wequal.insert(0,equal)
            wequal.config(state=DISABLED)
            break

        except:
            wequal.config(state=NORMAL)
            wequal.delete(0,END)
            wequal.insert(0,"Please Only Put Number(s)/Numeral(s)!")
            wequal.config(state=DISABLED)
            break



copyrighto = Label(root, text="© Sourge 2022", font=("Arial", 10, 'italic'), fg="white", bg="#202020") 
copyrighto.place(x=200,y=317)

Ekle = Button(root, text="Add", command=add, width=24, bg="#3c3c3c", fg="white")
Ekle.place(x=20,y=143)

Cikar = Button(root, text="Subtract", command=subtract, width=10, bg="#3c3c3c", fg="white")
Cikar.place(x=202,y=143)

Carp = Button(root, text="Multiply", command=multiply, width=10, bg="#3c3c3c", fg="white")
Carp.place(x=20,y=178)

Bol = Button(root, text="Divide", command=divide, width=24, bg="#3c3c3c", fg="white")
Bol.place(x=104,y=178)

Cleara = Button(root, text="Clear", command=clear, width=36, height=2, bg="#3c3c3c", fg="white")
Cleara.place(x=20,y=213)

Pico = Button(root, text="π", font=("Consolas",14), command=pi, height=1, width=3, fg="dark orange", bg="#3c3c3c")
Pico.place(x=20,y=300)

girinti1 = Entry(root,width=43,bg="#6C6C6C")
girinti1.place(x=20,y=20)

girinti2 = Entry(root,width=43,bg="#6C6C6C")
girinti2.place(x=20,y=50)

wequal = Entry(root,width=29,bg="orange",state=DISABLED,disabledbackground="#3c3c3c",disabledforeground="white")
wequal.place(x=104,y=93)

wequalcopy = Button(root, width=10, height=1, text="Copy Result", bg="#3c3c3c", fg="white", command=copyier)
wequalcopy.place(x=20,y=90)



root = mainloop()