import random

# Player and game stats
player_health = 100
enemy_health = 100
spells_list = ["Fire"] # List of available spells

enemy_list = ["Soldier", "Assassin", "Warrior", "Mage", "Archer",
            "Berserker", "Paladin", "Rogue", "Salamander", "Mandragora" , "Vampire"]
tier2enemy_list = {"Orc", "Giant Rat", "Goblin", "Dark Knight", "Necromancer", "Shadow Archer",
                "Fire Mage", "Ice Sorcerer", "Alpha Vampire", "Werewolf"}
attack_flavor_texts = ["swiftyly", "quickly", "brutally", "fiercely", "skillfully", "valiantly", "relentlessly", "mercilessly", "boldly", "fearlessly", "devilishly" , "wildly", "savagely", "viciously", "powerfully", "aggressively", "formidably", "intensely", "ferociously", "dauntlessly"]

enemy_adjectives = ["fierce", "cunning", "brutal", "sly", "vicious", "merciless", "menacing"] 
weapon_choice = ["Sword", "Axe", "Bow"]

# Tier 2 enemy stats
tier2enemy_stats = {
    "Orc": {"health": 150, "min_dmg": 10, "max_dmg": 18},
    "Giant Rat": {"health": 165, "min_dmg": 12, "max_dmg": 20},
    "Goblin": {"health": 120, "min_dmg": 8, "max_dmg": 15},
    "Dark Knight": {"health": 175, "min_dmg": 15, "max_dmg": 25},
    "Necromancer": {"health": 130, "min_dmg": 10, "max_dmg": 22},
    "Shadow Archer": {"health": 140, "min_dmg": 12, "max_dmg": 20},
    "Fire Mage": {"health": 120, "min_dmg": 15, "max_dmg": 25},
    "Ice Sorcerer": {"health": 120, "min_dmg": 15, "max_dmg": 25},
    "Alpha Vampire": {"health": 160, "min_dmg": 12, "max_dmg": 22},
    "Werewolf": {"health": 180, "min_dmg": 14, "max_dmg": 24},
    "King Snake": {"health": 200, "min_dmg": 20, "max_dmg": 30},
}

# Tier 3 enemy stats
tier3enemy_stats = {"The Omen": {"health": 500, "min_dmg": 20, "max_dmg": 35}}

# Flag and variable initialization
enemy = random.choice(enemy_list)
exp = 0
level = 1
heal_count = 3
min_damage = 5
max_damage = 15
enemy_min_dmg = 6
enemy_max_dmg = 12
fire_damage = 3
shock_damage = 2
burning = False
shocked_timer = 0
shocked = False 
whirling = False
whirling_timer = 0
tier2_unlocked = False  # Flag to trigger weapon choice once
player_evolved = False # Flag to track if player has chosen weapon & ascended. 
tier3_unlocked = False # Flag for tier 3 unlocks

# Game Introduction
print("Welcome to Children of Omen!")
player_name = input("Enter your combatant's Name Here! ")
print(f"Step into the caverns, {player_name}!")
print(f"A {enemy_adjectives[random.randint(0, len(enemy_adjectives)-1)]} {enemy} approaches. Ready yourself at once!")

while player_health > 0:

    # Apply burning damage first
    if burning:
        enemy_health -= fire_damage
        enemy_health = max(enemy_health, 0)
        print(f"The {enemy} suffers {fire_damage} burning damage from your spell! The {enemy}'s health is now {enemy_health}.")

    enemy_damage = random.randint(enemy_min_dmg, enemy_max_dmg)

    # Check for enemy defeat
    if enemy_health <= 0:
        if burning:
            print(f"The {enemy} completely burns away to ash!")
        elif shocked:
            print(f"The {enemy} collapses, unable to move from the shock!")    
        elif whirling:
            print(f"The {enemy} is ravaged by a giant gust of wind!")
        elif burning and shocked and whirling:
            print(f"The {enemy} has been utterly destroyed by your combined elemental prowess!")    
        else:
            print(f"You have defeated the {enemy}!")

        exp += 50
        print(f"You have gained 50 experience points! Total EXP: {exp}")

        # Level up
        while exp >= 100:
            level += 1
            exp = 0
            min_damage += 10
            max_damage += 10
            fire_damage = int(3 * (1.2 * level))
            print(f"Congratulations, {player_name}! You've leveled up to Level {level}!")
            print(f"Your minimum attack power has risen to {min_damage}.")
            print('A fire inside you grows...')

        # Tier 3 unlock
        if level == 10:
            tier3_unlocked = True
            print("You have reached the pinnacle of your power... A new element awakens within you... One of Wind!")
        
        if tier3_unlocked:
            enemy = "The Omen"
            enemy_health = tier3enemy_stats[enemy]["health"]
            enemy_min_dmg = tier3enemy_stats[enemy]["min_dmg"]
            enemy_max_dmg = tier3enemy_stats[enemy]["max_dmg"]
            print("The final challenge approaches... Prepare for... The Omen itself!")

        if tier3_unlocked and "Wind" not in spells_list:
            spells_list.append("Wind")
            print("You feel a gust of power... Wind magic has been acquired!")

        # Tier 2 unlocks enemies, ascension, and weapon choice
        if level >= 5 and not tier2_unlocked:
            tier2_unlocked = True
            player_evolved = True
            print("What's this...? You find a new weapon amongst the remains and rubble...")
            weapon_choice = input("What is it..?: (S)word, (A)xe, (B)ow: ")
            if weapon_choice in ['s', 'sword']:
                print("You have found the Sword of Damacles!")
            elif weapon_choice in ['a', 'axe']:
                print("You have found the Axe of the Storm!")
            elif weapon_choice in ['b', 'bow']:
                print("You have found the Bow of Blessings!")    
        player_health = 100 * 2  # Double health on tier 2 unlock        

        if level == 5:
            print("Tougher challenges await deeper in the caverns...")
            if "Lightning" not in spells_list:
                spells_list.append("Lightning")
                print("You feel a sharp spark... Lightning magic has been acquired!")

        if tier2_unlocked and weapon_choice.startswith('s'):
            print(f"As a sword wielder, {player_name} ascends to a higher plane of combat prowess!")
            print("You have become adept with a blade, you will sometimes strike critically!")
            player_evolved = True

#Spawn Logic

        if tier2_unlocked:
            enemy = random.choice(list(tier2enemy_stats.keys()))
            enemy_health = tier2enemy_stats[enemy]["health"]
            enemy_min_dmg = tier2enemy_stats[enemy]["min_dmg"]
            enemy_max_dmg = tier2enemy_stats[enemy]["max_dmg"]
        else:
            enemy = random.choice(enemy_list)
            enemy_health = 100
            enemy_min_dmg = 5
            enemy_max_dmg = 12

        # Reset player health and heal count for new fight
        player_health = 100
        if tier2_unlocked:
            player_health = 200
        burning = False
        heal_count = 3
        print(f"A {enemy_adjectives[random.randint(0, len(enemy_adjectives)-1)]} {enemy} enters the arena! Your health and potion count have been restored to prepare yourself!.\n")
        continue  # skip rest of turn


    turn_happened = False 
    # Player action
    combat = input("Do you want to '(A)ttack' , '(H)eal' , '(C)'heck level , or '(S)pell'? ")

    if combat.lower() in ["attack", "a"]:
        turn_happened = True
        if shocked_timer > 0:
            print(f"The {enemy} is shocked and cannot attack this turn!")
            shocked_timer -= 1
            player_damage = random.randint(min_damage, max_damage)
            enemy_health -= player_damage
            enemy_health = max(enemy_health, 0)
            print(f"You've struck the {enemy} for {player_damage} damage! The {enemy}'s health is now {enemy_health}.")
        else:
            turn_happened = True   
            shocked = False
            print(f"The {enemy} has recovered from the shock!")
            player_damage = random.randint(min_damage, max_damage)
            enemy_health -= player_damage
            enemy_health = max(enemy_health, 0)
            if enemy_health <= 0:
                continue  # Enemy defeated before it can attack
            player_health -= enemy_damage
            player_health = max(player_health, 0)
            print(f"You've struck the {enemy} for {player_damage} damage! The {enemy}'s health is now {enemy_health}.")
            print(f"The {enemy} attacks you {random.choice(attack_flavor_texts)} for {enemy_damage} damage! Your health is now {player_health}.")

    elif combat.lower() in ['spell', 's']:
        spell_choice = input(f"Choose your spell: {', '.join(spells_list)}: ")
        if spell_choice.lower() in ["fire", "f"]:
            spell_damage = int(3 * (1.2 * level))
            enemy_health -= spell_damage
            enemy_health = max(enemy_health, 0)
            burning = True
            print(f"You cast Fire! The {enemy} is set ablaze and takes {spell_damage} damage from burning every turn! It's health is now {enemy_health}.")
        elif spell_choice.lower() in ["lightning", "l"] and "Lightning" in spells_list:
            spell_damage = int(2 * (1.2 * level))
            enemy_health -= spell_damage
            enemy_health = max(enemy_health, 0)
            shocked = True
            shocked_timer = 1
            print(f"You cast Lightning! The {enemy} takes {spell_damage} damage and is now shocked for their next turn! Its health is now {enemy_health}.")
        elif spell_choice.lower() in ["Whirlwind", "w"] and "Wind" in spells_list:
            spell_damage = int(4 * (1.2 * level))
            enemy_health -= spell_damage
            enemy_health = max(enemy_health, 0)
            whirling = True
            whirling_timer = 3
            print(f"You cast Whirlwind! The {enemy} takes {spell_damage} damage and is caught in a powerful gust! Its health is now {enemy_health} and they deal less damage for the next 3 turns!")
        else:
            print("Invalid spell choice!")
            continue

    elif combat.lower() in ['check status', 'c']:
        print(f"You are currently level {level} with {exp} EXP and {player_health} HP.")
        if exp == 50:
            print("One more victory to level up!")
        continue

    elif combat.lower() in ['heal', 'h']:
        if heal_count > 0:
            heal_amount = random.randint(14, 30)
            player_health += heal_amount
            if tier2_unlocked is False and player_health > 100:
                player_health = 100
            if heal_amount + player_health >= 100:
                print("You swig one of the potions you've been carrying. You're fully healed to 100 HP!")
            else:
                print(f"You swig one of the potions you've been carrying. You've healed yourself for {heal_amount} HP to bring your total up to {player_health}!") 
            heal_count -= 1
            if heal_count == 0:
                print("Uh-oh... You're out of healing potions for this fight!")
        else:
            print(f"You want to drink from your bottle but... It's bone dry. Your health remains {player_health}.")

    else:
        print("Invalid action! Please choose again.")   
    turn_happened = False   

    # Weapon crit bonuses
    if player_evolved:
        crit_chance = random.randint(1, 5)
        if crit_chance == 1:
            crit_damage = int(player_damage * 0.5)
            enemy_health -= crit_damage
            enemy_health = max(enemy_health, 0)
            if weapon_choice == 's':
                print(f"Critical Hit! Your blade flashes again for {crit_damage} bonus damage!")
            elif weapon_choice == 'a':
                print(f"Critical Hit! Your axe cleaves for {crit_damage} bonus damage!")
            elif weapon_choice == 'b':
                print(f"Critical Hit! Arrows rain down for {crit_damage} bonus damage!")

# PLAYER DEFEATED
print(f"You, Child of OMEN, have been defeated by the {enemy}. Game Over, {player_name}! For now...")
