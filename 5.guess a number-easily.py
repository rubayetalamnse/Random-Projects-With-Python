import random

num = random.randrange(40,70)
your_gusess = int(input("Guess the number! It's between 40 to 70: "))

while your_gusess!= num:
    if your_gusess<num:
        print("try higher!")
        your_gusess = int(input("\nGuess the number! It's between 40 to 70: "))
    else:
        print("try lower!")
        your_gusess = int(input("\nGuess the number! It's between 40 to 70: "))

print("your number is correct!")