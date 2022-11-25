'''
    INPUT: Node and array of children nodes (nodes will form a tree structure)
    OUTPUT: with depth-first search -> store all node's names in an array and return it

    EXAMPLE:
                    A
                 /  |  \ 
                /   |   \
               B    C    D
              / \       / \
             E   F     G   H
                / \    \
               I   J    K

O(v + e) T | O(v) S -> where 'v' is the number os vertices (nodes) and 'e' is the number os edges
'''

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
          child.depthFirstSearch(array)
        return array

class Test:
    def main():
        name = 'a'
        node = Node(name)
        array = []
        node.addChild('b')
        node.addChild('c')
        node.addChild('d')
        node.addChild('e')
        node.addChild('f')
        node.addChild('g')
        node.addChild('h')
        node.addChild('i')
        node.addChild('j')
        node.addChild('k')
        print(node.depthFirstSearch(array))

    if __name__ == '__main__':
        main()


