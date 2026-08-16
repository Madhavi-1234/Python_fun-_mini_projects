import random

print('Guess the word')

name = input("what is your name :")                 
print("Good luck", name)                            

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

guesses = ''

turns = 6

while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:                      # Check against accumulated correct guesses
            print(char, end=" ")                 # Print the character if guessed
        else:
            print("_", end=" ")                  # Otherwise print underscore
            failed += 1                          # Increment failed count if character not guessed
    print()

    if failed == 0:
        print("You won!")
        print(f"The word is {word}")
        break

    guess = input("Guess a character: ").lower()  # Get new guess

    if len(guess) != 1:
        print("Please enter a single character to test your guess.")
        continue

    if guess in guesses:
        print('Hey, you already guessed that character.')
        continue

    guesses += guess

    if guess not in word:                         # Check if the guess is incorrect
        turns -= 1
        print('Your guess is wrong.')
        print(f"You have {turns} more chances.")

        if turns == 0:
            print("You lose!")
            print(f"The word was {word}")
