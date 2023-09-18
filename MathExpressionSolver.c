#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int operator = 1;
/**
 * 1 = Addition
 * 2 = Subtraction
 * 3 = Multiplication
 * 4 = Division
*/

int main() {
  int sum = 0;
  char expression[100];
  gets(expression);

  int k = 0;
  char number[50];

  for(int i=0; i<strlen(expression); i++) {
    if(isdigit(expression[i])) {
      number[k++] = expression[i];
      // puts(number);
    } else {
      // printf("%d\n", atoi(number));
      number[k] = '\0';
      k = 0;
      if(operator == 1) {
        sum += atoi(number);
        if(expression[i] == '+') operator = 1;
        else operator = 2;
      } else if(operator == 2) {
        sum -= atoi(number);
        if(expression[i] == '+') operator = 1;
        else operator = 2;
      }
    }
  }
  number[k] = '\0';
  if(operator == 1) sum += atoi(number);
  else sum -= atoi(number);
  printf("Result = %d", sum);

  return 0;
}