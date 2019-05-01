# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, curt_room):
        self.name = name
        self.curt_room = curt_room
        self.items = []
    def move(self, direction):
        if direction in ["n", "e", "s", "w"]:
            move_rooms = self.curt_room.that_room(direction)
            if move_rooms is not None:
                self.curt_room = move_rooms
                print(self.curt_room)
            else:
                print("Cannot go in that direction.")