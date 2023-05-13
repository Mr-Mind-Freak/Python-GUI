import tkinter as tk
import Database_Management as db

class OpenAccount:
    def __init__(self,window):
        input_frame = tk.Frame(window,bg='#0d0342')
        input_frame.pack(padx=30,pady=50,expand=True)
        OpenAccount.acno,OpenAccount.name,OpenAccount.book,OpenAccount.validity= tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
        row = 0
        ui_dict = {
            "Account No: " : OpenAccount.acno,
            "Name: " : OpenAccount.name,
            "Book He/She has:  " : OpenAccount.book,
            "Validity: " : OpenAccount.validity
        }
        for key,val in ui_dict.items():
            if key == "Account No: ":
                tk.Label(input_frame,text=key,font=('Franklin Gothic',25,'bold'),fg="white",\
                         bg='#0d0342').grid(row=row,column=0,pady=20)
                tk.Entry(input_frame,textvariable=val,bg='White',fg="black",width=15,font=('Ink Free',20,\
                                                    'bold')).grid(row=row,column=1,padx=10)
                tk.Button(input_frame,text="Open Account",bg='#00ff86',font=('Aharoni',15,'bold'),fg="black",\
                          relief=tk.RAISED,cursor="hand2",command = self.openac).grid(row=row+1,columnspan=2,pady=20)
                row += 1
            else:
                tk.Label(input_frame,text=key,font=('Franklin Gothic',25,'bold'),fg="white",textvariable=key,\
                         bg='#0d0342').grid(row=row,column=0,pady=20)
                tk.Label(input_frame,text=key,font=('Franklin Gothic',25,'bold'),fg="black",textvariable=val,\
                         width=15,bg='white').grid(row=row,column=1,pady=20)
            row+=1

    def openac(self):
        columns = ["name","book","validity"]
        data = db.fetch_data(columns,OpenAccount.acno.get())
        OpenAccount.name.set(data[0])
        OpenAccount.book.set(data[1])
        OpenAccount.validity.set(data[2])

def open_account(window):
    for widget in window.winfo_children():
       if str(widget) == '.!menu':
           continue
       widget.destroy()
    OpenAccount(window)