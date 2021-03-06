"""
    Implementation of doubly linked list
"""


class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return f"Node{self.value}"


def main():
    # Building our Nodes
    a = DoublyLinkedListNode(1)
    b = DoublyLinkedListNode(2)
    c = DoublyLinkedListNode(3)

    # Building doubly linked list using nodes
    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b

    # Testing doubly linked list
    # Testing value attribute
    print(f"a.value --> {a.value}")
    print(f"b.value --> {b.value}")
    print(f"c.value --> {c.value}")
    # Testing next_node attribute
    print(f"a.next_node --> {a.next_node}")
    print(f"b.next_node --> {b.next_node}")
    print(f"c.next_node --> {c.next_node}")
    # Testing prev_node attribute
    print(f"a.prev_node --> {a.prev_node}")
    print(f"b.prev_node --> {b.prev_node}")
    print(f"c.prev_node --> {c.prev_node}")
    # Testing next_node value
    print(f"a.next_node.value --> {a.next_node.value}")
    print(f"b.next_node.value --> {b.next_node.value}")
    # Testing prev_node value
    print(f"b.prev_node.value --> {b.prev_node.value}")
    print(f"c.prev_node.value --> {c.prev_node.value}")


if __name__ == '__main__':
    main()
