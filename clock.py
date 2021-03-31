# from tkinter import *
# from tkinter.ttk import *
# from time import strftime

# root=Tk()
# root.title("Clock")

# def time():
#     string=strftime('%H:%M:%S:%p')
#     label.config(text=string)
#     label.after((1000,time))


# label=Label(root,font=("Courier",80),background="black",foreground="cyan")
# label.pack(anchor='center')

# time()
# mainloop()


import time
from tkinter import *
root = Tk()
root.title("Clock")
root.geometry("450x300")
# root.resizable(1,1)
label = Label(root, font=("Courier", 50, 'bold'), bg="black", fg="red", bd =30)
label.grid(row =0, column=1)
label.pack(anchor='center')
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(1000, digitalclock)
digitalclock()
root.mainloop()