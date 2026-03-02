import random

# Player and game stats
player_health = 100
enemy_health = 100
enemy_list = ["Soldier", "Assassin", "Warrior", "Mage", "Archer",
              "Berserker", "Paladin", "Rogue", "Monk", "Druid"]
tier2enemy_list = ["Orc", "Troll", "Goblin", "Dark Knight", "Necromancer", "Shadow Archer",
                   "Fire Mage", "Ice Sorcerer", "Vampire", "Werewolf"]

enemy = random.choice(enemy_list)
exp = 0
level = 1
min_damage = 5
max_damage = 15
spell_damage = 3
burning = False
tier2_unlocked = False  # Flag to trigger weapon choice once

player_name = input("Enter your combatant's Name Here! ")
print(f"Welcome to the arena, {player_name}!")

while player_health > 0:

    # Apply burning damage first
    if burning:
        enemy_health -= spell_damage
        enemy_health = max(enemy_health, 0)
        print(f"The {enemy} suffers {spell_damage} burning damage from your spell! The {enemy}'s health is now {enemy_health}.")

    # Check for enemy defeat
    if enemy_health <= 0:
        if burning:
            print(f"The {enemy} completely burns to ashes!")
        else:
            print(f"You have killed the {enemy}!")

        exp += 50
        print(f"You have gained 50 experience points! Total EXP: {exp}")

        # Level up
        while exp >= 100:
            level += 1
            exp -= 100
            min_damage += 1
            max_damage += 1
            spell_damage = int(3 * (1.2 * level))
            print(f"Congratulations, {player_name}! You've leveled up to Level {level}!")
            print(f"Your minimum attack power has risen to {min_damage}).")
            print('A fire inside you grows...')

        # Unlock tier 2 enemies and weapon choice
        if level >= 5 and not tier2_unlocked:
            print("I think it's time for a new weapon, warrior!")
            weapon_choice = input("Choose your weapon: (S)word, (A)xe, (B)ow: ")
            if weapon_choice.lower() in ['s', 'sword']:
                print("You have chosen the sword!")
            elif weapon_choice.lower() in ['a', 'axe']:
                print("You have chosen the axe!")
            elif weapon_choice.lower() in ['b', 'bow']:
                print("You have chosen the bow!")    
                tier2_unlocked = True

        # Spawn new enemy
        if tier2_unlocked:
            enemy = random.choice(tier2enemy_list)
        else:
            enemy = random.choice(enemy_list)
        enemy_health = 100
        player_health = 100
        burning = False
        print(f"A new {enemy} enters the arena! Your health has been restored to {player_health} to prepare yourself!.\n")
        continue  # skip rest of turn

    # Player action
    combat = input("Do you want to '(A)ttack' , '(H)eal' , or '(S)pell' ? ")

    # ATTACK
    if combat.lower() in ["attack", "a"]:
        player_damage = random.randint(min_damage, max_damage)
        enemy_damage = random.randint(5, 12)
        enemy_health -= player_damage
        enemy_health = max(enemy_health, 0)

        print(f"You've struck the {enemy} for {player_damage} damage! The {enemy}'s health is now {enemy_health}.")

        # Enemy attacks back
        player_health -= enemy_damage
        player_health = max(player_health, 0)
        print(f"The {enemy} strikes back swiftly for {enemy_damage} damage! Your health has now fallen to {player_health}.")

    # HEAL
    elif combat.lower() in ['heal', 'h']:
        heal_amount = random.randint(5, 12)
        player_health += heal_amount
        if player_health > 100:
            player_health = 100
        enemy_damage = random.randint(5, 12)
        player_health -= enemy_damage
        player_health = max(player_health, 0)

        print(f"You've healed yourself for {heal_amount} HP!")
        print(f"The {enemy} takes the opportunity to strike for {enemy_damage} damage! Your health is now {player_health}.")

    # SPELL
    elif combat.lower() in ['spell', 's']:
        burning = True
        enemy_health -= spell_damage
        enemy_health = max(enemy_health, 0)
        print(f"You set the enemy ablaze with a spell on the {enemy}, dealing {spell_damage} damage per turn! The {enemy}'s health is now {enemy_health}.")

    # INVALID COMMAND
    else:
        print("Invalid command! Please choose attack or heal!")

# PLAYER DEFEATED
print(f"You have been defeated by the {enemy}. Game Over, {player_name}!")
