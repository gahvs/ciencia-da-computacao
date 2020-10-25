#include <stdio.h>
/*
AFD para identificadores da linguagem C
@author: Gabriel Vinícius Souto Abreu
*/
int isDigit(char simbolo)
{
  if(simbolo >= '0' && simbolo <= '9') return 1;
  return 0;
}

int isCN(char simbolo)
{
  if(simbolo == 'E' || simbolo == 'e') return 1;
  return 0;
}

int isDot(char simbolo)
{
  if(simbolo == '.') return 1;
  return 0;
}

int isOperator(char simbolo)
{
  if(simbolo == '+' || simbolo == '-') return 1;
  return 0;
}

int isOtherThing(char simbolo)
{
  if(!isDigit(simbolo) && !isCN(simbolo) && !isDot(simbolo) && !isOperator(simbolo)) return 1;
  return 0;
}

int delta(int estado, char simbolo)
{
  if(estado == 6 || isOtherThing(simbolo))
    return 6;
  else if(estado == 0 && isDigit(simbolo))
    return 1;
  else if(estado == 0 && (isCN(simbolo) || isDot(simbolo)))
    return 6;
  else if(estado == 0 && isOperator(simbolo))
    return 5;
  else if(estado == 1 && isDigit(simbolo))
    return 1;
  else if(estado == 1 && isCN(simbolo))
    return 2;
  else if(estado == 1 && isDot(simbolo))
    return 3;
  else if(estado == 1 && isOperator(simbolo))
    return 6;
  else if(estado ==2 && (isDigit(simbolo) || isOperator(simbolo))) 
  return 1;
  else if(estado == 2 && (isCN(simbolo) || isDot(simbolo)))
    return 6;
  else if(estado == 3 && isDigit(simbolo))
    return 4;
  else if(estado == 3 && (isCN(simbolo) || isDot(simbolo) || isOperator(simbolo)))
    return 6;
  else if (estado == 4 && isDigit(simbolo))
    return 4;
  else if(estado == 4 && (isCN(simbolo)))
    return 2;
  else if(estado == 4 && (isDot(simbolo) || isOperator(simbolo)))
    return 6;
  else if(estado == 5 && isDigit(simbolo))
    return 1;
  else if(estado == 5 && (isDot(simbolo) || isCN(simbolo) || isOperator(simbolo)))
    return 6;
}

int afd(char *entrada)
{
  int estado = 0;
  int i=0;
  for(; entrada[i] != '\0'; i++)
  {
    estado = delta(estado, entrada[i]);
  }

  if(estado == 1 || estado == 4) return 1;
  return 0;
}

int main(void) {
    FILE *arq;
    char entrada[50];

    arq = fopen("entrada_numeros_reais.txt", "r");
    while(fscanf(arq, "%s", entrada) != EOF)
    {
      if(afd(entrada))
        printf("%s: valido\n", entrada);
      else
        printf("%s: invalido\n", entrada);
    }
}
