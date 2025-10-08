#!/usr/bin/python3
import signal as sig
from time import sleep
import sys
import os 
def signal_handler(s, frame):
    print( "réception du signal ", sig.Signals(s).name )
    sys.exit(0)

def signal_handler_quit(s, frame):
    print("Réception du signal", sig.Signals(s).name )

sig.signal(sig.SIGINT, signal_handler)
sig.signal(sig.SIGQUIT, signal_handler_quit)

x=1
while True:
        print("pid=", os.getpid(), x)
        sleep(.5)
        x += 1

