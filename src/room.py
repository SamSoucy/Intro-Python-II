# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desciption, items=None):
        self.name = name,
        self.description = description
        if items is None:
            self.inventory = []
        else:
            self.inventory = items
            self.n_to = None
            self.s_to = None
            self.e_to = None
            self.w_to = None
        def __repr__(self):
            room_string = f"{self.name[0]}\n"
            room_string += f"Description: {self.description}\n"
            room_string += f"Move: {self.can_move()}\n"
            if len(self.inventory) > 0:
                room_string += f"Can get: {self.get_items()}"
                return room_string
        def can_move(self):
            move = []
            if self.n_to is not None:
                move.append("n")
            if self.s_to is not None:
                    move.append("s")
            if self.e_to is not None:
                    move.append("e")
            if self.w_to is not None:
                move.append("w")
            return ",".join(move)
        def get_items(self):
            return ", ".join([str(i) for i in self.inventory])
        def get_room_in_direction(self, direction):
            if direction == "n":
                return self.n_to
            elif direction == "e":
                return self.e_to
            elif direction == "s":
                return self.s_to
            elif direction == "w":
                return self.w_to
            

   