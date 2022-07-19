from robot import Robot
class Fleet:
    def __init__(self):
        self.robots=[Robot("Bleep",50),Robot("Bloop",50),Robot("Boop",50)]


    def get_names(self):
        for x in range(len(self.robots)):
            print(self.robots[x].name)

    def get_thing(self):
        for x in range(len(self.robots)):
            print(self.robots[x].weapons[x].attack_power)

    def get_weapon_name(self,choice):
        return self.robots[0].weapons[choice].name

    def get_weapon_damage(self,choice):
        return self.robots[0].weapons[choice].attack_power
    
    def remove(self):
        self.robots.pop(0)


