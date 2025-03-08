#Items.py
#General space for the items that may be encountered in the game
global endgame

class Items(object):
    """Initializes objects the player can interact with and store."""
    inventory = []
    
    def __init__(self, name, uses):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses #determines how many uses an object gets

    def display_items(self):
        """Displays the objects you have in your inventory."""
        
        print("Your Inventory: ")
        for items in self.inventory:
            print(items)
    
    def use_item(self):
        """Iterates the number of uses an object has."""
        uses = uses -1
        
        if uses != 0:
            print("You have used this object! Only "+ uses + " left!")
        elif uses == 0:
            print("You have used this object! No more uses left.")
    
    def take_item(self, thing):
        """Allows the player to put the object in their inventory."""
        self.inventory.append(thing)
        print("You have added "+ thing+" to your inventory.")

    def eat_item(self, item):
        """Allows the player to eat an item in their inventory."""
        
        print("You have eaten "+ item)
        self.inventory.pop(item)
        self.endgame = True

    def drop_item(self, item):
        """The player will drop an item in their inventory."""
        self.inventory.remove(item)
        print("You have chosen to drop "+ item)
        

class Key(Items):
    """Initializes keys that the player is trying to find."""
    def __Init__(self, name, uses):
        super().__init__(self, name, uses)
        """Sets up the basic instances of the key."""

        uses = 1

    def use_key(self):
        """Allows the player to get to locked spaces."""
        
        uses = uses -1
        print("You have used the key.")

class TreatJar(Items):
    """Initializes the treat jar (goal of game)."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)
        """Brings the function of the Items class here"""

        uses = 1

    def end_game(self):
        """Ends the game when the player finds the treat jar."""
        
        print("You found the treat jar! Congratulations!")
        return "The End!"




class Laptop(Items):
    """Creates a laptop that can be used. Careful!"""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def doggy_cam(self, password):
        """Allows the player to turn off the doggy cams."""
        if password == 1111:
            print("The cameras are disabled.")

class Phone(Items):
    """Creates a phone that can be used. Careful!"""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def hide_phone(self):
        """Hides humans' phone to create a distraction."""

        print("You have hidden the phone!")




class Stick(Items):
    """Creates a stick that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)


class Yarn(Items):
    """Creates a ball of yarn that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def unwind_yarn(self):
        """Creates a tripping hazard to distract the humans."""
        print("You have unwound the ball of yarn. This is a tripping hazard.")


class Shoes(Items):
    """Creates a shoe that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)

    def super_jump(self):
        """When worn, the player can jump 3x their usual height."""
        
        # import Exploring.jump_up() as jump

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
        print("The bowl clangs, distracting the humans.")
