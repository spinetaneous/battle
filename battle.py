import math
import random
from time import sleep

class Character:
    def __init__(self, name, hp, atk, hit_chance):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.xp = (self.hp+self.atk)/2
        self.hit_chance = hit_chance #float between 0.0 and 1.0 meaning a guaranteed hit
    
    def land_hit(self):
        hit = random.random()
        return True if hit < self.hit_chance else False
    
    def attack(self, enemy):
        damage = math.floor(random.random()*self.atk+1)
        enemy.hp -= damage
        return damage
        
    def give_xp(self):
        exp = math.floor((random.random()*self.xp*10))
        return exp
        
dragon = Character("dragon", 50, 15, 0.25)
slime = Character("slime", 10, 5, 0.50)
you = Character("you", 20, 10, 0.75)

def battle(enemy):
    slaying = True
    if enemy == you:
        print("Whoa! Another version of you hops in front of you!\nYou must become the alpha.")
        print("\nWith only {} HP, you commence battle with yourself!".format(you.hp))
    else:
        print("A wild {0} hops in front of you.\nWith only {1} HP, you attempt to fight it.".format(enemy.name, you.hp))
    sleep(2)
    while slaying:
        if you.land_hit():
            your_dmg = you.attack(enemy)
            print("\nYou have hit the {0}!\nYour hit inflicted {1} damage {2}!".format(enemy.name if enemy != you else "other you", your_dmg, "point" if your_dmg == 1 else "points"))
            if enemy.hp <= 0:
                print("Congratulations! You have defeated {0}! :)\nYou have gained {1} XP!".format("the" + enemy.name if enemy != you else "the other you!\nYour existence reigns supreme", enemy.give_xp()))
                slaying = False
            else:
                print("\nYou attempt to hit again.")
                sleep(2)
        else:
            print("\nYou missed! The {} attempts to hit you.".format(enemy.name if enemy != you else "other you"))
            sleep(2)
            if enemy.land_hit():
                enemy_dmg = enemy.attack(you)
                print("\nThe {0} inflicts {1} damage {2} on you.".format(enemy.name if enemy != you else "other you", enemy_dmg, "point" if enemy_dmg == 1 else "points"))
                if you.hp <= 0:
                    if enemy == you:
                        print("\nOh dear, the other you has defeated you.\nYour existence has been replaced. :(\nGAME OVER")
                    else:
                        print("\nOh dear, the {0} has defeated you.\nYou might want to rest at the nearest inn. :(".format(enemy.name))
                    slaying = False
                else:
                    print("\nYou have {} HP left.".format(you.hp))
                    sleep(2)
            else:
                print("\nThe {} luckily misses you.\nYou attempt to hit again.".format(enemy.name if enemy != you else "other you"))
                sleep(2)
                
battle(dragon)