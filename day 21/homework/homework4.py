number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if i % 2 == 0:
        print(f"{i} - Even")
    else:
        print(f"{i} - Odd")
