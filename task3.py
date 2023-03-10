lst1 = [int(value) for value in input().split()]
lst1=set(lst1)
lst2 = [int(value) for value in input().split()]
lst2=set(lst2)
print("1: ", lst1.intersection(lst2))
print("2: ", lst2.difference(lst1))