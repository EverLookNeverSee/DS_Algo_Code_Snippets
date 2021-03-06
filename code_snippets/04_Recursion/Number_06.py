"""
    String Permutation

    Problem:
        Given a string, write a function that uses recursion to output
        list of all the possible permutations of that string.

        For example: given s = 'abc'
            The function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: If a character is repeated, treat each occurrence as distinct. For
          example an input of 'XXX' would return a list with 6 versions of 'XXX'.

    Solution:
        1. Iterate through the initial string
        2. For each character in the initial string, set aside that character
           and get a list of all permutations of the string that's left. So,for
           example if the current iteration is on 'b', we would want to find all
           the permutations of the string 'ac'.
        3. Once you have the list from step 2, add each element from that list to
           the character from the initial string, and append the result to our list
           of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'],
           we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add
           to our final results.
        4. Return the list of final results.
"""

# import relevant libraries
from unittest import TestCase, main


def permute(s: str) -> list:
    """
    Implementation of the solution
    :param s: Given string
    :return: List of permutations
    """
    output = []
    # Base Case
    if len(s) == 1:
        output = [s]
    else:
        # for every letter in string
        for i, lett in enumerate(s):
            # for every permutation resulting fro step 2, 3
            for perm in permute(s[:i] + s[i + 1:]):
                # add it to output
                output += [lett + perm]
    return output


class TestPermute(TestCase):
    def test_permute(self):
        self.assertEqual(permute("abc"), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(permute("a"), ["a"])
        self.assertEqual(permute("xxx"), ["xxx", "xxx", "xxx", "xxx", "xxx", "xxx"])
        self.assertEqual(permute("Ab"), ["Ab", "bA"])


if __name__ == '__main__':
    main()
