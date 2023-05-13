import sqlite3, traceback,datetime
from tkinter import messagebox

def create_database(database_name="Userdatabase.db",table_name="User",default_column='acno'):  #dtype stands for data type
    """In this function we are going to create database and a table within the database"""
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        try:
            cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({default_column} TEXT PRIMARY KEY UNIQUE);")
            print(f"Table successfully created or already exists with column {default_column}")
            con.commit()
        except sqlite3.OperationalError as e:
            print("Unable to connect database or to create table")
            print(e)    
        cur.close()        

def column_list(database_name="Userdatabase.db",table_name="User",):
    """In this function we are going to return all the existing columns in the given table of given database"""
    with sqlite3.connect(database_name) as con:
        cur = con.cursor()
        cur.execute(f"pragma table_info ({table_name})") #This progma used to get the columns in the table
        con.commit()
        columns = [column[1] for column in cur.fetchall()]
        cur.close()
        return columns

def add_columns(column_name,column_type,database_name="Userdatabase.db",table_name="User"):
    """In this function we are going to add columns in the given table of given database"""
    if column_name in column_list(database_name,table_name):
        print(f"The column {column_name} is already exists in the {table_name} table")
        return
    else:
        try:
            with sqlite3.connect(database_name) as con:
                cur = con.cursor()
                cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name}  {column_type}")
                print(f"{column_name} is successfully added as a column into {table_name}")
                cur.close()
        except sqlite3.OperationalError as e:
            print("Unable to add column")
            print(e)   

def insert_values(val_dict,database_name="Userdatabase.db",table_name="User"):
    try:
        columns = column_list(database_name,table_name) #To get the columns in the data base
        data = [] #To store values which available in both columns and val_dict
        columns = [ x for x in columns if x in val_dict.keys()]#checking all the elements of columns has corresponding values in val_dict. if not then delete it
        for ele in columns:
            data.append(val_dict[ele])
        with sqlite3.connect(database_name) as con:
            cur = con.cursor()
            place_holders = "?,"*len(data)  # find the number of ? to use in query
            #The above variable contains , as last character so we wanna slice it
            query = f"insert into {table_name} ({','.join(columns)}) values ({place_holders[:-1]})"       
            cur.execute(query,data)
            con.commit()
            if table_name == "User":
                messagebox.showinfo(title="Status",message= "Account successfully created")
            elif table_name == "Books":
                messagebox.showinfo(title="status",message="Book successfully added into rack")    
            cur.close()
    except Exception as e:
        print(traceback.format_exc(),end="\n\n")
        print(e)
       
def fetch_data(column,key_value,default_column="acno",database_name="Userdatabase.db",table_name="User") -> list:
    """In this function,we're gonna fetch the datas from the given table with column lst and key value"""
    try:
        with sqlite3.connect(database_name) as con:
            cur = con.cursor()
            query = "select {col} from {tname} where {dcol} = {ac};".format(col = ",".join(column), tname = table_name,dcol=default_column,ac = key_value)
            cur.execute(query)
            con.commit()
            data = cur.fetchone()
            print(data)
            cur.close()
    except Exception as e:
        print(traceback.format_exc(),end="\n\n")
        print(e)
    return data    

def update_data(default_column,modify_column,key_value,data="",database_name='Userdatabase.db',table_name='User'):
    """ In this function we are going to update or insert values in existing row of a table"""
    if data == "":
        current_date = datetime.date.today()
        if modify_column == "validity":
            current_date = current_date + datetime.timedelta(days=15)
        current_date = current_date.strftime("%b-%d,%Y")
        data = current_date
    
    try:
        with sqlite3.connect(database_name) as con:
            cur = con.cursor()
            query = f"update {table_name} set {modify_column} = '{data}' where {default_column} = {key_value};"
            cur.execute(query)
            con.commit()
            if modify_column == "login":
                messagebox.showinfo(title= 'Status',message="Successfully Logged in :)")
            elif modify_column == "validity":
                messagebox.showinfo(title= 'Status',message=f"you can keep the book till {data}")
            else:
                messagebox.showinfo(title="Status",message="Value successfully added")    
            cur.close() 
    except Exception as e:
        print(traceback.format_exc(),end= "\n\n")
        print(e)       

def main():
    database_name = input("Enter your database name: ").title() + ".db"
    table_name = input("Enter your table name: ").title()
    create_database(database_name,table_name)
    no_of_columns = int(input("How many columns are you going to add: "))
    for column in range(no_of_columns):
        name = input(f"Enter {column+1} column name: ")
        dtype = input(f"Enter {column+1} column data type: ")
        add_columns(name,dtype,database_name,table_name,)
    print("columns of the table is:",column_list(database_name,table_name))

if __name__ == "__main__":
    main()