'''
Input: Binary Search Tree and target int

Problem: Find the closest value to the target value in the BST

EXAMPLE

INPUT: 
bst:
            10
          /    \
         5      15
        / \    /  \
       2   5  13   22
      /         \   
     1           14

target = 12

OUTPUT:
        13
'''

# AVARAGE: O(log n) Time, O(1) Space
# WORST: O(n) Time, O(1) Space

def findClosestValueInBst(tree, target):
    closest = tree.value
    check = float('inf')
    node = tree
    while node is not None:
      if abs(node.value - target) < check:
        check = abs(node.value - target)
        closest = node.value
      if node.value > target: 
        node = node.left
      elif node.value < target:
        node = node.right
      else:
        return node.value
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
