# -*- coding: utf-8 -*-

"""
HomeWork Task 2
"""

import argparse
import turtle


def koch_curve(t: turtle.Turtle, level: int, size: float) -> None:
    """Draw the Koch curve

    :param t: Turtle screen
    :param level: Recursion level
    :param size: Size of curve
    """
    if level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, level - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(depth: int, size: float = 300) -> None:
    """Draw the Koch snowflake

    :param depth: Recursion depth
    :param size: Size of curve
    """

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-(size / 2), (size / 3**0.5) / 2)
    t.pendown()

    for _ in range(3):
        koch_curve(t, depth, size)
        t.right(120)

    window.mainloop()


def cli() -> None:
    try:
        parser = argparse.ArgumentParser(description="Draw the Koch snowflake", epilog="Good bye!")
        # parser.add_argument("depth", type=int, help="Recursion depth (default 3)")
        parser.add_argument("-d", "--depth", type=int, default=3, help="Recursion depth (default 3)")

        args = parser.parse_args()

        draw_koch_snowflake(args.depth)
    except Exception as e:
        print(e)

    exit(0)
