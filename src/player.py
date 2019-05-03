# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def get_item_selector(self):
        return ", ".join([str(f"{i}") for i in self.inventory])
    def travel(self, direction):
        if direction in ["n", "s", "e", "w"]:
            move_rooms = self.current_room.get_room_in_direction(direction)
            if move_rooms is not None:
                self.current_room = move_rooms
                print(f'Current room: \n{self.current_room}\n')
            else:
                print("Cannot go in that direction.")
                print(f'Current room: \n{self.current_room}\n')
    def handle_action(self, action, value):
        if action == "take":
            object_in_room = self.current_room.find_item(value)
            self.inventory.append(object_in_room)
            print(f'Player inventory after take: {self.inventory}\n')
        elif action == "drop":
            for index2, val_loop in enumerate(self.inventory):
                if val_loop.name == value:
                    add_val = self.inventory[index2]
                    self.current_room.add_item(add_val)
                    del self.inventory[index2]
                    print(f"Player inventory after drop: {self.inventory}\n")