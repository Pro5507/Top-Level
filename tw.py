from tkinter import *
window= Tk()
window.geometry("600x600")
window.title("Main  Window")

def topwin():
    top= Toplevel()
    top.geometry("300x300")
    top.title("Top Window")
    l2= Label(top, text="This is top level window")
    l2.pack()
    top.mainloop()
l= Label(window, text="This is main window")
btn= Button(window, text="Click hear to open another window", command=topwin)
l.pack()
btn.pack()
window.mainloop()