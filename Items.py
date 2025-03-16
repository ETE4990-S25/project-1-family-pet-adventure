#Items.py
#General space for the physical items that may be encountered in the game
# Also, Initializes human NPC enemies that may be walking around because they can be distracted by items.
# Also menu function

import json

def save_game(player):
    """Save the game details to a json file."""
    game_data= {
        "pet_name": player.pet_name,
        "pet_type": player.pet_type,
        "jump_stat": player.jump,
        "sneak_stat": player.sneak,
        "inventory": [{"name": Items.name, "uses": Items.uses, "description": Items.description} for item in player.inventory]
    }

    with open("save_game.josn", "w") as save_file:
        json.dump(game_data, save_file, indent=4)

    print("Game saved successfully!")

def menu(player):  # added player parameter to resolve warning. 
    """""Creates a menu players can access."""

    options = ["Exit Menu", "Display Inventory","Save Game"]
    print("Options: \n")
    
    for i in enumerate(options, start = 1):
        print(i)

    choice = int(input("Enter the number of the chosen option: "))

    if choice == 1:
        return 
    elif choice == 2:
        for item in player.inventory:
            print(f"Item: {item.name}, Uses: {item.uses}, Description: {item.description}") 
        return

    elif choice == 3:
        save_game(player)
        return
    else:
        print("Invalid choice.")
    


#Items.py
#General space for the physical items that may be encountered in the game
# Also, Initializes human NPC enemies that may be walking around because they can be distracted by items.
# Also menu function

class Items(object):
    """Initializes objects the player can interact with and store."""  
       
    def __init__(self, name=None, uses=None, description=None, inventory_template=None):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses #determines how many uses an object gets
        self.description = description
        self.inventory_template= inventory_template
        
    def display_items(self):
        """Displays the objects you have in your inventory."""
        
        import json
        with open('Item_Data.json') as Item_Data:
            self.inventory_template = json.load(Item_Data)
        #print(json.dumps(shows, indent=2))
        inventory = json.dumps(self.inventory_template, indent=2)


        for all_Item_Data in self.inventory_template["items"]: #structure taken from ChatGPT
            print(all_Item_Data)

    
    def use_item(self):
        """Iterates the number of uses an object has."""
        self.uses -= 1
        
        if self.uses > 0:
            print("Only "+ self.uses + " left!")
        elif self.uses <= 0:
            print("Not so fast! Any more uses of this object, "
            "and the humans may get suspicious")
    
    def take_item(self, thing):
        """Allows the player to put the object in their inventory."""

        # import json
        # with open('Item_Data.json', 'r') as Item_Data: # taken from online
        #     data = json.load(Item_Data)
        #     data["name"] = self.name
        #     data["description"] = self.description
        #     data["uses"] = self.uses

        # with open('Item_Data.json', 'w') as Item_Data:
        #     json.dump(data, Item_Data)

        import json
        with open('Item_Data.json') as Item_Data:
            inventory_template = json.load(Item_Data)
        #print(json.dumps(shows, indent=2))
        inventory = json.dumps(inventory_template, indent=2)


        # self.inventory.append(thing)
        print("You have added "+ thing+" to your inventory.")


        #taken from ChatGPT
        # Iterate through the list of items
        for item in self.inventory_template["items"]:
            # Check for the condition where you want to modify the value
        
            x = 0
            for i in range(0, 11):
                if item["id"] == i:

                    if item["name"] == "Empty Slot":
                        # Change the 'name' value of the item with id 0
                        item["name"] = self.name  # You can change this to any value you want
                        item["description"] = self.description
                        item["uses"] = self.uses
                        
                        x = 1
                        break

                    if x == 1: 
                        break
                
                if x == 1:
                    break
            if x == 1:
                break
       
        # with open('Item_Data.json', 'w') as Item_Data:
        #     json.dump(data, Item_Data)



    def drop_item(self, number):
        """The player will drop an item in their inventory."""
        
        Items.display_items()

        int(input("What is the slot number of the item you want to drop?"))
        print("You have chosen to drop "+ number)

        #modified from ChatGPT
        # Iterate through the list of items
        for item in self.inventory_template["items"]:

            if item["id"] == number:
                item["name"] = "Empty Slot"  
                item["description"] = "Empty Slot"
                item["category"] = "Empty Slot"
        
# Endgame items. 
class Key(Items):
    """Initializes keys that the player is trying to find."""
    def __Init__(self, name, uses, description):
        super().__init__(self, name, uses, description)
        """Sets up the basic instances of the key."""

        uses = 1
        self.description = "Key"

    def use_key(self):
        """Allows the player to get to locked spaces."""
        
        uses = uses -1
        print("You have used the key.")

class TreatJar(Items):
    """Initializes the treat jar (goal of game)."""
    def __init__(self, name, uses, description):
        super().__init__(self, name, uses, description)
        """Ends the game."""

        uses = 1
        self.description ="Treat Jar"

        print("You found the treat jar! Congratulations!")
        return "The End!"

       


# Human items. Items that belong to the humans, but you can manipulate. 
class Laptop(Items):
    """Creates a laptop that can be used."""
    def __init__(self, name, uses, description):
        super().__init__(self, name, uses, description)

        self.uses = 1
        self.description = "Laptop"

    def pet_cam(self, password):
        """Allows the player to turn off the doggy cams."""
        if password == 1111:
            print("The cameras are disabled.")

        if self.uses == 0:
            print("You have already turned the cameras off.")


class Phone(Items):
    """Creates a phone that can be used. Careful!"""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

        uses = 1

        

    def hide_phone(self):
        """Hides humans' phone to create a distraction."""
        
        destraction_time = 1000
        print("You have hidden the phone!" + (destraction_time/60) + 
              "minutes before the humans are n olonger distracted.")
        
        if self.uses == 0:
            print("You've already hidden the phone.")

        uses -= 1


# Regular items
class Brick(Items):
    """Creates a stick that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def poke(self):
        """Allows user to use the stick. Great for annoying humans."""
        
        print("You have used the stick to poke at the thing in front of you.")
        Items.use_item()


class Yarn(Items):
    """Creates a ball of yarn that can be used."""
    def __init__(self, name, uses, length):
        super().__init__(self, name, uses)

        self.length = length


    def unwind_yarn(self):
        """Creates a tripping hazard to distract the humans."""
        print("You have unwound the ball of yarn. This is a tripping hazard.")
        print("The humans will have to spend five minutes cleaning it up.")



class Shoes(Items):
    """Creates a shoe that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def super_jump(self):
        """When worn, the player can jump 3x their usual height."""
        
        import Exploring
        jump = Exploring.jump_up()

        jump = jump*3 
        print("You super jumped!")
        print("Height: "+jump)


class Glasses(Items):
    """Creates a pair of glasses that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def xray_vision(self):
        """Allows the player to see into locked areas."""

        print("X-Ray vision!")
        print("You see . . . the treat jar! It has your favorite treats!")

        # find a way to show things in locked areas


class FoodBowl(Items):
    """Creates a food bowl that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def clang(self):
        """Creates a loud sound for a distraction."""
        
        destraction_time = 100
        print("The bowl clangs, distracting the humans.")
        print("The humans will be destracted for the next " + 
              destraction_time + "seconds")
