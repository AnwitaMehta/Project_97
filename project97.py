import random

number = random.randint (1,9)
print (number)

chances = 5

while (chances>0):
    userInput = int(input("Enter the number: "))
    if userInput == number:
        print ("You won!")
        break
    if userInput <number:
        print ("Your number is too low, try again.")
    if userInput >number:
        print ("Your number is too high, try again.")

    chances = chances -1