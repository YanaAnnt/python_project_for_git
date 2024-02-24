a = open("names.txt", "a+")
for name in a.writelines():
    print("hello" + name, end='')
