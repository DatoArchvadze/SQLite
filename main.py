import sqlite3
connection=sqlite3.connect('Database.db')
cursor=connection.cursor()

def remove_table():
    try:
        table_name=str(input("please enter table name to remove it -->".title()).strip().lower())
        query = "DELETE TABLE {} ".format(table_name)
        cursor.execute(query)
    except:
        print("this table does not exist in this database".title())


table_name=""
def create_new_table():
#------------get correct inputs--------------
    global table_name
    def get_table_name():
        global table_name
        table_name=str(input("please enter table name to create it \n !!!Note that SPACES CANNOT BE USED IN NAME --> ".title()).strip().lower())
    get_table_name()
    while table_name.isalpha() != True:
        print("--------enter valid name-------".strip())
        get_table_name()


    try:
        def set_colums_range():
            global table_columns
            table_columns=int(input("Select the number of columns max 6 and min 2  -->"))

    except:
        print("---------please enter number not text---------")
        set_colums_range()

#---------------------------------------------

    structure = []
#--------check table_columns range----------
    set_colums_range()
    while True:
        if table_columns > 6 or table_columns < 2:
            print("  ---------please select correct number----------".strip())
            set_colums_range()
        elif table_columns <= 6:
            break
#-------------------------------------------


# -----------QUARY FORMATING-------------
    for i in range(0,table_columns):
        column_name = input(f"Select the name of {i+1}th  column --> ").strip()
        column_type = input(f"Select the type of {i+1}th  column  \n !!!NOTICE  type 'text' or 'integer'--> ").strip()
        while column_type !="integer" and column_type !="text":
            column_type = input(f"Select the type of {i + 1}th  column  \n !!!NOTICE  type 'text' or 'integer'--> ").strip()

        structure.append(column_name)
        structure.append(column_type)

    if table_columns == 2:
        query = f"CREATE TABLE {table_name}({structure[0]} {structure[1]}, {structure[2]} {structure[3]})"
        cursor.execute(query)
    elif table_columns == 3:
        query = f"CREATE TABLE {table_name}({structure[0]} {structure[1]}, {structure[2]} {structure[3]},{structure[4]} {structure[5]})"
        cursor.execute(query)
    elif table_columns == 4:
        query = f"CREATE TABLE {table_name}({structure[0]} {structure[1]}, {structure[2]} {structure[3]},{structure[4]} {structure[5]},{structure[6]} {structure[7]})"
        cursor.execute(query)
    elif table_columns == 5:
        query = f"CREATE TABLE {table_name}({structure[0]} {structure[1]}, {structure[2]} {structure[3]},{structure[4]} {structure[5]},{structure[6]} {structure[7]},{structure[8]} {structure[9]})"
        cursor.execute(query)
    elif table_columns == 6:
        query = f"CREATE TABLE {table_name}({structure[0]} {structure[1]}, {structure[2]} {structure[3]},{structure[4]} {structure[5]},{structure[6]} {structure[7]},{structure[8]} {structure[9]},{structure[10]} {structure[11]})"
        cursor.execute(query)
#-----------------------------------------




#---------decorator function----------
def id(func):
    def wrapper(*args,**kargs):
        employee_id = int(str(input('Enter Employee ID --> ').strip()))
        return func(employee_id, *args, **kargs)
    return wrapper
#-------------------------------------


def add_new_employee():
    while True:
        id = int(str(input('Enter Employee ID --> ').strip()))
        id_length = [int(digit) for digit in str(id)]
        length = len(id_length)
    #check id length
        if length != 11:
            print(f"Entered ID : {id}")
            print("ID is invalid,please check and try again")
        else:
            break
    while True:
        name = input('Enter Employee NAME --> ').strip().title()
        lastname = input('Enter Employee LASTNAME --> ').strip().title()
        if isinstance(name,str) and isinstance(lastname,str):
            break
        else:
            print("try again,name and lastname must be text".upper())

    age = int(input('Enter Employee AGE --> ').strip().title())
    pay = int(input('Enter Employee PAY --> ').strip().title())

    #check unique id
    execute =cursor.execute ("SELECT id FROM data WHERE id=:id",{'id':id})
    fetch = execute.fetchall()
    fetch_int = None
    try:
        fetch_int = int(fetch[0][0])
    except:
        pass
    if fetch_int is  None:
        cursor.execute("INSERT INTO data VALUES(?,?,?,?,?)",(id,name,lastname,age,pay))
        print("Successful operation")
    else:
        print("This Employee is already in database".title())

@id
def fire_employee(employee_id):
    cursor.execute("DELETE FROM data WHERE id=:id",{'id':employee_id})


@id
def show_employee_info(employee_id):
    cursor.execute("SELECT * FROM data WHERE id=:id",{'id':employee_id})
    print(cursor.fetchall())


def update_employee_specific_data():

    action=str(input("what you want to update?\n we can update name,lastname,age and pay \n please choose --> "))
    @id
    def update_name(emloyee_id):
        new_name = str(input('Enter Employee NEW NAME --> ').strip().title())
        cursor.execute("UPDATE data SET name=:new_name WHERE id=:id",
                       {'new_name':new_name,'id':emloyee_id})


    @id
    def update_lastname(emloyee_id):

        new_lastname = str(input('Enter Employee NEW LASTNAME --> ').strip().title())
        cursor.execute("UPDATE data SET lastname=:new_name WHERE id=:id",
                       {'new_name': new_lastname,'id':emloyee_id})


    @id
    def update_age(emloyee_id):

        new_age = str(input('Enter Employee NEW AGE --> ').strip().title())
        cursor.execute("UPDATE data SET age=:new_age WHERE id=:id",
                       {'new_age': new_age, 'id':emloyee_id})

    @id
    def update_pay(emloyee_id):

        new_pay = str(input('Enter Employee NEW PAY --> ').strip().title())
        cursor.execute("UPDATE data SET pay=:new_name WHERE id=:id",
                       {'new_name': new_pay, 'id':emloyee_id})


    if action == "name":
        update_name()
    elif action == "lastname":
        update_lastname()
    elif action == "age":
        update_age()
    elif action == "pay":
        update_pay()
    else:
        print("----------please follow rules!!!----------".title())
        update_employee_specific_data()

@id
def update_employee_fulldata(emloyee_id):
    new_name = str(input('Enter Employee NEW NAME --> ').strip().title())
    new_lastname = str(input('Enter Employee NEW LASTNAME --> ').strip().title())
    new_age = int(input('Enter Employee NEW AGE --> ').strip().title())
    new_pay = int(input('Enter Employee NEW PAY --> ').strip().title())
    cursor.execute("UPDATE data SET name=:new_name, lastname=:new_lastname, age=:new_age, pay=:new_pay WHERE id=:id",
        {'new_name': new_name, 'new_lastname': new_lastname, 'new_age': new_age, 'new_pay': new_pay,
         'id':emloyee_id})
def start():
    prompt = str(input("""what you want to do? \nyou can  choose this functionalities >>>
  FIRST --> ADD NEW EMPLOYEE,\n  SECOND --> SHOW EMPLOYEE'S INFORMATION,
  THIRD --> FIRE EMPLOYEE,\n  FOURTH --> UPDATE EMPLOYEE'S SPECIFIC DATA,
  FIFTH --> UPDATE EMPLOYES'S FULL DATA\n  SIXTH --> CREATE NEW TABLE \nplease select suitable action (first,second,third,fourth,fifth or sixth) -->""").strip().lower())
    if prompt == "first":
        add_new_employee()
    elif prompt == "second":
        show_employee_info()
    elif prompt == "third":
        fire_employee()
    elif prompt == "fourth":
        update_employee_specific_data()
    elif prompt == "fifth":
        update_employee_fulldata()
    elif prompt== "sixth":
        create_new_table()
    else:
        print("---------please try again--------".title())
        start()
def next_action():
    global yesOrNo
    yesOrNo = str(input("do you want another action,please type YES or NO --> ").strip().lower())
try:
    def main():
        while True:

            start()
            next_action()
            if yesOrNo == "no":
                break
            elif yesOrNo == "yes":
                print("ok, lets continue")
            else:
                print("----------please follow rules!!!--------".strip())
    main()
except:
    main()




connection.commit()
connection.close()