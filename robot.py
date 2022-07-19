from weapon import Weapon

class Robot:
    def __init__(self, name,health):
        self.name=name
        self.health=health
        self.weapons=[Weapon("Laser",10),Weapon("Saw",15),Weapon("Plasma Beam",20)]




    def attack(self,dinosaur):
        pass


