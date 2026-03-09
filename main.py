# main.py - Hovedmenyen
from player import Player
from combat import start_kamp

def main():
    print("--- NEURAL DRIFT: KAMPMODUS ---")
    navn = input("Navn, merc: ")
    spiller = Player(navn)
    
    valg = input("Vil du [utforske] for å finne fiender? (ja/nei): ")
    
    if valg == "ja":
        resultat = start_kamp(spiller, "Cyber-vakt")
        if resultat:
            print("Du vant kampen!")
        else:
            print("Du overlevde så vidt...")
            
    print(spiller.status())

if __name__ == "__main__":
    main()