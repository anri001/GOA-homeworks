number = int(input("Enter number: "))

def even():
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(even())
