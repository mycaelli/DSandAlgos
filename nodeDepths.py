'''
INPUT: Binary Tree
OUTPUT: The sum of its nodes depths

Depth: The distance between a node in a Binary Tree and the tree's root


EXAMPLE 

INPUT:
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
          / \
         8   9
          
OUTPUT: 16
        Depth of node with value 2 is 1
        Depth of node with value 3 is 1
        Depth of node with value 4 is 2
        Depth of node with value 5 is 2
        Depth of node with value 8 is 3
                ...

'''






#O(n) Time | O(n) Space
def nodeDepths(root, sum = 0):
  currentSum = sum
  if root.left is None and root.right is None:
    return sum
  if root.left is not None:
    currentSum += nodeDepths(root.left, sum + 1)
  if root.right is not None:
    currentSum += nodeDepths(root.right, sum + 1)
  return currentSum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
