#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>

#define LOCKED 1
#define UNLOCKED 0

int lock = UNLOCKED;
long int *vector = NULL;
long int count = 0;
long int N;
long int sum = 0;
int n;

int TestAndSet(int* spinlock) {
    int oldValue = *spinlock;
    *spinlock = LOCKED;
    return oldValue;
}
void acquire(lock) {
	while(TestAndSet(&lock));
}
void release(lock) {
	lock = UNLOCKED;
}

void num_generator(){
	for (int i=0; i<N; i++){
		vector[i] = (rand() % 200) - 100;
		//printf("Numero gerado: %ld\n", vector[i]);
	}
}

void *counter(void *threadid)
{
	long tid = (long)threadid;
	int tmp = 0;
	int initial = tid*n;
	for (int i=0; i<n; i++){
		if((i+initial) >= N)
			break;
		//printf("Thread %ld, somando vetor[%d]\n",tid, i+initial);
		tmp += vector[i + initial];
	}
	acquire(lock);
	sum += tmp;
	count += n;
	release(lock);
   	pthread_exit(NULL);
}

int divide_vector(int n, int num_threads){
	float rest = n%num_threads;
	int number = trunc(n/num_threads);
	if (rest != 0)
		number += 1;
	return number;
}

int main(int argc, char *argv[]){
	/*
	argv[1] = numero de threads K = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30.
	argv[2] = tamanho N do vetor
				8 para 10^8, 
				9 para 10^9, 
				10 para 10^10.
	*/

	N = pow(10, atoi(argv[2]));
	vector = malloc(sizeof(long int)*N);
	
	int NUM_THREADS = atoi(argv[1]);
	pthread_t threads[NUM_THREADS];
    long t;
    //Generate random seed
	srand( (unsigned)time(NULL) );

    num_generator();

    //divide the vector size to the number of threads
    n  = divide_vector(N, NUM_THREADS);
    for(t=0; t<NUM_THREADS; t++){
        int err = pthread_create(&threads[t], NULL, counter, (void *)t);
        if (err){
        	printf("ERROR; return code from pthread_create() is %d\n", err);
        	exit(-1);
      	}
    }
    //Waiting for all the threads to finish
    while(N > count);
    free(vector);
    //printf("A soma total foi: %0.3ld\n", sum);
    exit(0);
}

