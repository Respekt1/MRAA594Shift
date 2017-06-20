#!/usr/bin/env python
# shifter594_demo.py - A script to demonstrate the functions
# module for 594 shift registers
# Copyright (c) 2017 Patric Lintschinger
# lint_patric@cable.vol.at

from time import sleep
import shifter594

#dataPin, clockPin, latchPin
Shifter = shifter594.Shifter(2,0,1)

def testFunc():
    Shifter.writeByte(0xFF)
    sleep(2)
    Shifter.writeByte(0x00)
    sleep(2)
    Shifter.writeByte(0xFF)
    sleep(2)
    Shifter.writeByte(0x00)

# Catch ^C and cleanup pins before exiting
try:
    testFunc()
except KeyboardInterrupt:
    Shifter.cleanup()
    exit(1)
Shifter.cleanup()
