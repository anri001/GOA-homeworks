numbers = [3, 8, 15, 22, 9, 44, 31, 17, 10, 5, 66, 28, 19, 77, 88, 100, 1, 34, 56, 11]

evens = []
odds = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

print("even numbers:", evens)
print("odd numbers:", odds)