import os
import util

from boggle import Boggle

def print_error_instructions():
    """Prints out instructions when a proper file is not selected."""

    print('Input file does not exist or contains incorrect format.')
    print('Choose a properly formatted input file from input_files folder.')
    print('Input file format example:')
    print('3')
    print('c j e')
    print('e a o')
    print('i t e')
    print('\n')
    print('The number signifies the N, in NxN grid and rest of N lines represent the grid.')
    print('\n')

def select_input():
    """Asks user to choose an input file from input_files folder
    and verifies that the file is properly formatted for Boggle.
    """

    input_file_path = None
    while input_file_path is None:
        input_file_path = util.INPUT_FOLDER + input('Choose a properly formatted input file from input_files folder: ')
        if not verify_boggle_input_format(input_file_path):
            input_file_path = None
            print_error_instructions()
    return input_file_path

def verify_boggle_input_format(input_file_path):
    """Checks if a file exists and then verifies the format is correct
    for creating a Boggle board

    Input file format example:
    3
    c j e
    e a o
    i t e

    The number signifies the N, in NxN grid and the rest of the N lines
    represent the grid.
    """
    if os.path.isfile(input_file_path):
        with open(input_file_path) as file:
            try:
                n = int(file.readline().strip())

                # Verify each grid cell is a letter
                # Verify there are exactly n letters per row
                # Verify there are at least n rows
                for _ in range(n):
                    line = file.readline().strip().split(' ')
                    if line == ['']:
                        return False
                    count = 0
                    for letter in line:
                        if not letter.isalpha():
                            return False
                        count += 1
                    if count != n:
                        return False

                # Verify there are exactly n rows
                line = file.readline().strip().split(' ')
                if line != ['']:
                    return False

            except ValueError:
                return False

        return True

    return False

def print_results(possible_words):
    """Prints the number of possible words and a list of all the words"""

    print("Number of Possible Words: ", len(possible_words))
    for word in possible_words:
        print(word)

if __name__=='__main__':
    input_file_path = select_input()
    boggle = Boggle(util.DICTIONARY_PATH, input_file_path)
    possible_words = boggle.solve()
    print_results(possible_words)
