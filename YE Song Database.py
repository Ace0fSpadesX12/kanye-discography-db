#Kanye West Song Database

import random

ye_songs = {
    "The College Dropout, 2004": {
        "Intro (Skit)" : {
            "Duration": 19,
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 1,
        },
        "We Don't Care" : {
            "Duration": 239,
            "Writer" : ["Kanye West, Miri Ben-Ari, Ross Vannelli"]
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 2,
        },
        "Graduation Day" : {
            "Duration": "0:19",
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 3,
        },
        "All Falls Down" : {
            "Duration": "0:19",
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 4,
        },
        "I'll Fly Away" : {
            "Duration": "0:19",
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 5,
        },
        "Spaceship" : {
            "Duration": "0:19",
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 6,
        }
    }
}
def main_Menu():
    print("Welcome to Kanye West Song Length Finder!")

    while True:
        user_input = input("Enter a Kanye West song name: ")
        if user_input.lower() == "exit":
            break
        else:
            print("Song notwww found in database. Please try again.")
            continue

main_Menu()