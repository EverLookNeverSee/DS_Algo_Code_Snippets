"""
    Implementation of stack

    Stack attributes and methods:
        Stack() --> Creates a new stack that is empty. It needs no parameters
            and returns an empty stack.
        push(item) --> Adds a new item to the top of the stack. It needs the
            item and return nothing.
        pop() --> Removes the top item from the stack. It needs no parameters
            and returns the item. The stack is modified.
        peek() --> Returns the top item from the stack but foes not remove it.
            It needs no parameters. The stack is not modified.
        isEmpty() --> Tests to see whether the stack is empty or not. It needs
            no parameters and returns a boolean value.
        size() --> Returns the number of items on the stack. It needs no para-
            -meters and returns an integer.
"""


class Stack(object):
    """Implementation of stack data structure"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def main():
    # Creating a stack object
    s = Stack()
    # Testing isEmpty() method
    print(f"Testing isEmpty() method: {s.isEmpty()}")
    # Testing push() method
    s.push(10)
    s.push('three')
    # Testing peek() method
    print(f"Testing peek() method: {s.peek()}")
    # Pushing another item
    s.push(True)
    # Testing size() method
    print(f"Testing size() method: {s.size()}")
    # Testing pop() method
    print(f"Testing pop() method: {s.pop()}")
    print(f"Testing pop() method: {s.pop()}")
    print(f"Testing pop() method: {s.pop()}")


if __name__ == '__main__':
    main()
