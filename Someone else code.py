# Source - https://stackoverflow.com/q/71899672
# Posted by Leria Bailey
# Retrieved 2026-02-15, License - CC BY-SA 4.0

#Leria Bailey simple navigation

#Dictionary linking planets and items in each desired room
planets = {
    'Home Planet': {'name': 'Home Planet', 'south': 'Yellow Planet', 'west': 'Red Planet', 'east': 'Grey Planet',
                    'text': 'You are in the Home Planet.'},

    'Red Planet': {'name': 'Red Planet', 'east': 'Home Planet', 'south': 'Orange Planet',
                'text': 'You are in the Red Planet.','item':'Red Light Crystal'},

    'Orange Planet': {'name': 'Orange Planet', 'north': 'Red Planet', 'east': 'Yellow Planet',
                      'text': 'You are in the Orange Planet.','item':'Orange Light Crystal'},

    'Yellow Planet': {'name': 'Yellow Planet', 'west': 'Orange Planet', 'north': 'Home Planet', 'east': 'Indigo Planet',
                      'south': 'Green Planet',
                      'text': 'You are in the Yellow Planet.','item':'Yellow Light Crystal'},

    'Green Planet': {'name': 'Green Planet', 'north': 'Yellow Planet', 'east': 'Blue Planet',
                     'text': 'You are in the Green Planet.','item':'Green Light Crystal'},

    'Blue Planet': {'name': 'Blue Planet', 'north': 'Yellow Planet', 'east': 'Blue Planet',
                    'text': 'You are in the Blue Planet.','item':'Blue Light Crystal'},

    'Indigo Planet': {'name': 'Indigo Planet', 'south': 'Blue Planet', 'west': 'Yellow Planet', 'east': 'Violet Planet',
                      'text': 'You are in the Indigo Planet.','item':'Indigo Light Crystal'},

    'Violet Planet': {'name': 'Violet Planet', 'west': 'Indigo Planet', 'north': 'Grey Planet',
                      'text': 'You are in the Violet Planet.','item':'Violet Light Crystal'},

    'Grey Planet': {'name': 'Grey Planet', 'south': 'Violet Planet', 'west': 'Home Planet',
                    'text': 'You are in the Grey Planet.','item': 'Light Crystal','item':'Shadow King'},
}

#start Player in Home Planet
direction = ['north', 'south', 'east', 'west']
current_room = planets['Home Planet']
show_instructions = "Enter north, south, east or west to explore different planets. Enter Exit to leave the game."

# inventory list to hold items and possible items
inventory = []
item = ['Red Light Crystal', 'Orange Light Crystal', 'Yellow Light Crystal', 'Green Light Crystal', 'Blue Light Crystal','Indigo Light Crystal', 'Violet Light Crystal', 'Shadow King']

#print game intr
print('----------------------------')
print("Light Hero Text Adventure Game!")
print("Collect 7 light crystals to win the game, or be defeated by the Shadow King.")
print("Let's get started!")
print('----------------------------')

#Planet navigation
while True:
    if current_room['name'] == 'Grey Planet':
        print('Congratulations! You have reached the Grey Planet and defeated the Shadow King!')
        break

    # display current location & Inventory
    print('You are in {}.'.format(current_room['name']))
    print('Your current inventory: {}\n'.format(inventory))                  
    if current_room['item']:
        print('Item in room: {}'.format(inventory.append(current_room['item'])))
        print('')                                                           


    # get user input
    print(show_instructions)
    command = input()
    print('----------------------------')

    # movement
    if command in direction:
        if command in current_room:
            current_room = planets[current_room[command]]

        elif command == 'get item':                                  
            if current_room['item'] != 'none':
                Inventory['Item' + str(len(Inventory.keys()) + 1)] = current_room['item']
                # Inventory.append(current_room['item'])

                print("You acquired : ", current_room['item'])
                print(Inventory)
                current_room['item'] = 'none'
            else:                                                    
                print("No items to collect in this room")            

        else:
            # bad movement
            print('*** You cannot go that way. Please try again ***')
    # quit game
    elif command == 'exit':
        print('You have exited the game. Thanks for playing!')
        break
    # bad command
    else:
        print('*** Invalid input. Please try again ***')

#get Item
def get_item(current_room):
    if 'item' in rooms[current_room]: #if statement
        return rooms[current_room]['item'] #return statement
    else:
        return 'This room has no item!' #return statement
