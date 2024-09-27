import random
n1 = -10
n2 = 10

mylist = [n1,n2]
choice =random.choice(mylist)
print(choice)
if choice == n1:
    print(n2)
elif choice == n2:
    print(n1)