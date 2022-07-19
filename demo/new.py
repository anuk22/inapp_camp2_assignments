"""#sshgs
print("sgfye")

#replace

print('hello'.replace('l','m',1))"""

"""
#split
str1='hello world'
mstr=str1.split(' ')
print(mstr)"""

#regular expressions
"""
import re
txt="hello sohe world hes hello sam grtgrrd "
print(re.findall("he.l",txt))
print(re.findall("^hello",txt))
print(re.findall("\Ahello",txt))
print(re.findall("world$",txt))
print(re.findall(r"\bhe",txt))
print(re.findall(r"\Bhe",txt))"""

"""
#detect email
import re
txt="my email is anukochumon1729@gmail.com"
regex=(r'\S+@\S+')
print(re.findall(regex,txt))"""
"""
#PYTHON LIST        

lst=[1,2,3,4,5,6,7]
print(lst[2:4])
print(lst[3:])
print(lst[:4])
print(lst[1:6:2])
print(lst[::-1])

#append to add a vlaue

lst.append(7)
lst.append("hii")
print(lst)
del lst[0]
print(lst)

lst1=["hii","its me"]
lst.extend(lst1)
print(lst)

#to check a variable is in the list

print("its" in lst1)
#length 

print(len(lst))
"""
#sorting and reversing the list
lst=[1,2,6,5,4]
lst.reverse()
print(lst)

#lst.sort()
print(sorted(lst))

lst2=[12,15,13]
lst3=[14,12,34,54]
print(lst2+lst3)

print(lst*2)