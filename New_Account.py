import tkinter as tk
from tkinter import messagebox
import Database_Management as db #importing user defined package for database manipulation

class NewAccount():
    def __init__(self,window):
        pic_frame = tk.Frame(window,bg='red',height=500,width=600)
        pic_frame.grid(row=0,column=0,pady=30,padx=30)
        pic = tk.PhotoImage(file="new_account_image.png")
        pic_label = tk.Label(pic_frame,bg="#0d0342",image = pic)
        pic_label.image = pic
        pic_label.pack()
        detail_frame = tk.Frame(window,height=500,width=600,bg='#0d0342')
        detail_frame.grid(row=0,column=1)
        NewAccount.acno,NewAccount.name,NewAccount.address,NewAccount.phone,NewAccount.mail,NewAccount.age,NewAccount.iam_val = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
        NewAccount.iam_val.set('Teacher   ')
        row = 0
        detail_dict = {
            "Account No: " : NewAccount.acno,
            "Name: " : NewAccount.name,
            "Age: " : NewAccount.age,
            "I am: " : NewAccount.iam_val,
            "Address: " : NewAccount.address,
            "Phone No: " : NewAccount.phone,
            "Mail Id: " : NewAccount.mail
        }
        rbutton_lst = ['Student   ','Teacher   ','Researcher','Citizen   ']
        for label,entry in detail_dict.items():
            if label == "Age: ":
                tk.Label(detail_frame,text=label,bg='#0d0342',fg='white',font=('Franklin Gothic',25,\
                        'bold')).grid(row=row,column=0,sticky= tk.N + tk.E + tk.S + tk.W,padx=10,pady=10)
                tk.Scale(detail_frame,from_=10,to=75,orient=tk.HORIZONTAL,bg='#0d0342',variable=entry,\
                        font=('Arial',20,'bold'),activebackground='green',\
                        fg='white').grid(row=row,column=1,sticky= tk.N + tk.E + tk.S + tk.W,padx=10,pady=10)
                row = row+1 
                continue
            elif label == "I am: ":
                tk.Label(detail_frame,text=label,bg='#0d0342',fg='white',font=('Franklin Gothic',25,\
                            'bold')).grid(row=row,column=0,sticky= tk.N + tk.E + tk.S + tk.W,padx=10,pady=10)
                iam_frame = tk.Frame(detail_frame,bg='#0d0342')
                for val in rbutton_lst:
                    tk.Radiobutton(iam_frame,text=val,fg='black',value=val,variable=entry,bg='#0d0342',font=('Arial',12,'bold')).pack(side=tk.LEFT)
                iam_frame.grid(row=row,column=1)
                row = row+1 
                continue
            else:
                tk.Label(detail_frame,text=label,bg='#0d0342',fg='white',font=('Franklin Gothic',25,'bold')).grid(row=row,column=0,sticky= tk.N + tk.E + tk.S + tk.W,padx=10,pady=10)
                tk.Entry(detail_frame,font=('Ink Free',20,'bold'),textvariable=entry).grid(row=row,column=1,sticky= tk.N + tk.E + tk.S + tk.W,padx=10,pady=10)
            row = row+1        
        tk.Button(detail_frame,text = "Create Account",bg='#00ff86',font=('Aharoni',15,'bold'),width=14,relief = tk.RAISED,cursor = 'hand2',command=self.connect_to_database).grid(row=row,column=1,columnspan=2,padx=10,pady=20)    

    def connect_to_database(self,*args):
        val_dict = {
            "acno" : NewAccount.acno.get(),
            "name" : NewAccount.name.get(),
            "age" : NewAccount.age.get(),
            "iam" : NewAccount.iam_val.get().strip(),
            "address" : NewAccount.address.get(),
            "phone" : NewAccount.phone.get(),
            "mail" : NewAccount.mail.get(),
        }
        db.insert_values(val_dict)
        NewAccount.acno.set("")
        NewAccount.name.set("")
        NewAccount.age.set(20)
        NewAccount.address.set("")
        NewAccount.iam_val.set('Student   ')
        NewAccount.phone.set("")
        NewAccount.mail.set("")

def create_new_account(window):
    for widget in window.winfo_children():
       if str(widget) == '.!menu':
           continue
       widget.destroy()
    NewAccount(window)   