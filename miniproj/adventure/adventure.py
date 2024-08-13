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