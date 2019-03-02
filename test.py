import util
import time

from boggle import Boggle

def test(dictionary, filename):
    # Actual implementation
    input_file_path = util.INPUT_FOLDER + filename
    start = time.time()
    boggle = Boggle(util.DICTIONARY_PATH, input_file_path)
    results = boggle.solve()
    end = time.time()
    print("Actual Time: ", end - start)
    print(len(results))

    # Naive implementation
    start = time.time()
    naive_results = naive_solution(boggle, dictionary)
    end = time.time()
    print("Naive Time: ", end - start)

    assert(results == naive_results)
    print('Numer of Possible Words: ', len(results))
    print('Results: ', results)
    print('\n')

def naive_solution(boggle, dictionary):
    """Naive implementation of Boggle. """

    board, tracking_board = boggle.get_boards()
    n = boggle.get_grid_size()

    results = set()
    for row in range(n):
        for col in range(n):
            naive_solution_recurse(n, board, tracking_board, [], row, col, dictionary, results)

    return results

def naive_solution_recurse(n, board, tracking_board, prefix, row, col, dictionary, results):
    """Naive solution of Boggle.
    Function will check if a word is in the dictionary and then if so,
    adds it to set of results (doesn't check prefixes).
    """

    word = ''.join(prefix)
    if len(word) >= 3 and word in dictionary:
        results.add(word)

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if not util.in_bounds(r, c, n, n):
                continue

            if tracking_board[r][c]:
                continue

            tracking_board[r][c] = 1
            prefix.append(board[r][c])
            naive_solution_recurse(n, board, tracking_board, prefix, r, c, dictionary, results)
            tracking_board[r][c] = 0
            prefix.pop()

def construct_dictionary():
    """Construct a dictionary with hashset"""

    dictionary = set()
    with open(util.DICTIONARY_PATH) as file:
        for word in file:
            word = word.strip()
            dictionary.add(word)

    return dictionary

if __name__=='__main__':
    dictionary = construct_dictionary()
    test(dictionary, 'basic_test_1.txt')
    test(dictionary, 'basic_test_2.txt')
    test(dictionary, 'medium_test_1.txt')
