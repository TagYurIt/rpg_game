# Version 3.6
# If you're reading this, I hope you're doing okay, and if you're not, whatever you're going through isn't going to last forever.

import random
from scenes import get_scenes  # Import of the function that returns the scenes list


def str_c(output,color):
    """
    Returns a "colored" string and resets the color of the strings that come after

    Args:
        output (String or Integer): String/Integer that needs to be colored 
        color (String): Color that has to be used
    
    Returns:
        Colored string
    """
    return (color + "" + str(output) + "" + reset)


# Setting constant variables
healpot = 3
kill = 0
coins = 0

# Colors
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
purple = "\033[35m"

# Difficulty Selection
print("Select your difficulty (1-3)")
print("1. " + str_c("Easy",green) + " (Enemies have less health and deal less damage)")
print("2. Normal (Enemies have normal health and deal normal damage)")
print("3. " + str_c("Hard",red) + " (Enemies have more health and deal more damage)")
diff = input(">>")
if diff not in ["1", "2", "3"]:
    diff = 2

# Class selection
print("Select your class (1-3)")
print("1. Basic (HP:" + str_c("15",green) + " | Damage:" + str_c("10",red) + " | Tolerance:" + str_c("20",purple) + ")")
print("2. Fast (HP:" + str_c("10",green) + " | Damage:" + str_c("15",red) + " | Tolerance:" + str_c("15",purple) + ")")
print("3. Tank (HP:" + str_c("20",green) + " | Damage:" + str_c("5",red) + " | Tolerance:" + str_c("25",purple) + ")")
classInput = input(">>")
if classInput not in ["1", "2", "3"]:
    classInput = 1

# Theres gotta be a better way to do this without all these print functions

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
    # Generate number that determines beat type
    beast = random.randint(0, 100)
    if 0 <= beast <= 75:
        beast_type = 1
        beast_name = "beast"
    elif 75 < beast <= 99:
        beast_type = 2
        beast_name = "brute"
    elif beast == 100:
        beast_type = 3
        beast_name = "Ricky Berwick" # Fucking run over coat hanger

    # Import of the scenes list from scenes.py thanks to the get_scenes function
    scene_list = get_scenes(beast_name)
    scene = scene_list[random.randint(0, len(scene_list) - 1)]
    print(scene)

    # Generate beast health
    if int(diff) == 1:
        if beast_type == 1:
            beasthp = random.randint(10, 20)
        elif beast_type == 2:
            beasthp = random.randint(15, 25)
        elif beast_type == 3:
            beasthp = 1
    elif int(diff) == 2:
        if beast_type == 1:
            beasthp = random.randint(10, 25)
        elif beast_type == 2:
            beasthp = random.randint(15, 30)
        elif beast_type == 3:
            beasthp = 1
    elif int(diff) == 3:
        if beast_type == 1:
            beasthp = random.randint(15, 30)
        elif beast_type == 2:
            beasthp = random.randint(20, 35)
        elif beast_type == 3:
            beasthp = 1


    while beasthp > 0:

        # Attack it
        attack = input("It has " + str_c(beasthp,green) + " health. Would you like to Attack, or run away (A/r)\n>>")
        if attack == "r":
            if kill == 1:
                print("You ran away like a little bitch.\nYou killed " + str(kill) + " beast.")
                exit()
            else:
                print("You ran away like a little bitch.\nYou killed " + str(kill) + " beasts.")
                exit()

        else:
            bphp = beasthp
            beasthp = beasthp - dmg
            if beasthp < 0:
                beasthp = 0
            if beasthp > 0:
                print("You hit the " + beast_name + " for " + str_c(dmg,red) + ". It now has " + str_c(beasthp,green) + " health.")

        # Beasts turn
        if beasthp > 0:
            if int(diff) == 1:
                if beast_type == 1:
                    beastdmg = random.randint(0, 5)
                elif beast_type == 2:
                    beastdmg = random.randint(0, 10)
                elif beast_type == 3:
                    beastdmg = random.randint(0, 1)
            elif int(diff) == 2:
                if beast_type == 1:
                    beastdmg = random.randint(0, 10)
                elif beast_type == 2:
                    beastdmg = random.randint(5, 15)
                elif beast_type == 3:
                    beastdmg = random.randint(0, 1)
            elif int(diff) == 3:
                if beast_type == 1:
                    beastdmg = random.randint(5, 15)
                elif beast_type == 2:
                    beastdmg = random.randint(10, 20)
                elif beast_type == 3:
                    beastdmg = random.randint(0, 1)

            php = hp
            hp = hp - beastdmg
            if hp < 0:
                hp = 0
            if hp > 0:
                print("The " + beast_name + " hit you for " + str_c(beastdmg,red) + " damage. You now have " + str_c(hp,green) + " health.")
            else:
                print("The " + beast_name + " hit you for " + str_c(php,red) + " damage.")
        if hp == 0:
            if kill == 1:
                print(str_c("You died.",red) + "\nYou killed " + str(kill) + " beast.")
                exit()
            else:
                print(str_c("You died.",red) + "\nYou killed " + str(kill) + " beasts.")
                exit()

        if beasthp == 0:
            if int(diff) == 1:
                if beast_type == 2:
                    coins = coins + 1
            if int(diff) == 2:
                if beast_type == 1 or beast_type == 3:
                    coins = coins +1
                elif beast_type == 2:
                    coins = coins + 2
            if int(diff) == 3:
                if beast_type == 1:
                    coins = coins + 2
                elif beast_type == 2:
                    coins = coins + 3
                elif beast_type == 3:
                    coins = coins + 1

            kill = kill + 1
            print("You hit the beast for " + str_c(bphp,red) + " damage.")
            print("You killed the beast!")

    # Script to go to the store, return to combat, or heal
    if hp > 0:
        choice = input("You have " + str_c(hp,green) + " health, " + str(healpot) + " healing potions, and " + str_c(coins,yellow) + " coins.\nWould you like to heal, go to the store, or continue adventuring?(h/s/B)\n>>")

        # Healing Script
        if choice == "h":
            if healpot == 0:
                print("You did not have enough healing potions to heal.")
            else:
                healpot = healpot - 1
                hp = hp + 5
                if hp >= odhp:
                    if kill == 1:
                        print("You died because you overdosed from using too many healing potions.\nYou killed " + str(kill) + " beast.")
                        exit()
                    else:
                        print("You died because you overdosed from using too many healing potions.\nYou killed " + str(kill) + " beasts.")
                        exit()
                else:
                    print("You now have " + str(hp,green) + " health and " + str(healpot) + " healing potions.")

        # TODO: Store colors
        # Stoer
        # print function hell time again yippieeee
        if choice == "s":
            print("Welcome to the store, What would you like to buy?(1-3)")
            print("1. Healing potion - Heals " + str_c("5",green) + " health (" + str_c("3",yellow) + " coins)")
            print("2. Potion of Tolerance - Raises your tolerance by " + str_c("3",purple) + " (" + str_c("5",yellow) + " coins)")
            print("3. Sword - Raises your damage by " + str_c("3",red) +" (" + str_c("5",yellow) + " coins)")
            buy = input(">>")
            if buy == "1":
                if coins >= 3:
                    coins = coins - 3
                    healpot = healpot + 1
                    heal = input("You bought a healing potion, you now have " + str(healpot) + " healing potions.\nWould you like to drink this now or later?(y/N)\n>>")
                    if heal == "y":
                        healpot = healpot - 1
                        hp = hp + 5
                        if hp >= odhp:
                            if kill == 1:
                                print("You died because you overdosed from using too many healing potions.\nYou killed " + str(kill) + " beast.")
                                exit()
                            else:
                                print("You died because you overdosed from using too many healing potions.\nYou killed " + str(kill) + " beasts.")
                                exit()
                        else:
                            print("You now have " + str(hp,green) + " health and " + str(healpot) + " healing potions.")
                else:
                    print("You're too fucking poor to afford this.")
            elif buy == "2":
                if coins >= 5:
                    coins = coins - 5
                    odhp = odhp + 3
                    print("You drank the potion as soon as you got outside. You now have " + str_c(odhp,purple) + " tolerance.")
                else:
                    print("You're too fucking poor to afford this.")
            elif buy == "3":
                if coins >= 5:
                    coins = coins - 52
                    dmg = dmg + 3
                    print("You bought a new sword, you now do " + str_c(dmg,red) + " damage.")
                else:
                    print("You're too fucking poor to afford this.")
                    # This happens when the player goes into the shop too early, and no, we arent gonna make a shop exit "feature"
                    # penis man lmao
