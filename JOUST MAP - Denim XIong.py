world_map = {
    'SPAWN (NORTH)': {
        'NAME': 'SPAWN (NORTH)',
        'DESCRIPTION': 'You see a phoenix and a spawn platform',
        'PATHS': {
            'SOUTHEAST': 'PHOENIX (NORTH)'
        }
    }, 'PHOENIX (NORTH)': {
        'NAME': 'PHOENIX (NORTH)',
        'DESCRIPTION': 'You see a path, a spawn platform, and a phoenix.',
        'PATHS': {
            'NORTHWEST': 'SPAWN (NORTH)',
            'SOUTHEAST': 'PHOENIX-TOWER INTERSECTION (NORTH)'
        }
    }, 'PHOENIX-TOWER INTERSECTION (NORTH)': {
        'NAME': 'PHOENIX-TOWER INTERSECTION (NORTH)',
        'DESCRIPTION': 'You see a turtle, a phoenix, and a tower',
        'PATHS': {
            'SOUTHWEST': 'MANA BUFF CAMP (NORTH)',
            'SOUTH': 'LANE HIGH MIDDLE',
            'NORTHWEST': 'PHOENIX (NORTH)'
        }
    }, 'MANA BUFF CAMP (NORTH)': {
        'NAME': 'MANA BUFF CAMP (NORTH)',
        'DESCRIPTION': 'You see two paths and a turtle',
        'PATHS': {
            'SOUTH': 'BULL DEMON KING INTERSECTION (NORTH)',
            'NORTHEAST': 'PHOENIX-TOWER INTERSECTION (NORTH)'
        }
    }, 'BULL DEMON KING INTERSECTION (NORTH)': {
        'NAME': 'BULL DEMON KING INTERSECTION (NORTH)',
        'DESCRIPTION': 'You see a turtle, a path, and a demon.',
        'PATHS': {
            'NORTH': 'MANA BUFF CAMP (NORTH)',
            'EAST': 'LANE HIGH MIDDLE',
            'SOUTH': 'BULL DEMON KING INTERSECTION (SOUTH)',
            'WEST': 'BULL DEMON KING'
        }
    }, 'LANE HIGH MIDDLE': {
        'NAME': 'LANE HIGH MIDDLE',
        'DESCRIPTION': 'You see two paths, a tower, and a tiger.',
        'PATHS': {
            'SOUTH': 'LANE MIDDLE',
            'SOUTHEAST': 'DAMAGE BUFF CAMP',
            'WEST': 'BULL DEMON KING INTERSECTION (NORTH)',
            'NORTH': 'PHOENIX-TOWER INTERSECTION (NORTH)'
        }
    }, 'LANE MIDDLE': {
        'NAME': 'LANE MIDDLE',
        'DESCRIPTION': 'You see two paths and a tiger.',
        'PATHS': {
            'NORTH': 'LANE HIGH MIDDLE',
            'SOUTH': 'LANE LOW MIDDLE',
            'EAST': 'DAMAGE BUFF CAMP'
        }
    }, 'DAMAGE BUFF CAMP': {
        'NAME': 'DAMAGE BUFF CAMP',
        'DESCRIPTION': 'You see three paths and a tiger',
        'PATHS': {
            'NORTHWEST': 'LANE HIGH MIDDLE',
            'WEST': 'LANE MIDDLE',
            'SOUTHWEST': 'LANE LOW MIDDLE'
        }
    }, 'LANE LOW MIDDLE': {
        'NAME': 'LANE LOW MIDDLE',
        'DESCRIPTION': 'You see two paths, a tower, and a demon',
        'PATHS': {
            'NORTH': 'LANE MIDDLE',
            'NORTHEAST': 'DAMAGE BUFF CAMP',
            'SOUTH': 'PHOENIX TOWER INTERSECTION (SOUTH)',
            'WEST': 'BULL DEMON KING INTERSECTION (SOUTH)',
        }
    }, 'BULL DEMON KING': {
        'NAME': 'BULL DEMON KING',
        'DESCRIPTION': 'You see two paths and a demon',
        'PATHS': {
            'SOUTHEAST': 'BULL DEMON KING INTERSECTION (SOUTH)',
            'NORTHEAST': 'BULL DEMON KING INTERSECTION (NORTH)'
        }
    }, 'BULL DEMON KING INTERSECTION (SOUTH)': {
        'NAME': 'BULL DEMON KING INTERSECTION (SOUTH)',
        'DESCRIPTION': 'You see two paths, a turtle, and a demon',
        'PATHS': {
            'NORTH': 'BULL DEMON KING INTERSECTION (NORTH)',
            'SOUTH': 'MANA BUFF CAMP',
            'EAST': 'LANE LOW MIDDLE',
            'WEST': 'BULL DEMON KING'
        }
    }, 'MANA BUFF CAMP (SOUTH)': {
        'NAME': 'MANA BUFF CAMP (SOUTH)',
        'DESCRIPTION': 'You see two paths and a turtle',
        'PATHS': {
            'NORTH': 'BULL DEMON KING INTERSECTION (SOUTH)',
            'SOUTHEAST': 'PHOENIX-TOWER INTERSECTION (SOUTH)'
        }
    }, 'PHOENIX-TOWER INTERSECTION (SOUTH)': {
        'NAME': 'PHOENIX-TOWER INTERSECTION (SOUTH)',
        'DESCRIPTION': 'You see a tower, a phoenix, and a turtle.',
        'PATHS': {
            'NORTH': 'LANE LOW MIDDLE',
            'SOUTHWEST': 'PHOENIX (SOUTH)',
            'NORTHWEST': 'MANA BUFF CAMP (SOUTH)'
        }
    }, 'PHOENIX (SOUTH)': {
        'NAME': 'PHOENIX (SOUTH)',
        'DESCRIPTION': 'You see a path, a spawn platform, and a phoenix.',
        'PATHS': {
            'NORTHEAST': 'PHOENIX-TOWER INTERSECTION (SOUTH)',
            'SOUTHWEST': 'SPAWN (SOUTH)'
        }
    }, 'SPAWN (SOUTH)': {
        'NAME': 'SPAWN (SOUTH)',
        'DESCRIPTION': 'You see a spawn platform and a phoenix.',
        'PATHS': {
            'NORTHEAST': 'PHOENIX (SOUTH)'
        }
    },
}

current_node = world_map['SPAWN (NORTH)']
directions = ['SOUTHEAST', 'NORTHWEST', 'SOUTH', 'WEST', 'EAST', 'NORTH', 'SOUTHWEST', 'NORTHEAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_ ')
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    if command == 'quit':
        exit(0)
    if command == 'help':
        print(' TYPE IN \'SOUTH\', \'NORTH\', \'WEST\', \'EAST\', \'NORTHEAST\', \'SOUTHWEST\', \'SOUTHEAST\', '
              'OR \'NORTHWEST\' TO MOVE. \'')
        print('TYPE \'quit\' TO QUIT.')
    else:
        print("Command not found.")
    print()

# Denim Xiong
