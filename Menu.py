import json
from Items import Items
from Players import Player_Choice #, Dog, Cat

def save_game(player):
    """Save the game details to a json file."""
    game_data= {
        "pet_name": player.pet_name,
        "pet_type": player.pet_type,
        "jump_stat": player.jump,
        "sneak_stat": player.sneak,
        "inventory": Items.display_items(player,2)
    }

    with open("save_game.json", "w") as save_file:
        json.dump(game_data, save_file, indent=4)

    print("Game saved successfully!")


def load_game():
    try:
        with open("save_game.json", "r") as load_file:
            data = json.load(load_file)
            player = Player_Choice(data["pet_name"], data["pet_type"])
            player.jump = data["jump_stat"]
            player.sneak = data["sneak_stat"]
            player.inventory = Items.display_items(player,2)
            print("Game loaded successfully!")
            return player
    except FileNotFoundError:
        print("No saved game found.")
        return None

def menu(player):
    """""Creates a menu players can access."""

    options = ["Exit Menu", "Display Inventory","Save Game"]
    print("Options: \n")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    try:
        choice = int(input("Enter the number of the chosen option: "))
        if choice == 1:
            return 
        elif choice == 2:
            for item in player.inventory:
                print(f"Item: {item.name}, Uses: {item.uses}, Description: {item.description}") 
        elif choice == 3:
            save_game(player)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

###Game Start
# print("Welcome to Family Pet Adventure!")
# load_choice = input("Would you like to load a saved game? (yes/no): ").lower()

# if load_choice == "yes":
#     player = load_game()
#     if not player:
#         player = Player_Choice()
#         player.Select_pet()
# else:
#     player = Player_Choice()
#     player.Select_pet()

# player.display_players()
# menu(player)