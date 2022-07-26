import pyodbc
import sys
conString='Driver={SQL Server};Server=DESKTOP-R1N5RGM;Database=Employee;Trusted_Connection=yes;'
myconn=pyodbc.connect(conString)
mycursor=myconn.cursor()
try:
    '''
    mycursor.execute('CREATE TABLE PhoneBook'
    '(contact_id INT IDENTITY PRIMARY KEY,'
    'name VARCHAR(10),'
    'contact BIGINT'
    ');')
    mycursor.execute("INSERT INTO PhoneBook VALUES(?,?)",('Ammu',9874563210))
    mycursor.execute("INSERT INTO PhoneBook VALUES(?,?)",("Abhiya",8456793210))
    mycursor.execute("INSERT INTO PhoneBook VALUES(?,?)",("Manu",7896541236))
    mycursor.execute("INSERT INTO PhoneBook VALUES(?,?)",("Devin",9632587410))
    mycursor.execute("INSERT INTO PhoneBook VALUES(?,?)",("Manya",9510263487))
  '''
    mycursor.execute("SELECT * FROM PhoneBook")
    myconn.commit()
    
except Exception as e:
    print(f"{type(e).__name__}")
    print(e)

def list():
    d=[]
    try:
        mycursor.execute("SELECT name,contact FROM PhoneBook ORDER BY name;")
    except:
        print("failed to fetch contacts")
    else:
        print("NAME      ","NUMBER")
        for i,j in mycursor.fetchall():
            print(i,"  ",j)

def add():
    name=input("Enter Name :")
    number=int(input("Enter Number:"))
    if(len(str(number))!=10 or number!=(mycursor.execute("SELECT contact FROM PhoneBook"))):
        print("Invalid Number or Number already exists")
        return
    try:
        mycursor.execute("INSERT INTO PhoneBook VALUES(?,?)",(name,number))
        myconn.commit()
    except Exception as e:
        print(f"{type(e).__name__}")
def delete():
    nm=input("Enter the name you want to delete")
    try:
        mycursor.execute("DELETE FROM PhoneBook WHERE name=(?)",(nm))
        myconn.commit()
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        if(mycursor.rowcount>0):
            print("Deleted")
        else:
            print(f"{nm} doesnt exists")
    
def SearchByName():
    nm=input("Enter the name you want to get details :")
    try:
        mycursor.execute("SELECT name,contact FROM PhoneBook WHERE name=(?)",(nm))
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        contacts=mycursor.fetchall()
        if(len(contacts)>0):
            for i,j in contacts:
                print(i,"  ",j)
            
        else:
            print(f"{nm} is not found")
myconn.commit()

def SearchByNumber():
    nm=int(input("Enter the number you want to get details :"))
    try:
        mycursor.execute("SELECT name,contact FROM PhoneBook WHERE contact=(?)",(nm))
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        contacts=mycursor.fetchall()
        if(len(contacts)>0):
            for i,j in contacts:
                print(i,"  ",j)
            
        else:
            print(f"{nm} doesnt exists in the phonebook")
myconn.commit()
myconn.close()

while True:
    ch=int(input("""Enter Your Choice
                     1.List All Contacts
                     2.Add A contact
                     3.Delete A contact
                     4.Search a contact by its name
                     5.Search a contact by its number
                     6.Exit"""))
    match ch:
        case 1:list()
        case 2:add()
        case 3:delete()
        case 4:SearchByName()
        case 5:SearchByContact()
        case 6:Exit()
        case _:print("Invalid Input")
