from tkinter import *

root = Tk()
root.title("Login App")
root.geometry("400x400")

frame = Frame(master = root, height = 200, width= 360, bg = "#9282cd")

lbl1 = Label(frame, text="Full Name", bg="#503d9a", fg="white", width=12)
lbl2 = Label(frame, text="Email ID", bg="#503d9a", fg="white", width=12)
lbl3 = Label(frame, text="Enter Password", bg="#503d9a", fg="white", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="👨🏿")

def display():
    name = name_entry.get()
    greet = f"Hello {name}!\n"
    message = "Congratulations for your new account."
    textbox.insert(END, greet)
    textbox.insert(END, message)
    
textbox = Text(bg="#BEBEBE", fg = "black")
btn = Button(text="Create Account", command = display, bg="pink")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()