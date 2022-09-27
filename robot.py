from weapon import Weapon
import random
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = Weapon("Laser gun", random.randint(1, 25))
    
    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon.attack_power
        print(f"{self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage! {dinosaur.name} now has {dinosaur.health} health!")
        if dinosaur.health <= 0:
            print(f"{dinosaur.name} was beaten!")