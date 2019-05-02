from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Sam", room['outside'])

sword = Item("sword", "Very sharp and pointy!")
shield = Item("shield", "The better to defend myself with!")
rope = Item("rope", "Can do anthing!")

room['outside'].inventory.extend([sword, shield, rope])
room['foyer'].inventory.extend([sword, shield, rope])
room['foyer'].inventory.extend([sword, shield, rope])
room['foyer'].inventory.extend([sword, shield, rope])
room['overlook'].inventory.extend([sword, shield, rope])
room['narrow'].inventory.extend([sword, shield, rope])
room['narrow'].inventory.extend([sword, shield, rope])
room['treasure'].inventory.extend([sword, shield, rope])


valid_directions = ["n", "e", "s", "w"]

# Write a loop that:
print(player.current_room)

def item_loop():
    item = ""
    while item is not "q":
        args = player.current_room.get_item_selector()
        print(args)
        item = input(f"Aquire Item: [{args}] [take or drop] or [q] =>")
        if item.find(" ") >= 0:
            item_value = item[:4]
            item_command = item[5:]
            if item_command == "take":
                if item_value in args:
                    print("take item")
                else:
                    print("Cannot take item")
            elif item_command == "drop":
                if item_value in args:
                    print("drop item")
                else:
                    print("Cannot drop item")
            else:
                print("Not right command")
                   


while True:
    cmd = input("Travel to: [n] [s] [e] [w], Take: [t], Drop: [d] or [q] =>")
    if cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "t":
         item_loop()
    elif cmd == "d":
        item_loop()
    elif cmd == "q":
        print("Goodbye Player!")
        break
    else:
        print("Cannot go that way!")

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
