# main.py - Hovedmenyen
from player import Player

def main():
    print("--- VELKOMMEN TIL NEURAL DRIFT ---")
    navn = input("Hva er navnet ditt, merc? ")
    
    # Vi oppretter spilleren basert på klassen i player.py
    spiller = Player(navn)
    
    print(f"\nVelkommen til Night City, {spiller.name}.")
    print(spiller.status())
    
    valg = input("\nVil du [utforske] eller [hvile]? ")
    
    if valg == "utforske":
        print("Du går ut i regnet. En vakt ser deg og angriper!")
        spiller.take_damage(20)
        print(spiller.status())

if __name__ == "__main__":
    main()