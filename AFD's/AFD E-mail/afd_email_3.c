#include<stdio.h>
/*
AFD para identificadores da linguagem C
@author: Gabriel Vinícius Souto Abreu
*/
int isAlpha(char simbolo)
{
  if(simbolo >= 'a' && simbolo <='z') return 1;
  return 0;
}

int isDigit(char simbolo)
{
  if(simbolo >= '0' && simbolo <='9') return 1;
  return 0;
}

int isDash(char simbolo)
{
  if(simbolo == '-' || simbolo == '_') return 1;
  return 0;
}

int isOtherThing(char simbolo)
{
  if(!isAlpha(simbolo) && !isDigit(simbolo) && !isDash(simbolo) && simbolo != '.' && simbolo != '@') return 1;
  return 0;
}

int delta(int estado, char simbolo)
{
  if(estado == 7 || isOtherThing(simbolo))
    return 7;
  else if(estado == 0 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 1;
  else if((estado == 0 || estado == 3 || estado == 5) && (isDash(simbolo) || simbolo == '@' || simbolo == '.'))
    return 7;
  else if(estado == 1 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 1;
  else if(estado == 1 && (isDash(simbolo) || simbolo == '.'))
    return 2;
  else if(estado == 1 && simbolo == '@')
    return 3;
  else if(estado == 2 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 1;
  else if(estado == 2 && simbolo == '@')
    return 3;
  else if(estado == 2 && (isDash(simbolo) || simbolo == '.'))
    return 7;
  else if(estado == 3 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 4;
  else if(estado == 4 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 4;
  else if(estado == 4 && (isDash(simbolo) || simbolo == '@'))
    return 7;
  else if(estado == 4 && simbolo == '.')
    return 5;
  else if(estado == 5 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 6;
  else if(estado == 6 && (isAlpha(simbolo) || isDigit(simbolo)))
    return 6;
  else if(estado == 6 && simbolo == '.')
    return 5;
}

int afd(char *entrada)
{
  int estado = 0;
  int i;
  for(i=0; entrada[i] != '\0'; i++)
  {
    estado = delta(estado, entrada[i]);
  }

  if(estado == 4 || estado == 6) return 1;
  return 0;
}

int main()
{
  FILE *arq;
  char entrada[50];

  arq = fopen("entrada_email.txt", "r");
  while(fscanf(arq, "%s", entrada) != EOF)
  {
    if(afd(entrada))
      printf("%s: valido\n", entrada);
    else
      printf("%s: invalido\n", entrada);
  }
}
