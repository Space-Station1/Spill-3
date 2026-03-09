# player.py
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        self.xp = 0
        self.inventory = []

    def status(self):
        return f"Name: {self.name} | Level: {self.level} | XP: {self.xp} | Health: {self.health}"

    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP!")
        if self.xp >= 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.health += 20
        print(f"--- CONGRATULATIONS! You reached level {self.level}! Health increased to {self.health}. ---")

    def take_damage(self, amount):
        self.health -= amount
        print(f"You took {amount} damage! Health is now: {self.health}.")