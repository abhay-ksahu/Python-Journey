dict1 = {
    "name": "Abhay",
    "age": 18
}

dict2 = {
    "college": "TCET",
    "branch": "AIDS-D"
}

# merge = dict1|dict2
# print(merge) 

dict1.update(dict2)
print(dict1)

# .update() changes dict1, while | creates a new dictionary