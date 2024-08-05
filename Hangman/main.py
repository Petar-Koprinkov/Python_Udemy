import random
from stages import stages
from logo import logo
from word import words_list


chosen_word = random.choice(words_list)
display = ['_' for _ in chosen_word]
end_of_game = False
lives = 6
guessed_letters = []

print(logo)

while not end_of_game:

    guess = input('Guess a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Wrong input! You have to type only one letter')
        continue

    if guess in guessed_letters:
        print(f'You already type the letter "{guess}"')

    if guess in chosen_word and guess not in guessed_letters:
        print(f'You guess the letter "{guess}"')

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]

    if guess not in chosen_word and guess not in guessed_letters:
        lives -= 1
        print(f'The letter {guess} is not in the word.')

    if '_' not in display:
        print('You guessed the word! You win!')
        end_of_game = True

    if lives == 0:
        end_of_game = True
        print('You lose!')

    guessed_letters.append(guess)

    print(stages[lives])
    print(display)