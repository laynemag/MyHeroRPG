import random

class Character:
    def __init__(self, name, health, power,):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):            
        #enemy.health -= self.power <-- implementing a take_damage feature
        print(f"The {self.name} attacks {enemy.name}!")
        enemy.take_damage(self.power)
    
    def is_alive(self):
            if self.health > 0:
                return True

    def print_status(self):
        if self.__class__.__name__ == "Hero":
            print(f"Your health is {self.health} and your power is {self.power}")
        else:
            print(f"The {self.name}'s health is {self.health} and its power is {self.power}")
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage")
        if self.health <= 0:
            print(f"The {self.name} is dead!")

class Hero(Character):
    def __init__(self, name, health, power,):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, enemy):
        print(f"You attack the {enemy.name}!")
        attack_chance = random.randint(1,10)
        if attack_chance >= 8:
            self.power *= 2
            print(f"Landed a critical strike on the {enemy.name}!") 
        enemy.take_damage(self.power)
        self.power = 60

class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Medic(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        heal_chance = random.randint(1,10)
        if self.health < 100 and heal_chance >= 8:
            self.health += 20
            print(f"The {self.name} just healed 20 health!")
        

cool_guy = Hero("Hero" ,100, 60,)
bad_guy = Goblin("goblin" ,100, 20,)

class Battle(object):

    def do_battle(self, hero, enemy):
        print("=" * 30)
        print(f"You have encountered a {enemy.name}!")
        print("=" * 30)

        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()

            print("-" * 30)
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
                print("You run away in terror")
                exit(0)
            else:
                print("Try again.")
                continue

            enemy.attack(hero)

        if hero.is_alive():
            print(f"You defeated the {enemy.name}")
            return True

        else:
            print("You are dead.")
            return False

battle_start = Battle()
battle_start.do_battle(cool_guy,bad_guy)