from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        d1=Dinosaur("Troodon",15,50)
        r1=Robot("Buzz",50,"Laser",15)
        r2=Robot("Bleep",50,"Saw",15)
        r3=Robot("Bloop",50,"Plasma Burst",15)
        self.robot_wins=True
        self.robot_wins=self.battle_phase(d1,r1)
        self.display_winner(self.robot_wins,d1,r1)






    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")

    def battle_phase(self,d1,r1):
        while (d1.health>0 and r1.health>0):
            print(f"{r1.name} HP: {r1.health}")
            print(f"{d1.name} HP: {d1.health}")
            print(f"{r1.name} attacks with his {r1.weapons[0].name} and deals {r1.weapons[0].attack_power} damage")
            d1.health-=r1.weapons[0].attack_power
            if (d1.health >0):
                print(f"{d1.name} attacks and deals {d1.attack_power} damage!")
                r1.health-=d1.attack_power
            else:
                pass
        
        if (r1.health<0):
            return False
        else:
            return True

            


    def display_winner(self,robot_wins,d1,r1):
        if (robot_wins == True):
            print(f"{r1.name} has won the fight!")
        else:
            print(f"{d1.name} has won the fight!")

    