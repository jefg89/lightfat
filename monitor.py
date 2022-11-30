import signal, os
import subprocess
import sys
import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog='monitor.py')
    parser.add_argument('-a', dest= 'app', required=True, help='application name')
    parser.add_argument('-s', dest='samp_period', default = 1 , help='sampling period in milliseconds')
    parser.add_argument('-d', dest='dur', default = 0.5, help='sampling duration in seconds')
    args = parser.parse_args()
    global app_name, sampl_time, duration
    app_name = args.app
    sampl_time =args.samp_period
    duration = args.dur


def handler(signum, frame):
    print("SIGNAL RECEIVED: Getting the traces...")
    subprocess.run(["scripts/get_trace.sh", app_name, sampl_time, duration])



def loop():
    cont = True
    print("Waiting for signal for " + app_name + " application...")
    signal.signal(signal.SIGUSR1, handler)
    while(cont):
        signal.pause()

    
if __name__ == '__main__':
    parse_args()
    print("Monitor process running with PID = " + str(os.getpid()))
    loop()