from tkinter import *
from tkinter import messagebox
from people_project import Database
db=Database('d:/python/people_database.db')
win=Tk()
win.geometry('500x500')
win.title('Ayda Yaghooby')
win.config(bg='#EDF4AE')
#functions
def add_item(): 
    if ent_name.get()=='' or ent_lastname.get()=='' or ent_adress.get()=='' or ent_number.get()=='':
        messagebox.showerror('Empty field','None of fields can be empty')
        return
    db.insert(ent_name.get(),ent_lastname.get(),ent_adress.get(),ent_number.get())
    delete_entries()
    show_list()

def remove_item():
    global record
    result=messagebox.askyesno('deleting record','Are you sure you want to delete the selected record?')
    if result==True:
        index=lst_contacts.curselection()
        info=lst_contacts.get(index)
        record=info.split(',')
        print(record)
        db.remove(record[0])
        delete_entries()
        show_list()

def show_list():
    lst_contacts.delete(0,END)
    data=db.fetch()
    for rec in data:
        lst_contacts.insert(0,f'{rec[0]},{rec[1]},{rec[2]},{rec[3]},{rec[4]}')

def delete_entries():
    ent_name.delete(0,END)
    ent_lastname.delete(0,END)
    ent_adress.delete(0,END)
    ent_number.delete(0,END)
    ent_name.focus_set()

def selected_item(event):
    global record
    index=lst_contacts.curselection()
    info=lst_contacts.get(index)
    record=info.split(',')
    print(record)
    db.remove(record[0])
    delete_entries()
    ent_name.insert(END,record[1])
    ent_lastname.insert(END,record[2])
    ent_adress.insert(END,record[3])
    ent_number.insert(END,record[4])
   

def remove_item():
    result=messagebox.askyesno('deleting record','Are you sure you want to delete the selected record?')
    if result==True:
        print(record)
        db.remove(record[0])
        show_list()

def update():
    db.update(record[0],ent_name.get(),ent_lastname.get(),ent_adress.get(),ent_number.get())
    show_list()

def search():
    records=db.serach(ent_search.get())
    lst_contacts.delete(0,END)
    for srch in records:
        lst_contacts.insert(END,srch)
#Labels
lbl_name=Label(text='Name:',bg='#EDF4AE')
lbl_name.place(x=20,y=20)
lbl_lastname=Label(text='Lastname:',bg='#EDF4AE')
lbl_lastname.place(x=20,y=60)
lbl_adress=Label(text='Adress:',bg='#EDF4AE')
lbl_adress.place(x=250,y=20)
lbl_number=Label(text='Phone number:',bg='#EDF4AE')
lbl_number.place(x=250,y=60)
#Entries
ent_name=Entry()
ent_name.place(x=90,y=20)
ent_lastname=Entry()
ent_lastname.place(x=90,y=60)
ent_adress=Entry(width=30)
ent_adress.place(x=310,y=20)
ent_number=Entry(width=25)
ent_number.place(x=340,y=60)
ent_search=Entry(width=30)
ent_search.place(x=220,y=160)

#Buttons
btn_add=Button(text='Add',width=10,bg='#C2747F',command=add_item)
btn_add.place(x=10,y=105)
btn_show_list=Button(text='Show list',width=10,bg='#C2747F',command=show_list)
btn_show_list.place(x=10,y=155)
btn_delete=Button(text='Delete',width=10,bg='#C2747F',command=remove_item)
btn_delete.place(x=110,y=105)
btn_search=Button(text='Search',width=10,bg='#C2747F',command=search)
btn_search.place(x=110,y=155)
btn_update=Button(text='Update',width=10,bg='#C2747F',command=update)
btn_update.place(x=220,y=105)
btn_delete_entries=Button(text='Delete entries',width=10,bg='#C2747F',command=delete_entries)
btn_delete_entries.place(x=330,y=105)

#listbox_and_scrollbar
lst_contacts=Listbox(win,width=75,height=15)
lst_contacts.place(x=20,y=220)

scroll_contacts=Scrollbar(win)
scroll_contacts.place(x=455,y=225,height=235)

lst_contacts.config(yscrollcommand=scroll_contacts.set)


scroll_contacts.config(command=lst_contacts.yview)

lst_contacts.bind('<<ListboxSelect>>',selected_item)












win.mainloop()