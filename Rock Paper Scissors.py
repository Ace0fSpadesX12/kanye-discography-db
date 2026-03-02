"""Rock, Paper, Scissors Game."""

import time
import random


def player_won_round(game_state, flavor_texts):
    """Handle player winning a round and update game state."""
    print(random.choice(flavor_texts))
    game_state['total_rounds'] += 1
    game_state['player_score'] += 1
    game_state['player_streak'] += 1


POSSIBLE_HANDS = ["Rock 🪨", "Paper 📃", "Scissors ✂️"]
PLAYER_WIN_FLAVOR_TXT = [
    "Bingo! You win!",
    "Congratulations are in order. Nice job!",
    "Great job taking home the victory",
    "What a crazy win!",
    "You snatch this round away. Lucky!",
    "Con-ga-rats!",
]
PLAYER_LOSS_FLAVOR_TXT = [
    "Oof! The computer takes this one. Better luck next time!",
    "Sorry. You lose this round!",
    "Oh no! You've lost. Maybe next round?",
    "The computer wins. Unlucky.",
    "Everybody fails sometimes..",
]

print("Welcome to a game as old as time... Rock, Paper, Scissors!!")

player_name = input("Please enter your name here: ")
print(f"Welcome, {player_name}")
print("Ok, now let's choose how long your game should run")

play_again = True
player_wins = 0
ai_wins = 0

# Rock beats scissors
# Paper beats rock
# Scissors beats paper


while play_again:
    game_state = {
        'player_score': 0,
        'ai_score': 0,
        'game_over': False,
        'player_streak': 0,
        'best_streak': 0,
        'total_rounds': 1,
        'target_score': 0,
    }

    while True:
        try:
            game_mode_select = input("What would you like your target score to be: ")
            game_state['target_score'] = int(f"{game_mode_select}")
            if game_state['target_score'] <= 0:
                print("Please enter a valid number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    print(f"Got it! First to {game_state['target_score']} wins.")

    while game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:

        print(f"Player Score: {game_state['player_score']}")
        print(f"Computer Score: {game_state['ai_score']}")
        if game_state['player_score'] == game_state['target_score'] - 1 and game_state['ai_score'] == game_state['target_score'] - 1:
            print("Next point wins!")
        elif game_state['player_score'] == game_state['target_score'] - 1 or game_state['ai_score'] == game_state['target_score'] - 1:
            print("Game point!")

        player_choice = input(
            "Which hand would you like to throw? (R)ock | (P)aper | (S)cissors: "
        )
        computer_choice = random.choice(POSSIBLE_HANDS)

        if player_choice.lower() == "rock" or player_choice.lower() == "r":
            print("You've chosen Rock 🪨")
            for i in range(2):
                print("The computer is thinking...")
                time.sleep(0.7)
            print(f"The computer has chosen... {computer_choice}")
            if computer_choice == POSSIBLE_HANDS[0]:
                print("It's a tie!")
                game_state['total_rounds'] += 1
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
            elif computer_choice == POSSIBLE_HANDS[1]:
                print(random.choice(PLAYER_LOSS_FLAVOR_TXT))
                game_state['total_rounds'] += 1
                game_state['ai_score'] += 1
                if game_state['player_streak'] >= 3:
                    print(f"🥲 Oh no, your streak has been broken at {game_state['player_streak']}!")
                game_state['player_streak'] = 0
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
            else:
                player_won_round(game_state, PLAYER_WIN_FLAVOR_TXT)
                if game_state['player_streak'] >= 3:
                    print("🔥 What a streak! You're on quite a roll!")
                    print(f"Win Streak: {game_state['player_streak']}")
                game_state['best_streak'] = max(game_state['best_streak'], game_state['player_streak'])
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
        elif player_choice.lower() == "scissors" or player_choice.lower() == "s":
            print("You've chosen Scissors ✂️")
            for i in range(2):
                print("The computer is thinking...")
                time.sleep(0.7)
            print(f"The computer has chosen... {computer_choice}")
            if computer_choice == POSSIBLE_HANDS[0]:
                print(random.choice(PLAYER_LOSS_FLAVOR_TXT))
                game_state['total_rounds'] += 1
                game_state['ai_score'] += 1
                if game_state['player_streak'] >= 3:
                    print(f"🥲 Oh no, your streak has been broken at {game_state['player_streak']}!")
                game_state['player_streak'] = 0
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
            elif computer_choice == POSSIBLE_HANDS[1]:
                player_won_round(game_state, PLAYER_WIN_FLAVOR_TXT)
                if game_state['player_streak'] >= 3:
                    print("🔥 What a streak! You're on quite a roll!")
                    print(f"Win Streak: {game_state['player_streak']}")
                game_state['best_streak'] = max(game_state['best_streak'], game_state['player_streak'])
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
            else:
                print("It's a tie!")
                game_state['total_rounds'] += 1
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")

        elif player_choice.lower() == "paper" or player_choice.lower() == "p":
            print("You've chosen Paper 📃")
            for i in range(2):
                print("The computer is thinking...")
                time.sleep(0.7)
            print(f"The computer has chosen... {computer_choice}")
            if computer_choice == POSSIBLE_HANDS[2]:
                print(random.choice(PLAYER_LOSS_FLAVOR_TXT))
                game_state['total_rounds'] += 1
                game_state['ai_score'] += 1
                if game_state['player_streak'] >= 3:
                    print(f"🥲 Oh no, your streak has been broken at {game_state['player_streak']}!")
                game_state['player_streak'] = 0
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
            elif computer_choice == POSSIBLE_HANDS[0]:
                player_won_round(game_state, PLAYER_WIN_FLAVOR_TXT)
                if game_state['player_streak'] >= 3:
                    print("🔥 What a streak! You're on quite a roll!")
                    print(f"Win Streak: {game_state['player_streak']}")
                game_state['best_streak'] = max(game_state['best_streak'], game_state['player_streak'])
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")
            else:
                print("It's a tie!")
                game_state['total_rounds'] += 1
                if game_state['player_score'] < game_state['target_score'] and game_state['ai_score'] < game_state['target_score']:
                    print(f"Round #{game_state['total_rounds']}")

        else:
            print("Sorry. Invalid option!")

        # GameWinnerScreen

        if game_state['player_score'] == game_state['target_score']:
            print(
                f"🎊 {player_name} wins the match in {game_state['total_rounds']-1} total rounds! 😎"
            )
            game_state['game_over'] = True
            player_wins += 1
            print(f"Total Player Wins: {player_wins} Total Computer Wins: {ai_wins}")
        elif game_state['ai_score'] == game_state['target_score']:
            print(
                f"😅 The computer wins the match in {game_state['total_rounds']-1} total rounds! 🤖"
            )
            game_state['game_over'] = True
            ai_wins += 1
            print(f"Total Player Wins: {player_wins} Total Computer Wins: {ai_wins}")
    if game_state['player_streak'] >= 2:
        print(
            f"Your best round win streak this game was: {game_state['best_streak']}. Try to beat it next game!"
        )

    while game_state['game_over']:
        play_again = input("Would you like to play again? Y/N: ").strip().lower()

        if play_again == "y":
            play_again = True
            game_state['game_over'] = False
            break

        elif play_again == "n":
            print("Thank you for playing. See ya!!")
            play_again = False
            break

        else:
            print("Please type in a valid input of Y or N")
