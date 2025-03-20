import random

# Word selection
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
word_completion = '_' * len(word)
guessed_letters = set()
tries = 6

# Hangman stages
stages = [
    "-----\n|   |\nO   |\n/|\\  |\n/ \\  |\n    |\n--------",
    "-----\n|   |\nO   |\n/|\\  |\n/    |\n    |\n--------",
    "-----\n|   |\nO   |\n/|\\  |\n     |\n    |\n--------",
    "-----\n|   |\nO   |\n/|   |\n     |\n    |\n--------",
    "-----\n|   |\nO   |\n|    |\n     |\n    |\n--------",
    "-----\n|   |\nO   |\n     |\n     |\n    |\n--------",
    "-----\n|   |\n     |\n     |\n     |\n    |\n--------"
]

# Game loop
print("Let's play Hangman!")
while tries > 0 and '_' in word_completion:
    print(stages[tries])
    print(word_completion)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.add(guess)
        word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    else:
        guessed_letters.add(guess)
        tries -= 1
        print(f"{guess} is not in the word.")

# Game result
if '_' not in word_completion:
    print("Congrats, you guessed the word! You win!")
else:
    print(f"Sorry, you ran out of tries. The word was {word}.")
