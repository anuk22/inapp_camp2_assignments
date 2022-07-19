#print the lst of nums which are divisible by 5 and multiple of 8 btw 2000 and 2500
from termios import NL1


print("Nums which are divisible by 5 and multiple of 8 btw 2000 and 2500 are:")
for i in range(2000,2501):
    if(i%5==0 and i%8==0):
        print(i,end=" ")
print("\n")
#create multiplication table of a  number from input
n=int(input("enter num: "))
print("multiplication table of num",n,"is :")
for i in range(1,11):
    print(n*i,end=" ")