"""
    Linked List Nth to Last Node

    Problem:
        Write a function that takes a head node an integer value
        n and then returns the nth to the last node in the linked
        list.
        For example:
            >> target_node = nth_to_last_node(2, head)
            >> target_node.value
            4

    Solution:
        Imagine you have a bunch of nodes and a 'block' which is n-nodes
        wide. We could walk this block all the way down the list, and
        once the front of the block reached the end, then the other end
        of the block would be the Nth node.

        So to implement this block, we would just have two pointers, a
        left and right pair of pointers. Let's mark out the steps we will
        need to take:
            * Walk one pointer n nodes from the head, this will be the
                right point
            * Put the other pointer at the head, this will be the left point
            * Walk/traverse the block (both pointers) towards the tail, one
                node at a time, keeping a distance n between them
            * Once the right point has hit the tail, we know that the left
                point is at the target.
"""