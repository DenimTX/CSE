class Room(object):
    def __init__(self, name, south, west, east, north, southwest, northeast, southeast, northwest):
        self.name = name
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.southwest = southwest
        self.northeast = northeast
        self.southeast = southeast
        self.northwest = northwest

    def move(self, direction):
        global current_node
        # current_node = spawn_n
        current_node = globals()[getattr(self, direction)]


spawn_n = Room("Spawn (North)", None, None, None, None, None, None, "phoenix_n", None)
phoenix_n = Room("Phoenix (North)", None, None, None, None,
                 None, None, "phoenix_tower_intersection_n", "spawn_n")
phoenix_tower_intersection_n = Room("Phoenix-Tower Intersection (North)", "lane_high_middle", None, None, None,
                                    "mana_buff_camp_n", None, None, "phoenix_n")
mana_buff_camp_n = Room("Mana Buff Camp (North)", "bull_demon_king_intersection_n", None, None, None, None,
                        "phoenix_tower_intersection_n", None, None)
bull_demon_king_intersection_n = Room("Bull Demon King Intersection (North)", "bull_demon_king_intersection_s",
                                      "bull_demon_king", "lane_high_middle", "mana_buff_camp_n", None, None, None, None)
lane_high_middle = Room("Lane High Middle", "lane_middle", "bull_demon_king_intersection_n", None,
                        "phoenix_tower_intersection_n", None, None, "damage_buff_camp", None)
lane_middle = Room("Lane Middle", "lane_low_middle", None, "damage_buff_camp", "lane_high_middle", None, None,
                   None, None)
lane_low_middle = Room("Lane Low Middle", "phoenix_tower_intersection_s", "bull_demon_king_intersection_s", None,
                       "lane_middle", None, "damage_buff_camp", None, None)
damage_buff_camp = Room("Damage Buff Camp", None, "lane_middle", None, None, "lane_low_middle", None, None,
                        "lane_high_middle")
bull_demon_king_intersection_s = Room("Bull Demon King Intersection (South)", "mana_buff_camp", "bull_demon_king",
                                      "lane_low_middle", "bull_demon_king_intersection_n", None, None, None, None)
bull_demon_king = Room("Bull Demon King", None, None, None, None, None, "bull_demon_king_intersection_n",
                       "bull_demon_king_intersection_s", None)
mana_buff_camp_s = Room("Mana Buff Camp (South)", None, None, None, "bull_demon_king_intersection_s", None, None,
                        "phoenix_tower_intersection_s", None)
phoenix_tower_intersection_s = Room("Phoenix-Tower Intersection (South)", None, None, None, "lane_low_middle",
                                    "phoenix_s", None, None, "mana_buff_camp_s")
phoenix_s = Room("Phoenix (South)", None, None, None, None, "spawn_s", "phoenix_tower_intersection_s", None, None)
spawn_s = Room("Spawn (South)", None, None, None, None, None, "phoenix_s", None, None)

# while True:
#     command = input(">_ ")
#     print(current_node.command)


# Denim Xiong
