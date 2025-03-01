# how players interact with the world

class Exploring(object):
    """Moving around the space."""
    def __init__(self, jump, sneak):
        """ Initialize jump, sneak, and effectiveness."""
        self.jump = jump
        self.sneak = sneak
    
    def jump_up(self, jump):
        """Allows player to jump. The more the player jumps, the stronger they become."""
        
        print("You jump "+ jump +"units.")
        #jump = jump + 0.25

    def sneaking(self, sneak):
        sneak = sneak + 1
        print("You decide to sneak.")
        
class CatMoves(Exploring):
    """initializes basic actions a cat can do"""
    def __init__(self, jump, sneak):
        """sets up basic actions"""
        super().__init__(self, jump, sneak)
        
    def furniture_leap(self):
        super().furniture_leap(self)
        print("You jump onto the furniture.")

    def climb(self):
        super().climb(self)
        print("You climb up the stucture.")

class DogMoves(Exploring):
    """initializes basic actions a dog can do"""
    def __init__(self, jump, sneak):
        """sets up basic actions"""
        super().__init__(self, jump, sneak)
        
    def sprint(self, ):
        super().sprint(self)
        print("You sprint.")

    def paw_stand(self):
        super().paw_stand(self)
        print("You stand.")