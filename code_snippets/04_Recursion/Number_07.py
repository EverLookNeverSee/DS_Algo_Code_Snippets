"""
    Problem:
        Implementation of fibonacci sequence in three different ways:
            * Recursively
            * Iteratively
            * Dynamically (Using memoization to store results)

    Note: Your function should accept a number n and return the nth
          number of the fibonacci sequence.
"""
# importing relevant libraries
import pytest
from functools import lru_cache


@lru_cache(maxsize=1024)
def recursive_fib(n: int) -> int:
    """
    Implementation of fibonacci sequence using recursion
    :param n: given integer number
    :return: nth number of fibonacci sequence
    """
    # Base case
    if n == 0 or n == 1:
        return n
    # recursive part
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def iterative_fib(n: int) -> int:
    """
    Implementation of fibonacci sequence using iteration
    :param n: Given integer number
    :return: nth number of fibonacci sequence
    """
    # start point
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


# Dynamically
# cache information
cache = {}


def dynamic_fib(num: int) -> int:
    """
    Implementation of fibonacci sequence using dynamic programming
    :param num: Given integer number
    :return: nth number of fibonacci sequence
    """
    # checking cache
    if num in cache:
        return cache[num]

    # Base case
    if num == 0 or num == 1:
        return num
    else:
        value = dynamic_fib(num - 1) + dynamic_fib(num - 2)
    cache[num] = value
    return value


parameters = [(1, 1), (2, 1), (10, 55),
              (100, 354224848179261915075),
              (200, 280571172992510140037611932413038677189525),
              (300, 222232244629420445529739893461909967206666939096499764990979600)]


@pytest.mark.parametrize("input, expected", parameters)
def test_recursive_fib(input, expected):
    assert recursive_fib(input) == expected


@pytest.mark.parametrize("input, expected", parameters)
def test_iterable_fib(input, expected):
    assert iterative_fib(input) == expected


@pytest.mark.parametrize("input, expected", parameters)
def test_dynamic_fib(input, expected):
    assert dynamic_fib(input) == expected

# Note: Use command below to run the tests in the terminal:
# $ pytest -v Number_07.py
