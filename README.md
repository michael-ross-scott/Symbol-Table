# Compiler Symbol Table Simulation

A functional hash-table implementation of a Symbol Table that handles simple constant definitions and uses them in a statically-scoped block structured language.

## Implementation

* Uses a stack to maintain copies of hash table arrays for outer scopes. 
* Uses a hash table array size of 5, with chaining for collision resolution. 

## Program I/O 

Accepts a single command-line parameter which is the name ofa data file containing actions to be performed on the symbol table. 

The following is a sample of the data file contents:

**Input:**
```
beginscope
define a 1
use a
endscope
use a
```
**Program Output:**
```
beginscope
define a 1
use a = 1
endscope
use a = undefined
```

## Running the file

`python Main.py`
