#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>

#define LIMIT 10000000
#define MAXIMUM_NUMBER 10000 //Max number of products consumed. (condição de parada)

long int N;
long int M;
long int *vector = NULL;

void num_generator(){
	long int n = (rand() % LIMIT);

	vector[i] = 
		printf("%ld\n", vector[i]);
	}
}


int main(int argc, char *argv[]){
	/*
	argv[1] = tamanho do vetor: N = 2, 4, 8, 16, 32
	argv[2] = numero de threads produtoras Np
	argv[3] = numero de threads consumidoras Nc
			(Np, Nc) = {(1, 1),(2, 2),(5, 5),(10, 10),(2, 10),(10, 2)}.
	*/

	N = atoi(argv[1]);
	//Initializes the vector with 0's. 
	vector = calloc(sizeof(long int)*N);
	
	int Np = atoi(argv[2]);
	int Nc = atoi(argv[3]);

	pthread_t produtor[Np];
	pthread_t consumidor[Nc];
    long t;
 	int err;

 	//Generate random seed
	srand( (unsigned)time(NULL) );

    //Creating producer threads
	for(t=0; t<Np; t++){
		err = pthread_create(&produtor[t], NULL, num_generator, (void *)t);
        if (err){
        	printf("ERROR; return code from pthread_create() is %d\n", err);
        	exit(-1);
      	}
    }
    //Creating consumer threads
    for(t=0; t<Nc; t++){
        err = pthread_create(&consumidor[t], NULL, num_avaliator, (void *)t);
        if (err){
        	printf("ERROR; return code from pthread_create() is %d\n", err);
        	exit(-1);
      	}
    }

    free(vector);
    pthread_exit(NULL);
}

