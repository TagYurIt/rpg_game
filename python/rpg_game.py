# Version 3.0.1
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
    # Generate beast health
    beasthp = random.randint(10, 25)
    print("You encountered a beast!")
    while beasthp > 0:
        # Attack it
        attack = input("It has " + str(beasthp) + " Health. Attack or run away (A/r)\n>>")
        if attack == "r":
            print("You ran away like a little bitch.\nYou killed " + str(kill) + " beasts.")
            exit()
        else:
            beasthp = beasthp - dmg
            if beasthp < 0:
                beasthp = 0
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
