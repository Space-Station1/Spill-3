# combat.py
import random

def start_kamp(spiller, enemy_name):
    print(f"\nYou encounter a {enemy_name}!")
    
    hit_chance = random.randint(1, 10)
    
    if hit_chance > 4:
        print(f"You defeated the {enemy_name}!")
        spiller.gain_xp(30)
        return True
    else:
        print(f"You missed the {enemy_name} and took damage!")
        spiller.take_damage(15)
        return False