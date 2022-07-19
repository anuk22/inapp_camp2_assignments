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


#Set comaprison operators
#checking if month1 is a superset of month2

mth1={"jan","feb","march","april","may","jun"}
mth2={"march","april","may","feb"}
mth3={"march","may","feb","april"}

print(mth1>mth2)
print(mth1<mth2)
print(mth2 == mth3)
print(mth1 >= mth2)

#FrozenSets is a new class that has the characteristics of a set,
#but it is immutable

mth4=frozenset(["nov","dec"])
print(mth4)
#add.frozenset("ghsf")#shows an error "exceptionOccured"
#print(mth4)

"""

