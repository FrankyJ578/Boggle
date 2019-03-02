import util

class Boggle:

    def __init__(self, dictionary_path, input_path):
        self._board, self._tracking_board = self.build_board(input_path)
        self._dictionary = util.construct_trie(dictionary_path)

    def build_board(self, input_path):
        """Builds the Boggle board and the tracking board, which will
        be necessary for keeping track of which letters we've used so far
        in a given path.

        Arguments: input_path - path to the file containing metadata for board
        Returns: board - board with letters
                 tracking_board - board to track paths
        """

        with open(input_path) as file:
            n = int(file.readline().strip())
            self._n = n
            tracking_board = [[0 for _ in range(n)] for _ in range(n)]
            board = [[] for _ in range(n)]

            for row in range(n):
                for letter in file.readline().strip().split(' '):
                    board[row].append(letter)

            return board, tracking_board

    def solve(self):
        """Finds all possible words given a dictionary and constructed
        Boggle board

        Returns: set of all possible words
        """

        results = set()
        for r in range(self._n):
            for c in range(self._n):
                self._solve_recursive([], r, c, self._dictionary, results)

        return results

    def _solve_recursive(self, prefix, row, col, trie_node, results):
        """Recursive helper for solving Boggle board.

        Arguments: prefix - list of letters used so far in path
                   row - row of current grid cell being considered
                   col - column of current grid cell being considered
                   trie_node - dictionary containing next letter of words
                               that are formed from prefix
                   results - set of words that have been constructed so far
        """

        # Add word to results if not seen before
        if len(prefix) >= 3 and util.END_WORD in trie_node:
            results.add(''.join(prefix))

        # Check all adjacent diagonal, horizontal and vertical grid cells
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                # Check that the grid cell is in bounds
                if not util.in_bounds(r, c, self._n, self._n):
                    continue

                # Check that we haven't already used this grid in current path
                if self._tracking_board[r][c]:
                    continue

                # Check that there exists a word in dictionary with
                # current prefix plus next letter
                letter = self._board[r][c]
                if letter not in trie_node:
                    continue

                # Perform Recursive Backtracking
                # 1) Set grid cell in tracking board to True
                # 2) Append to prefix
                # 3) Recurse
                # 4) Backtrack
                self._tracking_board[r][c] = 1
                prefix.append(self._board[r][c])
                self._solve_recursive(prefix, r, c, trie_node[letter], results)
                self._tracking_board[r][c] = 0
                prefix.pop()

    def get_boards(self):
        """Get method for testing purposes"""

        return self._board, self._tracking_board

    def get_grid_size(self):
        """Get method for testing purposes"""

        return self._n
