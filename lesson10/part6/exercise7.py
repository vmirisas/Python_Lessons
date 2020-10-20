from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

words = ["rise", "mild", "duke", "vote", "user", "mean", "main", "lemon", "code", "bolt",
         "root", "duty", "fund", "jail", "day"]

#hidden_word = words[randrange(len(words))]
hidden_word = "fast"
print(hidden_word)

guessed_letters = []
max_rounds = len(hidden_word)+int(len(hidden_word)/2)

for round in range(1, max_rounds):
    print(f"ROUND TO GO {max_rounds-round+1}")

    while True:
        players_guess = input("type a letter: ").lower()
        if len(players_guess) != 1:
            print("Error, type ONE letter")
        elif not players_guess.isalpha():
            print("Error, type letters")
        elif players_guess in guessed_letters:
            print("You have already typed this letter")
        else:
            break


    guessed_letters.append(players_guess)
    print(f"the letter \"{players_guess}\" exists {hidden_word.count(players_guess)} times in the hidden word.")

    found = True
    for char in hidden_word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            found = False
    print(""
          )
    if found:
        print("Success! You've found the word!")
        break
else:
    print("game over, you have maxed out the rounds")
    print(f"the hidden word was: {hidden_word}")
