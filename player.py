# player.py - Her holder vi styr på karakterens egenskaper

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def status(self):
        return f"Navn: {self.name} | Helse: {self.health} | Ryggsekk: {self.inventory}"

    def take_damage(self, amount):
        self.health -= amount
        print(f"Du tok {amount} skade! Din helse er nå {self.health}.")