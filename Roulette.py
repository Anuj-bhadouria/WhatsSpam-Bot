import random

secret_no=random.randint(1,3)

print(secret_no);
print("WELCCOME TO THE NUMBER GUESSING GAME")

print("I am thinking of a number between 1 and 10")
print("IF the guessed number is greater or less than the guessed number ")

guessed_no=int(input("GUESS THE NUMBER = "))

if secret_no > guessed_no:
    print("TOO LESS")
elif secret_no < guessed_no:
    print("TOO HIGH")
elif secret_no == guessed_no:
    print("You have guessed it! YOU'VE WON !")
else:
    print("Invalid Number")

print(secret_no)

