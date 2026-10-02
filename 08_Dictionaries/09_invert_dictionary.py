dictionary = {
    "name": "Abhay",
    "age": 18,
    "branch": "AIDS"
}

inverted = {value: key for key , value in dictionary.items()}

print(inverted)