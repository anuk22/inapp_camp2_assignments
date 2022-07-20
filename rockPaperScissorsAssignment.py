from random import choice
n=int(input("Enter how many times u want to play :"))
sh = sc = 0

b=["r","p","s"]

def fun(b):
    a=input('''Enter 
           r for rock 
           p for paper
           s for scissors :''')
    global sc
    global sh
    c=choice(b)
    print("computer output is :",c)
    match a:
        case 'r':
            if(c=="p"):
                sc+=1
                sh+=0
            elif(c=="s"):
                sh+=1
                sc+=0
            else:
                sc+=0
                sh+=0
        case 'p':
            if(c=="r"):
                sh+=1
                sc+=0
            elif(c=="s"):
                sc+=1
                sh+=0
            else:
                sc+=0

        case 's':
            if(c=="r"):
                sc+=1
            elif(c=="p"):
                sh+=1
            else:
                sc+=0
        case _:print("invalid input")
    return sc,sh

while(n!=0):
    fun(b)
    print("Score earned by player :",sh,"\nScore eraned by computer",sc)
    n-=1
if(sc>sh):
    print("Computer is the winner")
elif(sc==sh):
    print("tie")
else:
    print("You're the winner")

print("Score earned by player :",sh,"\nScore eraned by computer",sc)