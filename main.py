# main.py
from player import Player
from combat import start_kamp

def main():
    print("--- NEURAL DRIFT: COMBAT MODE ---")
    name = input("Enter your name, Merc: ")
    player = Player(name)
    
    choice = input("Do you want to [explore] to find enemies? (yes/no): ")
    
    if choice.lower() == "yes":
        result = start_kamp(player, "Cyber-Guard")
        if result:
            print("Victory!")
        else:
            print("You barely survived...")
            
    print(player.status())

if __name__ == "__main__":
    main()