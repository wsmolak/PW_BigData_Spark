#!/usr/bin/env python

import sys


def say_hello_world():
    """
    Function that says hello!
    """
    if len(sys.argv) <= 1:
        print('Program {} says hello world!'.format(sys.argv[0]))
    else:
        print('Program {} says hello to {}!'.format(sys.argv[0], sys.argv[1]))

if __name__ == "__main__":
    say_hello_world()
    sys.exit(0)
