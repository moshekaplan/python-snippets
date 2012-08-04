#!/usr/bin/env python

"""This is the script that replaced sys.exit with a custom function"""

import sys
def exit_replacement(arg):
    print "HAHA, NO YOU CAN'T!"
sys.exit = exit_replacement