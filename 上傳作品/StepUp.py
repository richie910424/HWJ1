"""
File: StepUp.py
Name: Huang, Wei-Jung
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


"""
algorithm:
turn_right
put_99_beepers
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def pick_37_beepers():
    for i in range(37):
        pick_beeper()


def put_15_beepers():
    for i in range(15):
        put_beeper()


def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_99_beepers()
    pick_37_beepers()
    move()
    turn_left()
    move()
    put_15_beepers()
    turn_right()
    move()
    move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)