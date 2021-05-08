from tkinter import *
from tkinter.messagebox import askokcancel
import sqlite3


def save_contact():
    name = contact_name.get()
    phone_no = phone.get()
    with sqlite3.connect('contacts.sqlite3') as conn:
        conn.cursor()
        command = "INSERT INTO Contacts VALUES(?, ?)"
        conn.execute(command, (name, phone_no))
        conn.commit()
        askokcancel("Contact Saved", "Contact Saved Successfully!")
    contact_name.delete(0, END)
    phone.delete(0, END)


screen = Tk()
screen.title("ContactBook")
screen.geometry("300x250")
Label(screen, text="- Contact Book -", fg="green", padx=7, pady=7,
      font="Calibri 20 italic underline").pack(padx=5, pady=7)

form = Frame(screen)

Label(form, text="Contact Name : ", ).pack()
contact_name = Entry(form, font="calibri 12")
contact_name.pack(padx=8, pady=5)

Label(form, text="Phone No. : ", ).pack()
phone = Entry(form, font="calibri 12")
phone.pack(padx=8, pady=5)

Button(form, text="Save", padx=15, command=save_contact).pack(padx=7, pady=12)

form.pack()
screen.mainloop()
