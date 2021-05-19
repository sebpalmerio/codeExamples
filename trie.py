##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##       Sebestien Palmerio
##    Trie Definition in Python
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##

class Trie:
    def __init__(self, data):
        '''Set the data to the given data.
        To start with an empty tree, pass the empty dictionary, {}.'''
        self.data = data

    def __repr__(self):
        return 'Trie({})'.format(self.data)

    def __eq__(self, other):
        return isinstance(other, Trie) and \
            self.data == other.data
    
    def add(self, word):
        '''
        Returns None and mutates self to create a Trie of each word
        Effects: Mutates self
        
        add: Trie Str -> None
        Examples:
           sample2 = Trie({})
           sample2.add(['a', 'an', 'and', 'was', 'wax', 'way', 'win'] => None
           sample2 is mutated to 
           Trie({'a': Trie({'': None, 'n': Trie({'': None, 
                    'd': Trie({'': None})})}), 
                           'w': Trie({'a': Trie({'s': Trie({'': None}), 
                               'x': Trie({'': None}), 'y': Trie({'': None})}), 
                                         'i': Trie({'n': Trie({'': None})})})})
        '''
        if word == '':
            return
        
        elif word[0] in self.data:
            if len(word) == 1:
                self.data[word[0]].data[''] = None
            
            self.data[word[0]].add(word[1:])
        
        else:
            if len(word) == 1:
                self.data[word[0]] = Trie({"": None})
                
            else:
                self.data[word[0]] = Trie({})
                
            self.data[word[0]].add(word[1:]) 
            
        return


    def readfile(self, filename):
        '''
        Returns None and mutates self to a Trie with each word on a line of a
        file, filename, put into self.
        Effects: Mutates self
        
        readfile: Trie Str -> None
        Example:
           sample2 = Trie({})
           sample2.readfile('sample.txt') => None
           sample2 is mutated to
           Trie({'a': Trie({'': None, 'n': Trie({'': None, 
                    'd': Trie({'': None})})}), 
                           'w': Trie({'a': Trie({'s': Trie({'': None}), 
                               'x': Trie({'': None}), 'y': Trie({'': None})}), 
                                         'i': Trie({'n': Trie({'': None})})})})
        '''
        fin = open(filename, 'r')
        name = fin.readline()
        while (name != ""):
            name = name.split()[0]
            self.add(name)
            name = fin.readline()
        
        fin.close()
        return
            
            
    def helper(self, word, new_L):
        '''
        Makes dump() work
        
        helper: Trie Str (listof Str) -> (listof Str)
        requires: new_L == []
        '''
        L = list(self.data.keys())
        for i in L:
            if i == "":
                new_L.append(word)
            
            else:
                self.data[i].helper(word + i, new_L)
                
        return new_L
            
            
    def dump(self):
        '''
        Returns a list of strings, determined by deconstructing a Trie
        
        dump: Trie -> (listof Str)
        
        Examples:
           sample1 = Trie({'a': Trie({'': None,
                           'n': Trie({'': None,
                                      'd': Trie({'': None})})}),
                'w': Trie({'a': Trie({'s': Trie({'': None}),
                                      'x': Trie({'': None}),
                                      'y': Trie({'': None})}),
                           'i': Trie({'n': Trie({'': None})})})})
                           
           sample1.dump() => ['a', 'an', 'and', 'was', 'wax', 'way', 'win']
        '''
        if self == Trie({'': None}):
            return ['']
        
        else:
            L = list(self.data.keys())
            new_L = []
            
            for i in L:
                new_L.append(self.data[i].helper(i, []))  
            
            L = []
            for i in new_L:
                for j in i:
                    L.append(j)
            
        return sorted(L)

# sample functions
def seek(T, word):
  '''
  Returns a string that identifies where the spelling of a string, word, has
  gone incorrect. This is determined by a Trie, T. 
  
  seek: Trie Str -> Str
  '''
  L = []
  for i in T.dump():
    L.append(i.lower())
  
  if word.lower() in L:
    return word
  
  
  def helper(T, word):
    string = ''
    if word == '':
      string += '*'
      
    elif word[0] not in T.data:
      string += '*' + word[word.index(word[0]):]
              
    else:
      string = word[0] + helper(T.data[word[0]], word[1:])

    return string
  
  new_s = helper(T, word.lower())
  index = new_s.index('*')
  word = word[:index] + '*' + word[index:]
  
  return word



def spellcheck_file(T, filein, fileout):
  '''
  Returns None. Rewrites a file, filein, to correct all misspelled words and
  writes the spelled-checked version to a file, fileout.
  
  spellcheck_file: Str Str -> None
  '''
  fin = open(filein, 'r')
  word = fin.readline()
  doc = []
  while (word != ""):
    L = word.split()
    new_L = []
    for i in L:
      s = ''.join(list(filter(lambda x: x.isalpha(), i)))
      new_L.append(s)

    L2 = []
    for j in new_L:
      L2.append(seek(T, j))
      
    doc.append(L2)
    word = fin.readline()
  
  fin.close()
  
  fout = open(fileout, 'w')

  for i in doc:
    sentence = ''
    
    for j in i:
      if i.index(j) == len(i) - 1:
        sentence += j
        
      else:
        sentence += j + ' '
        
    fout.write(str(sentence) + '\n')
      
  fout.close()