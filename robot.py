from weapon import Weapon

class Robot:
    def __init__(self, name,health,weapon_name,attack_power):
        self.name=name
        self.health=health
        self.weapons=[]
        self.add_weapon(self.weapon_name,self.attack_power)


    def attack(self,dinosaur):
        pass
    def add_weapon(self,name,attack_power):
        w1=Weapon(self.name,self.attack_power)
        self.weapons.append(w1)
