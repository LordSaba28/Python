import random


start = input("Do you want to roll the dice? (y/n): ").lower().strip()

if start == "y":
    while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
        score = die1 + die2
        if score >= 10:
            print("You Win!")
            print("You must be really lucky!")
        elif 3 <= score < 10:
            print("Not Bad!")
        else:
            print("You Lose!")
            print("Sucks to be you!")
        print(f"Your score was {score}!")
        again = input("Roll again? (y/n): ").lower().strip()
        if again == "":
            print("Please enter y or n")
        elif again == "n":
            break
        elif again == "y":
            continue
elif start == "n":
    print("Alright, maybe next time!")
else:
    print("Invalid input!")

#add a feature that allowsthe user specify how many times they wanna roll
# count how many times theyve rolled per session
# fix the nill entry causes a previous response copy bug
