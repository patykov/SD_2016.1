#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

/*
Signals handed by the program:
 1) SIGHUP       2) SIGINT       3) SIGQUIT 
*/

// Define the function to be called when 2 (SIGINT signal) is sent to process
void
signal_sighup_handler(int signum)
{
   printf("Caught signal %d\n",signum);
   exit(signum);
}
// Define the function to be called when 2 (SIGINT signal) is sent to process
void
signal_sigint_handler(int signum)
{
   printf("Caught signal %d, terminating program\n",signum);
   exit(signum);
}
// Define the function to be called when 2 (SIGINT signal) is sent to process
void
signal_sigquit_handler(int signum)
{
   printf("Caught signal %d\n",signum);
   exit(signum);
}


int main(int argc, char *argv[])
{
   /*
   ARGUMENTS:
    argc[1] : boolean
      Tells the program if it will be a 'busy wait' (0), or a 'blocking wait' (1)
*/

   // Register signals and signals handler
   signal(SIGHUP, signal_sighup_handler);
   signal(SIGINT, signal_sigint_handler);
   signal(SIGQUIT, signal_sigquit_handler);

   int waiting_type = atoi(argv[1]);
   if (waiting_type == 0){
      printf("Busy waiting for some signal\n");
      while(1){
         pause();
      }
   }
   if (waiting_type == 1){
      printf("Blocking waiting for some signal\n");
      sleep(60);
   }
   return EXIT_SUCCESS;
}
