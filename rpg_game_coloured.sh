#!/bin/bash
# Version 2.1.2

clear

healpot=3
kill=0

echo -e "Choose your class!
1: Average (\e[1;33m15\e[0m hp / \e[1;31m10\e[0m dmg)
2: Fighter (\e[1;33m10\e[0m hp / \e[1;31m15\e[0m dmg)
3: Tank (\e[1;33m20\e[0m hp / \e[1;31m5\e[0m dmg)"

read -p ">>" class

case $class in
    1)
        name="Average"
        odhp=21
        hp=15
        dmg=10
        ;;
    2)
        name="Fighter"
        odhp=16
        hp=10
        dmg=15
        ;;
    3)
        name="Tank"
        odhp=26
        hp=20
        dmg=5
        ;;
esac

while [[ $hp -ge 1 ]]
do

    # Randomly generate beast hp
    beasthp=$(( ( $RANDOM % 16 ) + 10 ))

    # beast script
    scene=$(( $RANDOM % 30 ))

    case $scene in
        0)
            echo "You walk into a forest and find a beast!"
        ;;
        1)
            echo "You go into the long grass and find a beast!"
        ;;
        2)
            echo "You find a castle and at the door you are greeted by a beast!"
        ;;
        3)
            echo "You are walking through a castle and you find a beast!"
        ;;
        4)
            echo "A wild beast appeared!"
        ;;
        5)
            echo "You wander into a cave and a beast appears from around the corner!"
        ;;
        6)
            echo "While wandering around a mansion you encounter a beast!"
        ;;
        7)
            echo "While looking around in a forest a beast starts running towards you!"
        ;;
        8)
            echo "You find a mansion, and you are greeted by a beast at the door!"
        ;;
        9)
            echo "While spelunking you are met with a beast!"
        ;;
        10)
            echo "While leaving a forest a beast runs up from behind you!"
        ;;
        11)
            echo "While checking out a cave you are met with a beast!"
        ;;
        12)
            echo "While scouting out an area, you see a beast running towards you!"
        ;;
        13)
            echo "You are looking around a dungeon and a beast starts to approach you!"
        ;;
        14)
            echo "You were looking around an abandoned town, and you spotted a beast coming right towards you!"
        ;;
        15)
            echo "You were exploring an abandoned building and you found a beast!"
        ;;
        16)
            echo "You were exploring a cave with masks on the wall, and you spotted a beast!"
        ;;
        17)
            echo "You killed a beast and out of its corpse comes another beast!"
        ;;
        18)
            echo "While exploring the Chernobyl exclusion zone you encounter a beast!"
        ;;
        19)
            echo "You look into the door of an abandoned building, and you are met by a beast!"
        ;;
        20)
            echo "You're walking around a cemetery and you encounter a beast!"
        ;;
        21)
            echo "You are wandering around the courtyard of a mansion, and you encounter a beast!"
        ;;
        22)
            echo "You stumbled upon an abandoned building and a beast appeared!"
        ;;
        23)
            echo "You investigate a cupboard in an abandoned building, and you find a beast!"
        ;;
        24)
            echo "You were riding around on your mobility scooter, and you found a beast!"
        ;;
        25)
            echo "You found a bunch of peach trees, but then you saw a beast running towards you!"
        ;;
        26)
            echo "You fell into a pit and there was a beast!"
        ;;
        27)
            echo "You were questioning your life choices when a beast spawned in!"
        ;;
        28)
            echo "While eating microplastics a beast appeared!"
        ;;
        29)
            echo "While out at night drunk as hell you ran into a beast!"
        ;;
        30)
            echo "I don't know. Here's a beast!"
        ;;
    esac

    while [[ $beasthp -ge 1 ]]
    do
        echo -e "It has \e[1;33m$beasthp\e[0m health. Attack it or run away? (A/r)"
        read -p ">>" attack

        # Run Away
        if [[ $attack == r ]]; then
            clear
            echo "You killed $kill beasts but you ran away like a little bitch"
            exit
        fi

        # Player attack
        if [[ $attack != r ]]; then
            beastphp=$beasthp
            beasthp=$(( $beasthp - $dmg ))
        fi
        if [[ $beasthp -le 0 ]]; then
                echo -e "You attacked the beast for \e[1;31m$beastphp\e[0m damage."
        else
                echo -e "You attacked the beast for \e[1;31m$dmg\e[0m damage."
        fi

        # Beast attack

        # Generate beast damage
        beastdmg=$(( ( $RANDOM % 10 ) + 1 ))

        # Generate beast attack chance
        beasthitchance=$(( $RANDOM % 4 ))
        if [[ $beasthitchance != 0 ]]; then
        beasthit=true
        fi

        # Run beast attack
        if [[ $beasthp -ge 1 && $beasthit == true ]]; then
            hp=$(( $hp - $beastdmg ))
            echo -e "The beast hit you for \e[1;31m$beastdmg\e[0m damage! You currenty have \e[1;33m$hp\e[0m health"
        elif [[ $beasthp -ge 1 ]]; then
            echo "The beast did not attack"
        fi

        if [[ $hp -le 0 ]]; then
            clear
            echo -e "\e[1;31mYou died\e[0m"
            echo "You killed $kill beasts"
            exit
        fi

        if [[ $beasthp -le 0 ]]; then
            kill=$(( $kill + 1 ))
            echo "You have killed the beast"
        fi

    done

    # Healing script
    if [[ $healpot > 0 && $hp -ge 1 ]]; then
        echo -e "You have \e[1;33m$hp\e[0m health and you have $healpot healing potions. Would you like to heal? (y/N)"
        read -p ">>" heal

        if [[ ($heal == y) && $healpot > 0 ]]; then
            hp=$(( $hp + 5))
            healpot=$(( $healpot - 1 ))
            echo -e "You now have \e[1;33m$hp\e[0m health and $healpot healing potions"
        else
            echo "You have not healed"
        fi
        #overdose script
        if [[ $hp -ge $odhp ]]; then
            clear
            echo "You overdosed and died because you used too many healing potions"
            echo "You killed $kill beasts"
            exit
        fi
    fi
    sleep 1.5
    clear
    # end of the while loop
done
