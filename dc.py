from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Denomination Counter")
window.configure(bg= 'light blue')
window.geometry("650x400")

label1= Label(window, text= "Hey Useser! Welcome to Denomination Counter Application.",bg= 'light blue')

label1.place(relx= 0.5, y=340, anchor= CENTER)

def msg():
    MsgBox= messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()
button1= Button(window, text="Let's get started!", command= msg, bg= 'brown', fg= 'white')
button1.place(x=260, y=360)

def topwin():
    top= Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg= 'light grey')
    top.geometry("600x350+50+50")

    label= Label(top, text="enter total amount", bg='lightgrey')
    entry= Entry(top)
    lbl= Label(top, text="Here")