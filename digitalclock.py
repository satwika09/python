from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("Clock")
def time():
    sr = strftime('%H : %M : %S %p')
    label.config(text=sr)
    label.after(1000,time)
label=Label(root,font=("fantasy",100),background="lightgray",foreground="slateblue")
label.pack(anchor='center')
time()
mainloop()