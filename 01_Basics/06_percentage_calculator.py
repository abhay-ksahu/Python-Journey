subject = {}
for i in range(5):
    print(f"\nSubject {i + 1}")

    name = input("Enter Subject name: ")
    obtained = float(input("Enter Marks obtained: "))
    maximum = float(input("Enter Maximum Marks: "))

    percentage = (obtained/maximum)*100

    subject[name] = (obtained, maximum, percentage)

total_obtained = sum(data[0] for data in subject.values())
total_maximum = sum(data[1] for data in subject.values())

overall_percentage = (total_obtained/total_maximum)*100

best_subject = max(subject, key=lambda name: subject[name][2])
best_percentage = subject[best_subject][2]

print(f"\n----- Result -----")

for name, data in subject.items():
    print(f"{name}: {data[0]}/{data[1]} = {data[2]:.2f}%")

print(f"\nOverall Percentage: {overall_percentage:.2f}%")
print(f"Best Subject: {best_subject}({best_percentage:.2f}%)")