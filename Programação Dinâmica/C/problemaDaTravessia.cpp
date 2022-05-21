#include<iostream>
#include<stdlib.h>
using namespace std;
/*
Uma formiga que s� pode
andar para o leste ou para o
sul deseja atravessar uma
regi�o no sentido norte-sul de
forma que a somat�ria das
diferen�as de altura entre
regi�es subsequentes de seu
caminho seja a menor poss�vel.
Determine esse caminho.
*/

int regiao [5][5] = {
    {23, 18, 17, 25, 31},
    {13, 15, 16, 22, 19},
    {10, 12, 13, 17, 15},
    {4, 3, 2, 9, 11},
    {5, 0, 1, 2, 7}
};

int way(int x, int y)
{
    if(x == 0) return regiao[x][y];
    return min(way(x-1, y) + abs(regiao[x][y]-regiao[x-1][y]),
               way(x, y-1) + abs(regiao[x][y]-regiao[x][y-1]));
}

int main()
{
    cout << way(1, 0) << endl;
    return 0;
}
