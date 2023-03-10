def input_list():
    data = input().split()
    if len(data) != 10:
        print("Wrong amount of numbers.")
        exit()
    lst = []
    for value in data:
        try:
            lst.append(float(value))
        except ValueError:
            print("Value is not integer.")
            exit()
    return lst


print("Enter first set of floats:")
lst1 = inputlist()
lst1 = set(lst1)
print("Enter second set of floats:")
lst2 = inputlist()
lst2 = set(lst2)

print("присутствуют в каждом из наборов: ", lst1.intersection(lst2))
print("присутствуют только во втором наборе: ", lst2.difference(lst1))
