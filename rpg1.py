#!/usr/bin/env python

# In this simple RPG game, the hero1 fights the goblin1. He has the options to:

# 1. fight goblin1
# 2. do nothing - in which case the goblin1 will attack him anyway
# 3. flee

def main():
    health = 10
    power = 5
    health = 6
    power = 2
    hero1 = Hero()
    goblin1 = Goblin()

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = ''

class Hero(Character):
    def __init__(self, health, power):
        self.name = 'Hero'
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self, health, power):
        self.name = 'Goblin'
        self.health = 6
        self.power = 2

    while goblin1.health > 0 and hero1.health > 0:
        print("You have {} health and {} power.".format(hero1.health, hero1.power))
        print("The goblin1 has {} health and {} power.".format(goblin1.health, goblin1.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin1")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin1
            goblin1.health -= hero1.power
            print("You do {} damage to the goblin1.".format(hero1.power))
            if goblin1.health <= 0:
                print("The goblin1 is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin1.health > 0:
            # Goblin attacks hero1
            hero1.health -= goblin1.power
            print("The goblin1 does {} damage to you.".format(goblin1.power))
            if hero1.health <= 0:
                print("You are dead.")

main()

