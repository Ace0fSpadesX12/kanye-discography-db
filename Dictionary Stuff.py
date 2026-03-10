guild = {
    "members": {
        "Aria": {
            "role": "mage",
            "level": 12,
            "spells": ["fireball", "blink"]
        },
        "Doran": {
            "role": "warrior",
            "level": 15,
            "spells": []
        },
        "Syl": {
            "role": "archer",
            "level": 10,
            "spells": ["mark"]
        }
    }
}

all_spells = []

for ally in guild["members"].values():
    all_spells.extend(ally["spells"])


##print(all_spells)

for n in range (1, 11):
    print(n)