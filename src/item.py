class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name}"
    def on_take(self):
        print("on_take placeholder")
        return self
    def on_drop(self):
        print("on_drop placeholder")