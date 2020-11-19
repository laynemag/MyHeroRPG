#!/usr/bin/env python

# In this simple RPG game, the hero fights the {enemy}. He has the options to:

# 1. fight {enemy}
# 2. do nothing - in which case the {enemy} will attack him anyway
# 3. flee

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The {enemy} has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight {enemy}")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks {enemy}
#             goblin_health -= hero_power
#             print("You do {} damage to the {enemy}.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The {enemy} is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The {enemy} does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()

class Hero:
    def __init__(self, health, power, alive):
        self.health = health
        self.power = power
        self.alive = alive
    
    def attack(self, enemy):            
        enemy.health -= self.power
        print(f"You do {self.power} damage to the {enemy}.")
        if enemy.health <= 0:
                print(f"The {enemy} is dead.")
    
    def is_alive(self):
        if self.health == 0:
            print(f"You are dead.")
            self.alive == False

    def print_status(self):
        print(f"Your health is {self.health}\n Your power is {self.power} \n")
        if self.alive == True:
            print("You're still alive")

    
class Goblin:
    def __init__(self, health, power, alive):
        self.health = health
        self.power = power
        self.alive = alive

    def attack(self, enemy):            
        enemy.health -= self.power
        print(f"You do {self.power} damage to the {enemy}.")
        if enemy.health <= 0:
                print(f"The {enemy} is dead.")

    def is_alive(self):
        if self.health == 0:
            print(f"You are dead.")
            self.alive == False

    def print_status(self):
        print(f"Your health is {self.health}\n Your power is {self.power} \n")
        if self.alive == True:
            print("You're still alive")

cool_guy = Hero(100, 6, True)
bad_guy = Goblin(100, 2, True)

cool_guy.attack(bad_guy)
cool_guy.print_status()