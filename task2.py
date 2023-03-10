lst = [word for word in input("Enter a string: ").split(";")]
print(lst)
str = input("Enter control string: ")
for word in lst:
    if word.startswith(str) == True:
        print(word)