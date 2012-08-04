#!/usr/bin/env python
"""This script highlights how the module namespace is global.

Once a module is imported, it is not imported again. Therefore, if a module
is modified, that module will be modified for the entire program.

If a custom module relies on a global state, this creates the possibility of
rather subtle bugs. One more reason to avoid using global variables.
"""

import sys
import evilexit
sys.exit("Work complete, exiting")