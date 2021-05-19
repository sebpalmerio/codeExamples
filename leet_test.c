#include <stdio.h>
#include <stdlib.h>
#include "leet.h"
#include <string.h>

// a simple I/O test client for leet

int main(void) {
  char src[100] = "";
  char command[10] = "";
  scanf("%s",command);
  while(strcmp(command,"quit")){
    if (!strcmp(command,"read")){
      scanf("%s",src);
    } else if (!strcmp(command,"leet")){
      leet(src);
    } else if (!strcmp(command,"undo")){
      undo_leet(src);
    } else if (!strcmp(command,"print")){
      printf("%s\n",src);
    }
    scanf("%s",command);
  }
}