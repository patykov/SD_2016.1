#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>
#include <errno.h>

int main ( int argc, char *argv[] )
{
/*
ARGUMENTS:
    argc[1] = number of the destination process
    argc[2] = signal to be send

RETURNS:
    error: If the process does not exists
*/
    pid_t process_number = atoi(argv[1]);
    int signal_number = atoi(argv[2]);
    if ( argc != 3 ){ 
        printf( "The program needs the following arguments to work correctly:  destination_process  signal \n" );
    }

    else {
        if(kill( process_number, signal_number ) != 0){
            //Returned and error
            if(errno == ESRCH){
                printf("The process %s could not be found\n", argv[1]);
            }
        }
        else{
            printf("The signal %s was send to the process %s\n", argv[2], argv[1]);
        }
    }
}