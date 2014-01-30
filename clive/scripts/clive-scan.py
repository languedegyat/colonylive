#!/usr/bin/env python

"""
 Start periodic scanning to measure colony growth

"""

import os
import time
from multiprocessing import Process

from clive.scan.cleaner import keep_clean
from clive.scan.cycle_scan import keep_scan


os.system("vuescan &")
time.sleep(20)

jobs = []
jobs += [Process(target=keep_clean, )]
jobs += [Process(target=keep_scan, )]

for j in jobs:
    j.start()
for j in jobs:
    j.join()

print "stop"
#reboot()
