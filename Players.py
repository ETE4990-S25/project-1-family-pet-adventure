###Gives option to the player to choose a pet character and their name.
##Two characters in our game are a dog or a cat.
import json
class Player_Choice(object):
    """Creates a class to choose a player and a pet."""

    def __init__(self, pet_name=None, pet_type=None, available_items=None):
        """For player's item collection."""
        self.pet_name = pet_name
        self.pet_type= pet_type
        self.inventory= []
        self.jump= 1.0
        self.sneak=1.0
        self.available_items = available_items if available_items else []

        starting_items = ["Brick","Shoes", "Laptop", "Food Bowl"]
        player = Player_Choice("Bobby", "Dog", available_items=starting_items)
        print("Available items for the player:", player.available_items)
    
    def show_info(self):
        """Displays player info and available items."""
        print(f"Pet Name: {self.pet_name}")
        print(f"Pet Type: {self.pet_type}")
        print(f"Jump Level: {self.jump}")
        print(f"Sneak Level: {self.sneak}")
        print("Available Items:")
        for item in self.available_items:
            print(f" - {item}")
        print()

    def Select_pet(self):
        """Allow the player to select their pet and pet's name."""
        self.pet_name = input ("Please enter your pet's name: ")
        valid_choices = ["Dog", "Cat"]
        self.pet_type = ""
        
        while self.pet_choice not in valid_choices:
            choice = input("Please choose your pet type (Dog or Cat): ").capitalize()
        if choice in valid_choices:
            self.pet_type = choice
        else:
            print("Invalid choice. Please type 'Dog' or 'Cat'.")
    def display_players(self):
        """Display the players info with their names and pet's name."""
        print(f"\nYou're playing as a {self.pet_type} named {self.pet_name}")


class Items(object):
      """Represents collectible and usuable items."""

      def __init__(self, name, uses, description):
           """Initialize the item."""
           self.name= name
           self.uses= uses
           self.description= description

      def use_item(self):
           """Uses an item if available."""
           if self.uses >0:
                self.uses -=1
                print(f"You've used the {self.name}. You have {self.uses} left in your inventory.")
           else:
                print(self.name + "has no uses left.")

      def display_item(self):
           """Displays item information."""
           print("Item: " + self.name + ":" + self.description + "(Uses:" +str(self.uses)+")")

player = Player_Choice()
player.Select_pet()

if player.pet_type == "Dog":
    player.available_items = ["Brick", "Shoes", "Laptop", "Food Bowl"]
else:
    player.available_items = ["Yarn", "Glasses", "Phone"]

player.display_players()
player.show_info()

#representative of Menu.py file
def save_game(player):
    """Save the game details to a json file."""
    game_data= {
        "pet_name": player.pet_name,
        "pet_type": player.pet_type,
        "jump_stat": player.jump,
        "sneak_stat": player.sneak,
        "inventory": [{"name": Items.name, "uses": Items.uses, "description": Items.description} for item in player.inventory]
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
            player.inventory = [Items(item["name"], item["uses"], item["description"]) for item in data["inventory"]]
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
print("Welcome to Family Pet Adventure!")
load_choice = input("Would you like to load a saved game? (yes/no): ").lower()

if load_choice == "yes":
    player = load_game()
    if not player:
        player = Player_Choice()
        player.Select_pet()
else:
    player = Player_Choice()
    player.Select_pet()

player.display_players()
menu(player)


#class Exploring(object):
#     """Moving around the space."""
#     def __init__(self, jump=1.0, sneak=1.0):
#         """ Initialize jump, and sneak."""
#         self.jump = jump
#         self.sneak = sneak
    
#     def jump_up(self):
#         """Allows player to jump. The more the player jumps, the stronger they become."""

#         print(f"You jump {self.jump} units.")  ###Learned to use f and {} instead of + here since a float is being passed from the internet. 
#         self.jump+= 0.25

#     def sneaking(self):
#         """Allows player to sneak around. The more the player does so, the stronger they become."""
#         print("You decide to sneak.")
#         self.sneak+= 0.25
        
#     def get_stats(self):
#         """Displays the stats of the player on the console."""
#         print("Your general stats are as follows: ")
#         print(f"Jump stat: {self.jump} units.")
#         print(f"Sneak stat: {self.sneak} units.")