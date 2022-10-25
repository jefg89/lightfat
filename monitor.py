import signal, os
import subprocess
import sys
import time


def handler(signum, frame):
    print("RECEIVED SIGNAL: starting monitoring...")
    subprocess.run(["./get_trace.sh", "VOLREND"])

cont = True
signal.signal(signal.SIGUSR1, handler)
while(cont):
    time.sleep(0.5)
    
    
