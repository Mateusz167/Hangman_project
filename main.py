import random
import hangman_art
import hangman_word

print(hangman_art.logo)
end_of_game = False
chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)

lives = 6
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    # Check whether a user has already selected this letter
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess} letter")
    #Check guessed letter
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
