// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//        Sebestien Palmerio
// Converting Strings to 1337 (leet)   
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include "leet.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// see leet.h for documentation
void leet(char *str){
  assert(str != NULL);
  int len = strlen(str); // O(n)
  int i = 0;
  while (i < len) { // loop runs O(n) times, Total: O(n^2)
    if (str[i] == 65) {
      len += 2;
      for (int j = len - 1; j > i; --j) { // loop runs O(n) times
        str[j + 2] = str[j];
      }
      str[i] = '/';
      str[i + 1] = '-';
      str[i + 2] = '\\';
      i += 2;
    } else if (str[i] == 69) str[i] = '3';
      else if (str[i] == 73) str[i] = '!';
      else if (str[i] == 76) str[i] = '1';
      else if (str[i] == 79) {
      len += 1;
      for (int j = len - 1; j > i; --j) { // loop runs O(n) times
        str[j + 1] = str[j];
      }
      str[i] = '[';
      str[i + 1] = ']';
      ++i;
    } else if (str[i] == 84) str[i] = '7';
      else if (str[i] == 85) {
      len += 2;
      for (int j = len - 1; j > i; --j) { // loop runs O(n) times
        str[j + 2] = str[j];
      }
      str[i] = '|';
      str[i + 1] = '_';
      str[i + 2] = '|';
      i += 2;
    }
    ++i;
  }
}


// see leet.h for documentation
void undo_leet(char *str){
  assert(str != NULL);
  int len = strlen(str); // O(n)
  int i = 0;
  while (i <= len) { // loop runs O(n) times, Total: O(n^2)
    if (i == len) str[i] = '\0';
    if (str[i] == 47 && str[i + 1] == 45 && str[i + 2] == 92) {
      str[i] = 'A';
      for (int j = i + 3; j < len; ++j) { // loop runs O(n) times
        str[j - 2] = str[j];
      }
      len -= 2;
    } else if (str[i] == 51) str[i] = 'E';
      else if (str[i] == 33) str[i] = 'I';
      else if (str[i] == 49) str[i] = 'L';
      else if (str[i] == 91 && str[i + 1] == 93) {
      str[i] = 'O';
      for (int j = i + 2; j < len; ++j) { // loop runs O(n) times
        str[j - 1] = str[j];
      }
      len -= 1;
    } else if (str[i] == 55) str[i] = 'T';
      else if (str[i] == 124 && str[i + 1] == 95 && str[i + 2] == 124) {
      str[i] = 'U';
      for (int j = i + 3; j < len; ++j) { // loop runs O(n) times
        str[j - 2] = str[j];
      }
      len -= 2;
    }
    ++i;
  }
}