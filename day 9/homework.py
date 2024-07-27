age = input("how old are you")
number = input("how many years to travel")
diraction = input("choose + or -")
age = int(age)
number = int(number)
if diraction == "+" :
    new_age = age + number
elif diraction == "-" :
    new_age = age - number
else:
    print("invalid choise. please choose + or -")
    new_age = None
if new_age is not None:
    print(new_age)








