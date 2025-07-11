#!/usr/bin/env checkio --domain=py run army-battles

# In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes and  functions to the existing ones. The new class should be theArmyand have the methodadd_units()- for adding the chosen amount of units to the army. The first unit added will be the first to go to fight, the second will be the second, ...
# Also you need to create aBattle()class with afight()function, which will determine the strongest army.
# The battles occur according to the following principles:
# at first, there is a duel between the first warrior of the first army and the first warrior of the second army (FIFO counting is used). As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the fight() function should returnTrue, if the first army won, orFalse, if the second one was stronger.
# 
# 
# Note that army 1 have the advantage to start every fight!
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:2 types of unitsFor all battles, each army is obviously not empty at the beginning.
# 
# 
# END_DESC

# Taken from mission The Warriors

class Warrior:
    health=50
    attack=5
    is_alive=True
class Knight(Warrior):
    attack=7
def fight(unit_1, unit_2):
    turn_of = 1
    while unit_1.is_alive and unit_2.is_alive: 
        if turn_of == 1:
            unit_2.health-=unit_1.attack
            turn_of=2
            if unit_2.health<0:
                unit_2.is_alive=False
                
        else:
            unit_1.health-=unit_2.attack
            turn_of=1
            if unit_1.health<0:
                unit_1.is_alive=False
            
            
    if unit_1.is_alive:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    print("Coding complete? Let's try tests!")


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")