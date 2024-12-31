import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
correct_guesses = []
guessed_letters = []

print(logo)

placeholder = ""
for _ in range(word_length):
    placeholder += "_"

print(f"Word to guess: {placeholder}")

while not end_of_game:
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if guess not in guessed_letters:
            if letter == guess:
                display += letter
                correct_guesses.append(letter)
            elif letter in correct_guesses:
                display += letter
            else:
                display += "_"  

    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.") 

        if lives == 0:
            end_of_game = True
            print("You lose.")

            print(f"***********************The word was {chosen_word}, YOU LOSE**********************")

    if display == chosen_word:
        end_of_game = True
        print("You win.")

    print(stages[lives])
