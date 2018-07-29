#!/usr/bin/python

import os
import subprocess
import re
from argparse import ArgumentParser

parser = ArgumentParser(
       description="Scanning i2c bus in range")

parser.add_argument('-f', '--from', dest='bus_from',
                        default=0,
                        help='Start scanning from.')
parser.add_argument('-t', '--to', dest='bus_to',
                        default=0,
                        help='Stop scanning at')

args = parser.parse_args()

for bus in range(int(args.bus_from), int(args.bus_to) + 1):
        print 'Scanning for bus {:d}'.format(bus)
        p = subprocess.Popen(['i2cdetect', '-y', str(bus)],stdout=subprocess.PIPE,)
        #cmdout = str(p.communicate())

        for i in range(0,9):

                line = str(p.stdout.readline())
                if ':' not in line:
                        continue
                _line = line.split(': ')[1].replace(' ', '')
                for j in range(0, len(_line), 2):
                        if _line[j].isdigit() or _line[j] == 'U':
                                print ' Found i2c device at 0x{:02X}'.format((i - 1)*16 + j/2)