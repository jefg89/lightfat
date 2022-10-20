
#include<stdio.h>
#include<wait.h>
#include<signal.h>



int main(int argc, char const *argv[])
{
    pid_t pid = 47778;
    kill(pid,SIGUSR1);
    return 0;
}

