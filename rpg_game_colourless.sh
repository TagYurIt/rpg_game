#!/bin/bash
# Version 1.8

clear

healpot=3
kill=0

echo -e "Choose your class!
1: Average (15 hp / 10 dmg)
2: Attack (10 hp / 15 dmg)
3: Health (20 hp / 5 dmg)"

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

            echo "It has $beasthp health. Attack it or run away? (A/r)"
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
                echo "You attacked the beast for $beastphp damage."
            else
                echo "You attacked the beast for $dmg damage."
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
            echo "The beast hit you for $beastdmg damage! You currenty have $hp health"
        elif [[ $beasthp -ge 1 ]]; then
            echo "The beast did not attack"
        fi

        if [[ $hp -le 0 ]]; then
            clear
            echo "You died"
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
        echo "You have $hp health and you have $healpot healing potions. Would you like to heal? (y/N)"
        read -p ">>" heal

        if [[ ($heal == y) && $healpot > 0 ]]; then
            hp=$(( $hp + 5))
            healpot=$(( $healpot - 1 ))
            echo "You now have $hp health and $healpot healing potions"
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
