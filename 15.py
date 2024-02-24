int()
try:
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    result = a / b
    print(result)
except ValueError:
    print("enter a correct answer")
except ZeroDivisionError:
    print("could not divide by zero")
except BaseException as e:
    print(e.args)
