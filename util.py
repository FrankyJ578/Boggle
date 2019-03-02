ROOT = './'
INPUT_FOLDER = ROOT + 'input_files/'
DICTIONARY_PATH = ROOT + 'dictionary.txt'
END_WORD = '*'

def construct_trie(dictionary_path):
    """Reads a dictionary text file line by line and constructs
    a trie to represent the dictionary.
    """

    trie = dict()
    with open(dictionary_path) as file:
        for word in file:
            word = word.strip()
            temp_dict = trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, {})
            temp_dict[END_WORD] = END_WORD

    return trie

def in_bounds(row, col, n, m):
    """Given nxm grid, return True if (row, col) is valid
    or False if not valid.
    """
    return row >= 0 and row < n and col >= 0 and col < m
