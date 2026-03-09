# combat.py
import random

def start_kamp(spiller, enemy_name):
    # ... (behold logikken for kamp slik den var)
    if hit_chance > 4:
        print(f"You defeated the {enemy_name}!")
        spiller.gain_xp(30)
        # Gi spilleren en belønning
        spiller.add_item("Data-Chip") 
        return True
    # ...