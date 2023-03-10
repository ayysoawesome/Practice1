def summultiplesof4(intlist):
    valuessum = 0
    while len(intlist) != 0:
        a = intlist.pop(0)
        if a % 4 == 0:
            valuessum += a
    return valuessum


data = input("Enter list of integers: ").split()
lst = []
for value in data:
    try:
        lst.append(int(value))
    except ValueError:
        print("Value is not integer.")
        exit(1)

print(lst)
print("Result:", summultiplesof4(lst))
