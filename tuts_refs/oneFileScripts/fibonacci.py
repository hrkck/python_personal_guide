

# 1, 1, 2, 3, 5, 8, 13, 21
# 1. 2. 3. 4. 5. 6. 7. 8.
# i, i, i+(i-1), i+(i-1)


def f(x):
    i = 1
    j = 0
    temp = 0
    for _ in range(x):
        temp = i
        i = i + j
        j = temp

    print(i)

#
# f(2)


def r(x):
    if(x == 1):
        return 1
    if(x == 0):
        return 0
    return r(x-1) + r(x - 2)


value = r(5)
print(value)
