# Code 1
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()

# Code 2
n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

# Code 3

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j,end="")
    print()

# Code 4
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(i, end="")
    print()

# Code 5
n = 5
for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end="")

    for j in range(1, i+1):
        print(j , end="")
    print()