import sys
print("hello")
print(sys.version)

#COMMENTING IN PYTHON
#hey its me!!!

"""
hey,
 again its me
"""

s="hey anu"
print(s.title())
print(s.upper())
print(s.lower())

#formatting

first_name="Anu"
last_name="Riju"

my_name=f"{first_name} {last_name}"
print(my_name)

print(f"hey,{my_name}")

my_test='{0} is different from {0}'.format('apple')
print(my_test)

#join method
seperator='-'
my_tupple=('h','e','e')
print(seperator.join(my_tuple))
