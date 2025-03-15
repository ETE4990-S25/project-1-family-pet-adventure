###Gives options to two players to choose a character and their name.
##Two characters in our game is a dog or a cat.
class Player_Choice(object):
    """Creates a class to choose a player and a pet."""
    def __init__(self, player1_name, player2_name, player1_pet, player2_pet):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_pet= player1_pet
        self.player2_pet= player2_pet
    def Select_Player(self, player_number):
        """Allow each player to select their character and their name."""
        self.player_number== player_number
        pets= ["Dog", "Cat"]

        if player_number== 1:  ###For player 1 to pick their pet's name and pet type. 
            self.player1_name= input ("Player 1, please enter your pet's name: ")
            self.player_name=input("Player 2, please choose your pet type dog or cat?: ")

            
            if self.player1_pet != pets:
                print ("Invalid choice, defaulting to a dog.") 
                self.player1_pet= "Dog"
            """For invalid pet type from player 1, this will deafult the selection to a dog."""

        elif player_number== 2:   ###For player 2 to pick their pet's name and pet type. 
            self.player2_name= input("Player 2, please enter your pet's name:")
            self.player2_pet= input("Player 2, please choose your pet type dog or a cat?: ")
            
    
            if self.player2_pet != pets:
                print("Invalid choice, making your selection to a dog.")
                self.player2_pet="Dog"
            """For invalid pet type from player 2, this will default their selection to a dog."""

    def display_players(self):
        """Display the players info with their names and pet's name."""
        print("\nPlayer1: " + self.player1_name + ":" + self.player1_pet)
        print("\nPlayer 2: " + self.player2_name + ":" + self.player2_pet)

Family_Pet_Adventure= Player_Choice()

Family_Pet_Adventure.SelectPlayer(1)
Family_Pet_Adventure.SelectPlayer(2)
"""Allow both players to choose their pets"""

Family_Pet_Adventure.display_players()
"""Displays the choices for btoh players."""
    
       
   