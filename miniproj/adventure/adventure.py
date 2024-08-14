# setting the stage, creating the rooms (might change)
rooms = {
    'living_room':{
        'description': 'You are in the livingroom of an abandoned house, there is a hall to the west and locked door to the east', 
        'exits': {
            'west': 'hall',
        },  
            'locked_door': True,
            'item': None
    },
    'hall':{
        'description': 'you are in a dark hallway. The living room is to the east, and there is a bedroom door at the end of the hallway to the west',
        'exits': {
            'east': 'living_room',
            'west': 'bedroom'
        }, 
            'item': None
    },
    'bedroom':{
        'description': 'you are in a bedroom, you see a shiny key on the bed',
        'exits': {
            'east': 'hall'
        }, 
            'item': 'key'
    }
}

# game logic
current_room = 'living_room'
inventory = []

# something to display inventory/room
def status():
    print("-------------------------------")
    print(rooms[current_room]['description'])
    
    # Had an issue where i used double quotes around exits, fixed by replacing with single quotes
    # quotes for actual print msg and inner quotes cannot be the same
    print(f'Exits: {"|".join(rooms[current_room]["exits"].keys())}')
    if rooms[current_room]['item']:
        print(f"You see a {rooms[current_room]['item']} here.")
    print("-------------------------------")

# updates current players position
def move(direction):
    # tried to use current room without making it global. you cannot do this 
    # you need to grab the "original" variable
    global current_room
    exits = rooms[current_room]['exits']

    if direction in exits:     # accedentally typed exists lol was stuck for a good 30 mins
        current_room = exits[direction]
    else:
        print("you can't go that way")

def game_loop():
    print("~~Welcome to the Adventure Game!~~")
    print('----------------------------------')
    print('How to play:')
    print("------------")
    print('* Enter: "north", "south", "east", or "west" from available exits to advance')
    print('* Enter: "quit" at any time to quit the game')

    #another example of using different outter/inner quote
    while True:
        status()

        direction = input("Which direction do you want to go?\n> ").lower() # stole this ">" from chadgpt
        
        if direction == 'quit':
            print("Thanks for playing!")
            break
        move(direction)

game_loop()