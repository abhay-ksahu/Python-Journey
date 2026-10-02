# UNION

a = {10,20,40,70}
b = {10,30,40,50}

print(a|b)

# INTERSECTION
a = {10,20,40,70}
b = {10,30,40,50}

print(a&b)

# DIFFERENCE
a = {10,20,40,70}
b = {10,30,40,50}

print(a-b) # --> present in a but not in b

print(b-a) # --> present in b but not in a

# SYMMETRIC DIFFERENCE
a = {10,20,40,70}
b = {10,30,40,50}

print(a^b) # --> present in both a and b

# SUBSET AND SUPERSET
a = {10,20,40,70}
b = {10,40}

print(a<=b) # --> b is subset of a --> TRUE
print(a>=b) # --> a is subset of b --> FALSE  --> a is superset of b --> TRUE

