from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))

datapath = os.path.join(modpath, 'data/orcl-1995-2014.txt')

print(datapath)