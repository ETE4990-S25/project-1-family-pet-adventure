###Gives option to the player to choose a pet character and their name.
##Two characters in our game are a dog or a cat.
import json
from Items import Items, Brick, Shoes, Laptop, FoodBowl, Yarn, Phone, Glasses
brick = Brick(uses=5)
shoes = Shoes(uses=5)
laptop = Laptop()
food_bowl = FoodBowl(uses=5)
yarn = Yarn(uses=5)
phone = Phone()
glasses = Glasses(uses=5)

dog_starting_items = [brick, shoes, laptop, food_bowl]
cat_starting_items = [yarn, phone, glasses]

class Player_Choice(object):
    """Creates a class to choose a player and a pet."""

    def __init__(self, pet_name=None, pet_type=None, inventory=None, jump=1.0, sneak=1.0):
        """For player's item collection."""
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.inventory = inventory if inventory is not None else []
        self.jump = jump
        self.sneak = jump

    
    def show_info(self):
        """Displays player info and available items."""
        print("=========================================")
        print(f"Pet Name: {self.pet_name}")
        print(f"Pet Type: {self.pet_type}")
        print(f"Jump Level: {self.jump}")
        print(f"Sneak Level: {self.sneak}")
        print("Available Items:")
        for item in self.inventory:
            print(f"\t-{item.name}\n\t  --{item.uses}\n\t  --'{item.description}'")
        print("=========================================")

    def select_pet(self):
        """Allow the player to select their pet and pet's name."""
        self.pet_name = input ("Please enter your pet's name: ")
        valid_choices = ["Dog", "Cat"]
        self.pet_type = ""
        
        flag = True
        while flag:
            choice = input("Please choose your pet type (Dog or Cat): ").capitalize()
            if choice in valid_choices:
                self.pet_type = choice
                flag = False
            else:
                print("Invalid choice. Please type 'Dog' or 'Cat'.")

        if choice == "Dog":          
            self.inventory = dog_starting_items
            for items in dog_starting_items:
                Items.add_item(items)

            return Dog(pet_name=self.pet_name, pet_type=self.pet_type,inventory=self.inventory, jump=1, sneak=3)
        elif choice == "Cat":
            self.inventory = cat_starting_items
            for items in cat_starting_items:
                Items.add_item(items)

            return Cat(pet_name=self.pet_name, pet_type=self.pet_type,inventory=self.inventory, jump=3, sneak=1)

    def display_players(self):
        """Display the players info with their names and pet's name."""
        print(f"\nYou're playing as a {self.pet_type} named {self.pet_name}")

class Dog(Player_Choice):
    """Represents Dog character."""
    def __init__(self, pet_name, pet_type, inventory, jump, sneak):
        super().__init__(pet_name, pet_type, inventory, jump, sneak)

        self.jump = 1
        self.sneak = 3
    
class Cat(Player_Choice):
    """Represents Cat charracter."""
    def __init__(self, pet_name, pet_type, inventory, jump, sneak):
        super().__init__(pet_name, pet_type, inventory, jump, sneak)

        self.jump = 3
        self.sneak = 1


# Testing values
# player = Player_Choice()
# animal = player.select_pet()
# print(f"Pet Type: {player.pet_type}")
# print(f"Brick:{brick}")
# player.display_players()
# player.show_info()