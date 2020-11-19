import random

class Character:
    def __init__(self, name, health, power,):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):            
        enemy.health -= self.power
        print(f"You do {self.power} damage to the {enemy.name}.")
        if enemy.health <= 0:
                print(f"The {enemy.name} is dead.")
    
    def is_alive(self):
            if self.health > 0:
                return True

    def print_status(self):
        if self.__class__.__name__ == "Hero":
            print(f"Your health is {self.health} and your power is {self.power}")
        else:
            print(f"The {self.name}'s health is {self.health} and its power is {self.power}")

class Hero(Character):
    def __init__(self, name, health, power,):
        self.name = name
        self.health = health
        self.power = power
    

    
class Goblin(Character):
    def __init__(self, name, health, power,):
        self.name = name
        self.health = health
        self.power = power


cool_guy = Hero("Hero" ,100, 60,)
bad_guy = Goblin("goblin" ,100, 20,)

class Battle(object):

    def do_battle(self, hero, enemy):
        print("=====================")
        print(f"You have encountered a {enemy.name}!")
        print("=====================")

        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()

            print("-----------------------")
            print("What do you want to do?")
            print(f"1. fight {enemy.name}")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')

            choice = int(input())
            if choice == 1:
                hero.attack(enemy)
            elif choice == 2:
                pass
            elif choice == 3:
                print("You have ran away in terror")
                exit(0)
            else:
                print("Try again.")
                continue

            enemy.attack(hero)

        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            return True

        else:
            print("YOU LOSE!")
            return False

battle_start = Battle
battle_start.do_battle(cool_guy,bad_guy)