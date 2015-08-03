import math
import random
from time import sleep

class Player:
    def __init__(self, name, hp, atk, agl, int, wis, crit_chance):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.xp = (self.hp+self.atk)/2
        self.agl = agl #float between 0.0 and 1.0, with 1.0 meaning a guaranteed hit
        self.int = int
        self.wis = wis #same as agl but for magic instead
        self.crit_chance = crit_chance
    
    def land_attack(self):
        hit = random.random()
        return True if hit < self.agl else False
    
    def attack(self, enemy):
        damage = math.floor(random.random()*self.atk+1)
        enemy.hp -= damage
        return damage
        
    def land_magic(self):
        hit = random.random()
        return True if hit < self.wis else False
        
    def magic(self, enemy):
        damage = math.floor(random.random()*self.int+5)
        enemy.hp -= damage
        return damage
        
    def turn(self, enemy):
        move = raw_input("Next move: ATTACK or USE MAGIC? ").lower()
        if move == "attack":
            print("You attempt to hit the {}!".format(enemy.name))
            if self.land_attack():
                print("Your hit inflicted {} damage points!".format(self.attack(enemy)))
            else:
                print("You missed!")
        elif move == "use magic":
            print("You attempt to cast a spell on the {}!".format(enemy.name))
            if self.land_magic():
                print("Your spell inflicted {} damage points!".format(self.magic(enemy)))
            else:
                print("You missed!")
        else:
            print("Invalid move.")
        
class Enemy:
    def __init__(self, name, hp, atk, agl, int, wis, mgc_tendency, crit_chance):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.agl = agl
        self.int = int
        self.wis = wis
        self.mgc_tendency = mgc_tendency #float between 0.0 and 1.0, where 1.0 means enemy uses magic 100% of the time
        self.crit_chance = crit_chance
        self.exp = (self.hp + self.atk)/2
        
    def land_attack(self):
        hit = random.random()
        return True if hit < self.agl else False
    
    def attack(self, enemy):
        damage = math.floor(random.random()*self.atk+1)
        enemy.hp -= damage
        return damage
        
    def land_magic(self):
        hit = random.random()
        return True if hit < self.wis else False
        
    def magic(self, enemy):
        damage = math.floor(random.random()*self.int+5)
        enemy.hp -= damage
        return damage
        
    def turn(self, enemy): #this assumes the enemy of the enemy is you
        if random.random() < self.mgc_tendency:
            print("The {} attempts to hit you!".format(self.name))
            if self.land_attack():
                print("The {} inflicts {} damage points on you!".format(self.name, self.attack(enemy)))
            else:
                print("The {} misses!".format(self.name))
        else:
            print("The {} attempts to cast a spell on you!".format(self.name))
            if self.land_magic():
                print("The {} inflicts {} damage points on you!".format(self.name, self.magic(enemy)))
            else:
                print("The {} misses!".format(self.name))
        print("You have {} HP left.".format(enemy.hp))
    
    def give_xp(self):
        exp = math.floor((random.random()*self.xp*10))
        return exp
        
#player_name = Player(name, hp, atk, agl, int, wis)
you = Player("you", 20, 10, 0.75, 15, 0.75)

#enemy_name = Enemy(name, hp, atk, agl, int, wis)
dragon = Enemy("dragon", 50, 15, 0.25, 20, 0.75, 0.50)
slime = Enemy("slime", 10, 5, 0.50, 2, 0.25, 0.10)

def battle(enemy):
    slaying = True
    if enemy == you:
        print("Whoa! Another version of you hops in front of you!\nYou must become the alpha.")
        print("\nWith only {} HP, you commence battle with yourself!".format(you.hp))
    else:
        print("A wild {0} hops in front of you.\nWith only {1} HP, you attempt to fight it.".format(enemy.name, you.hp))
    #sleep(2)
    while slaying:
        if you.land_attack():
            your_dmg = you.attack(enemy)
            print("\nYou have hit the {0}!\nYour hit inflicted {1} damage {2}!".format(enemy.name if enemy != you else "other you", your_dmg, "point" if your_dmg == 1 else "points"))
            if enemy.hp <= 0:
                print("Congratulations! You have defeated {0}! :)\nYou have gained {1} XP!".format("the " + enemy.name if enemy != you else "the other you!\nYour existence reigns supreme", enemy.give_xp()))
                slaying = False
            else:
                print("\nYou attempt to hit again.")
            #sleep(2)
        else:
            print("\nYou missed! The {} attempts to hit you.".format(enemy.name if enemy != you else "other you"))
            #sleep(2)
            if enemy.land_attack():
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
                    #sleep(2)
            else:
                print("\nThe {} luckily misses you.\nYou attempt to hit again.".format(enemy.name if enemy != you else "other you"))
                #sleep(2)
                
def fight(enemy):
    #while enemy.hp >= 0 or you.hp >= 0:
    if enemy == you:
        print ("You can't fight yourself.")
    else:
        fighting = True
        while fighting:
            you.turn(enemy)
            enemy.turn(you)
            fighting = False
        
#battle(dragon)
fight(dragon)