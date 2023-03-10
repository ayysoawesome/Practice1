def func(intlist):
    sum = 0
    while len(intlist) != 0:
        a = intlist.pop(0)
        if a % 4 == 0:
            sum += a

    return sum

lst = [int(value) for value in input("Enter list of integers: ").split()]
print(lst)
print(func(lst))