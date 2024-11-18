number = int(input("Enter number: "))

def is_greater_than_zero():
    if number > 0:
        return "The number is greater than zero."
    else:
        return "The number is not greater than zero."

print(is_greater_than_zero())
