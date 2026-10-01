# code 8 (DIAMOND)
n = 5

# Top half
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Bottom half
for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()