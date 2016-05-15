#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>
//#include <sys/sem.h>
#include <semaphore.h>

#define LIMIT 10000000
#define MAXIMUM_NUMBER 50 //Max number of products consumed. (stop condition)

int M; //Counter to the number of products consumed 
long int N; //Size of shared memory vector
long int *vector = NULL;
sem_t *sem_mutex;
sem_t *sem_full;
sem_t *sem_empty;

void *num_generator(void *threadid){
	long int n;
	long tid = (long)threadid;
	while(M != MAXIMUM_NUMBER){
		n = (rand() % LIMIT);
		//Produce
		sem_wait(&sem_empty);
		sem_wait(&sem_mutex);
		//Adding resource to the vector
		for (int i=0; i<N; i++){
			if (vector[i] == 0){
				printf("Thread %d produtora adicionando o numero: %d \n", tid, n );
				vector[i] = n;
				printf("vector[%d, %d, %d, %d]\n", vector[0],vector[1],vector[2],vector[3]);
				sleep(1);
				break;
			}
		}
		sem_post(&sem_mutex);
		sem_post(&sem_full);
	}
}

void *num_avaliator(void *threadid){
	long tid = (long)threadid;
	while(M != MAXIMUM_NUMBER){
		//Produce
		sem_wait(&sem_full);
		sem_wait(&sem_mutex);
		int flag = 0;
		//Consume an item
		for (int i=(N-1); i>=0; i--){
			long int n = vector[i];
			if (n != 0){
				//Check if it's a prime number
    			for (int i=2; i<=n/2; ++i){
        			if (n%i == 0){
            			flag = 1;
            			break;
        			}
    			}
    			vector[i] = 0;
    			M++;
				if(flag == 0)
        			printf("%ld is a prime number. Removed from vector[%d] Thread %d\n", n, i, tid);
    			else
        			printf("%ld is not a prime number.Removed from vector[%d] Thread %d\n", n, i, tid);
        		sleep(1);
        		sem_post(&sem_mutex);
				sem_post(&sem_empty);
    			break;
			}
		}
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
	vector = calloc(N, sizeof(long int));

	int Np = atoi(argv[2]);
	int Nc = atoi(argv[3]);

	pthread_t produtor[Np];
	pthread_t consumidor[Nc];
    long t;
 	int err;

	sem_init(&sem_mutex, 0, 1);
	sem_init(&sem_full, 0, 0);
	sem_init(&sem_empty, 0, N);


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
    sem_close(sem_mutex);
    sem_close(sem_full);
    sem_close(sem_empty);
    pthread_exit(NULL);
}

