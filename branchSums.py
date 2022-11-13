'''
INPUT: Binary Tree
OUTPUT: List of its branch sums ordered from leftmost branch sum to rightmost branch sum

EXAMPLE

INPUT:
                 1
              /     \
             2       3
           /   \    /  \
          4     5  6    7
         / \   /
        8   9 10

OUTPUT:
    [15, 16, 18, 10, 11]
'''

# O(n) Time | O(n) Space

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
  result = []
  calculateBranchSums(root, 0, result)
  return result

def calculateBranchSums(node, sum, result):
  if node is None:
    return
  sum += node.value
  if node.left is None and node.right is None:
    result.append(sum)
    return
  calculateBranchSums(node.left, sum, result)
  calculateBranchSums(node.right, sum, result)
  return result