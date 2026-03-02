song_artists = {  
    "rappers": {
        "Kanye West" : ["Flashing Lights" , "Diamonds from Sierra Leone", "Famous"],
        "Lil Wayne" : ["A Millie" , "Got Money" , "Tha Mobb"],
        "Rihanna" : ["Disturbia" , "Diamonds in the Sky"],
        "Jay Z" : ["99 Problems", "Threat"]
    },
    "singers": {
        "Sia" : ["Chandalier"],
        "NSYNC" : ["Bye Bye Bye"],
        "Bruno Mars" : ["24K Magic"],
        "Amerie" : ["1 Thing"]
    }
}


song_artists["singers"]["Sia"] = ["NA", "NA2", "NA3"]

print(song_artists)



song_artists["rappers"]["Travis Scott"] = ["90210"]
song_artists["rappers"]["Drake"] = ["Hotline Bling"]
song_artists["rappers"]["Kenny Mason"] = ["Spiritual"]



file = open(r"C:\Users\Ace0f\OneDrive\Documents\PythonInfo.txt", "a") 


def step_2():
    total = [1,2,3]
    result = []
    for num in total:
        result.append(num * 2)
    return result

