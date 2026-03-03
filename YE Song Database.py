#Kanye West Song Database

import random

ye_songs = {
    "The College Dropout, 2004": {
        "Intro (Skit)" : {
            "Duration": 19,
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Prouducer" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 1,
        },
        "We Don't Care" : {
            "Duration": 239,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West, Miri Ben-Ari, Ross Vannelli"],
            "Prouducer(s)" : "Kanye West",
            "Sample" : ["""We Don't Care contains samples of 'I Just Wanna Stop', 
                        written by Ross Vannelli and performed by the Jimmy Castor Bunch"""],
            "Track Descrition" : [],
            "Track Number" : 2,
        },
        "Graduation Day" : {
            "Duration": 82,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Miri Ben-Ari", "John Stephens"],
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 3,
        },
        "All Falls Down" : {
            "Duration": 223,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : ["""contains interpolations of 
                        Lauryn Hill's 'Mystery of Iniquity', 
                        performed here by Syleena Johnson."""],
            "Track Descrition" : [],
            "Track Number" : 4,
        },
        "I'll Fly Away" : {
            "Duration": 69,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 5,
        },
        "Spaceship" : {
            "Duration": 324,
            "Feature(s)" : ["Consequence", "GLC"],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 6,
        },
        "Jesus Walks" : {
            "Duration": 193,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 7,
        },
        "Never Let Me Down" : {
            "Duration": 324,
            "Feature(s)" : ["Jay-Z", "J. Ivy"],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 8,
        },
        "Get Em High" : {
            "Duration" : 289,
            "Feature(s)" : ["Talib Kweli", "Common"],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 9,
        },
        "Workout Plan (Skit)" : {
            "Duration" : 46,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 10,
        },
        "The New Workout Plan" : {
            "Duration": 322,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 11,
        },
        "Slow Jamz" : {
            "Duration": 316,
            "Feature(s)" : ["Twista", "Jamie Foxx"],
            "Writer(s)" : ["Kanye West"],
            "Prouducer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 12,
        },
        "Breathe In Breath Out" : {
            "Duration": 246,
            "Feature(s)" : ["Ludacris"],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : ["Kanye West", "Brian Miller"],
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 13,
        },
        "School Spirit (Skit)" : {
            "Duration": 78,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Track Descrition" : "[]",
            "Track Number" : 14,
        },
        "School Spirit" : {
            "Duration": 182,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Track Descrition" : "[]",
            "Track Number" : 15,
        },
        "School Spirit  (Skit 2)" : {
            "Duration": 43,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Track Descrition" : "[]",
            "Track Number" : 16,
        },
        "Lil Jimmy (Skit)" : {
            "Duration": 53,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Track Descrition" : "[]",
            "Track Number" : 17,
        },
        "Two Words" : {
            "Duration": 266,
            "Feature(s)" : ["Mos Def", "Freeway", "The Boys Choir of Harlem"],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Track Descrition" : "[]",
            "Track Number" : 18,
        },
        "Through the Wire" : {
            "Duration": 221,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : "[]",
            "Track Descrition" : "[]",
            "Track Number" : 19,
        },
        "Family Business" : {
            "Duration": 278,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 20,
        },
        "Last Call" : {
            "Duration": 760,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Michael Perretta", "Tony Williams", "Ken Lewis"],
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 21,
        },
        "Heavy Hitters" : {
            "Duration": 235,
            "Feature(s)" : ["GLC"],
            "Writer(s)" : ["Kanye West", "Leonard Harris"],
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 22,
        },
},
    "Late Registration" : {
        "Wake Up Mr. West" : {
            "Duration": 41,
            "Feature(s)" : [],
            "Writer(s)" : ["Michael Masser", "Gerry Goffin"],
            "Prouducer(s)" : "Kanye West",
            "Sample" : [],
            "Track Descrition" : [],
            "Track Number" : 1,
        }
    
    }
}


def feature_artist_search(album= None):
    searched_artist = input("Enter any artist to see if they've been featured on a Kanye West song: ")
    artist_found = False
    for album, track_titles in ye_songs.items():
        for track, track_details in track_titles.items():
            if searched_artist in track_details["Feature(s)"]:
                artist_found = True
                print(f"Kanye West has featured with {searched_artist} on the song(s) {track}.") 
    if artist_found == False:
        print(f"Kanye West has not featured with {searched_artist} on any songs.")

        print(len(ye_songs))


feature_artist_search()




































































































def main_Menu():
    print("Welcome to Kanye West Song Length Finder!")

    while True:
        user_input = input("Enter a Kanye West song name: ")
        if user_input.lower() == "exit":
            break
        else:
            print("Song notwww found in database. Please try again.")
            continue

#main_Menu()