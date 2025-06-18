import random

stages = [ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''''''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''''''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''''''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list =["work","barbosa","hogwarts","ironman","batman"]

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)  # Uncomment for debugging, but keep commented to avoid revealing the answer

placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display=""

    for letter in chosen_word:
        if letter ==guess:
            display+= letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display+= letter
        else:
            display+= "_"
    
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")


    print(stages[max(0, min(lives, len(stages) - 1))])