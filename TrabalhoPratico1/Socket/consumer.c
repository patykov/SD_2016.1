#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
 
#define MAXRCVLEN 127
#define PORTNUM 32001
 
int num_avaliator(int n){
    /* Returns 0 if n is a prime number or 1 if not.*/
    int flag = 0;
    for (int i=2; i<=n/2; ++i){
        if (n%i == 0){
            flag = 1;
            break;
        }
    }
    return flag;
}

int main(int argc, char *argv[])
{
   char msg[MAXRCVLEN];
   char buffer[MAXRCVLEN + 1]; /* +1 so we can add null terminator */
   int len, mysocket;
   struct sockaddr_in dest; 
 
   mysocket = socket(AF_INET, SOCK_STREAM, 0);
 
   memset(&dest, 0, sizeof(dest));                /* zero the struct */
   dest.sin_family = AF_INET;
   dest.sin_addr.s_addr = htonl(INADDR_LOOPBACK); /* set destination IP number - localhost, 127.0.0.1*/ 
   //dest.sin_addr.s_addr = inet_addr("192.168.0.106");
   dest.sin_port = htons(PORTNUM);                /* set destination port number */
 
   connect(mysocket, (struct sockaddr *)&dest, sizeof(struct sockaddr));

   int receiving = 1;
   while (receiving){
      //Receiving message from producer
      len = recv(mysocket, buffer, MAXRCVLEN, 0);

      buffer[len] = '\0';

      if(strcmp(buffer,"0") == 0) {
        receiving = 0;
        printf("Closed\n");
      }
      else{
        printf("Received number: %s from producer.\n", buffer);
        if (num_avaliator(atoi(buffer)) == 0)
          strcpy(msg, " is a prime number.\n");
        else
          strcpy(msg, " is not a prime number.\n");
       
        int qtdBytes =0;
        if (len != 0){ 
          //Sending message to producer
          qtdBytes = send(mysocket, msg, strlen(msg), 0); 
        }
      }
    }


   close(mysocket);
   return EXIT_SUCCESS;
}




