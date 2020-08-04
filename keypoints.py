(1)STRINGS:
    --> Input returns string.
    []--> sub operator.
 
(a)Slicing strings --> (x[0: 8])
(b)Manipulating strings
      (i)String Concatenation.
              (in as keyword --> to check if one string is "in" another string.
              (in as expression --> (logical expression) returns true/false & can be used in if statement.
      (ii)String  Comparision.
              ==
              <
              >
*String library:
       (a)Searching in a string.  --> .find('')
       (b)Upper case & lower case --> .upper()   .lower()
       (c)Search and replace      --> .replace('', '')
       (d)Stripping white space   --> lstrip() , rstrip() , strip()
       (e)Prefixes                --> .startswith('')
               
*Parsing and extracting: #extract 2013
       data = 'larajohn2013@gmail.com'
       pos  = data.find('@')
       print(pos)
       piece= data[pos+1:]
       print(piece)
            
  /************************************************************xxxxxxxxxxxxxxxxx*********************************************************/   
               
(2)FILES:
    A text file  can be thought as a sequence of lines.
    File is not the data, it's just a way to get at the data.
               
*Opening a file:
        open() returns a "file handle"
        handle = open(filename, mode)  --> mode is optional (r-read the file), (w-write to the file) 
    Ex: fhand = open('mbox.txt', 'r')
        returns a handle use to manipulate a file.
               
 *Handle: (a connection to file's data)
        A porthole b/w the program and the file that's on the disk.
           
 *Newline character: \n
 .read --> Read the whole file (including newlines) into the single string.
 Skipping with 'continue'          
           
/***********************************************************xxxxxxxxxxxxxxxxxxxx*********************************************************/        
           
(3)LISTS           
    A list is a collection
    In a single variable, we can have more than one thing.
    Lists are mutable.
    Strings are immutable.
    Range function returns a list of numbers.  print(range(4))
                                               [0,1,2,3]
           
*Manipulating lists:
    (a)Concatenating lists using +
    (b)Slicing t[:]
           
*Lists of method:   
    ['append', 'count', 'extend','index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    .sort --> to  get ordered list
    .split -> '   ' -> ['', '', '']
           
/****************************************************************xxxxxxxxxxxxxxxxxxxxxx***************************************************/
           
(4)DICTIONARIES:
     A 'bag' of values, each with its own 'label'.
     List of values in dict() --> keys()
     Contents are mutable.
     python dict feature in other programming language --> 'Associative arrays'
           
 *get method:           
      .get( , ) --> II parameter-> to provide a default value if the key is not found.
           
 /*************************************************************xxxxxxxxxxxxxxxxxxxxxxxxxx*************************************************/          
           
 (4)TUPLES:
      Limited version of lists.
      More efficient.
      Can't be modified.
      Strings and tuples are immutable.
      Can't append.    
      Can't sort.     
      Can't reverse.     
      Items give a list of tuples.
      Tuples are comparable.     
--> Tuples are prefered over lists --> tmp var -> discarded without modifying.         
           
           
               
               
               
