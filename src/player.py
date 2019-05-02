# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def travel(self, direction):
        if direction in ["n", "s", "e", "w"]:
            move_rooms = self.current_room.get_room_in_direction(direction)
            if move_rooms is not None:
                self.current_room = move_rooms
                print(self.current_room)
            else:
                print("Cannot go in that direction.")