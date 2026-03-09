# main.py - Starten på ditt spill

def spill_loop():
    print("Spillet har startet!")
    spiller_navn = input("Hva heter helten din? ")
    
    # Dette er selve hjertet av spillet
    kjører = True
    while kjører:
        valg = input(f"Velkommen {spiller_navn}. Vil du [utforske] eller [avslutte]? ")
        
        if valg == "utforske":
            print("Du går inn i den neon-belyste byen...")
        elif valg == "avslutte":
            print("Takk for at du spilte!")
            kjører = False
        else:
            print("Det forsto jeg ikke, prøv igjen.")

if __name__ == "__main__":
    spill_loop()
