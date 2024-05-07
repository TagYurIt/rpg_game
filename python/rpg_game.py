# Version 3.4
# If you're reading this, I hope youre having a fantastic day!
import random

# Setting constant variables
healpot = 3
kill = 0
coins = 0

# Difficulty Selection
print("""Select your difficulty (1-3)
Easy (Enemies have less health and deal less damage)
Normal (Enemies have normal health and deal normal damage)
Hard (Enemies have more health and deal more damage)""")
diff = input(">>")

# Class selection
print("""Select your class (1-3)
Basic (HP:15 | Damage:10 | Tolerance:20)
Fast (HP:10 | Damage:15 | Tolerance:15)
Tank (HP:20 | Damage:5 | Tolerance:25)""")
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
    # Generate number that ditermines beat type
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

    # List of the scenes and choosing a random one to print
    scene_list = [
    "You walk into a forest and find a " + beast_name + "!",
    "You go into the long grass and find a " + beast_name + "!",
    "You find a castle. At the door, you are greeted with a " + beast_name + "!",
    "You are walking through a castle when you found a " + beast_name + "!",
    "A wild " + beast_name + " appeared!",
    "You wandered into a cave and a " + beast_name + " appears from around the corner!",
    "While wandering around a mansion you encounter a " + beast_name + "!",
    "While looking around in a forest, a " + beast_name + " starts running towards you!",
    "You find a mansion. At the door, you are greeted by a " + beast_name + "!",
    "While spelunking you are met with a " + beast_name + "!",
    "While leaving a forest, a " + beast_name + " runs up from behind you!",
    "While checking out a cave, you are met with a " + beast_name + "!",
    "While scouting out an area, you see a " + beast_name + " running towards you!",
    "You are looking around a dungeon when a " + beast_name + " approaches you!",
    "You were looking around an abandoned town when you spotted a " + beast_name + " running towards you!",
    "You were exploring abandoned buildings when you found a " + beast_name + "!",
    "You were exploring a cave with masks on the wall, and you spotted a " + beast_name + "!",
    "You killed a beast and out of its corpse comes another " + beast_name + "!",
    "While exploring the Chernobyl exclusion zone, you encounter a " + beast_name + "!",
    "You look into the door of an abandoned building, and you are met with a " + beast_name + "!",
    "You are walking through a cemetery and you encounter a " + beast_name + "!",
    "You are wandering around the courtyard of a mansion, and you encounter a " + beast_name + "!",
    "You stumbled upon a building and a " + beast_name + " appeared!",
    "You investigate the cupboard of an abandoned building, and you find a " + beast_name + " inside!",
    "You are riding around on your mobility scooter, and you find a " + beast_name + "!",
    "You found a bunch of peach trees, but then you saw a " + beast_name + " running towards you!",
    "You fell into a pit and there was a " + beast_name + "!",
    "You were questioning your life choices when a " + beast_name + " spawned in!",
    "While you were eating microplastics, a " + beast_name + " appeared!",
    "While out drinking copious amounts of alcohol you ran into a " + beast_name + "!",
    "I don't know, here's a " + beast_name + "."]
    scene = scene_list[random.randint(0, 30)]
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
        attack = input("It has " + str(beasthp) + " health. Would you like to Attack, or run away (A/r)\n>>")
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
                print("You hit the " + beast_name + " for " + str(dmg) + ". It now has " + str(beasthp) + " health.")

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
                print("The " + beast_name + " hit you for " + str(beastdmg) + " damage. You now have " + str(hp) + " health.")
            else:
                print("The " + beast_name + " hit you for " + str(php) + " damage.")
        if hp == 0:
            if kill == 1:
                print("You died.\nYou killed " + str(kill) + " beast.")
                exit()
            else:
                print("You died.\nYou killed " + str(kill) + " beasts.")
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
            print("You hit the beast for " + str(bphp) + " damage.")
            print("You killed the beast!")

    # Script to go to the store, return to comabat, or heal
    if hp > 0:
        choice = input("You have " + str(hp) + " health, " + str(healpot) + " healing potions, and " + str(coins) + " coins.\nWould you like to heal, go to the store, or conntinue adventuring?(h/s/B)\n>>")

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
                    print("You now have " + str(hp) + " health and " + str(healpot) + " healing potions.")

        # Stoer
        if choice == "s":
            print("""Welcome to the store, What would you like to buy?(1-3)
1. Healing potion - Heals 5 damage (3 coins)
2. Potion of Tolerance - Raises your tolerance by 3 (5 coins)
3. Sword - Raises your damage by 3 (5 coins)""")
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
                            print("You now have " + str(hp) + " health and " + str(healpot) + " healing potions.")
                else:
                    print("You're too fucking poor to afford this.")
            elif buy == "2":
                if coins >= 5:
                    coins = coins - 5
                    odhp = odhp + 3
                    print("You drank the potion as soon as you got outside. You now have " + str(odhp) + " tolerance.")
                else:
                    print("You're too fucking poor to afford this.")
            elif buy == "3":
                if coins >= 5:
                    coins = coins - 5
                    dmg = dmg + 3
                    print("You bought a new sword, you now do " + str(dmg) + " damage.")
                else:
                    print("You're too fucking poor to afford this.")
                    # This happens when the player goes into the shop too early, and no, we arent gonna make a shop exit "feature"
