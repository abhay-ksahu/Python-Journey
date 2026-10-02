data = {
    "apple": 50,
    "banana": 20,
    "mango": 80,
    "orange": 30
}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print(sorted_data)