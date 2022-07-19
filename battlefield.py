import time
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
        time.sleep(3)

    def battle_phase(self):
        fleet1=Fleet()
        herd1=Herd()
        z=0
        while (z==0):
            print("Your Army:")
            for x in range(len(fleet1.robots)):
                print(f"{fleet1.robots[x].name}: {fleet1.robots[x].health}hp")
            print()
            time.sleep(1)
            print("Enemy Army:")
            for x in range(len(herd1.dinosaurs)):
                print(f"{herd1.dinosaurs[x].name}: {herd1.dinosaurs[x].health}hp")
            print()
            time.sleep(2)
            print("Which weapon do you want to attack with?\n0)Laser\n1)Saw\n2)Plasma Beam")
            choice=int(input("Select 0, 1 or 2: "))
            weapon_choice=fleet1.get_weapon_name(choice)
            weapon_damage=fleet1.get_weapon_damage(choice)

            print()


            print(f"{fleet1.robots[0].name} attacks with its {weapon_choice} and deals {weapon_damage} damage")
            herd1.dinosaurs[0].health-=weapon_damage
            if (herd1.dinosaurs[0].health <1):
                herd1.remove()
            if (len(herd1.dinosaurs) ==0):
                return True
                break
            print(f"{herd1.dinosaurs[0].name} attacks dealing {herd1.dinosaurs[0].attack_power}")
            fleet1.robots[0].health-=herd1.dinosaurs[0].attack_power

            if (fleet1.robots[0].health<1):
                fleet1.remove()
            
            if (len(fleet1.robots) ==0):
                return False
                break

            print()
            print()

            time.sleep(3)
            
            

    def display_winner(self,robot_wins):
        if (robot_wins == True):
            print("Robots have won the fight!")
        else:
            print("Dinosaurs have won the fight!")

    