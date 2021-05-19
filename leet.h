// leet(str) applies the leet encoding to the given string using:
//   O -> []   I -> !    E -> 3    T -> 7
//   A -> /-\  U -> |_|  L -> 1
//   The function assumes that the string array has enough 
//   space to hold the resulting leet string
// Implementation restriction: the function must not create
//   a new char array/string i.e. it must create the leet 
//   encoding "in place" by manipulating characters in the 
//   existing string
// requires: str is not NULL 
// effects: mutates *str
// time: O(n^2), n is the length of str
void leet(char *str);


// undo_leet(str) will undo a string that had previously 
//   been leet encoded. The sequence of application of leet 
//   followed by undo_leet only produces str again if str 
//   does not originally contain any of the leet encodings 
//   to begin with. For example, if str already had a 3, 
//   undo_leet will change that to an E.
// requires: str is not NULL 
// effects: mutates *str
// time: O(n^2), n is the length of str
void undo_leet(char *str);
