#Kanye West Discography Database
    ##By Sean James
"""CLI tool that models a large nested data set, 
implements search and random sampling, 
and supports user interaction. 
Skills demonstrated: Python dictionaries, loops, 
functions, data validation, filtering, and JSON handling."""


import time
import random
import json
import sys

ye_discography = {
    "The College Dropout": {
        "Intro (Skit)" : {
            "Duration": 19,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : "Kanye West",    #22 Song album
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "We Don't Care" : {
            "Duration": 239,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West, Miri Ben-Ari, Ross Vannelli"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : ["We Don't Care contains samples of 'I Just Wanna Stop' written by Ross Vannelli and performed by the Jimmy Castor Bunch"],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Graduation Day" : {
            "Duration": 82,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Miri Ben-Ari", "John Stephens"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "All Falls Down" : {
            "Duration": 223,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Lauryn Hill"],
            "Producer(s)" : "Kanye West",
            "Sample" : ["""contains interpolations of Lauryn Hill's 'Mystery of Iniquity', 
            performed here by Syleena Johnson."""],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "I'll Fly Away" : {
            "Duration": 69,
            "Feature(s)" : [],
            "Writer(s)" : ["Albert E. Brumley"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Spaceship" : {
            "Duration": 324,
            "Feature(s)" : ["Consequence", "GLC"],
            "Writer(s)" : ["Kanye West", "Leonard Harris", "Dexter Mills", 
                "Marvin Gaye", "Gwen Gordy Fuqua", "Sandra Greene"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Jesus Walks" : {
            "Duration": 193,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Che Smith", "Miri Ben-Ari"
                        "Curtis Lundy"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Never Let Me Down" : {
            "Duration": 324,
            "Feature(s)" : ["Jay-Z", "J. Ivy"],
            "Writer(s)" : ["Kanye West", "Shawn Carter", "James Richardson",
                        "Michael Bolton", "Bruce Kulick"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Get Em High" : {
            "Duration" : 289,
            "Feature(s)" : ["Talib Kweli", "Common"],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Workout Plan (Skit)" : {
            "Duration" : 46,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "The New Workout Plan" : {
            "Duration": 322,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Slow Jamz" : {
            "Duration": 316,
            "Feature(s)" : ["Twista", "Jamie Foxx"],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Breathe In Breath Out" : {
            "Duration": 246,
            "Feature(s)" : ["Ludacris"],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West", "Brian Miller"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "School Spirit (Skit)" : {
            "Duration": 78,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
        "School Spirit" : {
            "Duration": 182,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "School Spirit (Skit 2)" : {
            "Duration": 43,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "Lil Jimmy (Skit)" : {
            "Duration": 53,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Two Words" : {
            "Duration": 266,
            "Feature(s)" : ["Mos Def", "Freeway", "The Boys Choir of Harlem"],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Through the Wire" : {
            "Duration": 221,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Family Business" : {
            "Duration": 278,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West"],
            "Producer(s)" : ["Kanye West"],      
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        },
        "Last Call" : {
            "Duration": 760,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Michael Perretta", "Tony Williams", "Ken Lewis"],
            "Producer(s)" : ["Kanye West", "Evidence"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 21,
        },
        "Heavy Hitters" : {
            "Duration": 235,
            "Feature(s)" : ["GLC"],
            "Writer(s)" : ["Kanye West", "Leonard Harris"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 22,
        },
    },
    "Late Registration" : {
        "Wake Up Mr. West" : {
            "Duration": 41,
            "Feature(s)" : [],
            "Writer(s)" : ["Michael Masser", "Gerry Goffin"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Heard 'Em Say" : {
            "Duration": 203,
            "Feature(s)" : ["Adam Levine"],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West", "Jon Brion"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Touch the Sky" : {
            "Duration": 43,
            "Feature(s)" : ["Lupe Fiasco"],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],     #21 Song album.
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Gold Digger" : {
            "Duration": 207,
            "Feature(s)" : ["Jamie Foxx"],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Skit No. 1" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Drive Slow" : {
            "Duration": 272,
            "Feature(s)" : ["GLC", "Paul Wall"],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "My Way Home" : {
            "Duration": 103,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Lonnie Lynn", "Gil-Scott Heron"],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : ["Perfmored in it's entirety by Common"],
            "Track Number" : 7,
        },
        "Crack Music" : {
            "Duration": 271,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Roses" : {
            "Duration": 245,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Bring Me Down" : {
            "Duration": 199,
            "Feature(s)" : ["Brandy"],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Addiction" : { 
            "Duration": 267,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Skit No. 2" : {
            "Duration": 31,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Diamonds from Sierra Leone (Remix)" : {
            "Duration": 233,
            "Feature(s)" : ["Jay-Z"],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "We Major" : {
            "Duration" : 448,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
        "Skit No. 3" : {
            "Duration" : 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "Hey Mama" : {
            "Duration" : 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "Celebration" : {
            "Duration" : 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Skit No. 4" : {
            "Duration" : 78,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Gone" : {
            "Duration" : 333,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Diamonds from Sierra Leone (Bonus Track)" : {
            "Duration" : 238,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        },
        "Late (Hidden Track)" : {
            "Duration" : 230,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["Kanye West"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 21,
        },
    },
}

def feature_artist_search(album_filter= None):
    searched_artist = input("Enter an artist to see if they've been featured on a Kanye West song: ")
    artist_found = False
    for album, track_titles in ye_discography.items():
        for track, track_details in track_titles.items():
            if searched_artist in track_details["Feature(s)"]:
                artist_found = True
                print(f"Kanye West has featured with {searched_artist} on the following song(s): \n{track}, from the album {album}.") 
    if artist_found == False:
        print(f"Kanye West has not featured with {searched_artist} on any songs.")

def count_total_ye_songs():
    total_songs = 0
    for album_name, album_tracks in ye_discography.items():
        for song, details in album_tracks.items():
            total_songs += 1
    return total_songs

def random_ye_generator(): 
    while True:
        random_album = random.choice(list(ye_discography.keys()))
        random_track = random.choice(list(ye_discography[random_album].keys()))
        try:
            while "skit" in random_track.lower():
                random_track = random.choice(list(ye_discography[random_album].keys()))
            print(f"Your random Kanye West song is {random_track} from the album {random_album}")
        except IndexError:
            print("Search Error. Please try again.")      
        loop_again = input("Do you want to search again? (y/n): ")
        if loop_again.lower() == "y":
            continue
        elif loop_again.lower() == "n":
            print("(back to Main Menu...)")
            break
        else:
            print("Invalid input. Please try again.")

def introduction(count_total_ye_songs): 
    for x in range (3):
        print("Initializing Kanye West Song Database...")
        time.sleep(.5)
    print(f"Welcome to the most extensive Kanye West database on the web. Host of a whopping {count_total_ye_songs} songs across his discography!")
    input("...Press Enter to log in...")

album_alias_titles = {
    "The College Dropout" : {
        "Song Count" : 22,
        "Album Nicknames" : ["tcd", 1,"college dropout", "1st", "dropout", "the college dropout"],
    },
    "Late Registration" : {
        "Song Count" : 21,
        "Album Nicknames" : ["lr", "late registration", 2, "late reg", "2nd"],
    }
}

def album_choice():
    while True:
        album_choice = input("Please enter a Kanye West album to index: ").strip().lower()
        for album, info in album_alias_titles.items():
            if album_choice in info["Album Nicknames"]:
                print(f"You've selected the album: {album}, with a total of {info['Song Count']} songs.")
                return album
        else:
            print("Album not found. Please try again.")
                




def song_choice(chosen_album):
    print("You are now in song choice")
    print(chosen_album)



def track_search():
    chosen_album = album_choice()
    song_choice(chosen_album)


track_search()

def main_menu():
    while True:
        print("Your options in program are: \nRandom Generator \nTrack Search \nCollab Search \nExit")
        user_choice = input("What is your selection? ")
        if user_choice == "random generator".strip().lower():
            random_ye_generator()
        elif user_choice == "Exit".lower().strip():
            for x in range (3):
                print("Exiting Kanye West Song Database..")
                time.sleep(0.9)
            print("He made Graduation.")
            print("Program Closed...")
            sys.exit()
        elif user_choice == "Track Search".lower().strip():
            track_search()
        elif user_choice == "Collab Search".lower().strip():
            feature_artist_search()
        else:
            print("Invalid selection. Please select again.")
            


#Start_of_Run_Process

#introduction(count_total_ye_songs())
#main_menu()



































































































