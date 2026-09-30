sec = int(input("Enter seconds: "))
min = sec // 60
remaining_sec = sec % 60
hours = min // 60
remaining_min = min % 60
print(f"Converted tie is: {hours}.{remaining_min}.{remaining_sec}")