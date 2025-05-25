import random


def hangman():
    # List of 5 predefined words
    words = ['python', 'code', 'game', 'guess', 'word']
    # Select a random word
    word = random.choice(words)
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()  # Letters guessed by the player
    incorrect_guesses = 0
    max_incorrect = 6

    # Game loop
    while incorrect_guesses < max_incorrect and word_letters:
        # Display current state
        print("\nWord: ", end="")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print(f"\nIncorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

        # Get player input
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check guess
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word_letters:
            print("Good guess!")
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            print("Incorrect guess!")
            guessed_letters.add(guess)
            incorrect_guesses += 1

    # Game outcome
    if not word_letters:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")


# Start the game
print("Welcome to Hangman!")
hangman()