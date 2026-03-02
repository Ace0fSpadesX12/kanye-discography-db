"""Word Guessing Game - player guesses words chosen by the computer."""
import random

WORDS_POSSIBLE = ["cat", "dog", "red", "blue", "yellow", "big", "small", "tall"]

valid_name = False #Player Name upcoming

#while not valid_name: #Intro information
    
    #print("Welcome to the Word Guessing Game")
    #player_name = input("Now, what is your name, Player? \n")
    #if player_name:
       # input(f"Ah, welcome {player_name}. I wish you great luck.. The computer's tough!")
       # valid_name = True
    #else:
     #   input("Ah, welcome Player 1. I wish you great luck.. The computer's tough")
      #  valid_name = True

def computer_shuffler():
    """Select and return a random word from the list."""
    cpu_word = random.choice(WORDS_POSSIBLE)
    print("The computer will now shuffle around it's word shuffler..")
    return cpu_word

def run_post_game():
    another_game = input("Would you like to play another round? Y/N \n").strip().lower()
    post_game_screen = True
    while post_game_screen:   
        if another_game == "y":         #Post game screen asking to play again or not.
            post_game_screen = False
        elif another_game == "n":
            post_game_screen = False
        else:
            print("Invalid input. Please enter Y or N")
            another_game = input("Would you like to play another round? Y/N \n").strip().lower()
    return another_game

def guess_game(name="Player 1"):
    """Run the word guessing game with the player."""
    play_again = True
    round_over = False
    while play_again and not round_over:
        cpu_word = computer_shuffler()
        print("Will you now please select a random word from the displayed list?")
        print(WORDS_POSSIBLE)
        while not round_over:
            player_guess = input("Please type in your guess: ").lower().strip()
            if player_guess == cpu_word:
                print(f"Wow, you did it, {name}!")
                print("The computer's word was" + " " + cpu_word + "!")
                round_over = True
            elif player_guess not in WORDS_POSSIBLE:
                print("That word isn't even in the list! Try again!")
                continue
            else:
                print(f"Better luck next time, {name}!")
                print("The computer's word was" + " " + cpu_word + "!")
                round_over = True

def player_hint():
    pass


random_word = random.choice(WORDS_POSSIBLE)
random_index = random.choice(random_word)
print(random_index)


#guess_game()

#while True:
   # if run_post_game() == "y":
   #     guess_game()
    #else:
     #   break

    