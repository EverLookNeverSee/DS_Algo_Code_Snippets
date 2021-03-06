"""
    Problem:
        Given an integer, create a function which returns the sum of all
        the individual digits in that integer.

        For example:
            if n = 4321, return 4 + 3 + 2 + 1 which is 10

    Hints:
        You will need to use modulo --> 4321 % 10 = 1
        and floor division operator --> 4321 // 10 = 432
"""


def sum_func(n: int) -> int:
    """
    Implementation of solution
    :param n: given number that w're gonna sum its all individual digits
    :return: result of summation
    """
    # Base case
    if n == 0:
        return 0
    else:
        return n % 10 + sum_func(n // 10)
