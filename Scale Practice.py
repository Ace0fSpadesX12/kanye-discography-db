import random 

#Today's Lesson Will Help You Memorize Scale Degree Position  

major_scales = {
"C Major" : ["C" , "D" , "E" , "F" , "G" , "A" , "B"],#done
"C#/Db Major" : ["C#/Db" , "D#/Eb" , "F" , "F#/Gb" , "G#/Ab" , "A#/Bb" , "C"],#done
"D Major" : ["D" , "E" , "F#/Gb" , "G" , "A" , "B" , "C#/Db"],#done
"D#/Eb Major" : ["D#/Eb" , "F" , "G" , "G#/Ab" , "A#/Bb" , "C" , "D"],
"E Major" : ["E" , "F#/Gb" , "G#/Ab", "A" , "B" , "C#/Db" , "D#/Eb"],#done
"F Major" : ["F" , "G" , "A" , "A#/Bb" , "C" , "D" , "E"],#done
"F#/Gb Major" : ["F#/Gb" , "G#/Ab" , "A#/Bb" , "B" , "C#/Db" , "D#/Eb" , "F"],#done
"G Major" : ["G" , "A" , "B" , "C" , "D" , "E" , "F#"],
"G#/Ab Major" : [],
"A Major" : ["A" , "B" , "C#" , "D" , "E" , "F#/Gb" , "G#/Ab"],
"A#/Bb Major" : [],
"B Major" : ["B" , "C#/Db" , "D#/Eb" , "E" , "F#/Gb" , ""] 
}

minor_scales = {
"C Minor" : ["C" , "D" , "Eb/D#" , "F" , "G" , "A" , "B"],#done
"C#/Db Minor" : ["C#/Db" , ],
"D Minor" : ["D" , "E" , "F" , "G" , "A" , "Bb/A#" , "C"],#done
"D#/Eb Minor" : [],
"E Minor" : ["E" , "F#/Gb" , "G" , "A" , "B" , "C" , "D"],#done
"F Minor" : ["F" , "G" , "G#/Ab" , "A#/Bb" , "C" , "C#/Db" , "D#/Eb"],#done
"F#/Gb Minor" : ["F#/Gb" , "G#/Ab"],
"G Minor" : ["G" , "A" , "A#/Bb" , "C" , "D" , "D#/Eb" , "F"],#done
"G#/Ab Minor" : ["G#/Ab" , "A#/Bb" , "B" , ],
"A Minor" : ["A" , "B" , "C" , "D" , "E" , "F" , "G"],#done
"A#/Bb Minor" : ["A#/Bb" , ""],
"B Minor" : []
}


for i in range(3):
    print("Program now starting...")

print("Welcome to The Scale Degree Super SUPER Game!! " \
"Here, you'll be tasked with identifying the correct scale degree positions " \
"of different keys.")

game_start = input("Please press Enter to continue...")

def game_mode_select():
    print("Choose a mode:")
    print("1 - Random Scale Mode")
    print("2 - Select a Key Mode")
    
    choice = input("Enter 1 or 2: ")
    return choice

result = game_mode_select()

print("You've chosen", result)