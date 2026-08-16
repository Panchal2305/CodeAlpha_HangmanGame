"""
Hangman Game
Author: Palak Panchal

A beginner-friendly, text-based Hangman game built using Python standard library.
The player guesses a randomly selected word one letter at a time
with a maximum of 6 incorrect attempts allowed.
"""

import random

# Predefined list of beginner-friendly words (exactly 5 words)
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "algorithm"
]

# Maximum allowed incorrect guesses
MAX_INCORRECT_ATTEMPTS = 6


def choose_word() -> str:
    """
    Randomly selects and returns a word from the predefined word list.
    """
    return random.choice(WORDS)


def display_word(word: str, guessed_letters: list) -> str:
    """
    Returns the hidden representation of the secret word.
    Correctly guessed letters are revealed, and unguessed letters are shown as '_'.
    Letters and underscores are separated by spaces for clarity.
    """
    revealed_letters = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(revealed_letters)


def is_word_guessed(word: str, guessed_letters: list) -> bool:
    """
    Checks whether all letters of the secret word have been guessed.
    """
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def print_game_header() -> None:
    """
    Displays the game welcome banner and basic rules.
    """
    print("=" * 35)
    print("           HANGMAN GAME            ")
    print("=" * 35)
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_INCORRECT_ATTEMPTS} incorrect attempts allowed.")
    print("=" * 35)
    print()


def play_game() -> None:
    """
    Main function that executes the Hangman game loop.
    """
    secret_word = choose_word()
    guessed_letters = []
    incorrect_attempts = 0

    print_game_header()

    while incorrect_attempts < MAX_INCORRECT_ATTEMPTS:
        # Calculate remaining incorrect attempts
        remaining_attempts = MAX_INCORRECT_ATTEMPTS - incorrect_attempts

        # Format guessed letters for display
        guessed_display = ", ".join(guessed_letters) if guessed_letters else "None"

        # Display current game status
        print(f"Word: {display_word(secret_word, guessed_letters)}")
        print(f"Guessed letters: {guessed_display}")
        print(f"Remaining attempts: {remaining_attempts}")
        print("-" * 35)

        # Get user input and clean whitespace / normalize to lowercase
        user_input = input("Enter a letter: ").strip().lower()

        # Validate input: single character only
        if len(user_input) != 1:
            print("\n[!] Invalid input! Please enter exactly one letter at a time.\n")
            continue

        # Validate input: alphabetic character only (reject numbers and symbols)
        if not user_input.isalpha():
            print("\n[!] Invalid input! Please enter an alphabetic character (a-z).\n")
            continue

        # Validate input: prevent duplicate guesses
        if user_input in guessed_letters:
            print(f"\n[!] You have already guessed the letter '{user_input}'. Try a different one.\n")
            continue

        # Add valid new guess to the list of guessed letters
        guessed_letters.append(user_input)

        # Check if the guess is in the secret word
        if user_input in secret_word:
            print(f"\nGood guess! '{user_input}' is in the word.\n")
        else:
            incorrect_attempts += 1
            print(f"\nIncorrect guess! '{user_input}' is not in the word.\n")

        # Check win condition
        if is_word_guessed(secret_word, guessed_letters):
            print("=" * 35)
            print(f"Word: {display_word(secret_word, guessed_letters)}")
            print("=" * 35)
            print("Congratulations! You won!")
            print(f"You correctly guessed the word: '{secret_word}'")
            print("=" * 35)
            return

    # Loss condition (when 6 incorrect attempts are reached)
    print("=" * 35)
    print("GAME OVER! You ran out of attempts.")
    print(f"The correct word was: '{secret_word}'")
    print("Better luck next time!")
    print("=" * 35)


if __name__ == "__main__":
    play_game()
