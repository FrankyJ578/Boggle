Boggle

Given an NxN grid, find all possible words formed in Boggle.

The rules of Boggle:
- The letters must be adjoining in a 'chain'. (Letter cubes in the chain may be adjacent horizontally, vertically, or diagonally.)
- Words must contain at least three letters.
No letter cube may be used more than once within a single word.

Implementation:
To solve the problem, we use recursive backtracking. In addition, this implementation uses a trie data structure to store and search the dictionary for prefixes. This is a lot faster than the unoptimized naive solution (which is also provided in test.py) which just stores words in a hashset. By using a trie, we can eliminate a lot of search paths when we find a prefix that doesn't exist in the trie dictionary.

Dependencies:
- python3

Description of files:
input_files: folder of all the input files that are used to construct a Boggle board

boggle.py: file containing the implementation of Boggle

dictionary.txt: file containing all the words in the dictionary

main.py: main program used to get user input and solve a Boggle game

test.py: testing program used to verify correctness of the implementation (compares optimized solution to naive solution for correctness and efficiency)

util.py: contains helper functions useful for the implementation as well as some constants used in file navigation
