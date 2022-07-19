"""#set inpython
months={"jan","feb","mar"}

mths=set(["jan","feb","march","april"])
print(months)
print(mths)
print("type is:" ,type(months))

for i in months:
    print(i)

#to declare an empty set

days=set()
#add value to set
days.add("Mon")
days.add("tues")
days.add("wed")
days.update(["thursday","fri"])
print(days)

#remove items from set using discard method
days.discard("thursday")
print(days)
days.discard("thurs")#no key error
print(days)
#days.remove("thursday")#key error
print(days)
days.clear()
print(days)
 """

 #set operator

set1=set(["jan","feb","march","april"])
set2=set(["april","may","jun"])
 #union operator

set3 =set1 | set2
print("union :",set3)
set4=set1 & set2
print("intersection :",set4)

#intersect update the original set by removing 
#elements not present in both of set

set1=set(["tom","jerry","mickey"])
set2=set(["jerry","tom","donald"])
set3=set(["winne","tom","mickey"])
set1.intersection_update(set2)
print(set1)

#difference


print("difference : ",set3-set2)

#symmetric difference
print("symmetric diff :",set3 ^ set2)

