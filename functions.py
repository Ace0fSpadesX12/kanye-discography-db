import random

player = {
    "Sean" : {"Health" : 100, "Attack" : 14}
}

enemy_list = {
    "Goblin": {"Health": 100, "Attack": 6},
    "Archer": {"Health": 100, "Attack": 10},
}

def enemy_appears():
    random_enemy = random.choice(list(enemy_list.keys()))
    print(f"A wild {random_enemy} appears!!! You ready yourself...")
    input("Press Enter to continue..")
    return random_enemy

def player_attack_turn(enemy, damage):
    """
    Execute the player's attack turn.

    Parameters
    ----------
    enemy : str
        The name of the enemy that the player is attacking.
    damage : int
        The amount of damage that the player is dealing to the enemy.

    Returns
    -------
    None
    """
    # Choose a random enemy for the player to attack
    chosen_enemy = enemy_appears()
    # Reduce the enemy's health by the damage dealt
    chosen_enemy["Health"] -= damage
    # Print the player's attack message

def enemy_turn(player,damage):
    """Execute the enemy's attack turn."""
    chosen_enemy = enemy_appears()
    player["Sean"]["Health"] -= enemy_list[chosen_enemy]["Attack"]
    print(f"The {chosen_enemy} swifty retaliates and strikes Sean for {damage} damage")
    return chosen_enemy

def battle_sequence():
    """Execute the battle sequence between player and enemy.
    
    This function starts by randomly selecting an enemy from the enemy_list.
    It then calls the player_attack_turn function, passing the chosen enemy and the player's attack value.
    Finally, it calls the enemy_turn function, passing the player and the chosen enemy's attack value.
    """
    chosen_enemy = enemy_appears()
    player_attack_turn(chosen_enemy, player["Sean"]["Attack"])
    enemy_turn(player, enemy_list[chosen_enemy]["Attack"])


player_alive = True
enemy_alive = True

while player_alive and enemy_alive:
    battle_sequence()
