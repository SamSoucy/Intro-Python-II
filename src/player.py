# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def move(self, direction):
        if direction in ["n", "e", "s", "w"]:
            move_rooms = self.current_room.that_room(direction)
            if move_rooms is not None:
                self.current_room = move_rooms
                print(self.current_room)
            else:
                print("Cannot go in that direction.")