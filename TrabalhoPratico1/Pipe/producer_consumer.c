#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>

int fd[2];

int num_generator(){
    srand( (unsigned)time(NULL) );
    return (1 + (rand() % 100));
}

void num_avaliator(int n){
    int flag = 0;
    for (int i=2; i<=n/2; ++i){
        if (n%i == 0){
            flag = 1;
            break;
        }
    }
    if(flag == 0)
        printf("%d is a prime number.\n", n);
    else
        printf("%d is not a prime number.\n", n);
}

void producer(int limit){
    /*Closing 'read' since we will only write on the pipe for now*/
    close(fd[0]);

    int num;
    while(limit>=0){
        if(limit == 0)
            num = 0;
        else
            num = num_generator();
        printf("Enviando o numero: %d\n", num);
        
        char snum[10];
        sprintf(snum, "%d", num);
        /* Writing to the pipe */
        int teste = write(fd[1], snum, sizeof(snum));
        limit = limit - 1;
        sleep(2);
    }
    close(fd[1]);
    exit(0);
}

void consumer(){
    char str_received[10];
    int num_received;
    int connection;
    /* Closing 'write' since we will only read for now */
    close(fd[1]);
    while(1){
        connection = read(fd[0], str_received, sizeof(str_received));
        if (connection == -1)
            printf("Error!!\n");
        else if (connection == 0)
            printf("Nothing to read.\n");
        else{
            printf("Numero recebido pelo produtor : '%s'\n", str_received);
            num_received = atoi(str_received);
            if(num_received != 0)
                num_avaliator(num_received);
            else{
                printf("End producer - consumer\n");
                exit(0);
            }
        }
    }
}

int main(int argc, char *argv[])
{
/*
ARGUMENTS:
    argc[1] = number products to be produced.
*/

    pid_t process;

    if ( argc != 2 ){ 
        printf( "The program needs the following arguments to work correctly:  limit_number_of_products \n" );
    }
    else{
        int limit = atoi(argv[1]);

        /* Creating pipe */
        if(pipe(fd)<0) {
            perror("Error while creating pipe\n") ;
            return -1 ;
        }
        /* Creating child process*/
        if ((process = fork()) < 0){
            perror("Error while executing fork\n");
            exit(1);
        }
        if (process == -1)
            printf("Error with process creation.\n");


        /* Producer process*/
        else if (process > 0)
            producer(limit);

        /* Consumer process*/
        else
            consumer();
    }
    return(0);
}

