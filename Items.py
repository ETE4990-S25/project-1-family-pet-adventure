#Items.py
#General space for the items that may be encountered in the game

class Items(object):
    """Initializes objects the player can interact with."""
    def __init__(self, name, uses):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses

        uses = 5

    def use_object(self):
        uses = uses -1
        print("You have used this object! Only "+ uses + " left!")

class Key(Items):
    """Initializes keys that the player is trying to find."""
    def __Init__(self, ):
        super().__init__