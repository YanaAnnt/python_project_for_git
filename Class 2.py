a = 5
b = 14
my_name = "aviel"
if not my_name == "moshe" and b>=10 or a < 10:
    print("you are aviel")
    print("hello")
    print("world")
elif my_name =="aviel":
    print("found your name")
elif b > 5:
    print("b is good")

# ערך שיכול להיות או אמת או שקר - ערך בוליאני true or false

my_other_list = ["or", "tohar", "adam"]
my_other_name = "or"
if my_other_name in my_other_list:
    print("i found you")

tt = [1, 2, 3]
rr = [1, 2, 3]
print(tt is rr)
