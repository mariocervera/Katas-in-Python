# All K-Subsets

A K-subset for a given set S is a subset that contains exactly K elements from S.

Write a program that returns a list with all K-subsets of a given set. The list will contain the 0-subsets first; then, the 1-subsets, and so on, until K reaches N, which is the size of the original set.

For example, all K-subsets of the set {'a', 'b', 'c', 'd', 'e'} are:

For K = 0: {}

For K = 1: {'a'}, {'b'}, {'c'}, {'d'}, {'e'}

For K = 2: {'a','b'}, {'a','c'}, {'a','d'}, {'a','e'}, {'b','c'}, {'b','d'}, {'b','e'}, {'c','d'}, {'c','e'}, {'d','e'}

For K = 3: {'a','b','c'}, {'a','b','d'}, {'a','b','e'}, {'a','c','d'}, {'a','c','e'}, {'a','d','e'}, {'b','c','d'}, {'b','c','e'}, {'b','d','e'}, {'c','d','e'}

For K = 4: {'a','b','c','d'}, {'a','b','c','e'}, {'a','b','d','e'}, {'a','c','d','e'}, {'b','c','d','e'}

For K = 5: {'a','b','c','d','e'}
