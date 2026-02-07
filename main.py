import random

number = random.randint(1,100)
print("Guess the number")
attemps = 0
L=[]

while attemps < 5:

    a = int(input("Give a number :"))
    if a in L:
        print("You already tried this number!")
        continue

    L.append(a)
    attemps+=1

    if a == number:
        print("Excellent! You found the number", number)
        break

    else:

        if a<number:
            print("The number is higher ")

        elif a>number:
            print("the number is lower")

else:
    print("Sorry, you didn't find the number. It was", number)

print(L)


