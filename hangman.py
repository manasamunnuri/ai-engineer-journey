import random

# 5 predefined words
words = ["python", "laptop", "garden", "planet", "friend"]

# Randomly choose a word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters")

# Main game loop
while incorrect_guesses < max_wrong:
    # Show current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"\nWord: {display_word}")
    print(f"Guessed letters: {guessed_letters}")
    print(f"Wrong guesses left: {max_wrong - incorrect_guesses}")

    # Check if won
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nYou WON! The word was '{secret_word}'")
        break

    # Get input
    guess = input("Guess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(f"Good! '{guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Wrong! '{guess}' is not in the word.")

else:
    # Loop ended without break = lost
    print(f"\nGame Over! You lost. The word was '{secret_word}'")
