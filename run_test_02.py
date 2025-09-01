# -*- coding: utf-8 -*-

"""
Tests for Task 2
"""

import argparse

from tasks import draw_koch_snowflake


def main() -> None:
    try:
        parser = argparse.ArgumentParser(description="Draw the Koch snowflake", epilog="Good bye!")
        # parser.add_argument("depth", type=int, help="Recursion depth (default 3)")
        parser.add_argument("-d", "--depth", type=int, default=3, help="Recursion depth (default 3)")

        args = parser.parse_args()

        draw_koch_snowflake(args.depth)
    except Exception as e:
        print(e)

    exit(0)


if __name__ == "__main__":
    main()
