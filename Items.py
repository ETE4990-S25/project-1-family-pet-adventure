#Items.py
#General space for the physical items that may be encountered in the game
# Also, Initializes human NPC enemies that may be walking around because they can be distracted by items.
# Also menu function

def menu():
    """""Creates a menu players can access."""

    options = ["Exit Menu", "Display Inventory","Save Game"]
    print("Options: \n")
    
    for i in enumerate(options, start = 1):
        print(i)

    choice = int(input("Enter the number of the chosen option: "))

    if choice == 1:
        return 
    elif choice == 2:
        Items.display_items()
        return

    elif choice == 3:
        # Save the details of the game


        return
    else:
        return


class Items(object):
    """Initializes objects the player can interact with and store."""  
       
    def __init__(self, name, uses, description):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses #determines how many uses an object gets
        self.description = description
        
        
    def display_items(self):
        """Displays the objects you have in your inventory."""
        
        for all_Item_Data in self.inventory_template["items"]: #structure taken from ChatGPT
            print(all_Item_Data)

    
    def use_item(self):
        """Iterates the number of uses an object has."""
        uses = self.uses -1
        
        if uses > 0:
            print("Only "+ uses + " left!")
        elif uses <= 0:
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
        HumanNPC.distract_human(destraction_time)
        print("You have hidden the phone!" + (destraction_time/60) + 
              "minutes before the humans are n olonger distracted.")
        
        if self.uses == 0:
            print("You've already hidden the phone.")

        uses -= 1


# Regular items
class Stick(Items):
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
        self.destraction_time = length/2

    def unwind_yarn(self):
        """Creates a tripping hazard to distract the humans."""
        print("You have unwound the ball of yarn. This is a tripping hazard.")
        print("The humans will have to spend "+ self.destraction_time + " seconds cleaning it up.")

        HumanNPC.distract_human(self.destraction_time)


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
        print("You see . . . ")

        # find a way to show things in locked areas


class FoodBowl(Items):
    """Creates a food bowl that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def clang(self):
        """Creates a loud sound for a distraction."""
        
        destraction_time = 100
        HumanNPC(destraction_time)
        print("The bowl clangs, distracting the humans.")
        print("The humans will be destracted for the next " + 
              destraction_time + "seconds")




#For making the human NPC enemies
class HumanNPC(object):
    def __init__(self, distracted=False):
        """Initializes Human NPC states. Not distracted by default. """
        
        self.distracted = distracted

    def get_in_the_way(self):
        """Function to oppose the player. Uses chance to determine if the delay happens."""
        import time 
        import random

        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        total = dice_1 + dice_2

        if total >= 8:
            delay_time = 10
            current_time = time.time() #ChatGPT for this line
            end_time = current_time + delay_time

            while (current_time < end_time):
                print("The human is paying attention. Careful!")
            
            print("\n")
            print("The human has stopped paying attention.")
  
    
    def distract_human(self, seconds):
        """Function to stop get_in_the_way temporarily."""
        import time
                
        current_time = time.time() #ChatGPT for this line
        end_time = current_time + seconds

        while (current_time < end_time):
            self.distracted = True