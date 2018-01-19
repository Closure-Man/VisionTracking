import sys
import time
import logging
from networktables import NetworkTables

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Please supply an IP")
    exit(0)

ip = sys.argv[1]


NetworkTables.initialize(server=ip)

sd = NetworkTables.getTable("SmartDashboard")

def valueChanged(table, key, value, isNew):
    print("valueChanged: keys: {}; value: {}; isNew: {}".format(key, value, isNew))

def connectionListener(connected, info):
    print(info, '; Connected={}'.format(connected))

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

sd.addEntryListener(valueChanged)

while True:
    time.sleep(1)
