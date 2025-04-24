# Exploring
# how players interact with the world
import Items
import random
class Moves(object):
    """Moving around the space."""
    def __init__(self, jump = 1, sneak = 1):
        """ Initialize jump, and sneak."""
        self.jump = jump
        self.sneak = sneak
    
    def jump_up(self):
        """Allows player to jump. The more the player jumps, the stronger they become."""
        print(f"You jump {self.jump} units.")  ###Learned to use f and {} instead of + here since a float is being passed from the internet. 
        self.jump+= 0.25

    def get_stats(self):
        """Displays the stats of the player on the console."""
        print("Your general stats are as follows: ")
        print(f"Jump stat: {self.jump} units.")
        print(f"Sneak stat: {self.sneak} units.") 
# Child classes      
class CatMoves(Moves):
    """Represents the actions a cat can do."""
    def __init__(self, jump, sneak):
        """Sets up basic actions and specific actions."""
        super().__init__(jump, sneak)
        self.high_leap = True
        self.climb = True
        
    def furniture_leap(self):
        if self.high_leap: 
            print("You jump onto the furniture.")
        else:
            print("Your attempt failed.")

    def perform_action(self):
        if self.climb:
            print("You climb up the stucture.")
        else:
            print("You can't climb right now.")

    def cat_walking_and_obstacles(self): #added function name and took while from gameplay section
        """Mechanic for walking around the game and discovering things."""
        import Items
        import random
        yarn= Items.Yarn(name="Yarn", uses=10)
        glasses = Items.Glasses("Glasses", 5)
        phone = Items.Phone("Phone", 5) 
        
        x = 0
        
        while x != 6: # to keep the player in a playing loop, looking around the room
            
            print("You walk around the room, searching for the key . . .\n")
            
            if x%2==0:
                print("You find a pile of shredded paper. Does this have the key? Use your inventory.\n")
            elif x%2==1:
                print("You come across a tunnel. Use your inverntory to cross it.\n")
            elif x%2==2:
                print("You hear a human approaching. Distract them.")
                        
            print("You have 4 options to explore: \n1:Furniture Leap \n2:Get_stats \n3:Jump Up \n4:Climb up.")
            print("=============")
            print("You have 3 items to use to find your key: \n1:Yarn  \n2:Glasses \n3:Phone.")
            print("=============")
            
            move_choice= input("Choose an action (1-4):")
            item_choice= input("chosee an object(1-3):")
            moves={ "1": self.furniture_leap,
                    "2": self.get_stats,
                    "3": self.jump_up,
                    "4": self.climb_up}
            if move_choice in moves:
                moves[move_choice]()
            else:
                print("invalid move choice.")
            
            
            objects={"1":yarn.net_yarn, 
                    "2":glasses.night_vision, 
                    "3":phone.hide_phone}
            if item_choice in objects:
                objects[item_choice]()
            else:
                print("Invalid object choice.")

            x = random.randint(1,6)

        print("After much searching, you finally found the key!")
        print("Unfortunately, it requires you to answer a riddle to unlock the treat jar.\n")
        print("What walks on four legs in the morning, two at noon, and three at night?")
        answer = int(input("1. caterpillar\n 2. giant robot\n 3.humans"))

        if answer == 3:
            print("Congratulations! You found the treat jar and outsmarted the humans' dastardly riddle.")
            treat_jar = Items.TreatJar
            # treat_jar.add_item()

class DogMoves(Moves):
    """Represents the  actions a dog can do"""
    def __init__(self, jump, sneak):
        """sets up basic actions"""
        super().__init__(jump, sneak)
        self.energy = 5 ##Energy system to make actions more interactive.
        self.brick = Items.Brick(name="Brick", uses=1)
        self.shoes = Items.Shoes("Shoes", 5)
        self.food_bowl = Items.FoodBowl("Food Bowl", 5)

    def jump_up(self):
        """Allows player to jump. The more the player jumps, the stronger they become."""
        if self.energy > 0:
            print(f"You jump {self.jump} units.")  ###Learned to use f and {} instead of + here since a float is being passed from the internet. 
            self.jump += 0.25
            self.energy -= 1
            print(f"Your Jumpring improves! New jump height: {self.jump: .1f}")
            print(f"Energy left: {self.energy}")
        else:
            print("You're too tired to jump.")

    def sprint(self):
        """Run fast, using energy."""
        if self.energy >= 2:
            print("You sprint across the field!")
            self.energy -= 2
            print(f"Energy left: {self.energy}")
        else:
            print("You're too tired to sprint right now.")

    def paw_stand(self):
        """A cute trick that uses a little energy."""
        if self.energy >= 1:
            print("You do a paw stand. Humans are impressed!")
            self.energy -= 1
            print(f"Energy left: {self.energy}")
        else:
            print("You're too tired to perform tricks.")

    def get_stats(self):
        print(f"Current jump: {self.jump: .f}")
        print(f"Energy: {self.energy}")
    
    def get_valid_input(self, prompt, valid_options):
        """Simple input loop to get a valid choice."""
        while True:
            choice = input(prompt)
            if choice in valid_options:
                return choice
            else:
                print("Invalid choice. Please try again.\n")

    def dog_walking_and_obstacles(self): #added function name and took while from gameplay section
        """Mechanic for walking around the game and discovering things."""
        
        import Items
        import random
        brick= Items.Brick(name="Brick", uses=10)
        shoes = Items.Shoes("Shoes", 5)
        food_bowl = Items.FoodBowl("Food Bowl", 5)
        
        objects = {
                "1":self.brick.throw, 
                "2":Items.Laptop, 
                "3":self.shoes.super_jump, 
                "4":self.food_bowl.inspect
                }
        moves = { 
                "1": self.sprint,
                "2": self.get_stats,
                "3": self.jump_up,
                "4": self.paw_stand
                }

        found_key = False
        while found_key: # to keep the player in a playing loop, looking around the room
            print("You walk around the room, searching for the key . . .\n")
            print("You find a pile of sticks. Does this have the key? Use your inventory.\n")

            print("You have 4 options to explore: \n1:Sprint \n2:Get_stats \n3:Jump Up\n4:Paw Stand.")
            print("=============")
            move_choice = self.get_valid_input("Choose an action (1-4):", moves.keys())
            moves[move_choice]()

            print("You have 4 items to use to find your key: \n1:Brick \n2:Laptop \n3:Shoes \n4:Food_Bowl.")
            print("=============")
            item_choice= self.get_valid_input("chosee an object(1-4):", objects.keys())
            obj = objects[item_choice]
            if callable(obj):
                result = obj()
            else:
                print(f"Your inspect the {obj}.")
                result = None

            if item_choice == "4":
                print("You found the key in the Food Bowl. You go to the locked room, and it opens!")
                print("Congratulations! You found the Treat Jar! You win!")
                found_key = True
            else:
                print("Still no key. Keep looking.")