"""
File: PotholeFilling.py
Name: Huang, Wei-Jung
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    pre-condition: Karel is at the upper left of the pothole, facing East.
    post-condition: Karel is in the pothole, facing South.
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition: Karel is in the pothole, facing South.
    post-condition: Karel is at the upper left of the pothole, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def turn_around():
    for i in range(2):
        turn_left()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
