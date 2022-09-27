import random
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 150
        self.attack_power = attack_power

    def attack(self, robot):
        self.attack_power = random.randint(1, 25)
        robot.health = robot.health - self.attack_power
        print(f"{self.name} attacked {robot.name} for {self.attack_power} damage!")
        if robot.health <= 0:
            print(f"\nRobot {robot.name} has no more health left!\nDinosaur {self.name} has dismantled Robot {robot.name}!")
        else:
            print(f"{robot.name} now has {robot.health} health!")