#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define length 12
#define capacity 35

void detailSolution(int solution[])
{
	printf("SOLUCAO   : ");print(solution);
	printf("PESO      : %d\n", calculateSolutionWeight(solution));
	printf("BENEFICIO : %d\n\n\n", calculateSolutionBenefit(solution));
}

void print(int array[])
{
	int i;
	printf("[");
	for(i=0; i<length; i++)
	{
		if(i==length-1)
			printf("%d", array[i]);
		else
			printf("%d, ", array[i]);
		
	} printf("]\n");
}

int copy(int origin[], int destiny[])
{
	int i;
	for(i=0; i<length; i++)
		destiny[i] = origin[i];
}

int *generateValidInitialSolution()
{
	static int solution[length];
	int i;
	
	while(1)
	{
		for(i=0; i<length; i++)
		{
			solution[i] = rand() % 2;	
		}
		if(calculateSolutionWeight(solution) <= capacity)
			return solution;
	}
}

int calculateSolutionWeight(int solution[])
{
	int weights[length] = {4, 5, 7, 9, 6, 3, 9, 1, 2, 9, 4, 5};
	int i, totalWeight=0;
	
	for(i=0; i<length; i++)
	{
		if(solution[i])
			totalWeight += weights[i];
	}
	
	return totalWeight;
}

int calculateSolutionBenefit(int solution[])
{
	int benefits[length] = {2, 2, 3, 4, 4, 2, 3, 4, 2, 1, 1, 2};
	int i, totalBenefit=0;
	
	for(i=0; i<length; i++)
	{
		if(solution[i])
			totalBenefit += benefits[i];
	}
	
	return totalBenefit;
}

void generateNeighborhood(int solution[], int neighbors[length][length])
{
	//generates the neighbors of the parameter solution
    //the neighborhood are solutions that differ 1bit from the current solution
    int neighbor[12];
	int i, l;

    for(i=0; i<length; i++)
    {
    	copy(solution, neighbor);
    	neighbor[i] = (neighbor[i] == 1) ? 0 : 1;
    	
    	for(l=0; l<length; l++)
	    	neighbors[i][l] = neighbor[l];
	}
}

void getBestNeighbor(int neighbors[length][length], int bestNeighbor[])
{
	int i, l, bestBenefit=0, solutionBenefit=0;
	
	for(i=0; i<length; i++)
	{
		solutionBenefit = calculateSolutionBenefit(neighbors[i]);
		if(solutionBenefit > bestBenefit)
		{
			bestBenefit = solutionBenefit;
			for(l=0; l<length; l++)
				bestNeighbor[l] = neighbors[i][l];
		}
	}

}

int *uphill(int initialSolution[])
{
	static int bestSolution[length], bestNeighbor[length];
	copy(initialSolution, bestSolution);
	
	int bestBenefit = calculateSolutionBenefit(bestSolution), neighborBenefit;
	int neighborhood[length][length];
	
	
	while(1)
	{
		generateNeighborhood(bestSolution, neighborhood);
		getBestNeighbor(neighborhood, bestNeighbor);
		
		neighborBenefit = calculateSolutionBenefit(bestNeighbor);
		
		if(calculateSolutionWeight(bestNeighbor) <= capacity)
		{
			if(neighborBenefit > bestBenefit)
			{
				bestBenefit = neighborBenefit;
				copy(bestNeighbor, bestSolution);
			}
		}
		else if(neighborBenefit < bestBenefit)
		{
			return bestSolution;
		}	
	}
}

int main()
{
	srand(time(NULL));
	int *initialSolution, *finalSolution;
	initialSolution = generateValidInitialSolution();
	finalSolution   = uphill(initialSolution);
	
	detailSolution(initialSolution);
	detailSolution(finalSolution);
}








