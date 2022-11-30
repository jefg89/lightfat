import signal, os
import subprocess
import sys
import time

# This application starts the monitoring of a target application (argument)

def handler(signum, frame):
    print("SIGNAL RECEIVED: Getting the traces...")
    subprocess.run(["scripts/get_trace.sh", app_name])



def loop():
    cont = True
    print("Waiting for signal for " + app_name + " application...")
    signal.signal(signal.SIGUSR1, handler)
    while(cont):
        signal.pause()

    
    
if __name__ == '__main__':
    print("Monitor process running with PID = " + str(os.getpid()))
    global app_name
    app_name = sys.argv[1]
    loop()