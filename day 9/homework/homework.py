age = input("how old are you")
number = input("how many years to travel")
direction = input("choose + or -")
age = int(age)
number = int(number)
if direction == "+" :
    new_age = age + number
elif direction == "-" :
    new_age = age - number
else:
    print("invalid choice. please choose + or -")
    new_age = None
if new_age is not None:
    print(new_age)








