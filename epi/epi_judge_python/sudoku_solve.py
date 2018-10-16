import copy
import functools
import math
import numpy as np

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment):
    C = np.asarray(partial_assignment).reshape(-1)
    duplicate = True

    for i in range(0, 80):
        # if entry is zero, pass
        if C[i] == 0:
            continue

        else:
            for j in range(i + 1, 81):
                if C[i] == C[j]:
                    row_i = i // 9
                    row_j = j // 9
                    col_i = i % 9
                    col_j = j % 9
                    sub_matrix_i = [(i % 9) // 3, (i // 9) // 3]
                    sub_matrix_j = [(j % 9) // 3, (j // 9) // 3]
                    if row_i == row_j or col_i == col_j or sub_matrix_i == sub_matrix_j:
                        duplicate = False
                        break

            if duplicate is False:
                return duplicate
                break

    return duplicate


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))

    for i in range(len(solved)):
        assert_unique_seq(solved[i])
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
