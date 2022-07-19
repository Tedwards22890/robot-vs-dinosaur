from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.robot_wins=True
        self.robot_wins=self.battle_phase()
        self.display_winner(self.robot_wins)






    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")

    def battle_phase(self):
        fleet1=Fleet()
        herd1=Herd()
        z=0
        while (z==0):
            for x in range(len(fleet1.robots)):
                print(f"{fleet1.robots[x].name}: {fleet1.robots[x].health}hp")
            for x in range(len(herd1.dinosaurs)):
                print(f"{herd1.dinosaurs[x].name}: {herd1.dinosaurs[x].health}hp")
            choice

            
            quit()
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

            


    def display_winner(self,robot_wins):
        if (robot_wins == True):
            print(f"{r1.name} has won the fight!")
        else:
            print(f"{d1.name} has won the fight!")

    