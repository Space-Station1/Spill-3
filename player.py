# player.py
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        self.xp = 0
        self.inventory = [] # Her lagres gjenstandene dine

    def add_item(self, item_name):
        self.inventory.append(item_name)
        print(f"You picked up: {item_name}")

    def status(self):
        return f"Name: {self.name} | Lvl: {self.level} | Health: {self.health} | Inventory: {self.inventory}"

    # ... behold gain_xp, level_up og take_damage slik de var