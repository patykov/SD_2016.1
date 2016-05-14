#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <time.h>
 
#define MAXRCVLEN 127
#define PORTNUM 32001
#define MAXNUM 10000


int randon_number(int last_number){
    srand((unsigned)time(NULL));
    int n = (rand()%MAXNUM ) + 1;
    while ( last_number >= n)
        n = n + (rand()%100);
    return n;
}

int main(int argc, char *argv[])
{
/*ARGUMENTS:
    argv[1] = number products to be produced.
*/

    int limit = atoi(argv[1]);
	char buffer[MAXRCVLEN + 1]; /* +1 so we can add null terminator */                                         
	int len;

    struct sockaddr_in cons; /* socket info about the machine connecting to us */
    struct sockaddr_in prod; /* socket info about ourselves */
    int mysocket;            /* socket used to listen for incoming connections */
    socklen_t socksize = sizeof(struct sockaddr_in);  
 
    memset(&prod, 0, sizeof(prod));           /* zero the struct before filling the fields */
    prod.sin_family = AF_INET;                /* set the type of connection to TCP/IP */
    prod.sin_addr.s_addr = htonl(INADDR_ANY); /* set our address to any interface */
    prod.sin_port = htons(PORTNUM);           /* set the port number */    
 
    mysocket = socket(AF_INET, SOCK_STREAM, 0);
    /* bind prod information to mysocket */
    bind(mysocket, (struct sockaddr *)&prod, sizeof(struct sockaddr));
 
    /* start listening, allowing a queue of up to 1 pending connection */
    listen(mysocket, 1);
    printf("Producing\n");
    int consocket = accept(mysocket, (struct sockaddr *)&cons, &socksize);

    int old_random = 0;
    int new_random = 0;
    for (int i=limit; i>=0; i--){
        int qtdBytes = 0;
        char snum[10];
        if(i == 0)
            strcpy(snum, "0");
        else{
            new_random = randon_number(old_random);
            sprintf(snum, "%d", new_random);
        }

        printf("Send number %s to consumer.\n", snum);
        qtdBytes = send(consocket, snum, strlen(snum), 0);  

        //Receiving message from consumer
        len = recv(consocket, buffer, MAXRCVLEN, 0);
        buffer[len] = '\0';
 
        if (qtdBytes != 0)
        printf("Received from consumer:%s\n", buffer);
        old_random = new_random;
    } 

    close(consocket);
    close(mysocket);
    printf("Closed\n");
    return EXIT_SUCCESS;
}
