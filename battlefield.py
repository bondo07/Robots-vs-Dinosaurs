from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
import random

class Battlefield:
    def __init__(self):
        self.robot = Robot("Chip")
        self.dinosaur = Dinosaur("Gronk", random.randint(1, 25))

    # def run_game(self):
    #     return

    # def display_welcome():
    #     print("*----------------------------------*")
    #     print('Welcome to Robots vs Dinosaurs!')
    #     print("*----------------------------------*")
    
    def battle_phase(self):
        turn_1 = random.randint(1,2)
        if turn_1 == 1:
            print(f"Robot {self.robot.name} gets to attack first!\n")
        elif turn_1 == 2:
            print(f"Dino {self.dinosaur.name} gets to attack first!\n")

        while turn_1 == 1:
            self.robot.attack(self.dinosaur)
            turn_1 = 2
        else:
            self.dinosaur.attack(self.robot)
            turn_1 = 1
        # if turn_1 == 1:
        #     self.robot.attack(self.dinosaur)
        # elif turn_1 == 2:
        #     self.dinosaur.attack(self.robot)
    # def display_winner(self):
    #     return