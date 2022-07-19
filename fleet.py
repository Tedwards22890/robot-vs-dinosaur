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

    def get_damage(self,choice):
        print(self.robots[0].weapons[choice].name)


