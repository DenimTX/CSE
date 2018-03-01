class Room(object):
    def __init__(self, name, south, west, east, north, southwest, northeast, southeast, northwest, description):
        self.name = name
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.southwest = southwest
        self.northeast = northeast
        self.southeast = southeast
        self.northwest = northwest
        self.description = description

    def move(self, direction):
        global current_node
        # current_node = spawn_n
        current_node = globals()[getattr(self, direction)]


spawn_n = Room("Spawn (North)", None, None, None, None, None, None, "phoenix_n", None, 'You see a phoenix and a spawn '
                                                                                       'platform')
phoenix_n = Room("Phoenix (North)", None, None, None, None,
                 None, None, "phoenix_tower_intersection_n", "spawn_n", 'You see a path, a spawn platform, '
                                                                        'and a phoenix.')
phoenix_tower_intersection_n = Room("Phoenix-Tower Intersection (North)", "lane_high_middle", None, None, None,
                                    "mana_buff_camp_n", None, None, "phoenix_n", 'You see a turtle, a phoenix, and '
                                                                                 'a tower')
mana_buff_camp_n = Room("Mana Buff Camp (North)", "bull_demon_king_intersection_n", None, None, None, None,
                        "phoenix_tower_intersection_n", None, None, 'You see two paths and a turtle')
bull_demon_king_intersection_n = Room("Bull Demon King Intersection (North)", "bull_demon_king_intersection_s",
                                      "bull_demon_king", "lane_high_middle", "mana_buff_camp_n", None, None, None, None,
                                      'You see a turtle, a path, and a demon.')
lane_high_middle = Room("Lane High Middle", "lane_middle", "bull_demon_king_intersection_n", None,
                        "phoenix_tower_intersection_n", None, None, "damage_buff_camp", None,
                        'You see two paths, a tower, and a tiger.')
lane_middle = Room("Lane Middle", "lane_low_middle", None, "damage_buff_camp", "lane_high_middle", None, None,
                   None, None, 'You see two paths and a tiger.')
lane_low_middle = Room("Lane Low Middle", "phoenix_tower_intersection_s", "bull_demon_king_intersection_s", None,
                       "lane_middle", None, "damage_buff_camp", None, None, 'You see two paths, a tower, and a demon')
damage_buff_camp = Room("Damage Buff Camp", None, "lane_middle", None, None, "lane_low_middle", None, None,
                        "lane_high_middle", 'You see three paths and a tiger')
bull_demon_king_intersection_s = Room("Bull Demon King Intersection (South)", "mana_buff_camp", "bull_demon_king",
                                      "lane_low_middle", "bull_demon_king_intersection_n", None, None, None, None,
                                      'You see two paths, a turtle, and a demon')
bull_demon_king = Room("Bull Demon King", None, None, None, None, None, "bull_demon_king_intersection_n",
                       "bull_demon_king_intersection_s", None, 'You see two paths and a demon')
mana_buff_camp_s = Room("Mana Buff Camp (South)", None, None, None, "bull_demon_king_intersection_s", None, None,
                        "phoenix_tower_intersection_s", None, 'You see two paths and a turtle')
phoenix_tower_intersection_s = Room("Phoenix-Tower Intersection (South)", None, None, None, "lane_low_middle",
                                    "phoenix_s", None, None, "mana_buff_camp_s",
                                    'You see a tower, a phoenix, and a turtle.')
phoenix_s = Room("Phoenix (South)", None, None, None, None, "spawn_s", "phoenix_tower_intersection_s", None, None,
                 'You see a path, a spawn platform, and a phoenix.')
spawn_s = Room("Spawn (South)", None, None, None, None, None, "phoenix_s", None, None,
               'You see a spawn platform and a phoenix.')


directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
current_node = spawn_n

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_ ')
    if command == 'quit':
        exit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()

# Denim Xiong
