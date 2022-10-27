import signal, os
import subprocess
import sys
import time


def handler(signum, frame):
    subprocess.run(["./get_trace.sh", app_name])
    print("RECEIVED SIGNAL: starting monitoring...")


def loop():
    cont = True
    print("appname is " + app_name)
    signal.signal(signal.SIGUSR1, handler)
    i = 0
    while(cont):
        i = i+1

    
    
if __name__ == '__main__':
    global app_name
    app_name = sys.argv[1]
    loop()