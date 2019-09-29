"""
Main module what launch the game.
Contains argv flag to set Units health.
"""
import sys
from unit import Unit
from battle import Battle


health = 100

if len(sys.argv) > 1:
    try:
        health = int(sys.argv[1])
    except ValueError:
        print('Wrong flag value')
        sys.exit(1)

# Creating Units
computer = Unit(health=health, heal_boost=True)
player = Unit(health=health, name='Human')

# Creating battle with created Units
battle = Battle(computer, player)

print('Hello, we have two players.\n\n %s and\n %s' % (computer, player))

input('Press any key to start a fight!\n')

# Starting fight
battle.fight()

input('\nPress enter to exit the game...')
