import random
import time

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):            
        print(f"The {self.name} attacks {enemy.name}!")
        enemy.take_damage(self.power)
        time.sleep(1)

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
    def __init__(self, name, health, power,coins,armor,evade,vamp):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        self.evade = evade
        self.vamp = vamp

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def attack(self, enemy):
        print(f"You attack the {enemy.name}!")
        attack_chance = random.randint(1,10)
        if attack_chance >= 8:
            self.power *= 2
            print(f"You landed a critical strike on the {enemy.name}!") 
            enemy.take_damage(self.power)
            self.power = int(self.power / 2)
        else:
            enemy.take_damage(self.power)
        if self.vamp > 0:
            self.health += self.vamp
            print(f"You have drained {self.vamp} health from the enemy")    
        time.sleep(1)

    def take_damage(self, damage):
        evade_chance = self.evade
        if evade_chance >= random.randint(1,100):
            print (f"{self.name} has evaded the attack!")
        else:
            adj_damage = damage - self.armor
            if adj_damage <= 0:
                adj_damage = 0
            self.health -= adj_damage
            if self.armor > 0:
                print(f"Your armor has absorbed {self.armor} damage")
        print(f"{self.name} takes {adj_damage} damage")

    def restore(self, potency):
        self.potency = 100
        if self.health < 100:
            self.health = self.potency
            print(f"{self.name}'s heath is restored to {self.health}!")
        time.sleep(1)

class Goblin(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

class Medic(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage")
        heal_chance = random.randint(1,10)
        if heal_chance >= 8:
            self.health += 20
            print(f"{self.name} healed 20 points!")
        heal_chance = 0
        if self.health <= 0:
            print(f"The {self.name} is dead!")

class Shadow(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

    def take_damage(self, damage):
        self.health -= damage
        evade_chance = random.randint(1,10)
        if evade_chance < 10:
            self.health = 1
            print(f"Your attack went through the {self.name}!")
        evade_chance = 0
        if self.health <= 0:
            print(f"{self.name} takes {damage} damage")
            print(f"The {self.name} is dead!")
        
class Zombie(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage")
        evade_chance = random.randint(1,10)
        if evade_chance <= 10:
            self.health = 10
            print(f"The {self.name} won't die! You must flee!")
        evade_chance = 0

cool_guy = Hero("Hero" ,100, 60, 20, 0, 0, 0)
bad_guy = Goblin("Goblin" ,100, 20, 3)
medic_guy = Medic("Medic", 130, 15, 5)
shadow_guy = Shadow("Shadow", 1, 7, 7)
zombie_guy = Zombie("Zombie", 10, 1, 0)
enemy_list = [medic_guy, bad_guy, shadow_guy, zombie_guy]

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 20
        print(f"{hero.name}'s power increased to {hero.power}.")

class Super_Tonic(object):
    cost = 5
    name = 'super tonic'
    def apply(self, hero):
        hero.restore(80)
        print(f"{hero.name}'s health increased to {hero.health}.")

class Armor(object):
    cost = 5
    name = "armor"
    def apply(self, hero):
        hero.armor += 10
        print(f"{hero.name}'s armor increased to {hero.armor}.")

class Evade(object):
    cost = 5
    name = "evade"
    def apply(self,hero):
        hero.evade += 10
        print(f"{hero.name}'s evade increased to {hero.evade}")

class vamp_sword(object):
    cost = 10
    name = 'vamp sword'
    def apply(self, hero):
        hero.vamp += 5
        print(f"{hero.name}'s vampirism increased to {hero.vamp}.")


class Store(object):

    items = [Super_Tonic, Sword, Armor, Evade, vamp_sword]

    def shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f"You have {hero.coins} coins.")
            print("What do you want to do?")

            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f"{i + 1}. buy {item.name} ({item.cost})")
            print("6. leave")
            choice = int(input("> "))

            if choice == 6:
                break
                    
            else:
                ItemToBuy = Store.items[choice - 1]
                item = ItemToBuy()
                if hero.coins >= ItemToBuy.cost:
                    hero.buy(item)
                else:
                    print(f"You must have {ItemToBuy.cost} coins to buy a {ItemToBuy.name}")
                time.sleep(1)

class Battle(object):

    def do_battle(self, hero, enemy):
        print("=" * 30)
        print(f"You have encountered a {enemy.name}!")
        print("=" * 30)

        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)

            print("-" * 30)
            print("-" * 30)
            print("What do you want to do?")
            print(f"1. Fight {enemy.name}")
            print("2. Do nothing")
            print("3. Flee")
            print("> ", end=' ')

            choice = int(input())
            if choice == 1:
                hero.attack(enemy)
                if enemy.health > 0:
                        enemy.attack(hero)
            elif choice == 2:
                pass
            elif choice == 3:
                print("You run away in terror")
                World.main_menu(self,cool_guy)
            else:
                print("Try again.")
                continue

        if hero.is_alive():
            print(f"You defeated the {enemy.name}")
            hero.coins += enemy.bounty
            print(f"You have received {enemy.bounty} coins for killing a {enemy.name}!")
            return True

        else:
            print("You have fainted.")
            return False

class World(object):
    def main_menu(self, hero): 
        while hero.is_alive():
            print("-" * 30)
            print("What do you want to do?")
            print("1. Find a fight!")
            print("2. Go shopping.")
            print("3. Rest.")
            print("4. End journey.")
            print("> ", end=' ')

            choice = int(input())
            if choice == 1:
                Battle.do_battle(self,cool_guy,enemy_list[random.randint(0,3)])
            elif choice ==2:
                Store.shopping(self,cool_guy)
            elif choice == 3:
                if cool_guy.health < 100:   
                    cool_guy.restore(100)
                else:
                    print("You are already at full health")
            elif choice == 4:
                print(f"Til next time.")
                exit(0)
            else:
                ("Please try again.")
                

World.main_menu(cool_guy, enemy_list[random.randint(0,3)])


