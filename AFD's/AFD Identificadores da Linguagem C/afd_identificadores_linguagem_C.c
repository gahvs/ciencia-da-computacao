#include <stdio.h>
/*
AFD para identificadores da linguagem C
@author: Gabriel Vinícius Souto Abreu
*/

int isDigit(char simbolo)
{
  if(simbolo >= '0' && simbolo <= '9')
  {
    return 1;
  }
  else 
  {
    return 0;
  }
}

int isNonDigit(char simbolo)
{
  if((simbolo >= 'a' && simbolo <= 'z') || (simbolo >= 'A' && simbolo <= 'Z') || simbolo == '_')
  {
    return 1;
  }
  else
  {
    return 0;
  }
}

int isOtherCharcter(char simbolo)
{
  if(!isDigit(simbolo) && !isNonDigit(simbolo))
    return 1;
  else
  {
    return 0;
  }
}

int delta(int estado, char simbolo)
{
  if(estado == 2 || isOtherCharcter(simbolo))
    return 2;
  if(estado == 0 && isNonDigit(simbolo))
    return 1;
  else if(estado == 0 && isDigit(simbolo))
    return 2;
  else if(estado == 1 && isNonDigit(simbolo))
    return 1;
  else if(estado == 1 && isDigit(simbolo))
    return 1;
}

int afd(char *entrada)
{
  int estado = 0;
  int i;

  for(i=0; entrada[i]!='\0'; i++)
  {
    estado = delta(estado, entrada[i]);
  }

  if(estado == 1) return 1;
  return 0;
}

int main(void) {
  FILE *arq;
  char entrada[50];

  arq = fopen("entrada_id_C.txt", "r");
  if(!arq) return 0;

  while(fscanf(arq, "%s", entrada) != EOF)
  {
    if(afd(entrada))
      printf("%s: valida\n", entrada);
    else
      printf("%s: invalida\n", entrada);
  }

  return 0;
}
