#Kanye West Song Database

import random

ye_songs = {
    "The College Dropout, 2004": {
        "Intro (Skit)" : {
            "Duration": 19,
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 1,
        },
        "We Don't Care" : {
            "Duration": 239,
            "Feature(s)" : [],
            "Writer" : ["Kanye West, Miri Ben-Ari, Ross Vannelli"],
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 2,
        },
        "Graduation Day" : {
            "Duration": 82,
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 3,
        },
        "All Falls Down" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 4,
        },
        "I'll Fly Away" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]"
            "Short Descrition" : "[]",
            "Track Number" : 5,
        },
        "Spaceship" : {
            "Duration": "0:19",
            "Features" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 6,
        }
        "Jesus Walks" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 7,
        },
        "Never Let Me Down" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 8,
        },
        "Get Em High" : {
            "Duration" : "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 9,
        },
        "Workout Plan (Skit)" : {
            "Duration" : "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 10,
        },
        "The New Workout Plan" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 11,
        },
        "Slow Jamz" : {
            "Duration": "0:19",
            "Feature(s)" : ["Twista", "Jamie Foxx"],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 12,
        },
        "Breathe In Breath Out" : {
            "Duration": "0:19",
            "Feature(s)" : ["Ludacris"],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 13,
        },
        "School Spirit (Skit)" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 14,
        },
        "School Spirit" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 15,
        },
        "School Spirit  (Skit 2)" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 16,
        },
        "Lil Jimmy (Skit)" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 17,
        },
        "Two Words" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 18,
        },
        "Through the Wire" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 19,
        },
        "Family Business" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 20,
        },
        "Last Call" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 21,
        },
        "Heavy Hitters" : {
            "Duration": "0:19",
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Short Descrition" : "[]",
            "Track Number" : 22,
        }
},
    "Late Registration" : {
        
    }

































































































fef main_Menu():
    print("Welcome to Kanye West Song Length Finder!")

    while True:
        user_input = input("Enter a Kanye West song name: ")
        if user_input.lower() == "exit":
            break
        else:
            print("Song notwww found in database. Please try again.")
            continue

main_Menu()