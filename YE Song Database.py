#Kanye West Discography Database
    ##By Sean James

import time
import random

ye_discography = {
    "The College Dropout, 2004": {
        "Intro (Skit)" : {
            "Duration": 19,
            "Feature(s)" : [],
            "Writer" : "Kanye West",
            "Producer" : "Kanye West",    #22 Song album
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "We Don't Care" : {
            "Duration": 239,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West, Miri Ben-Ari, Ross Vannelli"],
            "Producer(s)" : "Kanye West",
            "Sample" : ["""We Don't Care contains samples of 'I Just Wanna Stop', 
            written by Ross Vannelli and performed by the Jimmy Castor Bunch"""],
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
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : ["""contains interpolations of 
            Lauryn Hill's 'Mystery of Iniquity', 
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
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Jesus Walks" : {
            "Duration": 193,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Never Let Me Down" : {
            "Duration": 324,
            "Feature(s)" : ["Jay-Z", "J. Ivy"],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
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
            "Writer(s)" : "Kanye West",
            "Producer(s)" : ["Kanye West", "Brian Miller"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "School Spirit (Skit)" : {
            "Duration": 78,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
        "School Spirit" : {
            "Duration": 182,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "School Spirit (Skit 2)" : {
            "Duration": 43,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "Lil Jimmy (Skit)" : {
            "Duration": 53,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Two Words" : {
            "Duration": 266,
            "Feature(s)" : ["Mos Def", "Freeway", "The Boys Choir of Harlem"],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Through the Wire" : {
            "Duration": 221,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Family Business" : {
            "Duration": 278,
            "Feature(s)" : [],
            "Writer(s)" : "Kanye West",
            "Producer(s)" : "Kanye West",      
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        },
        "Last Call" : {
            "Duration": 760,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Michael Perretta", "Tony Williams", "Ken Lewis"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 21,
        },
        "Heavy Hitters" : {
            "Duration": 235,
            "Feature(s)" : ["GLC"],
            "Writer(s)" : ["Kanye West", "Leonard Harris"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 22,
        },
    },
    "Late Registration, 2005" : {
        "Wake Up Mr. West" : {
            "Duration": 41,
            "Feature(s)" : [],
            "Writer(s)" : ["Michael Masser", "Gerry Goffin"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Heard 'Em Say" : {
            "Duration": 203,
            "Feature(s)" : ["Adam Levine"],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Touch the Sky" : {
            "Duration": 43,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",     #21 Song album.
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Gold Digger" : {
            "Duration": 207,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Skit No. 1" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Drive Slow" : {
            "Duration": 272,
            "Feature(s)" : ["GLC", "Paul Wall"],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "My Way Home" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : ["Kanye West", "Lonnie Lynn", "Gil-Scott Heron"],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : ["Perfmored in it's entirety by Common"],
            "Track Number" : 7,
        },
        "Crack Music" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Roses" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Bring Me Down" : {
            "Duration": 42,
            "Feature(s)" : ["Brandy"],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Addiction" : { 
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Skit No. 2" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Diamonds from Sierra Leone (Remix)" : {
            "Duration": 42,
            "Feature(s)" : ["J. Cole"],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "We Major" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
        "Skit No. 3" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "Hey Mama" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "Celebration" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Skit No. 4" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Gone" : {
            "Duration": 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Diamonds from Sierra Leone (Bonus Track)" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        },
        "Late (Hidden Track)" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : "Kanye West",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 21,
        },
    },
}

def feature_artist_search(album_filter= None):
    searched_artist = input("Enter any artist to see if they've been featured on a Kanye West song: ")
    artist_found = False
    for album, track_titles in ye_discography.items():
        for track, track_details in track_titles.items():
            if searched_artist in track_details["Feature(s)"]:
                artist_found = True
                print(f"Kanye West has featured with {searched_artist} on the song(s) {track} from the album {album}.") 
    if artist_found == False:
        print(f"Kanye West has not featured with {searched_artist} on any songs.")

def random_ye_generator():
    random_album = random.choice(list(ye_discography.keys()))
    random_track = random.choice(list(ye_discography[random_album].keys()))
    try:
        while "skit" in random_track.lower():
            random_track = random.choice(list(ye_discography[random_album].keys()))
        print(f"Your random Kanye West song is {random_track} from the album {random_album}")
    except IndexError:
        print("Search Error. Please try again.")

def introduction(): 
    for x in range (3):
        print("Initializing Kanye West Song Database...")
        time.sleep(1.5)
    print("Welcome to the largest Kanye West database on the internet!")
    input("Press Enter to continue...")
    

def track_finder():
    print("Input a track number and album number to find the track.")
    album_number = int(input("Album Number: "))
    if album_number == 1:
        print("Album: The College Dropout")
    elif album_number == 2:
        print("Album: Late Registration")
    elif album_number == 3:
        print("Album: Graduation")    
    track_number = int(input("Track Number: "))
    album = list(ye_discography.keys())[album_number - 1]
    track = list(ye_discography[album].keys())[track_number - 1]
    print(f"The track you are looking for is {track} from the album {album}")

def main_menu():
    while True:
        user_choice = input("What is your selection? ")
        if user_choice == "Random Generator".strip().lower():
            random_ye_generator()
        elif user_choice == "Exit".lower().strip():
            for x in range (3):
                print("Exiting Kanye West Song Database..")
                time.sleep(0.7)
            print("Program Closed...")
            break
        elif user_choice == "Track Finder".lower().strip():
            track_finder()
        else:
            print("Invalid selection. Please select again.")
            

track_finder()



#introduction()
#main_menu()






































































































