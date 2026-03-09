# combat.py - Logikk for kamp
import random

def start_kamp(spiller, fiende_navn):
    print(f"\nDu møter en {fiende_navn}!")
    
    # Vi ruller et tilfeldig tall mellom 1 og 10
    treff_sjanse = random.randint(1, 10)
    
    if treff_sjanse > 4:
        print(f"Du angriper {fiende_navn} og treffer perfekt!")
        return True # Seier
    else:
        print(f"Du prøvde å angripe {fiende_navn}, men bommet totalt!")
        spiller.take_damage(10)
        return False # Tap