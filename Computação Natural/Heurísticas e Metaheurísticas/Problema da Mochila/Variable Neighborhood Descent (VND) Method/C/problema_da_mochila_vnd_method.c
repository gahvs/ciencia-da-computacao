#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define length 12
#define capacity 35
#define structures 3


int *generateInitialValidSolution()
{

	static int solution[length], i;

    while(1)
    {
    	for (i = 0; i < length; i++)
		{
			solution[i] = rand() % 2;
		}
		if(calculateSolutionWeight(solution) <= capacity)
			return solution;
	}
	
}

int *getTwoDifferRandomValues(int limit)
{
	static int values[2];
	while(1)
	{
		values[0] = rand() % limit;
		values[1] = rand() % limit;

		if(values[0] != values[1])
		{
			return values;
		}
	}
}

int *copy(int array[])
{
	static int copy[length];
	int i;
	for (i = 0; i < length; i++) {
		copy[i] = array[i];
	}
	return copy;
}

int *slice(int array[], int start, int end)
{
	//returns only slices with lenght = 4	
	int i;
	static int slice[4]; //start-end = 4
	for(i=0; start<end; start++, i++)
	{
		slice[i] = array[start];
	}
	return slice;
}

void shuffle(int array[], int len)
{
	int randIndex = 0, temp = 0, i;
	for(i=len-1; i>=0; i--)
	{
		randIndex = rand() % (i + 1);
		temp = array[i];
		array[i] = array[randIndex];
		array[randIndex] = temp; 
	}
}

void insertShuffledSliceInArray(int array[], int sliced[], int init)
{
	int i;
	for(i=0; i<4; init++, i++) //i<len of slice
	{
		array[init] = sliced[i]; 
	}
}

int includes(int matrix[][length], int array[], int matrixLines)
{
	//checks if the array is already in the matrix
	int i,l,aux;
	for(i=0; i<matrixLines; i++)
	{
		for(l=0, aux=0; l<length; l++)
		{
			if(matrix[i][l] == array[l])
				aux++;
		}
		if(aux == length)
			return 1;
		aux = 0;
	}
	return 0;
}

void print(int array[])
{
	int i;
	printf("[");
	for(i=0; i<length;i++)
	{
		printf("%d", array[i]);
		if(i<(length-1)) printf(", ");	
	}
	printf("]\n");
}

void neighborhoodStructure1(int solution[], int neighbors[length][length])
{
	// this structure generates neighbors that differ 1 bit from the solution
	int i, l;

	for (i = 0; i < length; i++)
	{
		int *neighbor = copy(solution);

		neighbor[i] = (neighbor[i]==0) ? 1 : 0;

		for(l=0; l<length; l++) 
		{
			neighbors[i][l] = neighbor[l];
		}
	}

}

void neighborhoodStructure2(int solution[], int neighbors[length][length])
{
	/* this structure generates neighbors by exchanging the value of a random
    position with another position also random */
    int i=0,l, aux;
    while(i<length)
    {
    	int *neighbor = copy(solution);
    	int *indexes  = getTwoDifferRandomValues(length - 1);
    	
    	aux = neighbor[indexes[0]];
    	neighbor[indexes[0]] = neighbor[indexes[1]];
    	neighbor[indexes[1]] = aux;
    	
    	if(includes(neighbors, neighbor, i))
    	{
    		i = i - 1;
		} 
		else 
		{
			for(l=0; l<length; l++)
			{
				neighbors[i][l] = neighbor[l];
			}
		}
		
		i = i + 1;
	}
    
}

void neighborhoodStructure3(int solution[], int neighbors[length][length])
{
	// this structure chooses two random positions and changes its value
	int i=0, l;
	while(i < length)
	{
		int *neighbor = copy(solution);
		int *indexes  = getTwoDifferRandomValues(length - 1);
		int frst = indexes[0], scnd = indexes[1];
		
		neighbor[frst] = (neighbor[frst])==0 ? 1 : 0;
		neighbor[scnd] = (neighbor[scnd])==0 ? 1 : 0;
		
		if(includes(neighbors, neighbor, i))
		{
			i = i - 1;
		}
		else
		{
			for(l=0; l<length; l++)
			{
				neighbors[i][l] = neighbor[l];
			}
		}
		i = i + 1;
	}
}

/* void *neighborhoodStructure4(int solution[], int neighbors[length][length])
{
	// this structure randomly chooses a range of 4 values ??and shuffles them
	int i=0,l;
	while(i<length)
	{
		int *neighbor = copy(solution);
		int init = rand() % (length - 4), end = init + 4;
		
		int *sliced = slice(neighbor, init, end);
		insertShuffledSliceInArray(neighbor, sliced, init);
		
		if(includes(neighbors, neighbor, i))
		{
			printf("the problem is the random generate...\n");
			i = i - 1;
		}
		else
		{
			for(l=0; l<length; l++)
			{
				neighbors[i][l] = neighbor[l];
			}
		}
		i = i + 1;
	}
} */

int calculateSolutionWeight(int solution[])
{
	int i, totalWeight = 0;
	int weights[length] = {4, 5, 7, 9, 6, 3, 9, 1, 2, 9, 4, 5};

	for(i = 0; i<length; i++)
	{
		if(solution[i])
		{
			totalWeight += weights[i];
		}
	}

	return totalWeight;
}

int calculateSolutionBenefit(int solution[])
{
	int i, totalBenefit = 0;
	int benefits[length] = {2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2};

	for(i = 0; i<length; i++)
	{
		if(solution[i])
		{
			totalBenefit += benefits[i];
		}
	}

	return totalBenefit;
}

void generateNeighborhood(int solution[], int neighbors[length][length], int strucure)
{
	switch(strucure)
	{
		case 1:
			neighborhoodStructure1(solution, neighbors);
			break;
		case 2:
			neighborhoodStructure2(solution, neighbors);
			break;
		case 3:
			neighborhoodStructure3(solution, neighbors);
			break;
		// case 4:
		// 	neighborhoodStructure4(solution, neighbors);
		// 	break;
	}
}

int *bestImprovementMethod(int solution[], int currentStructure)
{
	int currentBenefit = calculateSolutionBenefit(solution);
	int neighbors[length][length];
	int *neighbor, *bestSolution = copy(solution);
	int i, neighborBenefit, neighborWeight;
	
	generateNeighborhood(solution, neighbors, currentStructure);
		
	for(i=0; i<length; i++)
	{
		neighbor = copy(neighbors[i]);	
		neighborBenefit  = calculateSolutionBenefit(neighbor);
		neighborWeight  = calculateSolutionWeight(neighbor);
		
		if(neighborBenefit > currentBenefit)
		{
			if(neighborWeight <= capacity)
			{
				bestSolution    = copy(neighbor);
				currentBenefit  = neighborBenefit;
			}
		}
	}
	return bestSolution;
}

int *vnd(int initialSolution[])
{
	int currentStructure = 1;
	int *currentSolution = copy(initialSolution);
	int currentBenefit = calculateSolutionBenefit(currentSolution);
	
	while(currentStructure <= structures)
	{
		int *bestNeighbor       = bestImprovementMethod(currentSolution, currentStructure);
		int bestNeighborWeight  = calculateSolutionWeight(bestNeighbor);
		int bestNeighborBenefit = calculateSolutionBenefit(bestNeighbor);
		
		print(currentSolution);
				print(bestNeighbor);
				print(bestImprovementMethod(currentSolution, currentStructure));
		
		if(bestNeighborBenefit > currentBenefit)
		{
			if(bestNeighborWeight <= capacity)
			{
				currentBenefit   = bestNeighborBenefit;
				currentSolution  = copy(bestNeighbor);
				currentStructure =  1;	
			}	
		}
		else
		{
			currentStructure = currentStructure + 1;
		}
	}
	return currentSolution;
}

int main()
{
	srand(time(NULL));
	
	int *initialSolution, *finalSolution;
	
	initialSolution = generateInitialValidSolution();
	finalSolution   = vnd(initialSolution);
	
	
	printf("Problema da Mochila - Variable Neighborhood Descent Method\n\n");
	printf("Solucao inicial   : "); print(initialSolution);
	printf("Peso inicial      : %d\n", calculateSolutionWeight(initialSolution));
	printf("Beneficio inicial : %d\n", calculateSolutionBenefit(initialSolution));
	
	printf("\nSolucao final     : "); print(finalSolution);
	printf("Peso final        : %d\n", calculateSolutionWeight(finalSolution));
	printf("Beneficio final   : %d\n", calculateSolutionBenefit(finalSolution));
	
	
}
