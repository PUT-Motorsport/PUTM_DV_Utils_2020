#!/usr/bin/env python

import can



can_interface = 'vcan0'
bus = can.interface.Bus(can_interface, bustype='socketcan')

print("hi")
while(True):
    message = bus.recv()
    print(message)