weight = 58
your_gusess = int(input("Guess the weight! It's between 40 to 70 kg: "))

while your_gusess!= weight:
    if your_gusess<weight:
        print("try higher!")
        your_gusess = int(input("\nGuess the weight! It's between 40 to 70kg : "))
    else:
        print("try lower!")
        your_gusess = int(input("\nGuess the weight! It's between 40 to 70kg : "))

print("my weight is revealed!")
