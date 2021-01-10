#!/usr/bin/env python3
#

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Nond(!{r})'.format(r=self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    print(root)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(1.1))
    child1.add_child(Node(1.2))
    child2.add_child(Node(2.1))
    child2.add_child(Node(2.2))
    for ch in root.depth_first():
        print(ch)
