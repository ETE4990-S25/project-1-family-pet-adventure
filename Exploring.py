# how players interact with the world

class Exploring(object):
    """Moving around the space."""
    def __init__(self, jump, sneak):
        """ Initialize jump, sneak, and effectiveness."""
        self.jump = jump
        self.sneak = sneak
        
    

class Cat_Moves(Exploring):
    """initializes basic actions a cat can do"""
    def __init__(self, jump, sneak):
        """sets up basic actions"""
        super().__init__(self, jump, sneak)
        self.poision = True
    def furniture_leap(self):
        super().furniture_leap(self)
    def climb(self):
        super().climb(self)

class Dog_Moves(Exploring):
    """initializes basic actions a dog can do"""
    def __init__(self, jump, sneak):
        """sets up basic actions"""
        super().__init__(self, jump, sneak)
        self.poision = True

    def sprint(self, ):
        super().sprint(self)
    def paw_stand(self):
        super().paw_stand(self)