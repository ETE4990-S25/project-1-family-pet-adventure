#Items.py
#General space for the items that may be encountered in the game

class Items(object):
    """Initializes objects the player can interact with."""
    def __init__(self, name, uses):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses #determines how many uses an object gets

    def use_object(self):
        """Iterates the number of uses an object has."""
        uses = uses -1
        
        if uses != 0:
            print("You have used this object! Only "+ uses + " left!")
        elif uses == 0:
            print("You have used this object! No more uses left.")
    
    def take_object(self):
        """Allows the player to put the object in their inventory."""
        inventory = {}

        x = 1

        

class Key(Items):
    """Initializes keys that the player is trying to find."""
    def __Init__(self, name, uses):
        super().__init__(self, name, uses)
        """Sets up the basic instances of the key."""

        uses = 1

class TreatJar(Items):
    """Initializes the treat jar (goal of game)."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)
        """Brings the function of the Items class here"""

        uses = 1

class Stick(Items):
    """Creates a stick that can be used."""
    def __init__(self, name, uses):
        super().__init__(self, name, uses)
