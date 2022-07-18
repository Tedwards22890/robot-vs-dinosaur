from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        d1=Dinosaur("Troodon",15,50)
        r1=Robot("Buzz",50)


    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur!")

    def battle_phase(self):
        pass

    def display_winner(self):
        print("winner")

    