from tkinter import *
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.title("Age Calculator")
root.geometry("300x300")

def calculate_age():
    try:
        birth_year = int(entry_year.get())
        birth_month = int(entry_month.get())
        birth_day = int(entry_day.get())
        
        today = datetime.today()
        
        birthdate = datetime(birth_year, birth_month, birth_day)
        age = today.year - birthdate.year
        
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1
            
        messagebox.showinfo("Age", f"Your age is: {age} years")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for year, month and date")
        
label_year = Label(root, text = "Year of Birth")
label_year.pack(pady=10)

entry_year = Entry(root)
entry_year.pack(pady=5)

label_month = Label(root, text = "Month of Birth")
label_month.pack(pady=10)

entry_month = Entry(root)
entry_month.pack(pady=5)

label_day = Label(root, text = "Day of Birth")
label_day.pack(pady=10)

entry_day = Entry(root)
entry_day.pack(pady=5)

calculate_button = Button(root, text = "Calculate Age", command = calculate_age)
calculate_button.pack(pady=20)

root.mainloop()