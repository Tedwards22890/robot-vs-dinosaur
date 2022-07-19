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
        if (choice=="1"):
            return self.robots[0].weapons[0].name
        elif (choice=="2"):
            return self.robots[0].weapons[1].name
        elif (choice=="3"):
            return self.robots[0].weapons[2].name
        else:
            return "None"

    def get_weapon_damage(self,choice):
        if (choice=="1"):
            return self.robots[0].weapons[0].attack_power
        elif (choice=="2"):
            return self.robots[0].weapons[1].attack_power
        elif (choice=="3"):
            return self.robots[0].weapons[2].attack_power
        else:
            return 0

    
    def remove(self):
        self.robots.pop(0)


