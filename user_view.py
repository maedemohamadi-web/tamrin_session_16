from user_controller import UserController
from user import *
from tkinter import *
from tkinter import messagebox, StringVar
from tkinter import ttk

controller = UserController()

def save_click():
    success, message = controller.save(User.name.get(), User.family.get(), User.the_national_id.get(), User.birth_date.get(), User.the_phone_number.get(), User.user_name.get(), User.password.get(), User.role.get())
    if success:
        messagebox.showinfo("User Save", message)
    else:
        messagebox.showerror("User Save Error", message)

def edit_click():
    success, message = controller.edit(User.name.get(), User.family.get(), User.the_national_id.get(), User.birth_date.get(), User.the_phone_number.get(), User.user_name.get(), User.password.get(), User.role.get())
    if success:
        messagebox.showinfo("User Edit", message)
    else:
        messagebox.showerror("User Edit Error", message)


def delete_click():
    success, message = controller.delete(User.the_national_id.get())
    if success:
        messagebox.showinfo("User Delete", message)
    else:
        messagebox.showerror("User Delete Error", message)


win = Tk()
win.geometry("1200x650")
win.title("Users")

#Name
User.name = StringVar()
Label(win, text="Name").place(x=10, y=20)
Entry(win, textvariable=User.name).place(x=100, y=20)

#Family
User.family = StringVar()
Label(win, text="Family").place(x=10, y=60)
Entry(win, textvariable=User.family).place(x=100, y=60)

# The_National_Id
User.the_national_id = StringVar()
Label(win, text="National Id").place(x=10, y=100)
Entry(win, textvariable=User.the_national_id).place(x=100, y=100)

# Birth_date
User.birth_date = StringVar()
Label(win, text="Birth Date").place(x=10, y=140)
Entry(win, textvariable=User.birth_date).place(x=100, y=140)

# The_phone_number
User.the_phone_number = StringVar()
Label(win, text="Phone Number").place(x=10, y=180)
Entry(win, textvariable=User.the_phone_number).place(x=100, y=180)

# Username
User.user_name = IntVar()
Label(win, text="Username").place(x=10, y=220)
Entry(win, textvariable=User.user_name).place(x=100, y=220)


# Password
User.password = StringVar()
Label(win, text="Password").place(x=10, y=260)
Entry(win, textvariable=User.password).place(x=100, y=260)

# Role
User.role= StringVar()
Label(win, text="Role").place(x=10, y=300)
Entry(win, textvariable=User.role).place(x=100, y=300)


Button(win, text="Save", width=7,command= save_click).place(x=20,y=500)
Button(win, text="Edit", width=7,command= edit_click).place(x=87,y=500)
Button(win, text="Delete", width=7,command= delete_click).place(x=154,y=500)

table = ttk.Treeview(
    win,
    columns=(1,2,3,4,5,6,7,8),
    show="headings",
)

table.heading(1, text="Name")
table.heading(2, text="Family")
table.heading(3, text="National Id")
table.heading(4, text="Birth Date")
table.heading(5, text="Phone Number")
table.heading(6, text="Username")
table.heading(7, text="Password")
table.heading(8, text="Role")

table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=125)
table.column(4, width=125)
table.column(5, width=125)
table.column(6, width=100)
table.column(7, width=100)
table.column(8, width=100)

table.place(x=300, y=60)

win.mainloop()
