/*********************** Signal example application ****************************
 * This program raises a signal to the process given in the argument (by pid)
 * After that, the program loops forever :) 
 * JGG 22***********************************************************************/

#include <stdlib.h>
#include<stdio.h>
#include<wait.h>
#include<signal.h>


int main(int argc, char const *argv[])
{
    pid_t pid = atoi(argv[1]);
    kill(pid,SIGUSR1);

    volatile unsigned int i = 0;
    while(1) {
        i++;
    }
}