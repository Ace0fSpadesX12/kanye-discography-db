import random

#Mini Practice Program

player_name = input("Please enter your name here to continue: ")
weapon = False 
print(f"Hello {player_name}")

print(f"""{player_name}, I'm going to keep it honest with you... We have a really long road ahead.
But regardless.. You're capable.""")

weapon_pool = ["Sword of Avarice", "Spear of Fate"]

while weapon != True:

    match input("Please choose your weapon: Sword or Spear \n").strip().lower(): #First practice with Match

        case "sword":
            print("You have selected the Sword of Avarice. Slash away your foes.")
            weapon = "sword"

        case "spear":
            print("You have selected the Spear of Fate. Impale your enemies.")
            weapon = "spear"
        
        case _:
            print(f"Why have you not selected a valid weapon, {player_name}?")
            
if weapon:
    print(f"Now young warrior.. Venture forth with {weapon} in hand and vanquish all that stand before you!")


print("We must decide on a destinaion to adventure of course!")

def player_continue_prompt():
    input("Press enter to continue onwards...")
player_continue_prompt()


def rejection_flavor_txt():
    flavor = ["I'm not kidding around here" , "You need to choose asap" , "What's taking so long??" ,
            "Just how long do you expect me to wait?" , "I'm dying over here..."]
    return random.choice(flavor)

while True:
    story_mode = input("Would you like to head to Dracula's Castle or Ivalice instead? \n" \
    "Choose wisely.. ").lower()

    if story_mode == "Dracula's Castle" or "Castle":
        print("Castlevania.. Excellent choice.")
        break

    elif story_mode == "Ivalice":
        print("Ahhh... Let's hope it's not your Final Fantasy...")
        break

    else:
        print(f"Why have you not chosen a valid destination {player_name}?")
        print(rejection_flavor_txt())
        continue

player_continue_prompt()