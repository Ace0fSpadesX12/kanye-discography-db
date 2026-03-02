manga = {
    "naruto": {
        "release_year": 1999,
        "volumes": 72,
        "author": "Masashi Kishimoto",
        "proper_title": "Naruto",
    },
    "dragonball": {
        "release_year" : 1980,
        "volumes" : 42,
        "author" : "Akira Toriyama",
        "proper_title" : "DragonBall",
    },
    "bleach": {
        "release_year" : 2001,
        "volumes" : 74,
        "author" : "Tite Kubo", 
        "proper_title" : "Bleach",
    }


    }

def info_printout(title):
    title_key = title.lower()
    if title_key in manga:
        info = manga[title_key]
        print(f"{info['proper_title']} was released in {info['release_year']}")
        print(f"It has {info['volumes']} volumes")
        print(f"Authored by: {info['author']}")
    else:
        print("Manga not found.")

info_printout("dragonBalL")
