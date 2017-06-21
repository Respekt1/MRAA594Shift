#! /usr/bin/env python
# MRAA594Shift
# Using the 594 shift register
# Copyright (c) 2017 Patric Lintschinger
# lint_patric@cable.vol.at

import mraa
from time import sleep

mraa.initJsonPlatform("/home/root/mraa-json-api/gs1-mraa-baseboard.json")


class Shifter:

    """Set pins for data, clock and latch; chain length and board mode respectively"""
    def __init__(self, dataPin, clockPin, latchPin, chain = 1):
        self.DATA = mraa.Gpio(dataPin)
        self.CLOCK = mraa.Gpio(clockPin)
        self.LATCH = mraa.Gpio(latchPin)
        self.CHAIN = mraa.Gpio(chain)
        self.CHAIN_PIN = chain

        """Value stored in 595's storage register"""
        self.STORED=0x00

        # Setup pins
        self.DATA.dir(mraa.DIR_OUT)
        self.LATCH.dir(mraa.DIR_OUT)
        self.LATCH.write(0)
        self.CLOCK.dir(mraa.DIR_OUT)
        self.CLOCK.write(0)


    """Push a single bit into the registers.
    writeLatch should be called after 8*CHAIN_PIN pushes"""
    def pushBit(self,state):
        self.CLOCK.write(0)
        self.DATA.write(state)
        self.CLOCK.write(1)

    """Transfer bits from shift register to storage register"""
    def writeLatch(self):
        self.LATCH.write(1)
        self.LATCH.write(0)

    """Write a byte of length 8*CHAIN_PIN to the 594"""
    def writeByte(self,value):
        for i in range(8*self.CHAIN_PIN):
            mybit = value & (1 << ((8*self.CHAIN_PIN - 1) - i ) )
            bit = mybit >> ((8*self.CHAIN_PIN - 1) - i )
            self.pushBit( bit )
        self.writeLatch()
        self.STORED=value

    """High level write to a single pin"""
    def writePin(self, pin, value):
        oldVal = (self.STORED >> pin) & 0x01
        if oldVal != value:
            self.togglePin(pin)

    """Togggle the state of a single pin"""
    def togglePin(self, pin):
        self.writeByte(self.STORED ^ (0x01 << pin))

    """Clean up pins"""
    def cleanup(self):
        self.DATA.write(0)
        self.LATCH.write(0)
        self.CLOCK.write(0)
