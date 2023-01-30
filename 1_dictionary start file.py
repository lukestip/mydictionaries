import random

phonebook = {}
phonebook = {'Chris': '555−1111',  # KEY ON THE LEFT, VALUE ON THE RIGHT
             'Katie': '555−2222',
             'Joanne': '555−3333'}
'''
mydictionary = dict(m=8, n=9)

print(mydictionary)

print(f"Number of key value pairs: {len(phonebook)}")


print()
print('*****  start section 1 - print dictionary ********')
print()


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name]) #Dictionary searches for 'name' to see if its in
else:
    print(f"{name} does not exist in the phonebook") #contingency for if name is mispelled or not in the phonebook


print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Chris'] = '555-4444'
phonebook['Joe'] = '555-0123'

print(phonebook)


print()
print('*****  end section 3 ********')
print()


print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook['Chris']

print(phonebook)


print()
print('*****  end section 4 ********')
print()


print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for i in phonebook:
    print(f"The key is: {i} and the value is {phonebook[i]}")

for value in phonebook.values():
    print(f"The value of the phonebook is {value}")

for k, v in phonebook.items():  # k is the key and v is the value in the items() function
    print(f"The key is: {k} and the value is {v}")

for ph_tuple in phonebook.items(): #If we do not split it up (like above for loop using k,v) then a tuple will be returned
    print(ph_tuple)

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


name = 'Chris'

phone = phonebook.get(name, 'key not found')

print("using the get funtion: "+phone)

phonebook.clear() #clears out contents ... DOES NOT DELETE PHONEBOOK

print("using the clear function: " + phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'not found')

print(remove)  # POP = removes value from dict but saves value in variable (remove in this instance)

print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem() #NOT RANDOMIZED

print(a)

print(phonebook)


print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()
