#include<stdio.h>
#include<string.h>
//VERIFICA SE UMA STRING É UM PALINDROMO (SE A PALAVRA É IGUAL SEU INVERSO)

int palindromo(char str[], int n)
{
    if(n <= 1) return 1;
    return str[0] == str[n-1] && palindromo(str + 1, n - 2);
}

int main()
{
    char word[] = "ARARA";
    if(palindromo(word, strlen(word)))
        printf("%s is paindrome\n", word);
    else
        printf("%s isn't palindrome\n", word);
}
