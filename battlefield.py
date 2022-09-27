from robot import Robot
from dinosaur import Dinosaur
import random

class Battlefield:
    def __init__(self):
        self.robot = Robot("Chip")
        self.dinosaur = Dinosaur("Gronk", random.randint(1, 25))

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("\n*----------------------------------*")
        print("Welcome to Robots vs Dinosaurs!")
        print("*----------------------------------*\n")
        print("Each combatant still start with 150 health! May the RNG be ever in your favor!\n")
        print(f"A coin toss will determine who get's to go first!\nWith Dino {self.dinosaur.name} choosing heads and Robot {self.robot.name} choosing tails!\n")
    
    def battle_phase(self):
        turn_1 = random.randint(1,2)
        if turn_1 == 1:
           print(f"The coin toss resulted in tails!\nRobot {self.robot.name} gets to attack first!\n")
        elif turn_1 == 2:
            print(f"The coin toss resulted in heads!\nDino {self.dinosaur.name} gets to attack first!\n")
        while self.dinosaur.health >= 0 and self.robot.health >= 0:
            if turn_1 == 1:
                self.robot.attack(self.dinosaur)
                print()
                turn_1 = 2
            elif turn_1 == 2:
                self.dinosaur.attack(self.robot)
                print()
                turn_1 = 1
        
    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"Robot {self.robot.name} has won the battle!\n")
        else:
            print(f"Dinosaur {self.dinosaur.name} has won the battle!\n")