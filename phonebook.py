
phone_dict={
    "abhiya":9874563215,
    "ammu":9123456789,
    "ela":9632587412
}
#displaying all lists
def display(phone_dict):
    for i in phone_dict:
        print(i,phone_dict[i])
    

#adding a new contact

def add(a,b,phone_dict):
    phone_dict.update({a:b})
    for i in phone_dict:
        print(i,phone_dict[i])

#delete a contact
def delete(c,phone_dict):
    phone_dict.pop(c)

#search by name
def searchByName(c,phone_dict):
    print(phone_dict.get(c))
#search by contact
def searchByNumber(c,phone_dict):
    for i in phone_dict:
        if(phone_dict[i]==c):
            print(i)
            break
flag=0
while(flag==0):
    a=int(input('''Enter
               1:List all contacts
               2.add new contact/update existing contact
               3.delete a contact
               4.search by name
               5.search by contact
               6.exit
            '''))
    if(a==1):
        display(phone_dict)
    elif(a==2):
        a=input("Enter name :")
        b=int(input("enter number: "))
        add(a,b,phone_dict)
    elif(a==3):
        c=input("enter the contact name you want to delete :")
        delete(c,phone_dict)
    elif(a==4):
        c=input("enter the contact name you want to search :")
        searchByName(c,phone_dict)
    elif(a==5):
        c=int(input("enter the contact number you want to search :"))
        searchByNumber(c,phone_dict)
    else:
        flag=1









