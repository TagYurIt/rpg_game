#!/bin/bash
# Version 1.8

clear

healpot=3
kill=0

echo -e "Choose your class!
1: Average (\e[1;33m15\e[0m hp / \e[1;31m10\e[0m dmg)
2: Attack (\e[1;33m10\e[0m hp / \e[1;31m15\e[0m dmg)
3: Health (\e[1;33m20\e[0m hp / \e[1;31m5\e[0m dmg)"

read -p ">>" class

case $class in
    1)
        name="Average"
        odhp=21
        hp=15
        dmg=10
        ;;
    2)
        name="Attack"
        odhp=16
        hp=10
        dmg=15
        ;;
    3)
        name="Health"
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
    echo "A beast has appeared!"

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

    # end of the while loop
done
