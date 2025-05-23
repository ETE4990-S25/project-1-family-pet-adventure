#Items.py
#General space for the physical items that may be encountered in the game
import json

class Items(object):
    """Initializes objects the player can interact with and store."""  
       
    def __init__(self, name=None, uses=None, description=None, inventory_dictionary=None):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses #determines how many uses an object gets
        self.description = description
        self.inventory_dictionary = inventory_dictionary


    def display_items(self, mode): # Moved from Items class
        """Displays the objects you have in your inventory."""

        with open('Item_Data.json') as Item_Data:
            inventory_dictionary = json.load(Item_Data)

        if mode == 1:
            """Displays inventory on console"""
            for all_Item_Data in inventory_dictionary["items"]: #structure taken from ChatGPT
                print(all_Item_Data)
        elif mode == 2: 
            """Returns inventory values to whoever is asking"""
            return inventory_dictionary
        else: 
            return

    def add_item(self):
        """Allows the player to put the object in their inventory."""
        
        with open('Item_Data.json') as Item_Data:
            inventory_dictionary = json.load(Item_Data) # this is the actual json object

        print(f"You have added {self.name} to your inventory.")

        flag = False

        for item in inventory_dictionary["items"]:

            if item["name"] == "Empty Slot":
                item["name"] = self.name 
                item["description"] = self.description
                item["uses"] = self.uses
                flag = True

                break
            
        if flag: # structure for saving item data taken from ChatGPT
            with open('Item_Data.json', 'w') as Item_Data:  
                json.dump(inventory_dictionary, Item_Data, indent=2)  

            print("Inventory successfully updated!")
        else:
            print("No empty slots available for the new item.")
       
    def drop_item(self):
        """The player will drop an item in their inventory."""
        
        self.display_items(1)
        inventory_dictionary = self.display_items(2)

        input_flag = True
        while input_flag:
            try:
                number = int(input("What is the slot number of the item you want to drop?"))
                print(f"You have chosen to drop {number}")
                input_flag = False
            
            except ValueError or TypeError:
                print("Oops! You have entered an invalid input.")
        
        flag = False
        for item in inventory_dictionary["items"]:
            if item["id"] == number:
                item["name"] = "Empty Slot" 
                item["description"] = "Empty Slot"
                item["uses"] = "Empty Slot"
                flag = True

                break
            
        if flag: # structure for saving item data taken from ChatGPT
            with open('Item_Data.json', 'w') as Item_Data:  
                json.dump(inventory_dictionary, Item_Data, indent=2)  

            print("Inventory successfully updated!")
        else:
            print("No empty slots available for the new item.")

# Endgame items. 

class TreatJar(Items):
    """Initializes the treat jar (goal of game)."""
    def __init__(self, name="Treat Jar", uses=1, description = "Treat Jar", inventory_dictionary = None):
        super().__init__(name, uses, description, inventory_dictionary)
        """Ends the game."""

        self.uses = uses
        self.description ="Treat Jar"

        print("You found the treat jar! Congratulations!")




# Human items. Items that belong to the humans, but you can manipulate. 
class Laptop(Items):
    """Creates a laptop that can be used."""
    def __init__(self, name="Laptop", uses=1, description="Laptop", inventory_dictionary=None):
        super().__init__(name, uses, description, inventory_dictionary)

        self.uses = uses
        self.description = description

    def pet_cam(self, password):
        """Allows the player to turn off the doggy cams."""
        if password == 2854:
            print("The cameras are disabled.")

        if self.uses == 0:
            print("You have already turned the cameras off.")


class Phone(Items):
    """Creates a phone that can be used. Careful!"""
    def __init__(self, name="Phone", uses=None, description = "A human's phone. Hide it to distract them.", inventory_dictionary = None):
        super().__init__(name, uses, description, inventory_dictionary)

        self.uses = 1   

    def hide_phone(self):
        """Hides humans' phone to create a distraction."""
        
        destraction_time = 1000
        
        if self.uses == 0:
            print("You've already hidden the phone.")
        else:
            print(f"You have hidden the phone! {destraction_time/60} minutes before the humans are no longer distracted.")
            self.uses -= 1


# Regular items
class Brick(Items):
    """Creates a brick that can be used."""
    def __init__(self, name="Brick", uses=None, description = "A heavy brick.", inventory_dictionary=None):
        super().__init__(name, uses, description, inventory_dictionary)

        self.name = name
        self.uses = uses
        self.description = description

    def throw(self):
        """Allows user to use the brick. Great for moving a pile of sticks."""

        self.uses -= 1
        if self.uses > 0:
            print("You have thrown the brick into the obstacle to clear it.")
            print(f"Only {self.uses} left!")
        elif self.uses <= 0:
            print("Not so fast! Any more uses of this object, "
            "and the humans may get suspicious")
            self.drop_item()


class Yarn(Items):
    """Creates a ball of yarn that can be used."""
    def __init__(self, name="Yarn", uses=None, description = "Yarn 100ft long.", inventory_dictionary = None):
        super().__init__(name, uses, description, inventory_dictionary)

        self.name = name
        self.uses = uses
        self.description = description


    def net_yarn(self):
        """Help to net the key out of the pile of shredded paper."""
        self.uses -= 1
        if self.uses > 0:
            print(f"Only {self.uses} left!")
        elif self.uses <= 0:
            print("Not so fast! Any more uses of this object, "
            "and the humans may get suspicious")
            self.drop_item()
        print("You can use the yarn to create a net and get your key out of a pile of shredded paper.")
        print("The humans will have to spend five minutes cleaning it up.")



class Shoes(Items):
    """Creates a shoe that can be used."""
    def __init__(self, name="Shoes", uses=None, description = "Shoes to help you superjump.", inventory_dictionary = None):
        super().__init__(name, uses, description, inventory_dictionary)
        self.name = name
        self.uses = uses
        self.description = description

    def super_jump(self):
        """When worn, the player can jump over any obstacle
        and towards whatever their heart desires most."""

        self.uses -= 1
        if self.uses > 0:
            print("You super jumped!")
            print("You were able to clear this obstacle and get one step closer to the key.")
            print(f"Only {self.uses} left!")
        elif self.uses <= 0:
            print("Not so fast! Any more uses of this object, "
            "and the humans may get suspicious")
            self.drop_item()



class Glasses(Items):
    """Creates a pair of glasses that can be used."""
    def __init__(self, name="Glases", uses=None, description = "Sees through obstacles", inventory_dictionary = None):
        super().__init__(name, uses, description, inventory_dictionary)
        self.name = name
        self.uses = uses
        self.description = description

    def night_vision(self):
        """Allows the player to see into locked areas."""

        self.uses -= 1
        if self.uses > 0:
            print(f"Only {self.uses} left!")
        elif self.uses <= 0:
            print("Not so fast! Any more uses of this object, "
            "and the humans may get suspicious")
            self.drop_item()

        print("Night vision!")
        print("You can pass the tunnel using the night vision.")



class FoodBowl(Items):
    """Creates a food bowl that can be used."""
    def __init__(self, name="Food Bowl", uses=None, description="Empty food bowl to make a loud sound", inventory_dictionary=None):
        super().__init__(name, uses, description, inventory_dictionary)
        self.name = name
        self.uses = uses
        self.description = description

    def clang(self):
        """Creates a loud sound for a distraction."""
        
        destraction_time = 100
        print("The bowl clangs, distracting the humans.")
        print(f"The humans will be destracted for the next {destraction_time} seconds")
