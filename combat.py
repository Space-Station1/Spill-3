# combat.py - Kamp gir nå XP
import random

def start_kamp(spiller, fiende_navn):
    print(f"\nDu møter en {fiende_navn}!")
    
    treff_sjanse = random.randint(1, 10)
    
    if treff_sjanse > 4:
        print(f"Du beseiret {fiende_navn}!")
        spiller.gain_xp(30) # Spilleren får 30 XP
        return True
    else:
        print(f"Du bommet på {fiende_navn} og fikk bank!")
        spiller.take_damage(15)
        return False