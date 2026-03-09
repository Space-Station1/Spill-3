# main.py
from player import Player
from combat import start_kamp

def main():
    print("--- NEURAL DRIFT: WELCOME TO NIGHT CITY ---")
    name = input("Enter your name, Merc: ")
    player = Player(name)
    
    running = True
    while running:
        print("\n--- MAIN MENU ---")
        print("1. Explore (Find enemies)")
        print("2. Check Status")
        print("3. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            start_kamp(player, "Cyber-Guard")
        elif choice == "2":
            print(f"\nSTATUS: {player.status()}")
        elif choice == "3":
            print("Disconnecting... Goodbye, Merc.")
            running = False
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()