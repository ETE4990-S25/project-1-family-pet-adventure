### REPRESENTATIVE OF FINAL
### JUPYTER NOTEBOOK CELL IN 
### PLAY_THIS_FinalGame_Project1.ipynb

# import Exploring
#from Items import Items, Laptop, Brick, Shoes, FoodBowl
from Players import Player_Choice
from Exploring import CatMoves, DogMoves
import Menu

def play (player):
    """Allows a dog or cat to use an item or explore."""
    
    if player.pet_type == "Dog":
        print("Where do you want to go? \n 1:left or \n2:right?")
        path= input("Enter 1 or 2:").strip()
        if path== "1":
            print("Dog fell into a ditch. Mission Unsuccessful.")
            return
        elif path== "2":
            print("Dog can proceed to explore to find the key.")
            dog_move_1 = DogMoves(1, 1)  #put instances of function
            dog_move_1.dog_walking_and_obstacles()
        else:
            print("Invalid input. Please choose 1 or 2.")
            
    elif player.pet_type== "Cat":
        print("Where do you want to go? \n 1:left or \n2:right?")
        path= input("Enter 1 or 2").strip()
        if path== "1":
            print("Cat can proceed to explore to find the key.")
            cat_move_1= CatMoves(1, 3)
            cat_move_1.cat_walking_and_obstacles()
        elif path== 2:
            print("Cat fell into a ditch. Mission Unsuccessful.")   
        else:
            print("Invalid input. Please choose 1 or 2.")


#### print title of game
print("Welcome to Family Pet Adventure\n")
print("You are a family pet, always searching for the treat jar the humans have hidden.")
print("The jar is in a locked area. You will need to find the key before you can get in.")
print("You will have to face great obstacles and answer a tricky riddle before you can get the treat jar.")
print("Start Game!")
print("===============================================")
load_choice = input("Would you like to load a saved game? (yes/no): ").lower()

if load_choice == "yes":
    player = load_game()
    if not player:
        player = Player_Choice()
        player.Select_pet()
else:
    player = Player_Choice()
    player.select_pet()

player.display_players()
Menu.menu(player)
play(player)