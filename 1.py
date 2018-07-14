print("Quetion1")
from tkinter import *
root = Tk()
root.geometry('800x250')
diict1 = {'riya' : '1234', 'gauri':'1235', 'anshul':'1236', 'meenal':'1237',
          'praneeta':'1238', 'anshika':'1239', 'raman':'1230', 'manoj':'234',
          'shweta':'5464', 'ishita':'8526', 'anju':'5454', 'vishal':'8546'}

def show_dict():
    sb = Scrollbar(root)
    sb.grid(row=4, column=1)
    myList = Listbox(root, yscrollcommand=sb.set)
    for i in diict1.keys():
        myList.insert(END,i)
    myList.grid(row=4, column=0)
    sb.configure(command=myList.yview)
B1 = Button(root, text='Show List', command=show_dict)
B1.grid(row=2, column=1)
print('*'*10)
print('\n')

print("Question2")
from tkinter import *
root = Tk()
diict2={}
def func():
    k=E1.get()
    v=E2.get()
    diict2[k]=v
def show2():
    sb = Scrollbar(root)
    sb.grid(row=4, column=6)
    mylist = Listbox(root, yscrollcommand=sb.set)
    for i in diict2.keys():
        mylist.insert(END,i)
    mylist.grid(row=4, column=5)
    sb.configure(command=mylist.yview)
L1 = Label(root, text='Name')
L2 = Label(root, text='Mobile_no')
L1.grid(row=0)
L2.grid(row=1)
E1 = Entry(root)
E1.grid(row=0, column=1)
E2 = Entry(root)
E2.grid(row=1, column=1)
B1 = Button(root, text='Add', command=func)
B1.grid(row=2)
B2 = Button(root, text='Show List', command=show2)
B2.grid(row=2, column=2)
root.mainloop()
