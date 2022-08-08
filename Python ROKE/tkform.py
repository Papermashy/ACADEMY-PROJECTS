from tkinter import *
import sqlite3
import csv
from PIL import ImageTk, Image
import os

try:
    os.remove("people.db")
except:
    print("Tried to clear existing db, but one was not present.")

dbc = sqlite3.connect("people.db")
cur = dbc.cursor()
infile = open("MOCK_DATA.csv")

s = "create table if not exists persons(name text, email text)"
cur.execute(s)

for line in csv.reader(infile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    cur.execute("insert into persons values(?, ?)", line)
infile.close()
dbc.commit()

wnd = Tk()


def exit_program():
    exit()


def search_program():
    searchstring = fld1.get()
    try:
        fld3.delete(0, 'end')
        s2 = f"select name, email from persons where name like '{searchstring}'"
        cur.execute(s2)
        rs = cur.fetchall()
        #mem1.insert(END, str(rs))
        fld3.insert(END, str(rs[0][1]))
    except:
        print("This name is not in the DB")


def add_record():
    my_name = fld1.get()
    my_email = fld3.get()

    try:
        s3 = f"insert into persons (name, email) values ('{my_name}', '{my_email}')"
        print (s3)
        cur.execute(s3)
        dbc.commit()
        fld1.delete(0, END)
        fld3.delete(0, END)

    except:
        print("You must provide both a name and email")


def delete_record():
    my_name = fld1.get()
    my_email = fld3.get()

    try:
        s4 = f"delete from persons where name = '{my_name}' and email = '{my_email}'"
        cur.execute(s4)
        fld1.delete(0, END)
        fld3.delete(0, END)

    except:
        print("an error occurred")


def show_imge():
    image1 = Image.open("1.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.pack()


frame1 = Frame(wnd)
frame1.pack(side="top", padx=15, pady=15)

frame2 = Frame(wnd)
frame2.pack(side="top", padx=15, pady=15)

lbl1 = Label(frame1, text="First Name")
lbl1.pack()

fld1 = Entry(frame1, width=50, background="white")
fld1.pack()

lbl2 = Label(frame1, text="Last Name")
lbl2.pack()

fld2 = Entry(frame1, width=50, background="white")
fld2.pack()

lbl3 = Label(frame1, text="Email Address")
lbl3.pack()

fld3 = Entry(frame1, width=50, background="white")
fld3.pack()

btn1 = Button(frame2, text="Exit", command=exit_program)
btn1.pack(side="left")

btn2 = Button(frame2, text="Search", command=search_program)
btn2.pack(side="left")

# mem1 = Text(frame2, width=50)
# mem1.pack()

btn3 = Button(frame2, text="Add Record", command=add_record)
btn3.pack(side="left")

btn4 = Button(frame2, text="Delete Record", command=delete_record)
btn4.pack(side="left")

btn5 = Button(frame2, text="Show Image", command=show_imge)
btn5.pack(side="left")



wnd.mainloop()