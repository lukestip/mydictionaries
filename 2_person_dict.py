person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# print name of second child
print(type(person["children"]))
print(person['children'][1])

# print name of cat
print(type(person["pets"]))
print(person['pets']['cat'])

# print out each child
for i in person['children']:
    print(i)

# Print out pets in format
for i, j in person['pets'].items():
    print(f'Type of pet {i} name of pet {j}')
