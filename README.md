# lightfat
Barebones implementation of perf process monitoring of IPC and L1-load-accesses with signals

## Cloning
To test with Splash-3 benchmark, please clone with submodules:

``git clone git@github.com:jefg89/lightfat.git --recurse-submodules``


## Usage
To start monitoring an application, run

`` python3 monitor.py application_name ``

After executing, note the process id of the monitor application

e.g., ``Monitor process running with PID = 29461 ``

Then, to trigger the monitoring from an external application, said application should raise a SIGUSR1 signal to the monitoring application (see examples/signal.cc).
Following the example:

``./examples/signal 29461``

Results are stored in the newly created `results` folder
