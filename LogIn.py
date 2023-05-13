import tkinter,traceback
import Database_Management as db #user defined file

def login(window):
    frame = tkinter.Frame(window,bg="#0d0342")
    frame.pack(padx=30,pady=50,expand=True)
    tkinter.Label(frame,text="LogIn",bg="#0d0342",font=("Franklin Gothic",25,'bold'),fg= '#f5024b').grid(row=0,columnspan=2)
    tkinter.Label(frame,text="Account No: ",bg="#0d0342",font=("Franklin Gothic",25,'bold'),fg= 'white').grid(row=1,column=0,pady=30)
    entry = tkinter.Entry(frame,font=("Ink Free",20,'bold'),width=10)
    entry.grid(row=1,column=1,padx=20)
    tkinter.Button(frame,text='LogIn',bg='#00ff86',cursor="hand2",relief=tkinter.RAISED,font=("Aharoni",15,'bold'),fg='black',command = lambda: db.update_data('acno','login',entry.get())).grid(row=2,columnspan=2,pady=30)

def login_account(window):
    for widget in window.winfo_children():
        if str(widget) == ".!menu":
            continue
        widget.destroy()
    login(window)    