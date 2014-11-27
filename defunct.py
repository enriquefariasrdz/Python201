#!/usr/bin/python
# -*- coding: utf8 -*-

import subprocess
import time
import threading

# Create 100 subprocesses 

proc = {}
for i in xrange(0,1000):
        proc[i] = subprocess.Popen(['ls','-l'])

# create zombies from this processes, observe one minute zombies
time.sleep(60)

# Zombies dead
proc.communicate()

time.sleep(5)
