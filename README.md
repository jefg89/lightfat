# lightfat
Barebones implementation of perf process monitoring of IPC and L1-load-accesses with signals

## Cloning
To test with Splash-3 benchmark, please clone with submodules:

``git clone git@github.com:jefg89/lightfat.git --recurse-submodules``


## Usage

usage: monitor.py [-h] -a APP [-s SAMP_PERIOD] [-d DUR]

arguments:

&nbsp;&nbsp;&nbsp;&nbsp;-h, --help  show this help message and exit

&nbsp;&nbsp;&nbsp;&nbsp;-a APP          application name  

&nbsp;&nbsp;&nbsp;&nbsp;-s SAMP_PERIOD  sampling period in milliseconds  [default = 1ms]

&nbsp;&nbsp;&nbsp;&nbsp;-d DUR          sampling duration in seconds    [default = 0.5s]
  


To start monitoring an application, run

`` python3 monitor.py -a application_name -s sampling_period -d duration ``

After executing, note the process id of the monitor application

e.g., ``Monitor process running with PID = 29461 ``

Then, to trigger the monitoring from an external application, said application should raise a SIGUSR1 signal to the monitoring application (see examples/signal.cc).
Following the example:

``./examples/signal 29461``

Results are stored in the newly created `results` folder
