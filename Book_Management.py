import Database_Management as db #user defined file
import tkinter
from tkinter import messagebox

class UiSetup:
    def setup_ui(self,window,operation):
        frame = tkinter.Frame(window,bg="#0d0342")
        frame.place(x=500,y=180)
        row = 0
        tkinter.Label(window,text=operation,bg="#0d0342",fg='white',font=("Arial Black",30,'bold')).pack(pady=30)       
        for label,entry in self.ui_dict.items():
            tkinter.Label(frame,text=label,bg = "#0d0342",font=("Franklin Gothic",20,'bold'),fg='white').grid(row=row,column=0,pady=10)
            tkinter.Entry(frame,textvariable=entry,font=("Ink Free",15,'bold'),width=15).grid(row=row,column=1,padx=20)
            row += 1

    def add(self) -> None:
        book_details={
            "bno" : self.book_no.get(),
            "bname" : self.book_name.get(),
            "row" : self.book_row.get(),
            "col" : self.book_col.get()
        }
        db.insert_values(book_details,"Bookdatabase.db","Books")

    def get(self) -> None:
        column = ['bno','bname','row','col']
        datas = db.fetch_data(column,self.book_no.get(),'bno',"Bookdatabase.db","Books")
        db.update_data("acno","book",self.acno.get(),datas[1])
        db.update_data("acno","validity",self.acno.get())
        
    def renual(self) -> None:
        db.update_data("acno","validity",self.acno.get())

    def retun(self) -> None:
        db.update_data("acno","book",self.acno.get(),"N/A")
        db.update_data("acno","validity",self.acno.get(),"last_minute") 
        print(db.fetch_data(['acno','name','age','iam','address','phone','mail','login','book','validity'],self.acno.get(),)) 

    def search(self) -> None:
        datas = db.fetch_data(['bno','bname','row','col'],self.book_no.get(),"bno","Bookdatabase.db","Books")
        if not datas:
            return
        messagebox.showinfo(title="Location",message=f"The asked book can be find at \nrow={datas[2]}\ncolumn={datas[3]}")     

def setup_database(database,table,dcolumn) -> None:
    db.create_database(database,table,dcolumn)
    no_of_columns = int(input("Enter how many columns are going to enter: "))
    while (no_of_columns > 0):
        name = input("Enter column name: ")
        ctype = input("Enter column type: ")
        db.add_columns(name,ctype,database,table)
        no_of_columns -= 1

def add_book(window) -> None:
    for widget in window.winfo_children():
        if str(widget) == ".!menu":
            continue
        widget.destroy() 
    addui = UiSetup()
    addui.book_no,addui.book_name,addui.book_row,addui.book_col = tkinter.StringVar(),tkinter.StringVar(),tkinter.IntVar(),tkinter.IntVar()     
    addui.ui_dict={
            "Book No: " : addui.book_no,
            "Book Name: " : addui.book_name,
            "Row: " : addui.book_row,
            "Column: " : addui.book_col
        }
    addui.setup_ui(window,"Add Books")
    tkinter.Button(window,text="add",bg="#00ff86",fg='black',font=('Aharoni',15,'bold'),cursor='hand2',width=4,command=addui.add).place(x=650,y=450)    

def get_book(window) -> None:
    for widget in window.winfo_children():
        if str(widget) == ".!menu":
            continue
        widget.destroy()
    getui = UiSetup()
    getui.acno,getui.book_no = tkinter.StringVar(),tkinter.StringVar()
    getui.ui_dict={
        "Account No:" : getui.acno,
        "Book No:" : getui.book_no
    }        
    getui.setup_ui(window,"Get Books")  
    tkinter.Button(window,text="get",bg="#00ff86",fg='black',font=('Aharoni',15,'bold'),cursor='hand2',width=4,command=getui.get).place(x=650,y=450)    

def renual_book(window) -> None:
    for widget in window.winfo_children():
        if str(widget) != ".!menu":
            widget.destroy()
    renualui = UiSetup()
    renualui.acno,renualui.book_no = tkinter.StringVar(),tkinter.StringVar()
    renualui.ui_dict = {
        "Account No: " : renualui.acno,
        "Book No: " : renualui.book_no
    }        
    renualui.setup_ui(window,"Renual Book")
    tkinter.Button(window,text="renual",bg="#00ff86",fg='black',font=('Aharoni',15,'bold'),cursor='hand2',width=6,command=renualui.renual).place(x=650,y=450)    

def return_book(window) -> None:
    for widget in window.winfo_children():
        if str(widget) != ".!menu":
            widget.destroy()
    returnui = UiSetup()
    returnui.acno,returnui.book_no = tkinter.StringVar(),tkinter.StringVar()
    returnui.ui_dict = {
        "Account No: " : returnui.acno,
        "Book No: " : returnui.book_no
    }
    returnui.setup_ui(window,"Return Book")
    tkinter.Button(window,text="return",bg="#00ff86",fg='black',font=('Aharoni',15,'bold'),cursor='hand2',width=6,command=returnui.retun).place(x=650,y=450)    
            
def search_book(window) -> None:
    for widget in window.winfo_children():
        if str(widget) != ".!menu":
            widget.destroy()
    searchui = UiSetup()
    searchui.book_no,searchui.book_name = tkinter.StringVar(),tkinter.StringVar()
    searchui.ui_dict = {
        "Book No:" : searchui.book_no,
        "Book Name: " : searchui.book_name
    }        
    searchui.setup_ui(window,"Search Books")
    tkinter.Button(window,text="search",bg="#00ff86",fg='black',font=('Aharoni',15,'bold'),cursor='hand2',width=6,command=searchui.search).place(x=650,y=450)    

if __name__ == "__main__":
    database_name = "Bookdatabase.db"
    table_name = "Books"
    default_column = "bno"
    setup_database(database_name,table_name,default_column)    