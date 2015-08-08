import math
import random

class Player:
    def __init__(self, name, hp, atk, agl, int, wis):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.xp = (self.hp+self.atk)/2
        self.agl = agl #float between 0.0 and 1.0, with 1.0 meaning a guaranteed hit
        self.int = int
        self.wis = wis #same as agl but for magic instead

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
    def __init__(self, name, hp, atk, agl, int, wis, mgc_tendency):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.agl = agl
        self.int = int
        self.wis = wis
        self.mgc_tendency = mgc_tendency #float between 0.0 and 1.0, where 1.0 means enemy uses magic 100% of the time
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

fight(dragon)
