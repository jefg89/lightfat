
#include<stdio.h>
#include<signal.h>
#include<unistd.h>
  

int caught = 0;
void handle_sigint(int sig)
{
    printf("Caught signal %d\n", sig);
    caught = 1;
}
  
int main()
{
    signal(SIGUSR1, handle_sigint);
    while (!caught)  {
        //sleep(1);
        printf("Waiting for signal \n");
    }
    return 0;
}