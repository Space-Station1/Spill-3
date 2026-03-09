# player.py - Oppdatert med XP og Level
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        self.xp = 0
        self.inventory = []

    def status(self):
        return f"Navn: {self.name} | Lvl: {self.level} | XP: {self.xp} | Helse: {self.health}"

    def gain_xp(self, amount):
        self.xp += amount
        print(f"Du fikk {amount} XP!")
        if self.xp >= 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.health += 20
        print(f"--- GRATULERER! Du har nådd level {self.level}! Helsen din økte til {self.health}. ---")

    def take_damage(self, amount):
        self.health -= amount
        print(f"Du tok {amount} skade! Helse: {self.health}.")