#Items.py
#General space for the items that may be encountered in the game

class Items(object):
    """Initializes objects the player can interact with."""
    def __init__(self, name, uses):
        """Sets up the basic details of the object."""

        self.name = name
        self.uses = uses