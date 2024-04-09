# Version 3.2
import random

# Setting constant variables
healpot = 3
kill = 0
coins = 0

# Class selection
print("""Select your class (1-3)
Basic (HP:15 | Damage:10)
Fast (HP:10 | Damage:15)
Tank (HP:20 | Damage:5)""")
classInput = input(">>")

# Applies Stats
if int(classInput) == 1:
    dmg = 10
    odhp = 20
    hp = 15
    agi = 2

elif int(classInput) == 2:
    dmg = 15
    odhp = 15
    hp = 10
    agi = 3

elif int(classInput) == 3:
    dmg = 5
    odhp = 25
    hp = 20
    agi = 1

while hp > 0:
    # List of the scenes and choosing a random one to print
    scene_list = [
    "You walk into a forest and find a beast!",
    "You go into the long grass and find a beast!",
    "You find a castle. At the door, you are greeted with a beast!",
    "You are walking through a castle when you found a beast!",
    "A wild beast appeared!",
    "You wandered into a cave and a beast appears from around the corner!",
    "While wandering around a mansion you encounter a beast!",
    "While looking around in a forest, a beast starts running towards you!",
    "You find a mansion. At the door, you are greeted by a beast!",
    "While spelunking you are met with a beast!",
    "While leaving a forest, a beast runs up from behind you!",
    "While checking out a cave, you are met with a beast!",
    "While scouting out an area, you see a beast running towards you!",
    "You are looking around a dungeon when a beast approaches you!",
    "You were looking around an abandoned town when you spotted a beast running towards you!",
    "You were exploring abandoned buildings when you found a beast!",
    "You were exploring a cave with masks on the wall, and you spotted a beast!",
    "You killed a beast and out of its corpse comes another beast!",
    "While exploring the Chernobyl exclusion zone, you encounter a beast!",
    "You look into the door of an abandoned building, and you are met with a beast!",
    "You are walking through a cemetery and you encounter a beast!",
    "You are wandering around the courtyard of a mansion, and you encounter a beast!",
    "You stumbled upon a building and a beast appeared!",
    "You investigate the cupboard of an abandoned building, and you find a beast inside!",
    "You are riding around on your mobility scooter, and you find a beast!",
    "You found a bunch of peach trees, but then you saw a beast running towards you!",
    "You fell into a pit and there was a beast!",
    "You were questioning your life choices when a beast spawned in!",
    "While you were eating microplastics, a beast appeared!",
    "While out drinking copious amounts of alcohol you ran into a beast!",
    "I don't know, here's a beast."]
    scene = scene_list[random.randint(0, 30)]
    # Generate beast health
    beasthp = random.randint(10, 25)
    print(scene)
    while beasthp > 0:
        # Attack it
        attack = input("It has " + str(beasthp) + " Health. Attack or run away (A/r)\n>>")
        if attack == "r":
            print("You ran away like a little bitch.\nYou killed " + str(kill) + " beasts.")
            exit()
        else:
            bphp = beasthp
            beasthp = beasthp - dmg
            if beasthp < 0:
                beasthp = 0
            if beasthp > 0:
                print("You hit the beast for " + str(dmg) + ". It now has " + str(beasthp) + " health.")

        # Beasts turn
        if beasthp > 0:
            beastdmg = random.randint(0, 10)
            hp = hp - beastdmg
            if hp < 0:
                hp = 0
            print("The beast hit you for " + str(beastdmg) + " damage. You now have " + str(hp) + " health.")
        if hp == 0:
            print("You died.\nYou killed " + str(kill) + " beasts.")
            exit()
        if beasthp == 0:
            kill = kill + 1
            coins = coins + 1
            print("You hit the beast for " + str(bphp) + " damage.")
            print("You killed the beast!")

    # Healing Script
    if healpot > 0 and hp > 0:
        heal = input("You have " + str(hp) + " health and have " + str(healpot) + " healing potions. Would you like to heal?(y/N)\n>>")
        if heal == "y":
            healpot = healpot - 1
            hp = hp + 5
            if hp == odhp:
                print("You died because you overdosed from using too many healing potions.")
                exit()
            else:
                print("You now have " + str(hp) + " health and " + str(healpot) + " healing potions.")
        else:
            print("You did not heal.")
