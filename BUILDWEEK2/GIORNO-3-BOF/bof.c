#include <stdio.h>

int main () {

int vector[10], i, j, k, ntemp, scelta;
int swap_var;
i=0;
j=0;
k=0;

while(1){
	printf("------- MENU --------\n");
	printf("1) Programma corretto\n");
	printf("2) Programma con possibile BOF\n");
	printf("---------------------\n");
	printf("Scelta: ");
	scanf("%d", &scelta);
	if(scelta > 2){
		printf("Inserisci un valore ammesso.\n\n");
	}else{
		break;
	}
}

switch(scelta){
	case (1):
		printf ("\n\n------ SCELTA 1 --------\n");
		printf ("Inserire 10 interi:\n");
		for ( i = 0 ; i < 10; i++)
		{
			int c= i+1;
			printf("[%d]:", c);
			scanf ("%d", &vector[i]);
		}


		printf ("Il vettore inserito e':\n");
		for ( i = 0 ; i < 10 ; i++)
		{
			int t= i+1;
			printf("[%d]: %d", t, vector[i]);
			printf("\n");
		}


		for (j = 0 ; j < 10 - 1; j++)
		{
			for (k = 0 ; k < 10 - j - 1; k++)
			{
				if (vector[k] > vector[k+1])
				{
					swap_var=vector[k];
					vector[k]=vector[k+1];
					vector[k+1]=swap_var;
				}
			}
		}

		printf("Il vettore ordinato e':\n");
		for (j = 0; j < 10; j++)
		{
			int g = j+1;
			printf("[%d]:", g);
			printf("%d\n", vector[j]);
		}
		
		break;
		
	case (2):
		printf ("\n\n------ SCELTA 2 --------\n");
		printf ("Inserire 10 interi:\n");

		while(1){
			printf("[%d]", i+1);
			printf("Inserisci il numero. -1 per uscire: ");
			scanf("%d", &ntemp);
			if(ntemp >= 0){
				vector[i] = ntemp;
				i=i+1;
			}else{
				break;
			}
			//printf("i= %d, j= %d, k= %d \n",i,j,k);
		}



		printf ("Il vettore inserito e':\n");
		for ( i = 0 ; i < 10 ; i++)
			{
				int t= i+1;
				printf("[%d]: %d", t, vector[i]);
				printf("\n");
			}


		for (j = 0 ; j < 10 - 1; j++)
			{
			for (k = 0 ; k < 10 - j - 1; k++)
				{
					if (vector[k] > vector[k+1])
					{
					swap_var=vector[k];
					vector[k]=vector[k+1];
					vector[k+1]=swap_var;
					}
				}
			}

		printf("Il vettore ordinato e':\n");
		for (j = 0; j < 10; j++)
			{
			int g = j+1;
			printf("[%d]:", g);
			printf("%d\n", vector[j]);
			}
	break;
}

return 0;


}
