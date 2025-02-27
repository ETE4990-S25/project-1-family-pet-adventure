# how players interact with the world
#Game Classes as of 2/7/2025
class Exploring(object):
    """Moving around the space."""
    def __init__(self, jump, sneak, effectiveness=0):
        """ Initialize jump, sneak, and effectiveness."""
        self.jump = jump
        self.sneak = sneak
        self.effectiveness = effectiveness
    def how_effective(self, target):
        target = target - self.effectiveness

class Cat_Moves(Exploring):
    """initializes basic actions a cat can do"""
    def __init__(self, jump, sneak, effectiveness=0):
        """sets up basic actions"""
        super().__init__(self, jump, sneak, effectiveness)
        self.poision = True
    def furniture_leap(self, effectiveness=0):
        super().furniture_leap(self, effectiveness)
    def climb(self, effectiveness=0):
        super().climb(self, effectiveness)

class Dog_Moves(Exploring):
    """initializes basic actions a dog can do"""
    def __init__(self, jump, sneak, effectiveness=0):
        """sets up basic actions"""
        super().__init__(self, jump, sneak, effectiveness)
        self.poision = True
    def sprint(self, effectiveness=0):
        super().sprint(self, effectiveness)
    def paw_stand(self, effectiveness=0):
        super().paw_stand(self, effectiveness)