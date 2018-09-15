import random, pytest


def selection_sort(lst):
    """
    Sorts a list using selection sort.
    :param lst:
    :return: lst, sorted
    """
    pass


def test_selection_sort():
    pass


def merge(lst, left, med, right):
    """
    Merges two lists in order.
    :param lst:
    :param left: index of first element of left sublist
    :param med: index of last element of left sublist
    :param right: index of last element of right sublist
    :return: lst, where the left and right sublists have been merged in order
    """
    pass


def test_merge():
    pass


def merge_sort_helper(lst, left, right):
    """
    Sorts a sublist of lst.
    :param lst:
    :param left: the index of first element in the sublist to be sorted
    :param right: the index of last element in the sublist to be sorted
    :return: lst, where the indicated sublist of lst has been sorted
    """
    pass


def test_merge_sort_helper():
    pass


def merge_sort(lst):
    """
    Sorts a list using merge sort.
    :param lst:
    :return: lst, sorted
    """


def test_merge_sort():
    pass


def partition(lst, low, high):
    """
    Takes the last element in lst as the pivot, places the pivot element at its correct position
    in the sorted list, and places all elements smaller than the pivot to its left and all elements
    larger than the pivot to its left.

    :param lst:
    :param low: index of first element in the sublist we are considering
    :param high: index of last element in the sublist we are considering
    :return: a non-negative integer (the partition index)
    """


def test_partition():
    pass


def quick_sort_helper(lst, low, high):
    """
    Sorts a sublist of lst.
    :param lst:
    :param low: the index of first element in the sublist to be sorted
    :param high: the index of last element in the sublist to be sorted
    :return:
    """


def test_quick_sort_helper():
    pass


def quick_sort(lst):
    """
    Sorts a list using quick sort.
    :param lst:
    :return: lst, sorted
    """


def test_quick_sort():
    pass


# TA testing method - do not modify any of this code
def sorting_method_tester(method):
    for lst in [[], [0], [0, 0], [0, 0, 0], [0, 1], [1, 0],
                [-1, 0, 1], [-1, 1, 0], [1, 0, -1], [1, -1, 0],
                [0, 1, -1], [0, -1, 1], [float('inf'), float('-inf')],
                [-10, 0, 10, 20, 30], [515, 91, 58, -19, 83, -0.1]]:
        tester_helper(lst, method)

    for x in range(100):
        low = random.randint(-100000, 90000)
        high = random.randint(low + 100, 100000)
        list_size = random.randint(1, 100)

        lst = random.sample(range(low, high), list_size)
        tester_helper(lst, method)


def tester_helper(lst, method):
    try:
        assert sorted(lst) == method(lst)
    except AssertionError:
        print(method.__name__ + " failed on the following list:" + str(lst))
        print("List was sorted by " + method.__name__ + " as follows: " + str(method(lst)))
        print()


if __name__ == "__main__":
    # To verify that your sorting methods pass your own test cases,
    # uncomment the following lines as you are ready.

    test_selection_sort()
    test_merge()
    test_merge_sort_helper()
    test_merge_sort()
    test_partition()
    test_quick_sort_helper()
    test_quick_sort()

    # To verify that your sorting methods pass the TA test cases,
    # uncomment the following lines as you  are ready. If there
    # is no output, then the test cases have passed.

    # sorting_method_tester(selection_sort)
    # sorting_method_tester(merge_sort)
    # sorting_method_tester(quick_sort)
