lst = [word for word in input("Enter a string: ").split(";")]
print(lst)
if len(lst) != 10:
    print("Wrong amount of words.")
    exit()
controlstr = input("Enter control string: ")
for word in lst:
    if word.startswith(controlstr):
        print("Result:", word)
